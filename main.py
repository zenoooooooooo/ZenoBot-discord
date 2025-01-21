import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

class Main(commands.Bot):
    def __init__(self, intents):
        super().__init__(intents=intents, command_prefix='!')

    async def on_ready(self):
        print('Bot is now ready to do anything!')


intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True  

bot = Main(intents=intents)

@bot.command()
async def hello( ctx):
        await ctx.send(f'Hello {ctx.author.mention}')

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

    await ctx.send(command_list)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(discord_token)