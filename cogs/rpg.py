import discord
import random
from discord.ext import commands


class Rpg(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dice(self, ctx, n):
        n = int(n)
        nickname = str(ctx.author.mention)
        print(f'{nickname}')
        await ctx.send(f'{nickname}, seu resultado foi {random.randrange(1, n)}')


def setup(client):
    client.add_cog(Rpg(client))


