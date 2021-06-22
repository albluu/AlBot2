import discord
import configparser
from discord.ext import commands

config = configparser.ConfigParser()
config.read('config.ini')

cmdPrefix = config['general']['prefix']
subtitle = config['general']['activity']
isCase = bool(config['general']['case_insensitive'])
token = config['general']['token']

print(f'prefix: {cmdPrefix}\tActivity: {subtitle}\tcase: {isCase}')

bot = commands.Bot(
    command_prefix = cmdPrefix,
    activity = discord.Game(name = subtitle),
    case_insensitive = isCase
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} : {bot.user.id}')

if (token):
    bot.run(token)
else:
    print('No Token loaded!')