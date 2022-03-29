import discord
import random
import roles

from discord.ext import commands
from config import settings

fkbot = commands.Bot(command_prefix = settings['prefix'])
@fkbot.event
async def on_ready():
    print(f'READY')

@fkbot.event
async def on_raw_reaction_add(payload):
    messageID = payload.message_id

    if messageID == roles.ROLE_POST:
        member = payload.member
        guild = member.guild
        emoji = payload.emoji.name

        if emoji == '🤖':
            role = discord.utils.get(guild.roles, name='ВОДНИК')
        if emoji == '👾':
            role = discord.utils.get(guild.roles, name='Twitch')
        if emoji == '💻':
            role = discord.utils.get(guild.roles, name ='!dev')
        await member.add_roles(role)

@fkbot.event
async def on_raw_reaction_remove(payload):
    messageID = payload.message_id

    if messageID == roles.ROLE_POST:
        guild = await(fkbot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name

        if emoji == '🤖':
            role = discord.utils.get(guild.roles, name='ВОДНИК')
        if emoji == '👾':
            role = discord.utils.get(guild.roles, name='Twitch')
        if emoji == '💻':
            role = discord.utils.get(guild.roles, name ='!dev')
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("Пользователь не найден")

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
@fkbot.command()
async def react(ctx):
    embed = discord.Embed(
        title="Выдача ролей",
        description='Для получения роли нажмите на реакцию: \n🤖 - Водник \n👾 - Twitch \n💻 - !dev',
        color=0x2ecc71
    )
    msg= await ctx.send(embed=embed)
    await msg.add_reaction('🤖')
    await msg.add_reaction('👾')
    await msg.add_reaction('💻')


fkbot.run(settings['token'])