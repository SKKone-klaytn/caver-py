from eth_utils.curried import (
    combomethod,
    hexstr_if_str,
    is_dict,
    keccak,
    text_if_str,
    to_bytes,
    to_int,
)

from hexbytes import (
    HexBytes,
)

from eth_keys import (
  keys
)

import os

def createKey(entropy) :
  extra_key_bytes = text_if_str(to_bytes, entropy)
  key_bytes = keccak(os.urandom(32) + extra_key_bytes)
  key = parsePrivateKey(key_bytes)

  return {
    "private_key" : key,
    "address" : key.public_key.to_checksum_address()
  }

def parsePrivateKey(key_bytes) :
  if isinstance(key_bytes, keys.PrivateKey):
    return key_bytes

  try:
    return keys.PrivateKey(HexBytes(key_bytes))
  except:
    raise ValueError("The private key must be exactly 32 bytes long")
