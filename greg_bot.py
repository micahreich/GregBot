import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from requests_html import HTMLSession
import time
import json
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
                                                   "**[4] !tictac :** starts up a good 'ole game of tic-tac-toe with Greg\n"
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

    if message.content.lower().startswith("i'm bored") or message.content.lower().startswith("im bored"):
        userID = message.author.id

        r = requests.get('https://api.giphy.com/v1/gifs/random?api_key=828kbYMfdDPSdI8XyeilltFHRdAL8Uhu&tag=&rating=PG')
        json_r = r.json()
        gif_url = json_r['data']['embed_url']
        await client.send_message(message.channel, "Well, <@%s>, enjoy this: %s" % (userID, gif_url))

    if message.content.lower().startswith("!tictac"):
        userID = message.author.id
        await client.send_message(message.channel, "Hey, <@%s>! Let's play tic-tac-toe; you can go first! \n**Input your moves as coordinates in the order of column, row, e.x. 1,3 = bottom left corner" % (userID))
        board = [[':black_large_square:', ':black_large_square:', ':black_large_square:'],
                 [':black_large_square:', ':black_large_square:', ':black_large_square:'],
                 [':black_large_square:', ':black_large_square:', ':black_large_square:']]

        def boardToString(arr):
            board_as_str = ""
            for i in board:
                for j in i:
                    board_as_str += j
                board_as_str += '\n'

            client.send_message(message.channel, board_as_str)

        gameStatus = False

        while gameStatus == False:
            boardToString(board)
            client.send_message(message.channel, "Your turn, <@%s>" % (userID))
            
            if message.content.lower() == "1,1":
                board[0][0] = ':x:'
            if message.content.lower() == "1,2":
                board[0][1] = ':x:'
            if message.content.lower() == "1,3":
                board[0][2] = ':x:'

            if message.content.lower() == "2,1":
                board[1][0] = ':x:'
            if message.content.lower() == "2,2":
                board[1][1] = ':x:'
            if message.content.lower() == "2,3":
                board[1][2] = ':x:'

            if message.content.lower() == "3,1":
                board[2][0] = ':x:'
            if message.content.lower() == "3,2":
                board[2][1] = ':x:'
            if message.content.lower() == "3,3":
                board[2][2] = ':x:'
            boardToString(board)

            client.send_message(message.channel, "Greg's turn")
            foundSpot = False
            while foundSpot == False:
                rind1 = np.random.randint(0, len(board[0]))
                rind2 = np.random.randint(0, len(board[1]))
                if board[rind1][rind2] == ":black_large_square:":
                    board[rind1][rind2] = ":o:"
                    foundSpot == True
                    boardToString(board)
                    break

            if (board[0][0] == ':x:' and board[1][0] == ':x:' and board[2][0] == ':x:') \
                    or (board[0][1] == ':x:' and board[1][1] == ':x:' and board[2][1] == ':x:') \
                    or (board[0][2] == ':x:' and board[1][2] == ':x:' and board[2][2] == ':x:') \
                    or (board[0][0] == ':x:' and board[0][1] == ':x:' and board[0][2] == ':x:') \
                    or (board[1][0] == ':x:' and board[1][1] == ':x:' and board[1][2] == ':x:') \
                    or (board[2][0] == ':x:' and board[2][1] == ':x:' and board[2][2] == ':x:') \
                    or (board[0][0] == ':x:' and board[1][1] == ':x:' and board[2][2] == ':x:') \
                    or (board[0][2] == ':x:' and board[1][1] == ':x:' and board[2][2] == ':x:'):
                client.send_message(message.channel, "You have won!")
                gameStatus = True

            elif (board[0][0] == ':o:' and board[1][0] == ':o:' and board[2][0] == ':o:') \
                    or (board[0][1] == ':o:' and board[1][1] == ':o:' and board[2][1] == ':o:') \
                    or (board[0][2] == ':o:' and board[1][2] == ':o:' and board[2][2] == ':o:') \
                    or (board[0][0] == ':o:' and board[0][1] == ':o:' and board[0][2] == ':o:') \
                    or (board[1][0] == ':o:' and board[1][1] == ':o:' and board[1][2] == ':o:') \
                    or (board[2][0] == ':o:' and board[2][1] == ':o:' and board[2][2] == ':o:') \
                    or (board[0][0] == ':o:' and board[1][1] == ':o:' and board[2][2] == ':o:') \
                    or (board[0][2] == ':o:' and board[1][1] == ':o:' and board[2][2] == ':o:'):
                client.send_message(message.channel, "Greg has won!")
        else:
            client.send_message(message.channel, "It's a tie!")
            gameStatus = True
client.run(TOKEN)