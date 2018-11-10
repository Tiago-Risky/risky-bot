import discord
import asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient

TOKEN = 'insert the token here'

startup_extensions = ["music"]

bot = commands.Bot(description="Risky Bot", command_prefix="!", pm_help=False)
@bot.event
async def on_ready():
    print("Risky Bot is online and ready")
    return await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('BANG BANG BANG'))

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(name="members",pass_context=True)
@commands.has_permissions(manage_guild=True)
async def members(ctx):
    server= ctx.guild
    x = server.members
    F = open('members.txt', 'wb')
    for member in x:
        linha = member.name + '\r\n'
        F.write(linha.encode("utf-8"))
    F.close()
    msg = 'Members\' list is ready'
    await ctx.send(msg, file=discord.File('members.txt', 'members.txt'))

@members.error
async def members_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = "You're not an admin"
        await ctx.send(msg)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{} {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


bot.run(TOKEN)