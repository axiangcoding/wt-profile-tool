from enum import Enum
from typing import Optional
from pydantic import BaseModel


# ProfileProto.java#L987
class BattleType(Enum):
    ARCADE = 0
    """Arcade battle"""

    REALISTIC = 1
    """Realistic battle"""

    HARDCORE = 2
    """Simulator battle"""
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


# ProfileProto.java#L6187
class BaseInfo(BaseModel):
    user_id: str
    """User ID"""

    nick: str
    """User nickname"""

    icon_id: Optional[str] = None
    title: Optional[str] = None
    """Title"""

    clan_id: Optional[str] = None
    """Clan ID"""

    clan_tag: Optional[str] = None
    """Clan tag displayed in game"""

    clan_type: Optional[str] = None
    clan_name: Optional[str] = None
    clan_member_role: Optional[str] = None


# ProfileProto.java#L7287
class LevelInfo(BaseModel):
    level: int
    """Level of the user"""

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
class BattleStatisticPVP(BaseModel):
    victories: Optional[int] = None
    """Number of victories"""

    time_tank_heavy: Optional[int] = None
    time_tank_destroyer: Optional[int] = None
    time_tank: Optional[int] = None
    time_spaa: Optional[int] = None
    time_fighter: Optional[int] = None
    time_bomber: Optional[int] = None
    time_attacker: Optional[int] = None
    target_ground: Optional[int] = None
    """Number of ground targets destroyed"""

    target_air: Optional[int] = None
    """Number of air targets destroyed"""

    session: Optional[int] = None
    finished: Optional[int] = None
    """Number of battles finished"""

    time_ship: Optional[int] = None
    time_torpedo_boat: Optional[int] = None
    time_gun_boat: Optional[int] = None
    time_torpedo_gun_boat: Optional[int] = None
    time_submarine_chaser: Optional[int] = None
    time_destroyer: Optional[int] = None
    time_naval_ferry_barge: Optional[int] = None
    target_naval: Optional[int] = None
    """Number of naval targets destroyed"""


# ProfileProto.java#L24147
class BattleStatistic(BaseModel):
    victories: Optional[int] = None
    time_played: Optional[int] = None
    missions_complete: Optional[int] = None


# ProfileProto.java#L17772
class LeaderBoardItem(BaseModel):
    value_month: Optional[float] = None
    place_month: Optional[int] = None
    value_total: Optional[float] = None
    place_total: Optional[int] = None


# ProfileProto.java#L18862
class LeaderBoard(BaseModel):
    victories_battles: LeaderBoardItem
    each_player_victories: LeaderBoardItem
    ground_kills: LeaderBoardItem
    air_kills: LeaderBoardItem
    flyouts: LeaderBoardItem
    time_pvp_played: LeaderBoardItem
    pvp_ratio: LeaderBoardItem
    wp_total_gained: LeaderBoardItem
    online_exp_gained_for_common: LeaderBoardItem
    deaths: LeaderBoardItem
    each_player_session: LeaderBoardItem
    average_relative_position: LeaderBoardItem
    average_active_kills_by_spawn: LeaderBoardItem
    average_script_kills_by_spawn: LeaderBoardItem
    average_score: LeaderBoardItem
    naval_kills: LeaderBoardItem


# ProfileProto.java#L24613
class CommonStatistic(BaseModel):
    battle_type: Optional[BattleType]
    pvp_played: BattleStatisticPVP
    single_played: BattleStatistic
    skirmish_played: BattleStatistic
    leaderboard: LeaderBoard
    effectiveness: Optional[float]
    rating: Optional[float]
    kills: int
    deaths: int


class PokerLeaderboard(BaseModel):
    ...


class Achievements(BaseModel):
    ...


class Titles(BaseModel):
    ...


# ProfileProto.java#L26892
class BattleListItem(BaseModel):
    battle_type: Optional[BattleType] = None
    """Battle type"""

    victories: Optional[int] = None
    battles: Optional[int] = None
    """Number of battles"""

    victories_battles: Optional[float] = None

    deaths: Optional[int] = None
    """Number of deaths"""

    flyouts: Optional[int] = None
    """Number of respawns"""

    air_kills: Optional[int] = None
    """Number of air targets destroyed"""

    ground_kills: Optional[int] = None
    """Number of ground targets destroyed"""

    online_exp_total: Optional[int] = None
    """Total online experience gained in the battle"""

    wp_total: Optional[int] = None
    id: str
    """Vehicle ID"""

    naval_kills: Optional[int] = None
    """Number of naval targets destroyed"""


class Clan(BaseModel):
    ...


class Settings(BaseModel):
    ...


# ProfileProto.java#L3444
class WTProfile(BaseModel):
    """War Thunder profile data

    All data is from protobuf format raw data.

    - Only the fields that have been manually proofread and added to the test case have descriptions
    - Fields without descriptions means that they have not been proofread, but still can be used

    USE AT YOUR OWN RISK!
    """

    base_info: BaseInfo
    """Basic information"""

    level_info: LevelInfo
    """Level information"""

    lang: str
    """Language"""

    battle_list: list[BattleListItem]
    """Battle list"""

    common_statistic: list[CommonStatistic]
    """Common statistic"""
