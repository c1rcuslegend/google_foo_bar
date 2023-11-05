# Decode foobar completing message
import base64

s = ''' '''  # your message here

key = ''  # your username here


def decode(s, key):
    for i, c in enumerate(base64.b64decode(s)):
        yield chr(c ^ ord(key[i % len(key)]))


print("".join(list(decode(s, key))))
