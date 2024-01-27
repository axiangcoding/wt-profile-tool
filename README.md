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

You can simply import the class and use it like the following

```python
from wt_profile_tool import WTProfileTool

wtpt = WTProfileTool()
```

Or you want to customize the tool, for example, you want to set all request timeout to 30 seconds, you can do it like the following

```python
wtpt = WTProfileTool(request_timeout=httpx.Timeout(30.0))
```

Parhaps you want to use a custom user agent instead of a random one, you can do it like the following

```python
wtpt = WTProfileTool(request_headers={"User-Agent": "YOUR UA HERE"}, random_ua=False,)
```

For more information about the parameters, please refer to the [source code](./wt_profile_tool/main.py).

### Get user ID by nick

After you initialize the tool, you can use `search_userid_by_prefix_nick` function to get user ID by prefix nickname.

```python
# This guy is real exist
user_id_map = wtpt.search_userid_by_prefix_nick("OnTheRocks")
```

**Note**: Every time you call a function it will send a request to a War Thunder server. Make sure your network can access the server and **DO NOT ABUSE IT**.

### Get user profile by ID

After you have the user ID, you can use `get_profile_by_userid` function to get user profile.

```python
# This guy is OnTheRocks
profile = wtpt.get_profile_by_userid("5363987")
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

**NOTE:** Data seems broken or missmatch? Please open an issue and provide example.

> Maybe you want to know why I use player `OnTheRocks` as an example. Because he was a cheater. I reported him and he was banned. This is the price you pay for using cheats to kill me 5 times in one battle. 😡😡😡

### More functions?

You can refer to the [source code](./wt_profile_tool/main.py) to find more functions.

## Contributing

If you have any issues or suggestions feel free to open one

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](./LICENSE)
