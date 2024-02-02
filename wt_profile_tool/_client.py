from typing import Optional
import httpx
from fake_useragent import FakeUserAgent  # type: ignore
from loguru import logger
from wt_profile_tool.decode.decoder import decode_profile_from_raw_bytes

from wt_profile_tool.schema.profile import WTProfile


class WTPTClient:
    """wt profile tool client"""

    __http_client: httpx.Client = httpx.Client(
        timeout=httpx.Timeout(60.0),
    )
    __random_ua: bool

    def __init__(
        self,
        random_ua: bool = False,
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        """init wt profile tool client

        Args:
            random_ua (bool, optional): use random user agent at each request. Defaults to False.
            http_client (Optional[httpx.Client], optional): http client. Defaults to None.
        """
        self.__random_ua = random_ua
        if http_client:
            self.__http_client = http_client

    def __get_http_user_agent(self) -> str:
        """get user agent

        Returns:
            str: user agent
        """
        if self.__random_ua:
            return FakeUserAgent().random
        return "wt-profile-tool"

    def get_player_profile_by_userid(self, userid: str) -> WTProfile:
        """get player profile by userid

        Args:
            userid (str): userid

        Returns:
            WTProfile: profile
        """
        logger.debug("get profile by userid [{}]", userid)
        response = self.__http_client.get(
            "https://companion-app.warthunder.com/call/",
            params={
                "classname": "eaw_ProfileBin",
                "method": "jzx_getPublicProfileBin",
                "bin": "true",
                "userid": userid,
                "lang": "en",
                "v": 7,
            },
            headers={"User-Agent": self.__get_http_user_agent()},
        )
        logger.debug("decode profile from raw bytes")
        profile = decode_profile_from_raw_bytes(response.content)
        logger.debug("decode success, set user id to profile base info")
        profile.base_info.user_id = userid
        return profile

    def get_player_profile_by_nickname(
        self,
        nick: str,
    ) -> WTProfile:
        """get player profile by nickname

        Args:
            nick (str): nick, must be match, case sensitive

        Raises:
            ValueError: nick not found

        Returns:
            WTProfile: profile
        """
        id_nick_map = self.get_player_userid_by_prefix_nick(nick)
        for userid, _nick in id_nick_map.items():
            if _nick == nick:
                logger.debug(f"found userid [{userid}] for nick [{nick}]")
                return self.get_player_profile_by_userid(userid)
        raise ValueError(f"nick {nick} not found")

    def get_player_userid_by_prefix_nick(self, nick_prefix: str) -> dict[str, str]:
        """get player userid by nick prefix

        Args:
            nick_prefix (str): nick prefix, fuzzy search as prefix

        Returns:
            dict[str, str]: userid and nick mapping
        """
        logger.debug("get userid by nick prefix [{}]", nick_prefix)
        response = self.__http_client.get(
            "https://companion-app.warthunder.com/call/",
            params={
                "classname": "eaw_Contacts",
                "method": "jzx_findUsersByNickPrefix",
                "count": "100",
                "nick": nick_prefix,
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
        logger.debug("login with loginname [{}]", login)
        response = self.__http_client.get(
            "https://login.gaijin.net/en/sso/login/",
            params={"login": login, "password": password, "format": "json", "v": "2"},
        )
        return response.json()
