import discord
from discord.ext.commands import context, CheckFailure, check

class notInVoiceChannel(CheckFailure):
    pass

def in_voice():
    async def predicate(ctx: context):
        if not ctx.author.voice:
            raise notInVoiceChannel("You're not in a voice channel.")
        return True
    return check(predicate)

