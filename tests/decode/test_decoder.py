from wt_profile_tool.decode.decoder import decode_profile_from_raw_bytes
from wt_profile_tool.schema.profile import (
    BaseInfo,
    BattleListItem,
    BattleType,
    LevelInfo,
)


def test_decode_profile_from_raw_bytes_1():
    with open("tests/example_proto/user1", "rb") as f:
        data = f.read()
    data = decode_profile_from_raw_bytes(data)

    assert data.base_info == BaseInfo(
        user_id="",
        nick="Malt_sugar",
        title="God of War",
        clan_id="1081754",
        clan_tag="┾TVNP┿",
    )

    assert data.level_info == LevelInfo(
        level=100,
        exp_has=145043150,
        exp_left=145043150,
        completeness=4607182418800017408,
    )

    assert len(data.common_statistic) == 12

    assert len(data.battle_list) == 695

    assert data.battle_list[0] == BattleListItem(
        battle_type=BattleType.ARCADE,
        battles=1,
        deaths=1,
        flyouts=1,
        ground_kills=1,
        online_exp_total=89,
        wp_total=238,
        id="cn_m8_greyhound",
    )

    assert data.battle_list[100] == BattleListItem(
        battle_type=BattleType.ARCADE,
        victories=9,
        victories_battles=1062302813.0,
        battles=11,
        deaths=24,
        ground_kills=118,
        air_kills=10,
        flyouts=29,
        online_exp_total=1770,
        wp_total=15928,
        id="ka_50",
    )

    assert data.lang == "en"


def test_decode_profile_from_raw_bytes_2():
    with open("tests/example_proto/user2", "rb") as f:
        data = f.read()
    data = decode_profile_from_raw_bytes(data)
    assert data.base_info == BaseInfo(
        user_id="",
        nick="OnTheRocks",
        title="Tank Destroyer",
        clan_id=None,
        clan_tag=None,
    )

    assert data.level_info == LevelInfo(
        level=100,
        exp_has=27169491,
        exp_left=27169491,
        completeness=4607182418800017408,
    )

    assert len(data.common_statistic) == 12

    arcade_stat = data.common_statistic[0]
    assert arcade_stat.battle_type == BattleType.ARCADE
    assert arcade_stat.pvp_played.victories == 3856
    assert arcade_stat.pvp_played.finished == 5673
    assert arcade_stat.pvp_played.target_air == 20770
    assert arcade_stat.pvp_played.target_ground == 13923
    assert arcade_stat.pvp_played.target_naval is None

    realistic_stat = data.common_statistic[1]
    assert realistic_stat.battle_type == BattleType.REALISTIC

    simulator_stat = data.common_statistic[2]
    assert simulator_stat.battle_type == BattleType.HARDCORE

    assert len(data.battle_list) == 774

    assert data.lang == "en"

    assert data.battle_list[0] == BattleListItem(
        battle_type=BattleType.REALISTIC,
        battles=1,
        online_exp_total=420,
        wp_total=900,
        id="hurricanemkii",
    )
