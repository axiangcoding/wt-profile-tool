import httpx
from loguru import logger

from wt_profile_tool.decode.decoder import decode_profile_from_raw_bytes
from wt_profile_tool.schema.profile import WTProfile


class WTProfileTool:
    @classmethod
    def get_profile_by_userid(cls, userid: str) -> WTProfile:
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
        )
        return decode_profile_from_raw_bytes(response.content)

    @classmethod
    def get_profile_by_nick(cls, nick: str):
        ...

    @classmethod
    def search_userid_by_nick(cls, nick: str) -> dict[str, str]:
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
        )
        return response.json()
