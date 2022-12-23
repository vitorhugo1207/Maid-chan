import discord, requests, json, datetime, time
from discord.ext import commands
from discord.ext.commands import bot
from random import choice
# from main import Maidchan

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
  async def avatar(self, ctx, *, user: discord.Member=None):
    user = user if user else ctx.author
    avatar = user.avatar_url
    await ctx.send(avatar)
    
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
      }'''
    anilistPOST = requests.post("https://graphql.anilist.co/", json={'query': anilistQuery, 'variables': {'id': img['result'][1]['anilist']}})
    anilistPOST = str(anilistPOST.text)
    anilistPOST = json.loads(str(anilistPOST))
    await ctx.send(f"""
Similarity: {(str(float((img['result'][1]['similarity'])*100)))[:5]}%
Anilist: https://anilist.co/anime/{img['result'][1]['anilist']}
Tittle romaji: {anilistPOST['data']['Media']['title']['romaji']}
Tittle romaji: {anilistPOST['data']['Media']['title']['english']}
Episode: {img['result'][1]['episode']}
Time between: {str(datetime.timedelta(seconds=(img['result'][1]['from'])))[:7]} and {str(datetime.timedelta(seconds=(img['result'][1]['to'])))[:7]}""")

  @commands.command()
  async def translate(self, ctx, *, input):
    lang = input[:+2]
    url = f"https://translation.googleapis.com/language/translate/v2?key={config.translation_key}"
    input = {
      "q": input[+3:],
      "target": lang,
      "format": "text",
      }
    res = requests.post(url, json=input)
    output = json.loads(res.text)
    await ctx.send(f"Detected languege: {output['data']['translations'][0]['detectedSourceLanguage']} \nTranslation: {output['data']['translations'][0]['translatedText']}")

async def setup(Maidchan):
    await Maidchan.add_cog(Utilities(Maidchan))
