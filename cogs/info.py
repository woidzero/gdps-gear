import discord
from discord.ext import bridge

from misc.config import CONFIG


class Other(discord.Cog):
    def __init__(self, bot: bridge.Bot) -> None:
        self.bot = bot
        self.bot.remove_command("help")

    @bridge.bridge_command()
    async def ping(self, ctx):
        emb = discord.Embed(
            description=f"Pong! ``{round(self.bot.latency * 1000)}``ms."
        )
        emb.set_author(name="Ping")
        await ctx.reply(embed=emb)

    @bridge.bridge_command()
    async def help(self, ctx):
        prefix = {CONFIG["prefix"]}
        emb = discord.Embed(
            description=f"""
            Prefix: {prefix}\n
            **────── GDPS**
            `{prefix}profile <nickname>` : View GDPS user profile.
            `{prefix}level <id>` : View the level information.
            `{prefix}leaders <query>` : View the GDPS leaderboard.
            `{prefix}weekly` : Weekly level info.
            `{prefix}daily` : Daily level info.\n
            **────── Other**
            `{prefix}ping` : Discord WebSocket latency.
            `{prefix}help` : Commands list.
            """
        )
        emb.set_author(
            name="Commands List",
            icon_url="https://cdn.discordapp.com/emojis/855111075379675137.png",
        )
        await ctx.reply(embed=emb)


def setup(bot: bridge.Bot) -> None:
    bot.add_cog(Other(bot))
