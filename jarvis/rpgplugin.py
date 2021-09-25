import lightbulb

class RpgPlugin(lightbulb.Plugin):
	@lightbulb.command()
	async def bal(self, ctx):
		bal = ctx.bot.interface.bal(ctx.author.id)

		await ctx.get_channel().send(f"You have {bal} moneys")
		

	@lightbulb.command()
	async def shop(self, ctx):
		shop_text = ctx.bot.interface.shop()
		
		await ctx.get_channel().send(shop_text)
