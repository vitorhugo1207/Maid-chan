import discord
from discord.ext import commands
from random import choice
from discord.ext.commands import bot
import requests
import json
import time

from main import Maidchan

class Utilities(commands.Cog):
    def __init__(self, Maidchan):
        pong = 0
        self.Maidchan = Maidchan
    
    @commands.command()
    async def say(self, ctx, *, said):
        await ctx.send(said)
        await ctx.message.delete()

    @commands.command()
    async def math(self, ctx, *, calc):
        if '+' in calc or '-' in calc or '/' in calc or '*' in calc or 'sqrt' in calc or '**':
            await ctx.send(eval(calc))
    
    @commands.command()
    async def avatar(self, ctx,*,user:discord.Member=None):
        if user == None:
            user = ctx.author
            urlAvatarUser = user.avatar_url
            await ctx.send(urlAvatarUser)
    
    @commands.command()
    async def ping(self, ctx): 
        await ctx.send(f'Pong! {round(self.Maidchan.latency * 1000)}ms.')

def setup(Maidchan):
    Maidchan.add_cog(Utilities(Maidchan))
