import discord
from discord.ext import commands
import json
import os
from pyson import pyson

# atualmente não funciona :p

bancoDoBrasil = pyson('bancoDoBrasil')


if 'name' not in bancoDoBrasil.data:
    bancoDoBrasil.data['name'] = '円'


def checkId(ID):
    if ID not in bancoDoBrasil.data:
        bancoDoBrasil.data[ID] = 0
        bancoDoBrasil.save()


class Okane(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def daily(self, ctx, amount):
        ID = ctx.author.id
        checkId(ID)
        print(ID)
        amount = int(amount)
        print(amount)
        bancoDoBrasil.data[ID] += amount
        bancoDoBrasil.save()
        await ctx.send(f'{amount}{bancoDoBrasil.data["name"]} foram adicionados a conta de{ctx.author.mention}')


def setup(client):
    client.add_cog(Okane(client))
