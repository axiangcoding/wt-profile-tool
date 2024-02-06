from typing import Optional
from typing_extensions import deprecated
import httpx
from loguru import logger

from fake_useragent import FakeUserAgent  # type: ignore
from wt_profile_tool.decode._profile_decoder import decode_profile_from_raw_bytes
from wt_profile_tool.schema.profile import WTProfile


@deprecated("WTPTClient is deprecated, use WTPTClient instead")
class WTProfileTool:
    __request_client: httpx.Client

    def __init__(
        self,
        request_timeout: httpx.Timeout = httpx.Timeout(60.0),
        request_headers: dict[str, str] = {},
        request_proxy: Optional[str] = None,
        request_mounts: Optional[dict[str, httpx.BaseTransport]] = None,
        random_ua: bool = True,
    ) -> None:
        """init WTProfileTool instance to send request

        Args:
            request_timeout (Optional[httpx.Timeout], optional): request timeout config. Defaults to httpx.Timeout(60.0).
            request_headers (Optional[dict[str, str]], optional): request headers config. Defaults to None.
            request_proxy (Optional[str], optional): request proxy config. Defaults to None. Can't coexist with request_mounts
            request_mounts (Optional[dict[str, str]], optional): request proxy mounts config. Defaults to None. Can't coexist with request_proxy
            random_ua (bool, optional): random user agent, if set to False, will use default user agent. Defaults to True.
        """

        if random_ua:
            logger.debug("random user agent enabled, override request headers's User-Agent")
            request_headers.__setitem__("User-Agent", FakeUserAgent().random)

        self.__request_client = httpx.Client(
            timeout=request_timeout,
            headers=request_headers,
            proxy=request_proxy,
            mounts=request_mounts,
        )

    def get_request_client(self) -> httpx.Client:
        """get request client, for advanced usage

        Returns:
            httpx.Client: request client
        """
        return self.__request_client

    def get_profile_by_userid(self, userid: str) -> WTProfile:
        """get profile by userid

        Args:
            userid (str): userid

        Returns:
            WTProfile: profile
        """
        logger.debug("start request")
        response = self.__request_client.get(
            "https://companion-app.warthunder.com/call/",
            params={
                "classname": "eaw_ProfileBin",
                "method": "jzx_getPublicProfileBin",
                "bin": "true",
                "userid": userid,
                "lang": "en",
                "v": 7,
            },
        )
        profile = decode_profile_from_raw_bytes(response.content)
        profile.base_info.user_id = userid
        return profile

    def get_profile_by_nick(
        self,
        nick: str,
    ) -> WTProfile:
        """get profile by specific nick

        Args:
            nick (str): nick, must be match, case sensitive

        Raises:
            ValueError: nick not found

        Returns:
            WTProfile: profile
        """
        id_nick_map = self.search_userid_by_prefix_nick(nick)
        for userid, _nick in id_nick_map.items():
            if _nick == nick:
                logger.debug(f"found userid {userid} for nick {nick}")
                return self.get_profile_by_userid(userid)
        raise ValueError(f"nick {nick} not found")

    def search_userid_by_prefix_nick(self, nick: str) -> dict[str, str]:
        """search userid by nick prefix

        Args:
            nick (str): nick, fuzzy search as prefix

        Returns:
            dict[str, str]: userid and nick mapping
        """
        logger.debug("start request")
        response = self.__request_client.get(
            "https://companion-app.warthunder.com/call/",
            params={
                "classname": "eaw_Contacts",
                "method": "jzx_findUsersByNickPrefix",
                "count": "100",
                "nick": nick,
                "v": 9,
            },
        )
        return response.json()

    def login(self, login: str, password: str) -> dict[str, str]:  # todo: allow 2fa
        """login use gaijin account. Be aware do not expose your account token to public

        Args:
            login (str): login name
            password (str): password

        Returns:
            dict[str, str]: account token etc
        """
        logger.debug("start request")
        response = self.__request_client.get(
            "https://login.gaijin.net/en/sso/login/",
            params={"login": login, "password": password, "format": "json", "v": "2"},
        )
        return response.json()
