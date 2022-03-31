import random

from threading import *
from time import sleep
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])

def counter():
    global nowScore
    nowScore = 0
    count = 0
    while True:
        count = count+random.randint(300, 400)
        nowScore = count
        print(count)
        sleep(3)

@bot.command()
async def score(ctx):
    await ctx.send(f'Now score is {str(nowScore)}')

thread1 = Thread(target = counter)
thread1.start()

bot.run(settings['token'])