import pytest
from wt_profile_tool import WTPTClient


@pytest.mark.scheduled
def test_get_player_profile_by_userid(test_client: WTPTClient):
    data = test_client.get_player_profile_by_userid("5363987")
    assert data.base_info.user_id == "5363987"
    assert data.base_info.nick == "OnTheRocks"


@pytest.mark.scheduled
def test_get_player_profile_by_userid_2(test_client: WTPTClient):
    with pytest.raises(ValueError) as excinfo:
        test_client.get_player_profile_by_userid("9107392")
    assert (
        "WarThunder API return 400, message: !ERROR:OBSOLETE_USER_PROFILE:coreGetUserStat - DROP non converted obsolete profile"
        == str(excinfo.value)
    )


@pytest.mark.scheduled
def test_get_player_profile_by_nickname(test_client: WTPTClient):
    data = test_client.get_player_profile_by_nickname("OnTheRocks")
    assert data.base_info.user_id == "5363987"
    assert data.base_info.nick == "OnTheRocks"


@pytest.mark.scheduled
def test_get_player_userid_by_prefix_nick(test_client: WTPTClient):
    data = test_client.get_player_userid_by_prefix_nick("OnTheRocks")
    assert data.get_userid_by_nickname("OnTheRocks") == "5363987"
    assert data.get_nickname_by_userid("5363987") == "OnTheRocks"
