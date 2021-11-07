import discord
from discord.ext import commands
import requests
import json
from random import choice

class Pics(commands.Cog):
    def __init__(self, Maidchan):
        self.Maidchan = Maidchan

    @commands.command()
    async def anime(self, ctx, *, category=None):
        if category == None:
            category = choice(['waifu','neko','shinobu','megumin','bully','cuddle','cry','hug','awoo','kiss','lick','pat','smug','bonk','yeet','blush','smile','wave','highfive','handhold','nom','bite','glomp','slap','kill','kick','happy','wink','poke','dance','cringe'])
        r = requests.get(f'https://api.waifu.pics/sfw/{category}')
        r = str(r.text)
        r = json.loads(str(r))
        await ctx.send(r['url'])
    
    @commands.command()
    # @commands.is_nsfw()
    async def hentai(self, ctx,*,category=None):
        if ctx.channel.is_nsfw() == True:
            if category == None:
                category = choice(['waifu','neko','trap','blowjob'])
            r = requests.get(f'https://api.waifu.pics/nsfw/{category}')
            r = str(r.text)
            r = json.loads(str(r))
            await ctx.send(r['url'])
        else:
            await ctx.send('M-master, wrong channel!')

def setup(Maidchan):
    Maidchan.add_cog(Pics(Maidchan))
