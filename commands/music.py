from time import time
import discord
from discord.ext import commands
import json
import youtube_dl
import time
import os

class Music(commands.Cog):
    def __init__(self, Maidchan):
        self.Maidchan = Maidchan
        with open('config.json') as r:
            configJSON = json.load(r)
            self.creator = configJSON['creator']
    
    @commands.command()
    async def join(self, ctx):
        if str(ctx.author.id) == str(self.creator):
            if ctx.author.voice is None:
                await ctx.send("Master, you aren't in a voice channel.")
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)
        else:
            await ctx.send("Sorry Master, but this Command is in Alpha Version, so you can't use it yet.")
    
    @commands.command()
    async def leave(self, ctx):
        if str(ctx.author.id) == str(self.creator):
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("Sorry Master, but this Command is in Alpha Version, so you can't use it yet.")

    @commands.command()
    async def stop(self, ctx):
        if str(ctx.author.id) == str(self.creator):
            ctx.voice_client.stop()
        else:
            await ctx.send("Sorry Master, but this Command is in Alpha Version, so you can't use it yet.")

    @commands.command()
    async def play(self, ctx, url):
        if str(ctx.author.id) == str(self.creator):
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
            os.system('clear'),
        else:
            await ctx.send("Sorry Master, but this Command is in Alpha Version, so you can't use it yet.")
                
    @commands.command()
    async def pause(self, ctx):
        if str(ctx.author.id) == str(self.creator):
            ctx.voice_client.pause()
            await ctx.send('Music paused master! ⏸')
            os.system('clear')
        else:
            await ctx.send("Sorry Master, but this Command is in Alpha Version, so you can't use it yet.")

    @commands.command()
    async def resume(self, ctx):
        if str(ctx.author.id) == str(self.creator):
            ctx.voice_client.resume()
            await ctx.send('Music resumed master! ▶️')
        else:
            await ctx.send("Sorry Master, but this Command is in Alpha Version, so you can't use it yet.")

    # @commands.command()
    # async def test(self, ctx):
    #     if ctx.voice_client.is_playing():
    #         await ctx.reply("playing")
    #     else:
    #         await ctx.reply("none")

async def setup(Maidchan):
    await Maidchan.add_cog(Music(Maidchan))
