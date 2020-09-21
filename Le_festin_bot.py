#imports stuff
import discord
import random
from discord.ext import commands

#prefix for channels
client = commands.Bot(command_prefix = '.')

TOKEN = ('Token')

#tells if bot is ready
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Ratatouille but its just the eating'))
    print('Bot is online')

#makes x ammount of rat 1s
@client.command()
async def rats(ctx, counter: int):
    if counter > 100 or counter < 0:
        await ctx.send('no rat for you')
    else:
        for i in range(counter):
            await ctx.send('https://imgur.com/7qS9M8h')
            await ctx.send('https://imgur.com/OOaHxgW')
            await ctx.send('https://imgur.com/LJKnFRF')

@client.command()
async def questionablegaming(ctx, counter: int):
    if counter > 100 or counter < 0:
        await ctx.send('no')
    else:
        for i in range(counter):
            await ctx.send('https://imgur.com/a/bCu6BCB')
            await ctx.send('questionable gaming <@231592825349734402>')

#bot responds with le rat
@client.command()
async def rat(ctx, counter: int):
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

@client.command()
async def dog(ctx, counter: int):
    if counter > 100 or counter < 0:
        await ctx.send('no dog for you')
    else:
        for i in range(counter):
            await ctx.send('https://imgur.com/XMrMvCD')


@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('You are not in a voice channel')

@client.command(pass_context=True) 
async def leave(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        voice_client = ctx.message.guild.voice_client
        await voice_client.disconnect()
    else:
        await ctx.send('You are not in a voice channel')

@client.command()
async def clear(ctx, ammount=3):
    await ctx.channel.purge(limit=ammount)

@client.command()
async def hotgarbage(ctx):
    hot_garbage = ['https://na.op.gg/summoner/userName=zedpolar']
    await ctx.send(random.choice(hot_garbage))

@client.command()
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

client.run(TOKEN)
