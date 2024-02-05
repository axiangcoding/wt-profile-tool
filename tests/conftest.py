import pytest

from wt_profile_tool._client import WTPTClient
from wt_profile_tool._main import WTProfileTool


@pytest.fixture(scope="module")
def test_tool() -> WTProfileTool:
    """generate WTProfileTool instance for test

    Returns:
        WTProfileTool: WTProfileTool instance
    """
    return WTProfileTool()


@pytest.fixture(scope="module")
def test_client() -> WTPTClient:
    """generate WTPTClient instance for test

    Returns:
        WTPTClient: WTPTClient instance
    """
    return WTPTClient()
