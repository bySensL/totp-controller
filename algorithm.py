import hmac
import hashlib
import time
import struct
import base64

def get_code(secret):
    key = base64.b32decode(secret, casefold=True)
    t = int(time.time() // 30)
    msg = struct.pack(">Q", t)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    offset = h[-1] & 0x0F
    code_bytes = h[offset:offset + 4]
    code_int = struct.unpack(">I", code_bytes)[0] & 0x7FFFFFFF
    return str(code_int % 1000000).zfill(6)
my_secret = "4YIZDRVKU4TVKFMHXARFGHRU5PWOOZ2Y"

secrets = [
    ("service", "4YIZDRVKU4TVKFMHXARFGHRU5PWOOZ2Y"),
]
for service, key in secrets:
    print(f"{service}: {get_totp_token(key)}")
