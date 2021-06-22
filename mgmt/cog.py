import os
import random

from discord.ext import commands

from util import populous_channel
from .models import Reset

reset_message = f'Next time I\'ll do better...'


class MgmtCommandsCog(commands.Cog, name='Management Commands'):

    @commands.command(aliases=['restart', 'reboot', 'stop_crashing'])
    async def reset(self, ctx):
        """Restarts the bot"""
        await ctx.send(reset_message)
        Reset.create(channel_id=ctx.channel.id)
        async with ctx.typing():
            os.system(r"python reset_bot.py")

    @commands.command(aliases=['random'])
    async def random_user(self, ctx):
        """Selects a random user from the most populous voice channel"""
        voice_channel = ctx.bot.get_channel(populous_channel(ctx))
        members = list(voice_channel.members)
        chosen = random.choice(members)
        snd = chosen.nick if chosen.nick else chosen
        await ctx.send(snd)


def setup(bot):
    bot.add_cog(MgmtCommandsCog(bot))
