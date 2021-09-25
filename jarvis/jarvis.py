import lightbulb
import os

from rpgplugin import RpgPlugin
from interface import GameInterface

class Bot(lightbulb.Bot):
	def __init__(self, *, token, prefix):
		super().__init__(token=token, prefix=prefix)
		self.interface = GameInterface("config.yml")

		self.add_plugin(RpgPlugin())

if __name__ == "__main__":
	TOKEN = os.environ.get("jarvis")
	bot = Bot(token=TOKEN, prefix="jarvis ")
	bot.run()