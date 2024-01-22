# WT Profile Tool

[![Lint](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/lint.yml/badge.svg)](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/lint.yml)
[![Test](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/test.yml/badge.svg)](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/test.yml)
[![Publish to PyPI and TestPyPI](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/release.yml/badge.svg)](https://github.com/axiangcoding/wt-profile-tool/actions/workflows/release.yml)
[![codecov](https://codecov.io/gh/axiangcoding/wt-profile-tool/graph/badge.svg?token=03RR71KMBF)](https://codecov.io/gh/axiangcoding/wt-profile-tool)

## Description

This project contains set of tools used to fetch user profile from the WarThunder server, include serval operation like:

- get userid by nick
- get user profile by userid

## Usage

First, you need to install the package. For example use pip directly:

```bash
pip install wt-profile-tool
```

also you can install it by [Poetry](https://python-poetry.org/):

```bash
poetry add wt-profile-tool
```

Then, You can simply import the class and use it like this:

```python
from wt_profile_tool import WTProfileTool

tool = WTProfileTool()
profile = tool.get_profile_by_userid("5363987")
print(profile)
```

**Note**: Every time you call `get_profile_by_userid` will send a request to WarThunder server. Make sure your network can access the server and **DO NOT ABUSE IT**.

Finally, you can do something with the data. Data class is a `Pydantic BaseModel`, you can use `profile.dump_model_as_json()` to get the json string if you like.

a json string should be like:

```json
{
  "base_info": {
    "user_id": "",
    "nick": "OnTheRocks", # he was banned (i reported him), so his account is suiteable for example.
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
  "battle_list": [...],
  ...
}
```

## Contributing

Pull requests are welcome.

## License

[MIT License](./LICENSE)
