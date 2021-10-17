import json
import os
import random
import discord
import asyncio
import datetime
from discord import message
from discord import member
from discord_buttons_plugin import *
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType, has_permissions, MissingPermissions
from math import sqrt
from dice.dice import *


with open('config.json') as e:
  infos = json.load(e)
  prefix = infos['prefix']
  
Maidchan = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=discord.Intents.all())

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
  diceImport = diceMain(dice).diceRoll
  # print(diceImport)

@Maidchan.command()
async def say(ctx,*,said):
  await ctx.send(said)
  await ctx.message.delete()

Maidchan.run('ODY1NjU3MDMzODY4MDUwNDMy.YPHL8A.Jz_HCn9JbzgHPGHbJkMVE2ivZiQ')
