from hashlib import sha256
import json
from datetime import datetime

class Block:
	def __init__(self, index, previous_hash, current_transactions, timestamp):
	  self.index=index
	  self.previous_hash = previous_hash
	  self.current_transactions = current_transactions
	  self.timestamp = timestamp
	  self.hash=self.compute_hash()

	def compute_hash(self):
		block_string = json.dumps(self.__dict__,  sort_keys=True)
		first_hash = sha256(block_string.encode()).hexdigest()
		second_hash = sha256(first_hash.encode()).hexdigest()
		return second_hash

	def __str__(self):
		return str(self.__dict__)
