import discord
from discord.ext import commands
from config import settings
import random
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
async def roll(ctx, arg):
    if int(arg) < 0:
        await ctx.send(random.randint(int(arg), 0))
    else:
        try:
            await ctx.send(random.randint(0,int(arg)))
        except ValueError:
            author = ctx.message.author
            await ctx.send(f'{author.mention}, введи число!')

fkbot.run(settings['token'])