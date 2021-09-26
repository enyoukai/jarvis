from entities import User
from items import Weapon
from utils import safe_load

class GameState:
	def __init__(self):
		self._users = {}
		
	def load(self, file):
		config = safe_load(file)
		self._weapons, self._weapons_list = Weapon.loader(config["weapons"])

	def user(self, id):
		# TODO: properly handle key errors later
		if id not in self._users:
			self._users[id] = User()

		return self._users[id]

class GameInterface:
	'''
	this class should allow all game logic
	to remain (almost) entirely independent 
	of the discord stuff
	'''
	def __init__(self, config):
		self.state = GameState()
		self.state.load(config)

	def bal(self, id):
		return self.state.user(id).bal

	def shop(self):
		shop_text = ""

		shop_text += "__Weapons__\n"
		
		for weapon in self.state._weapons_list:
			shop_text += str(weapon) + '\n'
		
		return shop_text
	
	def profile(self, id):
		return self.state.user(id)

	