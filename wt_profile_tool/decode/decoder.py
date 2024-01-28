import json
import numbers

import blackboxprotobuf  # type: ignore


from wt_profile_tool.schema.profile import (
    BaseInfo,
    BattleListItem,
    BattleStatistic,
    BattleStatisticPVP,
    BattleType,
    CommonStatistic,
    LeaderBoard,
    LeaderBoardItem,
    LevelInfo,
    WTProfile,
)


def protobuf_to_json(raw_bytes: bytes) -> str:
    message, typedef = blackboxprotobuf.protobuf_to_json(raw_bytes)
    print(message)
    return message


def decode_profile_from_raw_bytes(raw_bytes: bytes) -> WTProfile:
    msg_json: dict = json.loads(protobuf_to_json(raw_bytes))

    first_msg = msg_json.get("1", None)

    # sometimes response can be a error message
    if isinstance(first_msg, numbers.Number):
        raise ValueError(f"WarThunder API return {first_msg}, message: {msg_json.get('2')}")

    base_info = parse_base_info(first_msg)

    level_info = parse_level_info(msg_json.get("2", {}))

    common_statistic = parse_common_statistic(msg_json.get("6", []))

    battle_list = parse_battle_list(msg_json.get("10", {}))

    return WTProfile(
        base_info=base_info,
        level_info=level_info,
        common_statistic=common_statistic,
        battle_list=battle_list,
        lang=msg_json.get("11", ""),
    )


def parse_base_info(data: dict) -> BaseInfo:
    return BaseInfo(
        user_id="",
        nick=str(data.get("2")),
        title=data.get("4"),
        clan_id=data.get("5"),
        clan_tag=data.get("6"),
    )


def parse_level_info(data: dict) -> LevelInfo:
    return LevelInfo(
        level=data["1"],
        exp_has=data["2"],
        exp_left=data["3"],
        completeness=data["4"],
    )


def parse_battle_list(data: list[dict]) -> list[BattleListItem]:
    ret_list = []
    for item in data:
        bt = BattleType(item.get("1", 0))
        ret_list.append(
            BattleListItem(
                battle_type=bt,
                victories=item.get("2"),
                battles=item.get("3"),
                victories_battles=item.get("4"),
                deaths=item.get("5"),
                flyouts=item.get("6"),
                air_kills=item.get("7"),
                ground_kills=item.get("8"),
                online_exp_total=item.get("9"),
                wp_total=item.get("10"),
                id=str(item.get("11")),
                naval_kills=item.get("12"),
            )
        )

    return ret_list


def parse_common_statistic(data: list[dict]) -> list[CommonStatistic]:
    ret_list = []
    for item in data:
        bt = BattleType(item.get("1", 0))
        ret_list.append(
            CommonStatistic(
                battle_type=bt,
                pvp_played=parse_battle_statistic_pvp(item.get("2", None)),
                single_played=parse_battle_statistic(item.get("3", None)),
                skirmish_played=parse_battle_statistic(item.get("4", None)),
                leaderboard=parse_leaderboard(item.get("5", None)),
                effectiveness=item.get("6", None),
                rating=item.get("7", None),
                kills=item.get("8", None),
                deaths=item.get("9", None),
            )
        )
    return ret_list


def parse_battle_statistic_pvp(data: dict) -> BattleStatisticPVP:
    if not data:
        return BattleStatisticPVP()

    return BattleStatisticPVP(
        victories=data.get("1"),
        time_tank_heavy=data.get("2"),
        time_tank_destroyer=data.get("3"),
        time_tank=data.get("4"),
        time_spaa=data.get("5"),
        time_fighter=data.get("6"),
        time_bomber=data.get("7"),
        time_attacker=data.get("8"),
        target_ground=data.get("9"),
        target_air=data.get("10"),
        session=data.get("11"),
        finished=data.get("12"),
        time_ship=data.get("13"),
        time_torpedo_boat=data.get("14"),
        time_gun_boat=data.get("15"),
        time_torpedo_gun_boat=data.get("16"),
        time_submarine_chaser=data.get("17"),
        time_destroyer=data.get("18"),
        time_naval_ferry_barge=data.get("19"),
        target_naval=data.get("20"),
    )


def parse_battle_statistic(data: dict) -> BattleStatistic:
    if not data:
        return BattleStatistic()

    return BattleStatistic(
        victories=data.get("1"),
        time_played=data.get("2"),
        missions_complete=data.get("3"),
    )


def parse_leaderboard_item(data: dict) -> LeaderBoardItem:
    if not data:
        return LeaderBoardItem()

    return LeaderBoardItem(
        value_month=data.get("1", None),
        place_month=data.get("2", None),
        value_total=data.get("3", None),
        place_total=data.get("4", None),
    )


def parse_leaderboard(data: dict) -> LeaderBoard:
    return LeaderBoard(
        victories_battles=parse_leaderboard_item(data.get("1", None)),
        each_player_victories=parse_leaderboard_item(data.get("2", None)),
        ground_kills=parse_leaderboard_item(data.get("3", None)),
        air_kills=parse_leaderboard_item(data.get("4", None)),
        flyouts=parse_leaderboard_item(data.get("5", None)),
        time_pvp_played=parse_leaderboard_item(data.get("6", None)),
        pvp_ratio=parse_leaderboard_item(data.get("7", None)),
        wp_total_gained=parse_leaderboard_item(data.get("8", None)),
        online_exp_gained_for_common=parse_leaderboard_item(data.get("9", None)),
        deaths=parse_leaderboard_item(data.get("10", None)),
        each_player_session=parse_leaderboard_item(data.get("11", None)),
        average_relative_position=parse_leaderboard_item(data.get("12", None)),
        average_active_kills_by_spawn=parse_leaderboard_item(data.get("13", None)),
        average_script_kills_by_spawn=parse_leaderboard_item(data.get("14", None)),
        average_score=parse_leaderboard_item(data.get("15", None)),
        naval_kills=parse_leaderboard_item(data.get("16", None)),
    )
