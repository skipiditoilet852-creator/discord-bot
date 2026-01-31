import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

bot.run(os.getenv("MTQ2NTY2NjI0OTkxOTgyODA2Mg.GuAQxb.fA6OnpNA0wXQiMOwoVmJLlCSQocAofZ-K6L7V4"))  # using environment variable for security
