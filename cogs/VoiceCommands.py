import discord
from discord.ext import commands
import random
import Checks

class VoiceCommands(commands.Cog):
    """Contains features for managing users in voice channels"""

    def __init__(self, bot):
        self.bot = bot
        print('cog.VoiceCommands initialized')
        
    def split(self, l:list, n:int):
        for i in range(0, n):
            yield l[i::n]
    
    async def cog_command_error(self, ctx, error):
        await ctx.send(error)

    @commands.command(aliases=['cc'])
    @Checks.in_voice()
    @commands.has_guild_permissions(move_members = True)
    async def move(self, ctx, *, channel: str):
        """Moves users to a new voice channel (case sensitive)"""
        newChan = discord.utils.get(ctx.guild.voice_channels, name = channel)
        if newChan is None:
            await ctx.send("That channel doesn't exist.")
            return
        chMembs = ctx.author.voice.channel.members
        for mem in chMembs:
            await mem.move_to(newChan)
    
    @commands.command()
    @Checks.in_voice()
    async def team(self, ctx, teams: int):
        """Generates teams based on members in the current voice channel"""
        if (teams > 10):
            await ctx.send('Number of teams is limited to 10.')
            return
        chMembs = ctx.author.voice.channel.members
        random.shuffle(chMembs)
        teamList = list(self.split([m.mention for m in chMembs], teams))
        output = ''
        for teamNum in range(0, teams):
            output += f'Team {teamNum + 1}: ' + ' '.join(teamlist[teamNum]) + '\n'
        await ctx.send(output)

    @commands.command()
    @Checks.in_voice()
    @commands.has_guild_permissions(move_members = True)
    async def group(self, ctx, *, channel: str):
        """Pulls all users in voice channels into a specified channel"""
        newChan = discord.utils.get(ctx.guild.voice_channels, name = channel)
        if newChan is None:
            await ctx.send("That channel doesn't exist.")
            return
        voiceChan = ctx.guild.voice_channels
        chMembs = []
        for chan in voiceChan:
            if chan is not newChan:
                chMembs += chan.members
        for mem in chMembs:
            await mem.move_to(newChan)

    @commands.command()
    @Checks.in_voice()
    async def eject(self, ctx):
        """Leave the voice channel, in style."""
        if ctx.author.voice: # Intentionally not using checks to silently handle when not in vc
            await ctx.send(':crab: {0} is gone :crab:'.format(ctx.author.mention))
            await ctx.author.move_to(None)

def setup(bot: commands.Bot):
    bot.add_cog(VoiceCommands(bot))
