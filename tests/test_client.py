import httpx
from wt_profile_tool import WTPTClient


def test_init():
    client = WTPTClient()
    assert client is not None
    assert isinstance(client, WTPTClient)
    assert client._WTPTClient__random_ua is False


def test_init_2():
    client = WTPTClient(random_ua=True)
    assert client is not None
    assert isinstance(client, WTPTClient)
    assert client._WTPTClient__random_ua is True


def test_init_3():
    client = WTPTClient(
        http_client=httpx.Client(timeout=httpx.Timeout(33.0)),
    )
    assert client is not None
    assert isinstance(client, WTPTClient)
    assert client._WTPTClient__random_ua is False
    assert client._WTPTClient__http_client.timeout == httpx.Timeout(33.0)
