import discord
import requests
from discord.ext import commands

class Api(commands.Cog):
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

    @commands.command()
    async def send_quote(self, ctx):
        response = requests.get('https://quotes-api-self.vercel.app/quote')
        quote = response.json()['quote']
        author = response.json()['author']
        await ctx.reply(f'{quote}\n~ {author}')

def setup(bot):
    bot.add_cog(Api(bot)) 
