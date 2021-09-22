import lightbulb
import random

class RpgPlugin(lightbulb.Plugin):
	@lightbulb.command()
	async def mine(self, ctx):
		# TODO: do something about this like a decorator idk lol
		manager = ctx.bot.manager
		user = manager.get_user(ctx.author.id)

		mine_amt = random.randint(1, 10)
		user.bal += mine_amt
		await ctx.get_channel().send(f"Mined {mine_amt} moneys")

	@lightbulb.command()
	async def bal(self, ctx):
		bal = ctx.bot.manager.get_user(ctx.author.id).bal
		await ctx.get_channel().send(f"You have {bal} moneys")
		

	@lightbulb.command()
	async def shop(self, ctx):
		pass
