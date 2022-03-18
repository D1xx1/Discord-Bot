import discord
from discord.ext import commands
from config import settings
#import roles
import random
b = 0
a = 0
fkbot = commands.Bot(command_prefix = settings['prefix'])
@fkbot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')
@fkbot.command()
async def привет(ctx):
    author = ctx.message.author
    await ctx.send(f'Привет, {author.mention}')
@fkbot.command()
async def rnd(ctx,a ,b):
    print(b)
    if b < a:
        a, b = b, a
    elif a==b:
        await ctx.send(a)
        return

    try:
        await ctx.send(random.randrange(int(a),int(b)))
    except ValueError:
        author = ctx.message.author
        await ctx.send(f'{author.mention}, долбоёб, введи число!')

fkbot.run(settings['token'])
