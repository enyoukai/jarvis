import lightbulb
import os

from rpgplugin import RpgPlugin
from rpgmanager import RpgManager

class Bot(lightbulb.Bot):
	def __init__(self, *, token, prefix):
		super().__init__(token=token, prefix=prefix)
		self.add_plugin(RpgPlugin())

		self.manager = RpgManager()


if __name__ == "__main__":
	TOKEN = os.environ.get("jarvis")
	bot = Bot(token=TOKEN, prefix="jarvis ")
	bot.run()