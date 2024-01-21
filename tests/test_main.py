from wt_profile_tool.main import WTProfileTool


def test_get_profile_by_userid():
    data = WTProfileTool.get_profile_by_userid("5363987")
    assert data.base_info.nick == "OnTheRocks"


def test_search_userid_by_nick():
    data = WTProfileTool.search_userid_by_nick("OnTheRocks")
    assert data["5363987"] == "OnTheRocks"
