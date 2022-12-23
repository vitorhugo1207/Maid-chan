import discord, youtube_dl
from discord.ext import commands
from config import CREATOR

class Music(commands.Cog):
  def __init__(self, Maidchan):
    self.Maidchan = Maidchan
    self.creator = CREATOR

  def check_if_creator(self, ctx):
    if str(ctx.author.id) != str(self.creator):
      await ctx.send("Oh dear Master, I'm so sorry but I'm only available for my creator to use! You can't use me yet. Be a good little Master and wait patiently until I'm released to the public, okay? I promise it won't be long~")
      return False
    return True

  @commands.command()
  async def join(self, ctx):
    if not self.check_if_creator(ctx): return
    if ctx.author.voice is None:
      await ctx.send("Master, you need to be in a voice channel for me to join you!")
    else:
      await ctx.send("Joining you now Master! Just a moment please~") 
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)

  @commands.command()
  async def leave(self, ctx):
    if not self.check_if_creator(ctx):
      return
    await ctx.voice_client.disconnect()

  @commands.command()
  async def stop(self, ctx):
    if not self.check_if_creator(ctx):
      return
    ctx.voice_client.stop()

  @commands.command()
  async def play(self, ctx, url):
    if not self.check_if_creator(ctx):
      return
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
    try:
      vc.play(source)
    except:
      await ctx.send('Master, try the command "join" before this.')

  @commands.command()
  async def pause(self, ctx):
    if not self.check_if_creator(ctx):
      return
    ctx.voice_client.pause()
    await ctx.send('Music paused master! ⏸')

  @commands.command()
  async def resume(self, ctx):
    if not self.check_if_creator(ctx):
      return
    ctx.voice_client.resume()
    await ctx.send('Music resumed master! ▶️')

  # @commands.command()
  # async def test(self, ctx):
  #   if ctx.voice_client.is_playing():
  #     await ctx.reply("Master I'm playing music!")
  #   else:
  #     await ctx.reply("Master I'm not playing music!")

async def setup(Maidchan):
  await Maidchan.add_cog(Music(Maidchan))
