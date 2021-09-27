
import os
import platform
import random
import asyncio
import requests
import pafy
import schedule
from discord import FFmpegPCMAudio, PCMVolumeTransformer, channel, member
import sys
import ffmpeg
import datetime
from discord.utils import get
import discord
import csv
from discord_slash import SlashCommand
import yaml
import time
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import mysql.connector
import threading
from datetime import datetime
import json
from datetime import datetime
from dislash import InteractionClient, ActionRow, Button, ButtonStyle,SelectMenu, SelectOption


@commands.command()
async def on_ready():
    print("Everything's all ready to go~")


if not os.path.isfile("config.yaml"):
    sys.exit("'config.yaml' not found! Please add it and try again.")
else:
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

"""	
Setup bot intents (events restrictions)
For more information about intents, please go to the following websites:
https://discordpy.readthedocs.io/en/latest/intents.html
https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents


Default Intents:
intents.messages = True
intents.reactions = True
intents.guilds = True
intents.emojis = True
intents.bans = True
intents.guild_typing = False
intents.typing = False
intents.dm_messages = False
intents.dm_reactions = False
intents.dm_typing = False
intents.guild_messages = True
intents.guild_reactions = True
intents.integrations = True
intents.invites = True
intents.voice_states = False
intents.webhooks = False

Privileged Intents (Needs to be enabled on dev page), please use them only if you need them:
intents.presences = True
intents.members = True
"""

intents=discord.Intents.all()

bot = Bot(command_prefix=config["bot_prefix"], intents=intents)


slash = SlashCommand(bot, sync_commands=True)
guild_ids = [840686652950577172]
Slash = InteractionClient(bot)

# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    await loop_starts()
@tasks.loop(minutes=1)
async def Check_Twitch_event42null():
    URL = 'https://api.twitch.tv/helix/streams?user_login=mrmoonshouse'
    authURL = 'https://id.twitch.tv/oauth2/token'
    Client_ID = 'eyy2yqemupxdz250jl02owpqhk11ke'
    Secret  = '2ayx9y6v7kpuej4g0e99kk4hemwd1b'

    AutParams = {'client_id': Client_ID,
                'client_secret': Secret,
                'grant_type': 'client_credentials'
                }


    async def Check():
        AutCall = requests.post(url=authURL, params=AutParams) 
        access_token = AutCall.json()['access_token']

        head = {
        'Client-ID' : Client_ID,
        'Authorization' :  "Bearer " + access_token
        }

        r = requests.get(URL, headers = head).json()['data']

        if r:
            r = r[0]
            if r['type'] == 'live':
                print(r)
                msg = "__**"+r['user_name']+'**__ Is now live on twitch\n playing '+r['game_name']+"\n"+r['title']+"\n https://www.twitch.tv/"+r['user_name']
                channel = bot.get_channel(890434212790956073)
                await channel.send(msg)
                await asyncio.sleep(43200)
            else:
                return False
        else:
            return False
    await (Check())

@tasks.loop(minutes=1)
async def Check_Twitch_lastgenmedia():
    URL = 'https://api.twitch.tv/helix/streams?user_login=lastgenmedia'
    authURL = 'https://id.twitch.tv/oauth2/token'
    Client_ID = 'eyy2yqemupxdz250jl02owpqhk11ke'
    Secret  = '2ayx9y6v7kpuej4g0e99kk4hemwd1b'

    AutParams = {'client_id': Client_ID,
                'client_secret': Secret,
                'grant_type': 'client_credentials'
                }


    async def Check():
        AutCall = requests.post(url=authURL, params=AutParams) 
        access_token = AutCall.json()['access_token']

        head = {
        'Client-ID' : Client_ID,
        'Authorization' :  "Bearer " + access_token
        }

        r = requests.get(URL, headers = head).json()['data']

        if r:
            r = r[0]
            if r['type'] == 'live':
                msg = "__**"+r['user_name']+'**__ Is now live on twitch\n playing '+r['title']+"\n https://www.twitch.tv/"+r['user_name']
                channel = bot.get_channel(890434212790956073)
                await channel.send(msg)
                await asyncio.sleep(43200)
            else:
                return False
        else:
            return False
    await (Check())


@tasks.loop(minutes=1)
async def Check_Twitch_akabaka_():
    URL = 'https://api.twitch.tv/helix/streams?user_login=akabaka_'
    authURL = 'https://id.twitch.tv/oauth2/token'
    Client_ID = 'eyy2yqemupxdz250jl02owpqhk11ke'
    Secret  = '2ayx9y6v7kpuej4g0e99kk4hemwd1b'

    AutParams = {'client_id': Client_ID,
                'client_secret': Secret,
                'grant_type': 'client_credentials'
                }


    async def Check():
        AutCall = requests.post(url=authURL, params=AutParams) 
        access_token = AutCall.json()['access_token']

        head = {
        'Client-ID' : Client_ID,
        'Authorization' :  "Bearer " + access_token
        }

        r = requests.get(URL, headers = head).json()['data']

        if r:
            r = r[0]
            if r['type'] == 'live':
                msg = "__**"+r['user_name']+'**__ Is now live on twitch\n playing '+r['title']+"\n https://www.twitch.tv/"+r['user_name']
                channel = bot.get_channel(890434212790956073)
                await channel.send(msg)
                await asyncio.sleep(43200)
            else:
                return False
        else:
            return False
    await (Check())


@tasks.loop(hours=1)
async def epic_check():
    day = datetime.today().weekday()
    time = datetime.now().strftime('%H:%M')
    channel = await bot.fetch_channel(868347011232055296)
    #print(channel)
    if day == 3 and time == "12:00":
        url = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=PL&allowCountries=PL'
        r = requests.get(url)
        data = r.json()
        for item in data['data']['Catalog']['searchStore']['elements'] :
            if (item['price']['totalPrice']['discountPrice']) == 0:
                if(item['price']['totalPrice']['originalPrice']) >0:
                    url = item['keyImages'][4]['url']
                    url = url.replace(" ","%20")
                    embed = discord.Embed(
					    title = item['title'],
						description=item['description'],
						color=config["success"])
                    embed.set_image(url = url)
                    await channel.send(embed=embed)

# @tasks.loop(minutes=1)
# async def Check_Streams():
#     me = await bot.fetch_user('205865007395766272')
#     print(me)
#     channel1 = bot.get_channel
#     print(channel1)
#     channel1.send_message(me, "Hello!")
#     URL = 'https://api.twitch.tv/helix/streams?user_login=sodapoppin'
#     authURL = 'https://id.twitch.tv/oauth2/token'
#     Client_ID = 'eyy2yqemupxdz250jl02owpqhk11ke'
#     Secret  = '2ayx9y6v7kpuej4g0e99kk4hemwd1b'

#     AutParams = {'client_id': Client_ID,
#                 'client_secret': Secret,
#                 'grant_type': 'client_credentials'
#                 }


#     def Check():
#         AutCall = requests.post(url=authURL, params=AutParams) 
#         access_token = AutCall.json()['access_token']

#         head = {
#         'Client-ID' : Client_ID,
#         'Authorization' :  "Bearer " + access_token
#         }

#         r = requests.get(URL, headers = head).json()['data']
#         #print(r)

#         if r:
#             r = r[0]
#             if r['type'] == 'live':
#                 msg = r['user_name']+' Is now live on twitch playing '+r['title']
#                 print (msg)
#                 #print('live')
#                 #return True
#             else:
#                 return False
#         else:
#             return False
#     print(Check())


async def loop_starts():
    bot.wait_until_ready
    Server_Statistics.start()
    Check_Twitch_event42null.start()
    Check_Twitch_akabaka_.start()
    Check_Twitch_lastgenmedia.start()
    #epic_check.start()
    #Check_Streams.start()
    #check_giveaway.start()

@tasks.loop(seconds=1.0)
async def status_task():
    client = discord.client
    statuses = [f"Baby Bear,Fish Swim"]
    print('ok')

@tasks.loop(seconds=10.0)
async def Server_Statistics():
    member_channel = bot.get_channel(888889394352775278)
    total_posts = bot.get_channel(888902434334867506)
    total_voice = bot.get_channel(888902452223574046)
    totalvoicefile = open("totalvoice.txt")
    total_voice_count = totalvoicefile.read()
    totalvoicefile.close()
    totalpostsfile = open("totalposts.txt")
    total_post_count = totalpostsfile.read()
    totalpostsfile.close()
   
    await member_channel.edit(name="Total Members: "+str(member_channel.guild.member_count))
    await total_posts.edit(name = "Total Server Posts: "+str(total_post_count))
    await total_voice.edit(name = "Total Server Voice Time: "+str(total_voice_count))




@tasks.loop(hours=24.0)
async def check_giveaway():
    channel = bot.get_channel(868347011232055296)#Channel to check posts from
    async for msg in channel.history(limit=50):
        if msg.author.id == 840791042130444320:#Bot Id
            users = await msg.reactions[0].users().flatten()
            for user in users:
                print (user.name)

# Removes the default help command of discord.py to be able to create our custom help command.
bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


# @bot.event
# async def on_voice_state_update(member,before,after):
#     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
#     if before.channel == None:
#         if member.id == 205865007395766272:
#             channel = member.voice.channel
#             searchterms = "https://www.youtube.com/watch?v=hq2A-AYw4bE"
#             await bot.guild.voice_client.disconnect()
#             vc = await channel.connect()

#             song = pafy.new(searchterms)  # creates a new pafy object
#             audio = song.getbestaudio()  # gets an audio source
#             source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use
#             #await ctx.send("Now Playing "+searchterms)
#             vc.play(source)  # play the source
#             vc.source = discord.PCMVolumeTransformer(vc.source)
#             vc.source.volume = 0.65



@bot.event
async def on_voice_state_update(member,before,after):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    FMT = '%H:%M:%S'

    if before.channel == None:
        msg = member.name +" Has joined a voice channel at "+dt_string+"\n"
        with open("Voice_Log.txt","a") as a:
            a.write(msg)
            a.close()
            global current_join_time
            current_join_time = now.strftime("%H:%M:%S")
            current_join_time = current_join_time
            if member.id == 205865007395766272: #Seperoph

                channel = member.voice.channel
                searchterms = "https://www.youtube.com/watch?v=GzImQ50PZ-w"
                guild = bot.get_guild(840686652950577172)
                voice_state = member.guild.voice_client
                if (member.guild.voice_client) == None:
                    vc = await channel.connect()
                    #await member.guild.voice_client.disconnect()

                    song = pafy.new(searchterms)  # creates a new pafy object
                    audio = song.getbestaudio()  # gets an audio source
                    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use
                    vc.play(source)  # play the source
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 0.65
                if (member.guild.voice_client) != None:
                    await member.guild.voice_client.disconnect()
                    vc = await channel.connect()

                    song = pafy.new(searchterms)  # creates a new pafy object
                    audio = song.getbestaudio()  # gets an audio source
                    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use
                    vc.play(source)  # play the source
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 0.65

    if after.channel == None:
        msg = member.name +" Has left a voice channel at "+dt_string+"\n"
        with open("Voice_Log.txt","a") as a:
            a.write(msg)
            a.close()
            current_join_time = current_join_time
            current_leave_time = now.strftime("%H:%M:%S")
            current_leave_time = current_leave_time
            tdelta = datetime.strptime(current_leave_time, FMT) - datetime.strptime(current_join_time, FMT)
            tdeltatl = tdelta.seconds
            print(tdeltatl)
            hours = float(tdeltatl) / 3600
            print(hours)
            hours = round(hours,2)
            with open('users.json','r') as f:
                users = json.load(f)
                users['840686652950577172'][str(member.id)]['voice'] += hours
            with open('users.json','w') as f:
                json.dump(users, f)



                
            totalvoice = open("totalvoice.txt")
            totalvoicecurrent = totalvoice.read()
            totalvoicesnew = float(totalvoicecurrent)+hours
            totalvoice = open("totalvoice.txt","w")
            totalvoice.write(str(totalvoicesnew))
            totalvoice.close()


# The code in this event is executed every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):
    # #print(message)
    # print(message.attachments)
    # #messageid = message.id
    # #messageauthor = message.author.name
    # messagecontent = message.content
    # channelid = message.channel.id
    # #messageidlink = 'https://discordapp.com/channels/840686652950577172/868347011232055296/'+str(messageid)
    # #channelfetch = await bot.fetch_channel(channelid)
    # msg = messagecontent+"\n Was already posted in the house"
    # if channelid == 406866527187632147 and message.author.id != 387117334961061888:
    #     with open ('memes.txt') as f:
    #         content = f.readlines()
    #     if messagecontent+"\n" in content:
    #         await message.delete()
    #         user = message.author
    #         await user.send(msg)
    #     if messagecontent+"\n" not in content:
    #         file1 = open('memes.txt','a')
    #         file1.write(messagecontent+"\n")
    #         file1.close()

    number = random.randint(1,10)
        
    if not message.author.bot:
        #print('test load')
        with open('users.json','r') as f:
            users = json.load(f)
            #print('testfile load')
        await update_data(users, message.author,message.guild)
        await add_experience(users, message.author, number, message.guild)
        await level_up(users, message.author,message.channel, message.guild)
        with open('users.json','w') as f:
            json.dump(users, f)
        if message.channel.id == 888997834018406460:
            totalmemecount = open("totalmemecount.txt")
            totalmemecountcurrent = totalmemecount.read()
            totalmemecountnew = int(totalmemecountcurrent)+1
            totalmemecount = open("totalmemecount.txt","w")
            totalmemecount.write(str(totalmemecountnew))
            totalmemecount.close()
            totalposts = open("totalposts.txt")
            totalpostscurrent = totalposts.read()
            totalpostsnew = int(totalpostscurrent)+1
            totalposts = open("totalposts.txt","w")
            totalposts.write(str(totalpostsnew))
            totalposts.close()

        if message.channel.id != 888997834018406460:
            totalposts = open("totalposts.txt")
            totalpostscurrent = totalposts.read()
            totalpostsnew = int(totalpostscurrent)+1
            totalposts = open("totalposts.txt","w")
            totalposts.write(str(totalpostsnew))
            totalposts.close()
    await bot.process_commands(message)





async def update_data(users, user,server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 0
            users[str(server.id)][str(user.id)]['posts'] = 0
            users[str(server.id)][str(user.id)]['voice'] = 0
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 0
            users[str(server.id)][str(user.id)]['posts'] = 0
            users[str(server.id)][str(user.id)]['voice'] = 0
async def add_experience(users, user, exp, server):
  pluspost = 1
  users[str(user.guild.id)][str(user.id)]['experience'] += exp
  users[str(user.guild.id)][str(user.id)]['posts'] += pluspost

async def level_up(users, user, channel, server):
  post = users[str(user.guild.id)][str(user.id)]['posts']
  experience = users[str(user.guild.id)][str(user.id)]['experience']
  lvl_start = users[str(user.guild.id)][str(user.id)]['level']
  if str(user.guild.id) != '757383943116030074':
    if(lvl_start*10*.95 <= experience):
        lvl_start = int(lvl_start)+1
        users[str(user.guild.id)][str(user.id)]['level'] = lvl_start
        users[str(server.id)][str(user.id)]['experience'] = 1
        await channel.send("🎉with "+str(post)+" posts"+" {} has leveled up to Level {}🎉".format(user.mention, lvl_start,))


# The code in this event is executed every time a command has been *successfully* executed
@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(
        f"Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})")


# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="Error!",
            description="This command is on a %.2fs cool down" % error.retry_after,
            color=config["error"]
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Error!",
            description="You are missing the permission `" + ", ".join(
                error.missing_perms) + "` to execute this command!",
            color=config["error"]
        )
        await context.send(embed=embed)
    raise error
@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id) # Get guild
    member = get(guild.members, id=payload.user_id) # Get the member out of the guild
    # The channel ID should be an integer:
    if payload.channel_id == 879844063103307786: # Only channel where it will work
        if str(payload.emoji) == "🎉": # Your emoji
            role = get(payload.member.guild.roles, id=879536615897313352) # Role ID
        else:
            role = get(guild.roles, name=payload.emoji)
        if role is not None: # If role exists
            await payload.member.add_roles(role)
            print(f"Added {role}")

    if payload.channel_id == 879844063103307786: # Only channel where it will work
        if str(payload.emoji) == "🏆": # Your emoji
            role = get(payload.member.guild.roles, id=852766744199299112) # Role ID
        else:
            role = get(guild.roles, name=payload.emoji)
        if role is not None: # If role exists
            await payload.member.add_roles(role)
            print(f"Added {role}")


    if payload.channel_id == 890083261290778674:
        if str(payload.emoji) == "🤝":
            role = get(payload.member.guild.roles,id = 891014663523938345)
        else:
            role = get(guild.roles,name=payload.emoji)
        if role is not None: # If role exists
            await payload.member.add_roles(role)


# Run the bot with the token
bot.run(config["token"])
