from rpgclasses import User

class RpgManager:
	def __init__(self):
		self.users = {}

	def get_user(self, id):
		if id not in self.users:
			self.users[id] = User()

		return self.users[id]