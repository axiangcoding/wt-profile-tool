import httpx
from httpx._utils import URLPattern
import pytest
from wt_profile_tool._main import WTProfileTool


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


def test_init_3():
    test_tool = WTProfileTool(
        request_mounts={
            "http://": httpx.HTTPTransport(proxy="http://localhost:10809"),
            "https://": httpx.HTTPTransport(proxy="http://localhost:10809"),
        },
    )
    assert test_tool.get_request_client()._mounts.get(URLPattern("http://")) is not None
    assert test_tool.get_request_client()._mounts.get(URLPattern("https://")) is not None


@pytest.mark.scheduled
def test_get_profile_by_userid(test_tool: WTProfileTool):
    data = test_tool.get_profile_by_userid("5363987")
    assert data.base_info.user_id == "5363987"
    assert data.base_info.nick == "OnTheRocks"


@pytest.mark.scheduled
def test_get_profile_by_userid_2(test_tool: WTProfileTool):
    with pytest.raises(ValueError) as excinfo:
        test_tool.get_profile_by_userid("9107392")
    assert (
        "WarThunder API return 400, message: !ERROR:OBSOLETE_USER_PROFILE:coreGetUserStat - DROP non converted obsolete profile"
        == str(excinfo.value)
    )


@pytest.mark.scheduled
def test_get_profile_by_nick(test_tool: WTProfileTool):
    data = test_tool.get_profile_by_nick("OnTheRocks")
    assert data.base_info.nick == "OnTheRocks"


@pytest.mark.scheduled
def test_search_userid_by_prefix_nick(test_tool: WTProfileTool):
    data = test_tool.search_userid_by_prefix_nick("OnTheRocks")
    assert data["5363987"] == "OnTheRocks"
