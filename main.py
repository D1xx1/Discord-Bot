from discord import utils
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
async def roll(ctx, arg='100'):
    try:
        if int(arg) < 0:
            await ctx.send(random.randint(int(arg), 0))
            return
        else: 
            await ctx.send(random.randint(0,int(arg)))
            return
    except ValueError:
        author = ctx.message.author
        await ctx.send(f'{author.mention}, введи число!')
        return

fkbot.run(settings['token'])