import discord
import requests
import json
import random

class Pics(commands.Cog):
  def __init__(self, Maidchan):
    self.Maidchan = Maidchan
    self.session = requests.Session()

  async def send_pic(self, ctx, url):
    try:
      r = self.session.get(url)
      r = r.json()
      await ctx.channel.send(r['url'])
    except Exception as e:
      await ctx.channel.send(f'An error occurred: {e}')

  async def get_category(self, ctx, sfw=True):
    if sfw:
      categories = ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']
    else:
      categories = ['waifu', 'neko', 'trap', 'blowjob']

    if ctx.channel.is_nsfw() == True:
      return categories[random.randint(0, len(categories) - 1)]
    else:
      await ctx.channel.send('M-master, wrong channel!')
      return None

  @commands.command()
  async def anime(self, ctx, *, category=None):
    category = category or await self.get_category(ctx)
    if category is not None:
      await self.send_pic(ctx, f'https://api.waifu.pics/sfw/{category}')

  @commands.command()
  async def hentai(self, ctx, *, category=None):
    category = category or await self.get_category(ctx, sfw=False)
    if category is not None:
      await self.send_pic(ctx, f'https://api.waifu.pics/nsfw/{category}')
    
  @commands.command()
  async def fox(self, ctx):
    await self.send_pic(ctx, "https://randomfox.ca/floof/")

async def setup(Maidchan):
  await Maidchan.add_cog(Pics(Maidchan))
