import pytest

from wt_profile_tool.decode.decode import decode_profile_from_raw_bytes


def test_decode_profile_from_raw_bytes():
    with open("tests/example_proto/user1", "rb") as f:
        data = f.read()
    data = decode_profile_from_raw_bytes(data)
    assert data.nickname == "Malt_sugar"
    assert data.title == "God of War"
    assert data.clan_name == "┾TVNP┿"
