import requests
from bs4 import BeautifulSoup
import os
import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix='!', description="NetArt Generator Bot")
slash = SlashCommand(bot, sync_commands=True)
#---------------------------config------------------------------------
token='TOKEN'

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@slash.slash(name="Info", description="Info Command")
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Netart bot", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"0x111")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/O6g_6ZA-NDahp6o3RwIVr7foHN7KjkW5hZBx9YnLZNI/https/nag.iap.de/gen/anonymous-bot%40Mar_7_18.54.58_2022.jpg')

    await ctx.send(embed=embed)

@slash.slash(name="NetArt", description="Info Command")
async def netart(ctx,arg):
    url = 'https://nag.iap.de/?ac=create&name=anonymous&query='+arg+'&comp=100&width=800&ext=jpg'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    for image in images:
        title = image['title']
        link = image['src']
        link = 'https://nag.iap.de/'+link
    await ctx.channel.send(link)

@bot.command()
async def how(ctx):
    await ctx.channel.send("!netart ((searchterm) or (serachterm1+searchterm2))")

bot.run(token)