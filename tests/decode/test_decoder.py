from wt_profile_tool.decode.decoder import decode_profile_from_raw_bytes
from wt_profile_tool.schema.profile import BaseInfo, BattleListItem, LevelInfo


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

    assert len(data.battle_list) == 695

    assert data.battle_list[0] == BattleListItem(
        battles=1,
        deaths=1,
        flyouts=1,
        ground_kills=1,
        online_exp_total=89,
        wp_total=238,
        id="cn_m8_greyhound",
    )

    assert data.lang == "en"
