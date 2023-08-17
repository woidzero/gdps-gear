import discord
from discord.ext import bridge


class Leaderboard(discord.Cog):
    def __init__(self, bot: bridge.Bot) -> None:
        self.bot = bot


def setup(bot: bridge.Bot) -> None:
    bot.add_cog(Leaderboard(bot))
