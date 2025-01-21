import discord
import requests
from discord.ext import commands

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def send_meme(self, ctx, subreddit: str):
        response = requests.get(f'https://meme-api.com/gimme/{subreddit}')
        if response.status_code == 200:
            image_url = response.json()['url']
            title = response.json()['title']
            print(image_url)
            await ctx.reply(f'r/{subreddit}\n{title}')
            await ctx.send(image_url)

def setup(bot):
    bot.add_cog(Memes(bot)) 
