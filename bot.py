import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.', case_insensitive=True)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Moderating SAF'))




@client.event
async def on_message(message):
    
    if message.content == 'No u':
        general_channel = client.get_channel(766993851776106526)
        await general_channel.send('no u') 

    await client.process_commands(message)

@client.command()
async def Check(ctx): #You need to pass context here.
  await ctx.send('')


@client.command(name='ping')
async def ping(context):
    """
    A Command Used To Find Your Ping!
    """

    await context.message.channel.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
     await ctx.channel.purge(limit=amount)

@commands.command()
@commands.guild_only()
@commands.has_guild_permissions(ban_members=True)
async def kick(self, ctx, member: discord.Member , *, reason=None):
    await ctx.guild.kick(user=member, reason=reason)

@commands.command()
@commands.guild_only()
@commands.has_guild_permissions(ban_members=True)
async def ban(self, ctx, member: discord.Member , *, reason=None):
    await ctx.guild.ban(user=member, reason=reason)

@commands.command()
@commands.guild_only()
@commands.has_guild_permissions(ban_members=True)
async def unban(self, ctx, member, *, reason=None):
    member = await self.bot.fetch_user(int(member))
    await ctx.guild.unban(member, reason=reason)


client.run('NzY5NzcyNzIxMDUxNTMzMzIy.X5T4tg.HZn8w3oa7ibJORpuARmU_p1teBs')
