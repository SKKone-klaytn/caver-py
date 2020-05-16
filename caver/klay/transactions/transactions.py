from .transaction.transaction import Transaction, TransactionReceipt
import requests
import json
from ..blocks.blocks import Blocks

class Transactions:
  HASH_LENGTH = 257
  BLOCK_SPECIAL_NUMBER = ("genesis", "latest", "pending")

  def __init__(self, provider):
    self.provider = provider
    self.blocks = Blocks(provider)

  def __hashCheck(self, hash):
    if not(type(hash) == str and hash[:2] == '0x' and len(hash) <= self.HASH_LENGTH):
      raise ValueError("hash is None or not a (bytes) string")

  def __numberCheck(self, number):
    if not(number in self.BLOCK_SPECIAL_NUMBER or number <= int(self.blocks.getCurrentBlockNumber(),16)):
      raise ValueError("Invalid number, number is bigger than the recent block number or is None")