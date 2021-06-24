import discord
import configparser
from discord.ext import commands

config = configparser.ConfigParser()
config.read('config.ini')

cmdPrefix = config['general']['prefix']
subtitle = config['general']['playing']
isCase = bool(config['general']['case_insensitive'])
token = config['general']['token']

print(f'prefix: {cmdPrefix}\tActivity: {subtitle}\tcase insensitive: {isCase}')

bot = commands.Bot(
    command_prefix = cmdPrefix,
    activity = discord.Game(name = subtitle),
    case_insensitive = isCase
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} : {bot.user.id}')

bot.load_extension('cogs.BotManagement')
bot.load_extension('cogs.General')
bot.load_extension('cogs.VoiceCommands')

if (token):
    try:
        bot.run(token)
    except discord.errors.LoginFailure as e:
        print('Invalid token provided!')
else:
    print('No Token loaded!')
