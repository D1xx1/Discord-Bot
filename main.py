import discord
import random

from discord.ext import commands
from config import settings

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'READY, logged on as {self.user}!')
    async def on_message(self, message):
        if message.content.startswith('!hello'): #say hello in English
            author = message.author
            await message.channel.send(f'Hello, {author.mention}!')

        if message.content.startswith('!привет'): #say hello in Russian
            author = message.author
            await message.channel.send(f'Привет, {author.mention}')

        if message.content.startswith('!roll'): #random generator
            if message.content[5::1] == '':
                arg = 100
            else:
                arg = message.content[6::1]
                print(arg)
            try:
                if int(arg) < 0:
                    a = random.randint(int(arg), 0)
                    await message.channel.send(a)
                    print(a)
                    return
                else: 
                    a = random.randint(0,int(arg))
                    await message.channel.send(a)
                    print(a)
                    return
            except ValueError:
                author = message.author
                await message.channel.send(f'{author.mention}, введи число!')
                return

dsbot=MyClient()
dsbot.run(settings['token'])