import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello( ctx):
        await ctx.reply(f'Hello {ctx.author.mention}')

    @commands.command()
    async def troll(self, ctx, count: int):
        if str(ctx.author.id) != user_id:
            await ctx.reply(f'{ctx.author.mention}, You are not allowed to use this command')
            return
        for i in range(count):
            await ctx.send(f'Spamming messages...{i}x')

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def show_repo(self, ctx):
        await ctx.reply('The code repository of this chatbot is on https://github.com/zenoooooooooo/ZenoBot-discord')
        
def setup(bot):
    bot.add_cog(General(bot)) 
