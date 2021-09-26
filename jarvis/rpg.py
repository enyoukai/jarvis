from entities import User
from items import Weapon
from utils import safe_load
from utils import to_id

class GameState:
	def __init__(self):
		self._users = {}
		self._items = {}
		
	def load(self, file):
		config = safe_load(file)
		weapons_dict, self._weapons_list = Weapon.loader(config["weapons"])

		self._items = self._items | weapons_dict # merge two dicts

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

	def buy(self, user_id, item):
		item_id = to_id(item)

		if item_id in self.state._items:
			return self.state._items[item_id]
		
		else:
			return "That item does not exist"
		
	