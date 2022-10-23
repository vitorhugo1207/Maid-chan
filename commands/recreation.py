import discord
from discord.ext import commands
from commands.engine.dice.Dice import *

class Recreation(commands.Cog):
    def __init__(self, Maidchan):
        self.Maidchan = Maidchan

    @commands.command()
    async def dice(self, ctx, *, dice):
        diceImport = diceMain(dice)
        diceImport.main()
        await ctx.send(f'{dice}\n{diceImport.rollList} -> {diceImport.rollTotal}')


async def setup(Maidchan):
    await Maidchan.add_cog(Recreation(Maidchan))
