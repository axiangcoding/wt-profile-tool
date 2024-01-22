import pytest

from wt_profile_tool.main import WTProfileTool


@pytest.fixture(scope="module")
def test_tool() -> WTProfileTool:
    """generate WTProfileTool instance for test

    Returns:
        WTProfileTool: WTProfileTool instance
    """
    return WTProfileTool()
