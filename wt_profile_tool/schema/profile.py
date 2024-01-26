from enum import Enum
from typing import Optional
from pydantic import BaseModel


# ProfileProto.java#L6187
class BaseInfo(BaseModel):
    user_id: str
    nick: str
    icon_id: Optional[str] = None
    title: Optional[str] = None
    clan_id: Optional[str] = None
    clan_tag: Optional[str] = None
    clan_type: Optional[str] = None
    clan_name: Optional[str] = None
    clan_member_role: Optional[str] = None


# ProfileProto.java#L7287
class LevelInfo(BaseModel):
    level: int
    exp_has: int
    exp_left: int
    completeness: float


# ProfileProto.java#L7794
class PrivateInfo(BaseModel):
    ...


# ProfileProto.java#L11049
class Contact(BaseModel):
    ...


class EquipmentStatistic(BaseModel):
    ...


# ProfileProto.java#L22994
# TODO
class BattleStatisticPVP(BaseModel):
    victories: int
    time_tank_heavy: int
    time_tank_destroyer: int
    time_tank: int
    time_spaa: int
    time_fighter: int
    time_bomber: int
    time_attacker: int
    target_ground: int
    target_air: int
    session: int
    finished: int
    time_ship: int
    time_torpedo_boat: int
    time_gun_boat: int
    time_torpedo_gun_boat: int
    time_submarine_chaser: int
    time_destroyer: int
    time_naval_ferry_barge: int
    target_naval: int


# ProfileProto.java#L24613
# TODO
class CommonStatistic(BaseModel):
    battle_type: int
    pvp_played: BattleStatisticPVP
    single_played: BattleStatistic
    skirmish_played: BattleStatistic
    leaderboard: LeaderBoard
    effectiveness: float
    rating: float
    kills: int
    deaths: int


class PokerLeaderboard(BaseModel):
    ...


class Achievements(BaseModel):
    ...


class Titles(BaseModel):
    ...


# ProfileProto.java#L987
class BattleType(Enum):
    ARCADE = 0
    REALISTIC = 1
    HARDCORE = 2
    TANK_ARCADE = 3
    TANK_REALISTIC = 4
    AIR_ARCADE = 5
    AIR_REALISTIC = 6
    SHIP_ARCADE = 7
    SHIP_REALISTIC = 8
    TANK_SIMULATION = 9
    AIR_SIMULATION = 10
    SHIP_SIMULATION = 11
    BATTLE_TYPE_TEMP_1 = 12
    BATTLE_TYPE_TEMP_2 = 13
    BATTLE_TYPE_TEMP_3 = 14
    UNRECOGNIZED = -1


# ProfileProto.java#L26892
class BattleListItem(BaseModel):
    battle_type: Optional[BattleType] = None
    victories: Optional[int] = None
    battles: Optional[int] = None
    victories_battles: Optional[float] = None
    deaths: Optional[int] = None
    flyouts: Optional[int] = None
    air_kills: Optional[int] = None
    ground_kills: Optional[int] = None
    online_exp_total: Optional[int] = None
    wp_total: Optional[int] = None
    id: str
    naval_kills: Optional[int] = None


class Clan(BaseModel):
    ...


class Settings(BaseModel):
    ...


# ProfileProto.java#L3444
class WTProfile(BaseModel):
    base_info: BaseInfo
    level_info: LevelInfo
    lang: str
    battle_list: list[BattleListItem]
