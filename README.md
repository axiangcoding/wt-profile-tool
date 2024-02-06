# WT Profile Tool

[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/axiangcoding/wt-profile-tool)
[![Lint](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/lint.yml/badge.svg)](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/lint.yml)
[![Test](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/test.yml/badge.svg)](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/test.yml)
[![Publish to PyPI and TestPyPI](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/release.yml/badge.svg)](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/release.yml)
[![codecov](https://codecov.io/gh/axiangcoding/wt-profile-tool/graph/badge.svg?token=03RR71KMBF)](https://codecov.io/gh/axiangcoding/wt-profile-tool)

## Description

This package contains set of tools used to to fetch War Thunder profiles, including:

- Get user profile by ID
- Get user ID by nick
- etc...

All data comes from public API.

**IMPORTANT**: This project is **NOT** affiliated with Gaijin Entertainment in any way, but is built by developers in the War Thunder community who love War Thunder. **If it infringes upon your rights, please contact author**.

Many thanks to [@RaidFourms](https://github.com/RaidFourms) for his immense help which inspired this project.

### Not a python developer?

You can use API server directly by [RaidFourms's wtpt-api](https://github.com/RaidFourms/wtpt-api) project.

### Don't know how to use API server?

Well, this is a tool project and not intended for non-developers 😵😵😵

## Usage

### Install

You can easily install it with pip:

```bash
pip install wt-profile-tool
```

Or you can install it with [Poetry](https://python-poetry.org/):

```bash
poetry add wt-profile-tool
```

### Initialize the tool

you can simply import the class and use it like the following

```python
from wt_profile_tool import WTPTClient

client = WTPTClient()
```

Or you can customize the client, for example, you want to set all request timeout to 30 seconds

```python
client = WTPTClient(
        http_client=httpx.Client(timeout=httpx.Timeout(30.0)),
)
```

You can customize the http_client to enable proxy, headers, etc.

Random user agent when sending request?

```python
client = WTPTClient(random_ua=True)
```

For more information about the parameters, please refer to the client description.

#### For old version

`WTProfileTool` is still available, but it is not recommended to use it. it has been makred deprecated and will be removed in the future. You can simply import the class and use it like the following

```python
from wt_profile_tool import WTProfileTool

wtpt = WTProfileTool()

...
```

### Get player's userid by nickname prefix

After you initialize the tool, you can use client's method to get player's userid by nickname prefix.

```python
# This guy is real exist
data = client.get_player_userid_by_prefix_nick("OnTheRocks")
```

**Note**: Every time you call a method needs to send http request, it will send a request to a War Thunder server. Make sure your network can access the server and **DO NOT ABUSE IT**.

### Get player's profile by userid

After you have the userid, you can use another method to get player's profile.

```python
# This guy is OnTheRocks
profile = client.get_player_profile_by_userid("5363987")
```

Then, you can do something with the `profile`.

```
base_info = profile.base_info

nick = base_info.nick
```

`profile` is a `Pydantic V2 BaseModel`, you can use `profile.model_dump_json()` to get the json string if you like.

```python
profile_json = profile.model_dump_json()
```

A JSON string should look like the following:

```json
{
  "base_info": {
    "user_id": "",
    "nick": "OnTheRocks",
    "icon_id": null,
    "title": "Tank Destroyer",
    "clan_id": null,
    "clan_tag": null,
    "clan_type": null,
    "clan_name": null,
    "clan_member_role": null
  },
  "level_info": {
    "level": 100,
    "exp_has": 27169491,
    "exp_left": 27169491,
    "completeness": 4.6071824188000174e18
  },
  "lang": "en",
  "battle_list": []
}
```

**NOTE:** Data seems broken or missmatch? Please open an issue and provide a right example.

> Maybe you want to know why I use player `OnTheRocks` as an example. Because he was a cheater. I reported him and he was banned. This is the price you pay for using cheats to kill me 5 times in one battle. 😡😡😡

### More features?

You can refer to the `WTPTClient`'s descritpion to find more available methods.

## Contributing

If you have any issues or suggestions feel free to open one.

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](./LICENSE)
