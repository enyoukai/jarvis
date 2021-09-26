import lightbulb

class RpgPlugin(lightbulb.Plugin):
	@lightbulb.command()
	async def bal(self, ctx):
		bal = ctx.bot.interface.user_bal(ctx.author.id)

		await ctx.get_channel().send(f"You have {bal} moneys")
		
	@lightbulb.command()
	async def shop(self, ctx):
		shop_text = ctx.bot.interface.shop()
		
		await ctx.get_channel().send(shop_text)

	@lightbulb.command()
	async def profile(self, ctx):
		profile_text = ctx.bot.interface.profile(ctx.author.id)

		await ctx.get_channel().send(profile_text)

	@lightbulb.command()
	async def buy(self, ctx, *, item: str):
		buy_text = ctx.bot.interface.buy(ctx.author.id, item)
		await ctx.get_channel().send(buy_text)

	@lightbulb.command()
	async def fight(self, ctx):
		pass