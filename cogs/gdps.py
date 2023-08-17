"""
GDPSGear
~~~~~~~~~~~~~~~~~~~
Discord bot for managing Geometry Dash IOCore based private servers

:copyright: (c) 2023 woidzero
:license: MIT, see LICENSE for more details.
"""

from datetime import datetime

import aiohttp
import discord
from discord.ext import bridge

from misc.config import CONFIG
from misc.utils import fetch_rank, fetch_role


class GDPS(discord.Cog):
    def __init__(self, bot: bridge.Bot) -> None:
        self.bot = bot
        self.endpoint = CONFIG["gdps_api"]

    @bridge.bridge_command(name="profile", description="Information about profile")
    async def profile(self, ctx, name: str) -> None:
        try:
            async with aiohttp.ClientSession() as se:
                req = await se.get(self.endpoint + "/getUserInfo.php?username={name}")
                res = await req.json(content_type="text/html")

            twitch = "**None**"
            twitter = "**None**"
            youtube = "**None**"

            if res["tw"]:
                twitch = f"**[Redirect](https://twitch.com/{res['tw']})**"
            if res["th"]:
                twitter = f"**[Redirect](https://twitter.com/{res['th']})**"
            if res["yt"]:
                youtube = f"**[Redirect](https://youtube.com/channel/{res['yt']})**"

            lp = datetime.utcfromtimestamp(int(res["time"])).strftime(
                "%d/%m/%Y %H:%M:%S"
            )
            rd = datetime.utcfromtimestamp(int(res["regdate"])).strftime(
                "%d/%m/%Y %H:%M:%S"
            )

            frs = "**Open**"
            ms = "**From All**"
            cs = "**Open**"

            if res["frs"] == "1":
                frs = "**Closed**"
            if res["ms"] == "1":
                ms = "**From Friends**"
            if res["ms"] == "2":
                ms = "**Closed**"
            if res["cs"] == "1":
                cs = "**Closed**"

            emb = discord.Embed(
                description=f"""
                **────── Player stats {res['user_name']}**
                <:r:934846351949312070> Stars: **{res['stars']}**
                <:r:934852496927621220> Diamonds: **{res['diamonds']}**
                <:r:934846351731208314> Secret Coins: **{res['coins']}**
                <:r:934846351949312000> User Coins: **{res['ucoins']}**
                <:r:934846351919943733> Demons: **{res['demons']}**
                <:r:934846351806713886> Creator Points: **{res['creatorPoints']}**\n
                **────── Common information**
                <:r:934854253237899275> Role: **{fetch_role(res["role"])}**
                <:r:934854252789129226> Last Online: **{lp}**
                <:r:934846351877996594> Registered: **{rd}**
                <:r:934854252805890128> Rank: **{fetch_rank(res["rank"])}**\n
                **────── Social network links**
                <:r:934846352075149413> YouTube: {youtube}
                <:r:934846351974481991> Twitch: {twitch}
                <:r:934846351974486016> Twitter: {twitter}
                <:r:962414962431643768> Discord: **None**\n
                **────── Friends & comments**
                <:r:934854996233695255> Friend Requests: **{frs}**
                <:r:934854252927528990> Private Messages: **{ms}**
                <:r:934854253053354074> Comment History: **{cs}**
                """
            )
            emb.set_author(name="Profile")
            emb.set_thumbnail(url=res["iconSprite"])
            emb.set_footer(
                text=f"Account ID: {res['accountID']} | User ID: {res['userID']}"
            )

            await ctx.respond(embed=emb)
        except Exception as err:
            print(err)
            if res["message"]:
                await ctx.respond(embed=discord.Embed(description=res["message"]))

    @bridge.bridge_command(name="level", description="Level information")
    async def level(self, ctx, id):
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.get(
                    f"{self.server}/getLevelInfo.php?levelid={id}"
                )
                res = await response.json(content_type="text/html")

                ud = datetime.utcfromtimestamp(int(res["date"])).strftime(
                    "%d/%m/%Y %H:%M:%S"
                )

                lenght = "**Неизвестно**"

                if res["length"] == "0":
                    lenght = "**Tiny**"
                if res["length"] == "1":
                    lenght = "**Short**"
                if res["length"] == "2":
                    lenght = "**Medium**"
                if res["length"] == "3":
                    lenght = "**Long**"
                if res["length"] == "4":
                    lenght = "**XL**"

                likes = int(res["likes"])

                if likes < 0:
                    likes = f"<:r:934854253263081482> Dislikes: **{res['likes']}**"
                elif likes >= 0:
                    likes = f"<:r:934846351966105610> Likes: **{res['likes']}**"

                coins = "**None**"
                if res["coins"] == "1":
                    coins = "<:r:934846351949312000>"
                if res["coins"] == "2":
                    coins = "<:r:934846351949312000> <:r:934846351949312000>"
                if res["coins"] == "3":
                    coins = "<:r:934846351949312000> <:r:934846351949312000> <:r:934846351949312000>"

                listed = "**Listed**"
                if res["unlisted"] == "1":
                    listed = "**Unlisted**"

                objects = int(res["objects"])
                if objects > 60000:
                    objects = f"{res['objects']} <:r:960558095434645616>"

                desc = f"`{res['descd']}`"
                if res["descd"] == "":
                    desc = "**Not provided**"

                emb = discord.Embed(
                    description=f"""
                    **────── {res['name']} Stats**
                    {likes}
                    <:r:934854253581856848> Downloads: **{res['dwls']}**
                    <:r:934846351949312000> Coins: **{coins}**
                    <:r:934854252789129226> Length: **{lenght}**\n
                    **────── About Level**
                    <:r:934854253237899275> Author: **{res['author']}**
                    <:r:960558411488063508> Description: **{desc}**
                    <:r:934846351877996594> Published: **{ud}**
                    <:r:934846351932547132> Objects: **{objects}**
                    <:r:934854252659085413> Status: **{listed}**\n
                    """
                )
                emb.set_author(name="Level Info")
                emb.set_thumbnail(url=res["rate_icon"])
                emb.set_footer(text=f"ID: {id}")
                await ctx.respond(embed=emb, mention_author=False)
        except Exception as err:
            print(err)

    @bridge.bridge_command(name="daily", description="Information about daily level")
    async def daily(self, ctx):
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.get(f"{self.server}/getDailyLevel.php")
                res = await response.json(content_type="text/html")

                ud = datetime.utcfromtimestamp(int(res["date"])).strftime(
                    "%d/%m/%Y %H:%M:%S"
                )

                lenght = "**Unknown**"

                if res["length"] == "0":
                    lenght = "**Tiny**"
                if res["length"] == "1":
                    lenght = "**Short**"
                if res["length"] == "2":
                    lenght = "**Medium**"
                if res["length"] == "3":
                    lenght = "**Long**"
                if res["length"] == "4":
                    lenght = "**XL**"

                likes = int(res["likes"])

                if likes < 0:
                    likes = f"<:r:934854253263081482> Dislikes: **{res['likes']}**"
                elif likes >= 0:
                    likes = f"<:r:934846351966105610> Likes: **{res['likes']}**"

                coins = "**None**"
                if res["coins"] == "1":
                    coins = "<:r:934846351949312000>"
                if res["coins"] == "2":
                    coins = "<:r:934846351949312000> <:r:934846351949312000>"
                if res["coins"] == "3":
                    coins = "<:r:934846351949312000> <:r:934846351949312000> <:r:934846351949312000>"

                listed = "**Listed**"
                if res["unlisted"] == "1":
                    listed = "**Unlisted**"

                objects = int(res["objects"])
                if objects > 60000:
                    objects = f"{res['objects']} <:r:960558095434645616>"

                desc = f"`{res['descd']}`"
                if res["descd"] == "":
                    desc = "**Not provided**"

                emb = discord.Embed(
                    description=f"""
                    **────── {res['name']} Stats**
                    {likes}
                    <:r:934854253581856848> Downloads: **{res['dwls']}**
                    <:r:934846351949312000> Coins: **{coins}**
                    <:r:934854252789129226> Length: **{lenght}**\n
                    **────── About Level**
                    <:r:960558411488063508> Description: **{desc}**
                    <:r:934854253237899275> Author: **{res['author']}**
                    <:r:934846351877996594> Published: **{ud}**
                    <:r:934846351949312070> Rate: **Недоступно**
                    <:r:934846351932547132> Objects: **{objects}**
                    <:r:934854252659085413> Status: **{listed}**\n
                    """
                )
                emb.set_author(name="Daily Level")
                emb.set_footer(text=f"ID: {res['id']} | Featured ID: {res['feaid']}")
                emb.set_thumbnail(url=res["rate_icon"])
                await ctx.reply(embed=emb, mention_author=False)
        except Exception as err:
            print(err)

    @bridge.bridge_command(name="weekly", description="Information about weekly level")
    async def weekly(self, ctx):
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.get(f"{self.server}/getWeeklyLevel.php")
                res = await response.json(content_type="text/html")

                ud = datetime.utcfromtimestamp(int(res["date"])).strftime(
                    "%d/%m/%Y %H:%M:%S"
                )

                length = "**Неизвестно**"

                if res["length"] == "0":
                    length = "**Tiny**"
                if res["length"] == "1":
                    length = "**Short**"
                if res["length"] == "2":
                    length = "**Medium**"
                if res["length"] == "3":
                    length = "**Long**"
                if res["length"] == "4":
                    length = "**XL**"

                likes = int(res["likes"])

                if likes < 0:
                    likes = f"<:r:934854253263081482> Dislikes: **{res['likes']}**"
                elif likes >= 0:
                    likes = f"<:r:934846351966105610> Likes: **{res['likes']}**"

                coins = "**None**"
                if res["coins"] == "1":
                    coins = "<:r:934846351949312000>"
                if res["coins"] == "2":
                    coins = "<:r:934846351949312000> <:r:934846351949312000>"
                if res["coins"] == "3":
                    coins = "<:r:934846351949312000> <:r:934846351949312000> <:r:934846351949312000>"

                listed = "**Listed**"
                if res["unlisted"] == "1":
                    listed = "**Unlisted**"

                objects = int(res["objects"])
                if objects > 60000:
                    objects = f"{res['objects']} <:r:960558095434645616>"

                desc = f"`{res['descd']}`"
                if res["descd"] == "":
                    desc = "**Not provided**"

                emb = discord.Embed(
                    description=f"""
                    **────── {res['name']} Stats**
                    {likes}
                    <:r:934854253581856848> Downloads: **{res['dwls']}**
                    <:r:934846351949312000> Coins: **{coins}**
                    <:r:934854252789129226> Length: **{length}**\n
                    **────── About Level**
                    <:r:960558411488063508> Description: **{desc}**
                    <:r:934854253237899275> Author: **{res['author']}**
                    <:r:934846351877996594> Published: **{ud}**
                    <:r:934846351949312070> Rate: **Недоступно**
                    <:r:934846351932547132> Objects: **{objects}**
                    <:r:934854252659085413> Status: **{listed}**\n
                    """
                )
                emb.set_author(name="Weekly Level")
                emb.set_footer(text=f"ID: {res['id']}")
                emb.set_thumbnail(url=res["rate_icon"])
                await ctx.reply(embed=emb, mention_author=False)
        except Exception as err:
            print(err)


def setup(bot) -> None:
    bot.add_cog(GDPS(bot))
