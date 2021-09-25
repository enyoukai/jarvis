class User:
	def __init__(self, *, bal=0, hp=100):
		self._bal = bal
		self._hp = hp

	@property
	def bal(self):
		return self._bal

	@bal.setter
	def bal(self, new_bal):
		self._bal = new_bal

class Item:
	def __init__(self, *, name):
		self.name = name

# like a pickaxe
class Pick(Item):
	def __init__(self, *, name, mul):
		self.name = name
		self._mul = mul
	
	@property
	def mul(self):
		return self._mul