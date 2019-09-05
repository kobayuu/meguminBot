import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # comandos
    @commands.Cog.listener()
    async def on_ready(self):
        print('waga na wa Megumin!')

    # eventos
    @commands.command()
    async def e(self, ctx):
        await ctx.send('amigos')


def setup(client):
    client.add_cog(Example(client))
