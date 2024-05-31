import asyncio
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))  # type: ignore

bot = discord.Bot(debug_guilds=[GUILD_ID])


@bot.slash_command(name="muterng")
@discord.default_permissions(mute_members=True)
async def hello(ctx: discord.ApplicationContext) -> None:
    voice = ctx.author.voice  # type: ignore

    if not voice:
        await ctx.respond("You are not in a voice channel")
        return

    users = list(voice.channel.voice_states.keys())  # type: ignore

    user = await ctx.guild.fetch_member(random.choice(users))  # type: ignore

    if not user:
        await ctx.respond("Command Failed!")
        return

    await user.edit(mute=True)
    await ctx.respond(f"{user.display_name} has been muted for 20 seconds")
    await asyncio.sleep(20)
    await user.edit(mute=False)


@bot.event
async def on_ready() -> None:
    print(f"{bot.user} is Online!")


bot.run(TOKEN)  # type: ignore
