import lightbulb
import os

from rpg import Rpg

TOKEN = os.environ.get("jarvis")

bot = lightbulb.Bot(token=TOKEN, prefix="jarvis ", logs="INFO")
bot.add_plugin(Rpg())

bot.run()