from entities import User
from items import Weapon
from utils import safe_load
from utils import to_id
from config import Config

class GameState:
	def __init__(self):
		self._users = {}
		
	def load_game(self, file):
		data = safe_load(file)
		self._weapons_dict, self._weapons_list = Weapon.loader(data["weapons"])

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
	def __init__(self, data):
		self.state = GameState()
		self.state.load_game(data)

	def user_bal(self, id):
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
		user = self.state.user(user_id)

		# generalize to items later
		if item_id in self.state._weapons_dict:
			weapon = self.state._weapons_dict[item_id]
			
			if weapon.value > user.bal:
				return Config.NOT_ENOUGH_MONEY
			else:
				user.bal -= weapon.value
				return Config.PURCHASE_SUCCESSFUL
		
		else:
			return Config.ITEM_NOT_FOUND

			

		
	