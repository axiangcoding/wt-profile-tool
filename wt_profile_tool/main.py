from typing import Optional
import httpx
from loguru import logger

from wt_profile_tool.decode.decoder import decode_profile_from_raw_bytes
from wt_profile_tool.schema.profile import WTProfile


class WTProfileTool:
    timeout: Optional[httpx.Timeout] = httpx.Timeout(timeout=60)
    """request timeout"""

    def __init__(self, timeout: Optional[httpx.Timeout] = None) -> None:
        """init WTProfileTool instance

        Args:
            timeout (Optional[httpx.Timeout], optional): request timeout config. Defaults to None.
        """
        if timeout:
            self.timeout = timeout

    def get_profile_by_userid(self, userid: str) -> WTProfile:
        """get profile by userid

        Args:
            userid (str): userid

        Returns:
            WTProfile: profile
        """
        logger.debug("start request")
        response = httpx.get(
            "https://companion-app.warthunder.com/call/",
            params={
                "classname": "eaw_ProfileBin",
                "method": "jzx_getPublicProfileBin",
                "bin": "true",
                "userid": userid,
                "lang": "en",
                "v": 7,
            },
            timeout=self.timeout,
        )
        return decode_profile_from_raw_bytes(response.content)

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
        response = httpx.get(
            "https://companion-app.warthunder.com/call/",
            params={
                "classname": "eaw_Contacts",
                "method": "jzx_findUsersByNickPrefix",
                "count": "100",
                "nick": nick,
                "v": 9,
            },
            timeout=self.timeout,
        )
        return response.json()
    
    
    def login(cls, login: str, password: str) -> dict[str, str]: #todo: allow 2fa
        logger.debug("start request")
        response = httpx.get(
            "https://login.gaijin.net/en/sso/login/",
            params={
                "login": login,
                "password": password,
                "format": "json",
                "v": "2"
            },
        )
        return response.json()
