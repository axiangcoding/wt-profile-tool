import pytest

from wt_profile_tool.main import WTProfileTool


@pytest.fixture(scope="module")
def test_tool():
    return WTProfileTool()
