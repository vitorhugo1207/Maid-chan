import discord
from discord import activity
from discord.ext import commands
import json
import os
import time

os.system('clear')

with open('config.json') as r:
  infos = json.load(r)
  prefix = infos['prefix']
  token = infos['token']
  creator = infos['creator']


Maidchan = discord.ext.commands.Bot(command_prefix=prefix, case_insensitive=True, intents=discord.Intents.all())

@Maidchan.event
async def on_ready():
  print(f"{'-'*10}Bot on{'-'*10}")
  print(f'Hi my master, I am here!')
  print(f'My name is {Maidchan.user.name}.')
  print(f'My user id is {Maidchan.user.id}.')
  print(f"{'-'*10}IkkiArtz{'-'*10}")
  await Maidchan.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Master!'))

print(f"{'-'*10}Commands Loading{'-'*10}")
for filename in os.listdir('./commands'):
  if os.path.isdir(f'./commands/{filename}') == True:
    print(f'Unable to load dir "{filename}".')
  else:
      if filename.endswith('.py'):
        Maidchan.load_extension(f'commands.{filename[:-3]}')
        print(f'{filename[:-3]} loaded')
      else:
        print(f'Unable to load {filename}.')

@Maidchan.command(hidden=True)
async def load(ctx, *, filename):
    if str(ctx.author.id) == str(creator):
        Maidchan.load_extension(f'commands.{filename}')
        await ctx.send(f'My master, the {filename} commands was loaded')
    else:
        await ctx.send('Sorry master, only creator may loaded a module.')
        
@Maidchan.command(hidden=True)
async def unload(ctx, *, filename):
    if str(ctx.author.id) == str(creator):
        Maidchan.unload_extension(f'commands.{filename}')
        await ctx.send(f'My master, the {filename} commands was unloaded')
    else:
        await ctx.send('Sorry master, only creator may unloaded a module.')

@Maidchan.command(hidden=True)
async def reload(ctx, *, filename):
    if str(ctx.author.id) == str(creator):
        Maidchan.reload_extension(f'commands.{filename}')
        await ctx.send(f'My master, the {filename} commands was reloaded')
    else:
        await ctx.send('Sorry master, only creator may reloaded a module.')

Maidchan.run(token)
