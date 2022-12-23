import discord, sys, subprocess
from discord.ext import commands
import config

def clear_console():
  if sys.platform == "linux" or sys.platform == "linux2":
    subprocess.run("clear")
  elif sys.platform == "darwin":
    subprocess.run("clear")
  elif sys.platform == "win32":
    subprocess.run("cls")

Maidchan = commands.Bot(command_prefix=config.prefix, case_insensitive=True, intents=discord.Intents.all())

@Maidchan.event
async def on_ready():
  print(f"{'-'*10}Bot on{'-'*10}")
  print(f'Heya Master, I am here!')
  print(f'My name is {Maidchan.user.name}.')
  print(f'My user id is {Maidchan.user.id}.')
  print(f"{'-'*10}IkkiArtz{'-'*10}")
  await Maidchan.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you!'))

async def command_init():
  print(f"{'-'*10}Commands Loading{'-'*10}")
  for filename in os.listdir('./commands'):
    if os.path.isdir(f'./commands/{filename}') or not filename.endswith('.py'):
      continue
    await Maidchan.load_extension(f'commands.{filename[:-3]}')
    print(f'{filename[:-3]} loaded')

@Maidchan.command(hidden=True)
async def load(ctx, *, filename):
  if str(ctx.author.id) == str(config.creator):
    await Maidchan.load_extension(f'commands.{filename}')
    await ctx.send(f'My master, the {filename} commands was loaded')
  else:
    await ctx.send('Sorry master, only creator may load a module.')

@Maidchan.command(hidden=True)
async def unload(ctx, *, filename):
  if str(ctx.author.id) == str(config.creator):
    await Maidchan.unload_extension(f'commands.{filename}')
    await ctx.send(f'My master, the {filename} commands was unloaded')
  else:
    await ctx.send('Sorry master, only creator may unloaded a module.')

@Maidchan.command(hidden=True)
async def reload(ctx, *, filename):
  if str(ctx.author.id) == str(config.creator):
    await Maidchan.reload_extension(f'commands.{filename}')
    await ctx.send(f'My master, the {filename} commands was reloaded')
  else:
    await ctx.send('Sorry master, only creator may reloaded a module.')

async def main():
  async with Maidchan:
    await command_init()
    await Maidchan.start(config.token)

clear_console()
asyncio.run(main())
