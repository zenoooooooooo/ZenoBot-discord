import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
user_id = os.getenv('USER_ID')
class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.reply(a + b)

    @commands.command()
    async def get_mean(self, ctx, *args: int):
        if not args:
            await ctx.send(f'{ctx.author.mention}, Please provide some numbers')
            return
        
        mean = sum(args) / len(args)
        await ctx.reply(f'The mean of numbers {args} is {mean}')

    @commands.command()
    async def troll(self, ctx, count: int):
        if str(ctx.author.id) != user_id:
            await ctx.reply(f'{ctx.author.mention}, You are not allowed to use this command')
            return
        for i in range(count):
            await ctx.send(f'Spamming messages...{i}x')

def setup(bot):
    bot.add_cog(Math(bot)) 
