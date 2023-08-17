import discord
from discord.ext import bridge, commands


class MyCog(discord.Cog):
    def __init__(self, bot: bridge.Bot) -> None:
        self.bot = bot

    @bridge.bridge_group(name="account", description="Account linking")
    async def account(self) -> None:
        pass

    @account.command(name="help", description="Account linking help")
    async def help(self, ctx) -> None:
        pass
        emb = discord.Embed(
            description="""
        **────── Account linking**
        1: Go to GDPS website and login.
        2: Go to `Profile` and copy the token from `Link code` field.
        3: Write this command in the bot's DM: `g?account link <link code>` .

        **────── Account commands**
        » Unlink your account: `g?account unlink`.
        » View your account info: `g?profile`.
        » View your GDPS levels: `g?profile levels`.
        """
        )
        emb.set_author(
            name="How link account to the bot?",
            icon_url="https://cdn.discordapp.com/emojis/855111075379675137.png",
        )
        await ctx.reply(embed=emb)

    @commands.dm_only()
    @account.command(name="link")
    async def link(self, ctx: bridge.Context, code: str) -> None:
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.reply("soon")

    @commands.dm_only()
    @account.command(name="unlink")
    async def unlink(self, ctx: bridge.Context) -> None:
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.reply("soon")


def setup(bot: bridge.Bot) -> None:
    bot.add_cog(MyCog(bot))
