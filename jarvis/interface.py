from entities import User
from items import Weapon
from utils import safe_load

class GameState:
	def __init__(self):
		self._users = {}
		
	def load(self, file):
		config = safe_load(file)
		self._weapons = Weapon.loader(config["weapons"])

	def user(self, id):
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
		shop_text = ""

		shop_text += "__Weapons__\n"
		for weapon in self.state._weapons:
			shop_text += str(weapon) + '\n'
		
		return shop_text

	
	def profile(self, id):
		return self.state.user(id)