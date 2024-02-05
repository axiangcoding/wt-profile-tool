from typing import Dict, Optional
from pydantic import BaseModel


class UserIdNick(BaseModel):
    id_nick_map: Dict[str, str] = {}

    def get_nickname_by_userid(self, userid: str) -> Optional[str]:
        """Get nickname by userid

        Args:
            userid (str): userid

        Returns:
            Optional[str]: nick
        """
        return self.id_nick_map.get(userid, None)

    def get_userid_by_nickname(self, nickname: str) -> Optional[str]:
        """Get userid by nickname

        Args:
            nickname (str): nick

        Returns:
            Optional[str]: userid
        """
        for userid, _nick in self.id_nick_map.items():
            if _nick == nickname:
                return userid
        return None
