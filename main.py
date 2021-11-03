import json
import os
import random
import discord
import asyncio
import datetime
from discord import *
from discord import *
from discord.abc import *
from discord.enums import * 
from discord_buttons_plugin import *
from discord.ext import *
from discord.ext.commands import *
from math import sqrt
from dice.dice import *
import aiofiles
import discord.client

with open('config.json') as r:
  infos = json.load(r)
  prefix = infos['prefix']
  token = infos['token']

Maidchan = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=discord.Intents.all())
client = discord.Client()

@Maidchan.event
async def on_ready():
  print('Hi master, I am here!')
  print(Maidchan.user.name)
  print(Maidchan.user.id)
  print('------IkkiArtz------')

@Maidchan.command()
async def math(ctx, *, calc):
  if '+' in calc or '-' in calc or '/' in calc or '*' in calc or 'sqrt' in calc or '**':
    await ctx.send(eval(calc))

@Maidchan.command()
async def dice(ctx, *, dice):
  diceImport = diceMain(dice)
  diceImport.main()
  await ctx.send(f'{dice}\n{diceImport.rollList} -> {diceImport.rollTotal}')

@Maidchan.command()
async def say(ctx,*,said):
  await ctx.send(said)
  await ctx.message.delete()

@Maidchan.command()
async def avatar(ctx,*,user:discord.Member=None):
  if user == None:
    user = ctx.author
  urlAvatarUser = user.avatar_url
  await ctx.send(urlAvatarUser)

# @Maidchan.command()
# async def test(ctx):
#   channel = ctx.channel

#   def check(m):
#       return m.content == 'hello' and m.channel == channel

#   msg = await client.wait_for('message', check=check)
#   await channel.send('Hello {.author}!'.format(msg))
  
Maidchan.run(token)
