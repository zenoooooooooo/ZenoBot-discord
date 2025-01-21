import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def hello( ctx):
        await ctx.reply(f'Hello {ctx.author.mention}')

    @bot.command()
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
    

def setup(bot):
    bot.add_cog(General(bot)) 
