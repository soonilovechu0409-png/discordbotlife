import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!" , intents=intents)

@bot.event
async def on_ready():
	print("봇이 온라인 상태입니다!")

@bot.command()
async def 노술게이(ctx):
	await ctx.send("노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다 노술은 게이다")

from datetime import timedelta
import discord
from discord.ext import commands

@bot.command()
@commands.has_permissions(moderate_members=True)
async def 타임아웃(ctx, member: discord.Member, minutes: int):
    try:
        await member.timeout(
            timedelta(minutes=minutes),
            reason=f"{ctx.author}에 의해 타임아웃"
        )
        await ctx.send(f"⏱️ {member.mention} 님을 {minutes}분 동안 타임아웃했어요.")
    except Exception as e:
        await ctx.send("❌ 타임아웃을 할 수 없어요.")
@bot.command()
@commands.has_permissions(moderate_members=True)
async def 타임아웃해제(ctx, member: discord.Member):
    await member.timeout(None)
    await ctx.send(f"✅ {member.mention} 님의 타임아웃을 해제했어요.")

bot.run("TOKEN")

import os
bot.run(os.getenv("TOKEN")


