import discord
import asyncio
from discord.ext import commands

class General:
    # General purpose commands, these are meant to be further organised in other modules, if needed
    __slots__: ('bot', 'current_game', 'current_status')

    def __init__(self, bot):
        self.bot = bot
        self.current_game = ''
        self.current_status = ''
    
    #Command to change the status
    @commands.command(name="status",pass_context=True)
    @commands.is_owner()
    async def change_status(self, ctx, arg="noarg"):
        options = {"on": discord.Status.online,
                    "online": discord.Status.online,
                    "off": discord.Status.invisible,
                    "offline": discord.Status.invisible,
                    "invisible": discord.Status.invisible,
                    "dnd": discord.Status.dnd,
                    "away": discord.Status.idle,
                    "idle": discord.Status.idle}
        arg = arg.strip()
        if arg in options:
            bot = self.bot # Why doesn't this work directly with self.bot.change_presence
            self.current_status = options[arg]
            await bot.change_presence(status=self.current_status,activity=discord.Game(self.current_game))
            await ctx.send("Status changed")
        else:
            raise commands.BadArgument

    @change_status.error
    async def change_status_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            msg = "You're not the bot owner"
            await ctx.send(msg)
        if isinstance(error, commands.BadArgument):
            msg = "That status is invalid"
            await ctx.send(msg)

    #Command to change currently playing game
    @commands.command(name="activity",pass_context=True)
    @commands.is_owner()
    async def change_activity(self, ctx, *, arg="noarg"):
        arg = arg.strip()
        if arg != "noarg":
            self.current_game = arg
            bot = self.bot
            await bot.change_presence(status=self.current_status,activity=discord.Game(self.current_game))
            await ctx.send("Activity changed")
        else:
            self.current_game = ''
            bot = self.bot
            await bot.change_presence(status=self.current_status,activity=None)
            await ctx.send("Activity changed")

    @change_activity.error
    async def change_activity_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            msg = "You're not the bot owner"
            await ctx.send(msg)
        if isinstance(error, commands.BadArgument):
            msg = "That activity is invalid"
            await ctx.send(msg)

    @commands.command(name="members",pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def members(self, ctx):
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
    async def members_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            msg = "You're not an admin"
            await ctx.send(msg)

def setup(bot):
    bot.add_cog(General(bot))