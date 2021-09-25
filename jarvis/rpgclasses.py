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

class Item:
	def __init__(self, *, name, description, value):
		self.name = name		
		self.value = value
		self.desc = description

	def loader(self, data):
		raise NotImplementedError

class Weapon(Item):
	def __init__(self, *, name, description, atk, value):
		super().__init__(name=name, description=description, value=value)
		self.atk = atk

	def __str__(self):
		weapon_text = ""
		weapon_text += f"**{self.name}**\n"
		weapon_text += f"ATK: {self.atk}\n"
		weapon_text += f"Price: {self.value}\n"
		weapon_text += f"Description: {self.desc}\n"
		
		return weapon_text

	@staticmethod
	def loader(data):
		'''
		loads weapons data from config.yml
		returns a list of weapons
		TODO: store in a better data structure
		'''
		weapons = []
		
		for weapon in data:
			weapon_obj = Weapon(name=weapon["name"], atk=weapon["atk"], value=weapon["value"], description=weapon["desc"])
			weapons.append(weapon_obj)

		return weapons