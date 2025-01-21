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
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")
        
bot.run(discord_token)