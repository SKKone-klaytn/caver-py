from .account.account import Account
from .wallet.wallet import Wallet
from .accountUtil.accountUtil import createKey
from .accountKey.accountKeyPublic import AccountKeyPublic
from .accountKey.accountKeyMultiSig import AccountKeyMultiSig
from .accountKey.accountKeyRoleBase import AccountKeyRoleBase
from .accountKey.accountKeyLegacy import AccountKeyLegacy

from eth_keys import (
  keys
)

from eth_utils import (
  decode_hex
)

from hexbytes import (
    HexBytes,
)

#this Accounts Object hase two feature
# 1. Wallet
# 2. Account Factory Methods

class Accounts:
  def __init__(self) :
    self.wallet = Wallet()

  # Default Factoriy Method with AccoutkeyPublic
  # user don't have to specify anything(entropy, accountType or something)
  # just call Caver.Klay.Accounts.create()
  # then will be return Account Object

  # createWith{someting} is method for make complete Account Factory Method
  @staticmethod
  def create(entropy=''):
    key_pair = createKey(entropy)
    return Account(key_pair["address"], AccountKeyLegacy(key_pair["private_key"]))

  @staticmethod
  def createWithAccountKeyLegacy(self, key):
    private_key = self.createAccountKeyLegacy(key)
    address = private_key.public_key.to_checksum_address()
    return Account(address, private_key)

  @staticmethod
  def createWithAccountKeyPublic(self, address, key):
    # TODO public have to be implemented
    return Account(address, self.createAccountKeyPublic(key))

  @staticmethod
  def createWithAccountKeyRoleBase(address, accountKey):
    # TODO RoleBase have to be implemented
    pass

  @staticmethod
  def createWithAccountKeyMultiSig(address, keys):
    # TODO multiSig have to be implemented
    pass

  # createAccountKey{Type} is method for customKeyType for Factory method
  # ex))
  # account_key_multi_sig = Caver.Klay.Accounts.createAccountKeyMultiSig(values)
  # my_account = Caver.Klay.Accounts.createWithAccountKeyMultiSig(account_key_multi_sig)
  # now you can use my_account
  @staticmethod
  def createAccountKeyLegacy(key):
    if type(key) is keys.PrivateKey :
      return AccountKeyLegacy(key)
    if type(key) is str :
      key_bytes = HexBytes(decode_hex(str))
      private_key = keys.PrivateKey(key_bytes)
      return AccountKeyLegacy(private_key)

  @staticmethod
  def createAccountKeyPublic(key):
    # TODO public have to be implemented
    if type(key) is keys.PrivateKey :
      return AccountKeyPublic(key)
    if type(key) is str :
      key_bytes = HexBytes(decode_hex(str))
      private_key = keys.PrivateKey(key_bytes)
      return AccountKeyPublic(private_key)



  @staticmethod
  def createAccountKeyMultiSig(values = []):
    # TODO multiSig have to be implemented
    return AccountKeyMultiSig()

  @staticmethod
  def createAccountKeyRoleBase(values = []):
    # TODO Rolebase have to be implemented
    return AccountKeyRoleBase()
