class Item:
	def __init__(self, *, name, description, value, id):
		self.name = name		
		self.value = value
		self.desc = description
		self.id = id

	@staticmethod
	def loader():
		raise NotImplementedError

class Weapon(Item):
	def __init__(self, *, name, description, atk, value, id):
		super().__init__(name=name, description=description, value=value, id=id)
		self.atk = atk

	def __str__(self):
		weapon_text = ""
		weapon_text += f"**{self.name}** ({self.id})\n"
		weapon_text += f"ATK: {self.atk}\n"
		weapon_text += f"Price: {self.value}\n"
		weapon_text += f"Description: {self.desc}\n"
		
		return weapon_text

	@staticmethod
	def loader(data):
		# TODO: store weapons in a better data structure

		weapons = {}
		weapons_list = []
		
		for weapon in data:
			weapon_obj = Weapon(name=weapon["name"], atk=weapon["atk"], value=weapon["value"], description=weapon["desc"], id=weapon["id"])
			weapons[weapon_obj.id] = weapon_obj
			weapons_list.append(weapon_obj)

		return weapons, weapons_list