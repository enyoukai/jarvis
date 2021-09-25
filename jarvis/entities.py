class User:
	def __init__(self, *, bal=0, hp=100, inventory=[], weapon=None):
		self._bal = bal
		self._hp = hp
		self._inv = inventory
		self._weapon = weapon

	def __str__(self):
		return f"**HP:** {self._hp}\n**Balance:** {self._bal}"

	@property
	def bal(self):
		return self._bal

	@bal.setter
	def bal(self, new_bal):
		self._bal = new_bal