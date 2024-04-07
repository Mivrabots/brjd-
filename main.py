import random
import discord 
from discord.ext import commands
import os
import sqlite3 
import aiohttp
import asyncio


TOKEN = os.environ['TOKEN']

# Define the intents
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.members = True

# Create a bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)
# Event: Bot is ready and the status
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')
    print("status is in developement")
    await bot.change_presence(activity=discord.Game(name="in develepment │!commands"))

@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title="Thanks for inviting me!", description="I'm your friendly bot. Let's have some fun!", color=0x00ff00)
    embed.set_thumbnail(url=bot.user.avatar.url)  # Corrected line
    embed.add_field(name="Command Prefix", value="My default prefix is `!`. You can change it with `!setprefix <new_prefix> **in develepment**`", inline=False)
    embed.add_field(name="commands", value="Use `!commands` to see a list of available commands join the support server for more info [here](https://discord.gg/muQqyqwCXa).", inline=False)
    embed.set_footer(text="Have a great time!")
    await guild.system_channel.send(embed=embed)

# Function to check if the user is the owner of the bot
def is_owner(ctx):
    return ctx.author.id == int(os.getenv('OWNER_ID'))

#help command and it add the commands by it self and it add a embed
@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Help/**in development more come**", description="List of available commands:", color=discord.Color.blue())
    embed.add_field(name="!commands", value="Displays this commands message.", inline=False)
    embed.add_field(name="!ping", value="Pings the bot and returns its latency.", inline=False)
    embed.add_field(name="!roll [number]", value="Rolls a dice with the specified number of side. Default is 6.", inline=False)
    embed.add_field(name="!flip", value="Flips a coin.", inline=False)
    embed.add_field(name="!clear [number]", value="Clears the specified number of messages from the channel. Default is 5.", inline=False)
    embed.add_field(name="!command_suggest [command] [description]", value="you suggest a new command .", inline=False)
    embed.add_field(name="!say", value="make the bot say something.", inline=False)
    embed.add_field(name="!userinfo", value="Displays information about the user.", inline=False)
    embed.add_field(name="!serverinfo", value="Displays information about the server.", inline=False)
    embed.add_field(name="!avatar", value="Displays the user's avatar.", inline=False)
    embed.add_field(name="!servericon", value="Displays the server's icon.", inline=False)
    embed.add_field(name="!serverbanner", value="Displays the server's banner.", inline=False)
    embed.add_field(name="!serversplash", value="Displays the server's splash.", inline=False)
    embed.add_field(name="!serverowner", value="Displays the server's owner.", inline=False)
    embed.add_field(name="!serverregion", value="Displays the server's region.", inline=False)
    embed.add_field(name="!serverafkchannel", value="Displays the server's AFK channel.", inline=False)
   

                  
    
    

#to send the embed
    await ctx.send(embed=embed)
#ping command and it pings the bot and return the latency
@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(f'Pong! Latency: **{latency * 1000:.2f}**ms')

#roll command and it rolls a dice with the specified number of side. Default is 6
@bot.command()
async def roll(ctx, sides: int = 6):
    result = random.randint(1, sides)
    await ctx.send(f'You rolled a {sides}-sided dice and got: **{result}**')

#flip command and it flips a coin
@bot.command()
async def flip(ctx):
    result = random.choice(['Heads', 'Tails'])
    await ctx.send(f'You flipped a coin and got: **{result}**')

#clear command and it clears the specified number of messages from the channel. Default is 5
@bot.command()
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Cleared **{amount}** messages.')

#command suggestion command and it add a command suggestion to the bot dev dm
@bot.command()
async def command_suggest(ctx, command: str, description: str):
    # Replace 'YOUR_USER_ID' with your Discord user ID
    user_id = '719648115639975946'
    user = await bot.fetch_user(user_id)
    if user:
        await user.send(f'New command suggestion from {ctx.author.name}:\nCommand: **{command}**\nDescription: **{description}**')
        await ctx.send('Your command suggestion has been sent to the bot developer.')
    else:
        await ctx.send('Failed to send the command suggestion. Please try again later.')

#fun commands
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

#userinfo command and it display the user info
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title="User Info", color=member.color)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name="Username", value=member.name, inline=True)
    embed.add_field(name="Discriminator", value=member.discriminator, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="Joined Discord", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    await ctx.send(embed=embed)

#serverinfo command and it display the server info
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title="Server Info", color=discord.Color.blue())
    embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="Server Name", value=guild.name, inline=True)
    embed.add_field(name="Server ID", value=guild.id, inline=True)
    embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
  
    await ctx.send(embed=embed)

#avatar command and it display the user avatar]
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title="Avatar", color=member.color)
    embed.set_image(url=member.avatar.url)
    await ctx.send(embed=embed)

#servericon command and it display the server icon
@bot.command()
async def servericon(ctx):
    guild = ctx.guild
    embed = discord.Embed(title="Server Icon", color=discord.Color.blue())
    embed.set_image(url=guild.icon.url)
    await ctx.send(embed=embed)

#serverbanner command and it display the server banner
@bot.command()
async def serverbanner(ctx):
    guild = ctx.guild
    if guild.banner:
        embed = discord.Embed(title="Server Banner", color=discord.Color.blue())
        embed.set_image(url=guild.banner.url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("This server does not have a banner.")
    await ctx.send(embed=embed)


#serversplash command and it display the server splash
@bot.command()
async def serversplash(ctx):
    guild = ctx.guild
    if guild.splash:
        embed = discord.Embed(title="Server Splash", color=discord.Color.blue())
        embed.set_image(url=guild.splash.url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("This server does not have a splash.")
    await ctx.send(embed=embed)

#serverowner command and it display the server owner
@bot.command()
async def serverowner(ctx):
    guild = ctx.guild
    owner = guild.owner
    embed = discord.Embed(title="Server Owner", color=discord.Color.blue())
    embed.add_field(name="Owner", value=owner.mention, inline=True)
    await ctx.send(embed=embed)

#serverregion command and it display the server region
@bot.command()
async def serverregion(ctx):
    guild = ctx.guild
    region = guild.region
    embed = discord.Embed(title="Server Region", color=discord.Color.blue())
    embed.add_field(name="Region", value=region, inline=True)
    await ctx.send(embed=embed)

#serverafkchannel command and it display the server afk channel
@bot.command()
async def serverafkchannel(ctx):
    guild = ctx.guild
    afk_channel = guild.afk_channel
    embed = discord.Embed(title="Server AFK Channel", color=discord.Color.blue())
    embed.add_field(name="AFK Channel", value=afk_channel.mention if afk_channel else "None", inline=True)
    await ctx.send(embed=embed)

















bot.run(TOKEN)





