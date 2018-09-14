import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from requests_html import HTMLSession
import time

Client = discord.Client()
client = commands.Bot(command_prefix="!")

TOKEN = 'NDkwMDI2ODcyNzcyNjI0Mzg0.DnzU0Q._tl4cCTNKbpWf3SKjdXnMmKQMt0'

@client.event
async def on_ready():
    print("Greg is online and connected to Discord!")

@client.event
async def on_message(message):
    if message.content.lower().startswith('!help'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Below are a list of commands to use with Greg:\n"
                                                   "**[1] !help :** displays a list of available commands\n"
                                                   "**[2] !manual :** provides links to FTC manuals for the 2018-19 season\n"
                                                   "**[3] !quote :** sends a random quote for your reading pleasure\n"
                                                   "**[4] !info :** information about Greg\n" % (userID))

    if message.content.lower().startswith('!quote'):
        session = HTMLSession()
        r = session.get('https://www.eduro.com')
        quote = r.html.find('dailyquote', first=True)
        author = r.html.find('.author', first=True)
        await client.send_message(message.channel, str(quote.text))

    if message.content.lower().startswith('!manual'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Here is the 2018-19 FTC manual:\n"
                                               "**Part One :** https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/game-manual-part-1.pdf\n"
                                               "**Part Two :** https://firstinspiresst01.blob.core.windows.net/ftc/2019/gemf2.pdf\n"
                                               "**Game Description :** https://firstinspiresst01.blob.core.windows.net/ftc/2019/gonemlpg.pdf\n" % (
                                  userID))

    if message.content.lower().startswith('greg'):
        userID = message.author.id
        await client.send_message(message.channel, "Hey, <@%s>! Type !help for a list of commands" % (userID))

client.run(TOKEN)