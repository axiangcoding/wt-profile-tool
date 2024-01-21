from pydantic import BaseModel


class WTProfile(BaseModel):
    userid: str
    nickname: str
    title: str
    clan_name: str
