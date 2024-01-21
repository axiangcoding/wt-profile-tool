import json
import blackboxprotobuf
from loguru import logger

from wt_profile_tool.schema.profile import WTProfile

def decode_profile_from_raw_bytes(raw_bytes: bytes) -> WTProfile:
    message, typedef = blackboxprotobuf.protobuf_to_json(raw_bytes)
    msg_json = json.loads(message)
    nickname =  msg_json["1"]["2"]
    title = msg_json["1"]["4"]
    clan_name = msg_json["1"]["6"]
   
    return WTProfile(
        # userid can't find in response yet
        userid="",
        nickname=nickname,
        title=title,
        clan_name=clan_name
    )