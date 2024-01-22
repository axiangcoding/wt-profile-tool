import httpx
from loguru import logger

from wt_profile_tool.decode.decoder import decode_profile_from_raw_bytes
from wt_profile_tool.schema.profile import WTProfile


class WTProfileTool:
    @classmethod
    def get_profile_by_userid(cls, userid: str) -> WTProfile:
        logger.debug(f"Starting UID request for: {userid}")
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
        if response.status_code != 200:
            logger.error(f"Error while requesting profile {userid}")
            logger.error(f"Status code: {response.status_code}")
            logger.error(f"Response: {response.text}")
            raise Exception("Error while searching for " + userid + "\n " + response.text) # no idea why, but f-string didn't work here. i'll try fixing later
            pass
        return decode_profile_from_raw_bytes(response.content)

    @classmethod
    def get_profile_by_nick(cls, nick: str):
        ...

    @classmethod
    def search_userid_by_nick(cls, nick: str) -> dict[str, str]:
        logger.debug("Starting search for: " + nick)
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
        if response.status_code == 200:
            logger.error(f"Error while searching for {nick}")
            logger.error(f"Status code: {response.status_code}")
            logger.error(f"Response: {response.text}")
            raise Exception("Error while searching for " + nick + "\n " + response.text) # well it was here lol
            pass
        return response.json() 
