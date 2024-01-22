# WT Profile Tool

## Description
This tool is used to fetch user profile from the WarThunder server and returns a readable class
## Usage
First, you need to install the package using pip:

```bash
pip install wt-profile-tool
```

Then, You can simply import the class and use it like this:

```python
data = WTProfileTool.get_profile_by_userid(userid="1234567890")
print(data)
```

## Contributing
Pull requests are welcome.

## License
[MIT License](./LICENSE)
