from discord.ext import commands

class BotManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('cog.BotManagement initialized')

    @commands.command(hidden = True)
    @commands.is_owner()
    async def reloadext(self, ctx, ext: str):
        await ctx.send('Reloading extension {0}'.format(ext))
        self.bot.reload_extension(ext)

    @commands.command(hidden = True)
    @commands.is_owner()
    async def startext(self, ctx, ext: str):
        await ctx.send('Starting extension {0}'.format(ext))
        self.bot.load_extension(ext)

    @commands.command(hidden = True)
    @commands.is_owner()
    async def stopext(self, ctx, ext: str):
        await ctx.send('Stopping extension {0}'.format(ext))
        self.bot.unload_extension(ext)

    @commands.command(hidden = True)
    @commands.is_owner()
    async def shutdownbot(self, ctx):
        await ctx.send('Shutting down the bot.')
        await self.bot.logout()

def setup(bot: commands.Bot):
    bot.add_cog(BotManagement(bot))