import discord
from discord.ext import commands
from random import choice
import requests
import json

class Utilities(commands.Cog):
    def __init__(self, Maidchan):
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
    async def avatar(ctx,*,user:discord.Member=None):
        if user == None:
            user = ctx.author
            urlAvatarUser = user.avatar_url
            await ctx.send(urlAvatarUser)

def setup(Maidchan):
    Maidchan.add_cog(Utilities(Maidchan))
