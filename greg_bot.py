import discord
from discord.ext.commands import Bot
import random
from discord.ext import commands
import asyncio
from requests_html import HTMLSession
import time
import json
import praw
import pprint
import numpy as np
import requests

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
                                                   "**[4] !meme :** provides you with one spicy meme –– only use in goof\n"
                                                   "**[5] !info :** information about Greg\n" % (userID))

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

    if message.content.lower().startswith('!info'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Here is Greg's information:\n"
                                               "**Who is Greg? :** I'm a bot made to entertain you plebeians\n"
                                               "**Who made Greg? :** Dude named Micah. Pretty cool if you ask me...\n"
                                               "**Do you want more of Greg? :** Ask Micah to make me cooler with more features\n" % (
                                  userID))

    if message.content.lower().startswith('greg'):
        userID = message.author.id
        await client.send_message(message.channel, "Hey, <@%s>! Type !help for a list of commands" % (userID))

    if message.content.lower().startswith('!meme'):
        userID = message.author.id
        reddit = praw.Reddit(client_id='_AEXMPgAMMzAyQ',
                             client_secret='Cdzk9VgV6nTmsP1D7Wr-zcoGyBw',
                             password='12344321',
                             user_agent='reddit api for greg bot',
                             username='MekaMuffin')
        meme_urls = []
        for submission in reddit.subreddit('dankmemes').hot(): # Change this to change the subreddit from which the memes are scraped
            meme_urls.append(submission.url)
        randidx = random.randint(0, len(meme_urls))
        await client.send_message(message.channel, "Here's your filthy meme, <@%s>: %s" % (userID, meme_urls[randidx]))

    if message.content.lower().startswith("i'm bored") or message.content.lower().startswith("im bored"):
        userID = message.author.id

        r = requests.get('https://api.giphy.com/v1/gifs/random?api_key=828kbYMfdDPSdI8XyeilltFHRdAL8Uhu&tag=&rating=PG')
        json_r = r.json()
        gif_url = json_r['data']['embed_url']
        await client.send_message(message.channel, "Well, <@%s>, enjoy this: %s" % (userID, gif_url))

client.run(TOKEN)