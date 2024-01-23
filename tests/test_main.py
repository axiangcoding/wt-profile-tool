from wt_profile_tool.main import WTProfileTool


def test_get_profile_by_userid(test_tool: WTProfileTool):
    data = test_tool.get_profile_by_userid("5363987")
    assert data.base_info.nick == "OnTheRocks"


def test_get_profile_by_nick(test_tool: WTProfileTool):
    data = test_tool.get_profile_by_nick("OnTheRocks")
    assert data.base_info.nick == "OnTheRocks"


def test_search_userid_by_prefix_nick(test_tool: WTProfileTool):
    data = test_tool.search_userid_by_prefix_nick("OnTheRocks")
    assert data["5363987"] == "OnTheRocks"
