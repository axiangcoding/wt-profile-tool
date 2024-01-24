import httpx
from wt_profile_tool.main import WTProfileTool


def test_init():
    test_tool = WTProfileTool()
    assert test_tool.get_request_client().timeout == httpx.Timeout(60.0)
    assert test_tool.get_request_client().headers["User-Agent"] != ""


def test_init_2():
    test_tool = WTProfileTool(
        request_timeout=httpx.Timeout(30.0),
        request_headers={"User-Agent": "test"},
        random_ua=False,
    )
    assert test_tool.get_request_client().timeout == httpx.Timeout(30.0)
    assert test_tool.get_request_client().headers["User-Agent"] == "test"


def test_get_profile_by_userid(test_tool: WTProfileTool):
    data = test_tool.get_profile_by_userid("5363987")
    assert data.base_info.nick == "OnTheRocks"


def test_get_profile_by_nick(test_tool: WTProfileTool):
    data = test_tool.get_profile_by_nick("OnTheRocks")
    assert data.base_info.nick == "OnTheRocks"


def test_search_userid_by_prefix_nick(test_tool: WTProfileTool):
    data = test_tool.search_userid_by_prefix_nick("OnTheRocks")
    assert data["5363987"] == "OnTheRocks"
