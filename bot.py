import discord
import asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient

TOKEN = 'insert the token here'

startup_extensions = ["modules.music", "modules.general"]

bot = commands.Bot(description="Risky Bot", command_prefix="!", pm_help=False)
@bot.event
async def on_ready():
    print("Risky Bot is online and ready")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{} {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(TOKEN)