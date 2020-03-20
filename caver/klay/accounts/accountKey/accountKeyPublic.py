from eth_keys import (
  keys
)

class AccountKeyPublic:
  def __init__(self, private_key) :
    if type(private_key) is keys.PrivateKey :
      self.public_key = private_key.public_key.to_checksum_address()
      self.key = private_key
      self.type = '0x02' # '0x02 is accountKeyPublic'
    else :
      raise Exception # TODO Specify Exception Type
