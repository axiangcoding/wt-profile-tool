import json
import blackboxprotobuf  # type: ignore

from wt_profile_tool.schema.profile import (
    BaseInfo,
    BattleListItem,
    BattleType,
    LevelInfo,
    WTProfile,
)


def protobuf_to_json(raw_bytes: bytes) -> str:
    message, typedef = blackboxprotobuf.protobuf_to_json(raw_bytes)
    return message


def decode_profile_from_raw_bytes(raw_bytes: bytes) -> WTProfile:
    msg_json = json.loads(protobuf_to_json(raw_bytes))

    base_info = parse_base_info(msg_json["1"])

    level_info = parse_level_info(msg_json["2"])

    battle_list = parse_battle_list(msg_json["10"])

    return WTProfile(
        base_info=base_info,
        level_info=level_info,
        lang=msg_json["11"],
        battle_list=battle_list,
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
        bt = BattleType(item.get("1")) if item.get("1") else None
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
