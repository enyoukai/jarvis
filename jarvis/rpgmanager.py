import random

from rpgclasses import User
from utils import safe_load

class GameState:
	def __init__(self):
		self._users = {}
		
	def load(self, file):
		config = safe_load(file)
		self.shop_text = config["shop-text"]

	def user(self, id):
		# if user id not found, make a new user
		# TODO: properly handle key errors later
		if id not in self._users:
			self._users[id] = User()

		return self._users[id]

class GameInterface:
	def __init__(self, file):
		self.state = GameState()
		self.state.load(file)

	def bal(self, id):
		return self.state.user(id).bal

	def shop(self):
		return self.state.shop_text