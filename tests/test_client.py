from wt_profile_tool import WTPTClient


def test_init():
    client = WTPTClient()
    assert client is not None
    assert isinstance(client, WTPTClient)
    assert client._WTPTClient__random_ua is False
