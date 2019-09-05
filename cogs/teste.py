import discord
from discord.ext import commands


class Curso(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def teste(self, ctx):
        await ctx.send('funcou')


def setup(client):
    client.add_cog(Curso(client))