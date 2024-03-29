from hashlib import sha256
import json
from datetime import datetime

class Block:
	def __init__(self, index, previous_hash, current_transactions, timestamp, nonce):
	  self.index=index
	  self.previous_hash = previous_hash
	  self.current_transactions = current_transactions
	  self.timestamp = timestamp
	  self.nonce=nonce
	  self.hash=self.compute_hash()

	def compute_hash(self):
		block_string = json.dumps(self.__dict__,  sort_keys=True)
		first_hash = sha256(block_string.encode()).hexdigest()
		second_hash = sha256(first_hash.encode()).hexdigest()
		return second_hash

	def __str__(self):
		return str(self.__dict__)

class Blockchain:

	def __init__(self):
		self.chain=[]
		self.gen_block=self.genesis_block()

	def genesis_block(self):
		genesis_block=Block(0,0x0,[3,4,5,6,7],'datetime.now().timestamp()',0)
		genesis_block.hash = genesis_block.compute_hash()
		self.chain.append(genesis_block.hash)
		return genesis_block

	def getLastBlock(self):
		return self.chain[-1]

	def proof_of_work(self, block):
		difficulty=1
		block.nonce=0
		computed_hash=block.compute_hash()
		while not computed_hash.endswith('0' * difficulty):
			block.nonce += 1
			computed_hash = block.compute_hash()
		return computed_hash

	def add(self,data):
		block=Block(len(self.chain),self.chain[-1],data,'datetime.now().timestamp()',0)
		block.hash = self.proof_of_work(block)
		self.chain.append(block.hash)
		return block

def main():
	B=Blockchain()
	[print('Block #{} :\n{}\n'.format(i, B.add([i*i*i]))) for i in range(1,11)]
	fourth_block={
		'transactions':
		[
			{
			'block_index':1,
			'from': 'John',
			'to': 'Mike',
			'message':'Hey How are You Today?',
			'coin_amount': 55
			},
			{
			'block_index':2,
			'from': 'Rick',
			'to': 'Janet',
			'message':'Thanks for the Ice Cream',
			'coin_amount': 5
			},
			{
			'block_index':3,
			'from': 'Michelle',
			'to': 'Ronald',
			'message':'Here is your bonus',
			'coin_amount': 500
			},
		]
	}

	a=B.add(fourth_block)
	print(a)

if __name__=='__main__':
	main()
