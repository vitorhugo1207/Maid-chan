import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, Maidchan):
        self.Maidchan = Maidchan

def setup(Maidchan):
    Maidchan.add_cog(Music(Maidchan))
