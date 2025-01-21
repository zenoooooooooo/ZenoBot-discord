import discord
from discord.ext import commands

class Commands(commands.Cog):
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

def setup(bot):
    bot.add_cog(Commands(bot)) 
