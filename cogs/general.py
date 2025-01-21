import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello( ctx):
        await ctx.reply(f'Hello {ctx.author.mention}')

    @commands.command()
    async def show_commands( ctx):
        command_list = (
            "📋 **Available Commands**:\n\n"
            "➕ **!add <a> <b>**: Add two numbers together\n"
            "📊 **!get_mean <numbers...>**: Calculate the mean of given numbers\n"
            "💥 **!troll <count>**: Spam a specified number of messages\n\n"
            "🐸 **!send_meme <subreddit>**: Fetch a meme from a specified subreddit\n\n"
            "Use `!command_name` to call each command. Enjoy using the bot! 😄"
        )
        await ctx.reply(command_list)
    
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
        
def setup(bot):
    bot.add_cog(General(bot)) 
