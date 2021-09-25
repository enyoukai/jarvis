import random

from rpgclasses import User

class GameState:
	def __init__(self):
		self._users = {}
		# dynamically build this later
		self.shop_text = "Nothing here yet"

	def user(self, id):
		# if user id not found, make a new user
		# TODO: properly handle key errors later
		if id not in self._users:
			self._users[id] = User()

		return self._users[id]

class GameInterface:
	def __init__(self):
		self.state = GameState()

	def mine(self, id):
		user = self.state.user(id)
		mine_amt = random.randint(1, 10)
		user.bal += mine_amt

		return mine_amt
	
	def bal(self, id):
		return self.state.user(id).bal

	def shop(self):
		return self.state.shop_text