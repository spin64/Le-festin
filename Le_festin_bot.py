#imports stuff
import discord
import random
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient

#prefix for channels
client = commands.Bot(command_prefix = '.')

TOKEN = ('Token')

#prefix for channels
client = commands.Bot(command_prefix = '.')

#text channel stuff
#---------------------
#tells if bot is ready
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Ratatouille but its just the eating'))
    print('Bot is online')

#makes x ammount of rat 1s
@client.command(help='Spams rat 1s')
async def rats(ctx, counter: int = 0):
    if counter > 100 or counter < 0:
        await ctx.send('no rat for you')
    else:
        for i in range(counter):
            await ctx.send('https://imgur.com/7qS9M8h')
            await ctx.send('https://imgur.com/OOaHxgW')
            await ctx.send('https://imgur.com/LJKnFRF')

@client.command(help='questionable gaming')
async def questionablegaming(ctx, counter: int = 0):
    if counter > 100 or counter < 0:
        await ctx.send('no')
    else:
        for i in range(counter):
            await ctx.send('https://imgur.com/a/A2wH7BO')
            await ctx.send('questionable gaming <@161276565693399040>')

#bot responds with le rat
@client.command(help='prints out long rats')
async def rat(ctx, counter: int=0):
    if counter > 100 or counter < 0 :
        await ctx.send('That rat was over 100 or under 0')
        await ctx.send('But here is rat 1')
        await ctx.send('https://imgur.com/7qS9M8h')
        await ctx.send('https://imgur.com/OOaHxgW') 
    elif counter == 0:
        await ctx.send('https://imgur.com/7qS9M8h')
    else:
        await ctx.send('https://imgur.com/7qS9M8h')  
        for i in range(counter):
            await ctx.send('https://imgur.com/OOaHxgW')
    await ctx.send('https://imgur.com/a/mF5uBUV')

@client.command(help='prints out food')
async def dog(ctx, counter: int = 0):
    if counter > 100 or counter < 0:
        await ctx.send('no dog for you')
    else:
        for i in range(counter):
            await ctx.send('https://imgur.com/XMrMvCD')

@client.command(help='clears messages')
async def clear(ctx, ammount=3):
    await ctx.channel.purge(limit=ammount)

@client.command(help='gives some hot garbage')
async def hotgarbage(ctx):
    hot_garbage = ['https://na.op.gg/summoner/userName=zedpolar']
    await ctx.send(random.choice(hot_garbage))

@client.command(help='gives a random spongbob video')
async def spongebob(ctx):
    spongebob = ['https://youtu.be/oOOzF4VLTE0',
                 'https://youtu.be/lBpMSmYP7to',
                 'https://youtu.be/M_i4FbzaYww',
                 'https://youtu.be/KQi3r88-rT4',
                 'https://youtu.be/RuJNUXT2a9U',
                 'https://youtu.be/IyVPlEhRKBo',
                 'https://youtu.be/CN1OV9fh3uI',
                 'https://youtu.be/gSv4WiQ_gOM',
                 'https://youtu.be/pgiyA91A-cA',
                 'https://youtu.be/9_xbv_Bkd9s']
    await ctx.send(random.choice(spongebob))

#join/leave
@client.command(help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command( help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()


#voice commands
@client.command()
async def imarat(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('Media/rat.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

@client.command()
async def ratattack(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('Media/rat_attack.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

@client.command()
async def canada(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('Media/Canada.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)


client.run(TOKEN)
