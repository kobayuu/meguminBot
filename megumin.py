import discord
import random
import os
import json
from discord.ext import commands

client = commands.Bot(command_prefix='k?')

with open('./tkn.json') as f:
    token = json.load(f)
    print(token)


@client.event
async def on_member_join(member):
    print(f'{member}...募集の張り紙見させてもらいました')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('k?help 爆裂魔法を勉強している'))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('comando inválido.')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send('vai tomar no cu que saco, você não manda em mim')


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms')


@client.command(aliases=['8ball', '8bola'])
async def _8ball(ctx, *, pergunta):
    respostas = [

        'Sim!'
        'Com certeza!',
        'Acho que sim.',
        'Talvez.',
        'Sabe deus.',
        'Acho que não.',
        'De maneira alguma.',
        'Não.',
        'むり！！.',
        'Pergunte mais tarde',
        'Fontes indicam o contrário.',
        'É amigos.',
        ]
    await ctx.send(f' "{pergunta}" você me pergunta...  {random.choice(respostas)}')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 2):
    await ctx.channel.purge(limit=amount)
    await ctx.send('Mensagens apagadas!')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} reloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(token)

