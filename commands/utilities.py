import discord
from discord.ext import commands
from random import choice
from discord.ext.commands import bot
import requests
import json
import time
from main import Maidchan
import datetime

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

    @commands.command()
    async def animesearch(self, ctx, *, img):
        # Search
        img = requests.get(f'https://api.trace.moe/search?cutBorders&url={img}')
        img = str(img.text)
        img = json.loads(str(img))

        # Get anime info
        anilistQuery = '''
        query ($id: Int) {
        Media (id: $id, type: ANIME) {
            id
            title {
            romaji
            english
            native
            }
        }
        }
        '''
        anilistPOST = requests.post("https://graphql.anilist.co/", json={'query': anilistQuery, 'variables': {'id': img['result'][1]['anilist']}})
        anilistPOST = str(anilistPOST.text)
        anilistPOST = json.loads(str(anilistPOST))

        # Show data
        await ctx.send(f"""
Similarity: {(str(float((img['result'][1]['similarity'])*100)))[:5]}%

Anilist: https://anilist.co/anime/{img['result'][1]['anilist']}
Tittle romaji: {anilistPOST['data']['Media']['title']['romaji']}
Tittle romaji: {anilistPOST['data']['Media']['title']['english']}
Episode: {img['result'][1]['episode']}
Time between: {str(datetime.timedelta(seconds=(img['result'][1]['from'])))[:7]} and {str(datetime.timedelta(seconds=(img['result'][1]['to'])))[:7]}
        """)

def setup(Maidchan):
    Maidchan.add_cog(Utilities(Maidchan))
