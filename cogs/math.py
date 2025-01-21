import discord
from discord.ext import commands

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)

    @commands.command()
    async def get_mean(self, ctx, *args: int):
        if not args:
            await ctx.send(f'{ctx.author.mention}, Please provide some numbers')
            return
        
        mean = sum(args) / len(args)
        await ctx.send(f'The mean of numbers {args} is {mean}')

    @commands.command()
    async def troll(self, ctx, count: int):
        for i in range(count):
            await ctx.send(f'{i + 1}. Spamming messages...')

def setup(bot):
    bot.add_cog(Math(bot)) 
