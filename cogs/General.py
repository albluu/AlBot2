from discord.ext import commands
import random

from discord.ext.commands.context import Context

class General(commands.Cog):
    """General Commands"""
    
    def __init__(self, bot):
        self.bot = bot
        print('cog.General initialized')

    @commands.command()
    async def hello(self, ctx):
        """Responds with \"Hello @[username]!\""""
        await ctx.send(f'Hello {ctx.author.mention}!')

    @commands.command()
    async def roll(self, ctx: Context, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
            if (rolls > 50 or limit > 10000):
                await ctx.send('You\'re limited to 50d10000.')
                return
            rollList = [random.randint(1, limit) for r in range(rolls)]
            output = f'{ctx.author.mention} rolled {dice}: {", ".join(map(str, sorted(rollList)))} ({sum(rollList)})'
            await ctx.send(output)
        except Exception:
            await ctx.send('Format has to be in NdN!')
        

def setup(bot: commands.Bot):
    bot.add_cog(General(bot))