#List of imports
import asyncio
import os
import sys
import re
import discord
import requests
from discord import utils
import yaml
import discord.ext
from discord.ext import commands
from datetime import datetime
import urllib
import pafy
import youtube_dl
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import ffmpeg
from discord import client
from dislash import InteractionClient, Option, OptionType,slash_command, ActionRow, Button, ButtonStyle


guild_ids = [317357005687750657]
client = discord.Client()

if not os.path.isfile("config.yaml"):
	sys.exit("'config.yaml' not found! Please add it and try again.")
else:
	with open("config.yaml") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #Initiallizing slash command 
    @slash_command(name="mp3",description="plays audio file that is saved on the server. Need to contact (Dev) if audio is wanted to be added.",guild_ids = guild_ids)
    async def play(self,ctx,*soundname):
        file = ""
        sourcedirectory = "Resources\\Sounds\\"
        source = sourcedirectory+file
        if "1" in soundname:
            file = "1.mp3"
        if "2" in soundname:
            file = "2.mp3"
        if "3" in soundname:
            file = "3.mp3"
        channel = ctx.author.voice.channel
        if (ctx.guild.voice_client) != None:
            await ctx.guild.voice_client.disconnect()
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable='ffmpeg', source=source+file))
            await ctx.send("Now playing "+file)
            
        else:
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable='ffmpeg', source=source+file))
            await ctx.send("Now playing "+file)


    #Initiallizing slash command 
    @slash_command(name="leave",description="Makes the bot leave the current channel",guild_ids = guild_ids)
    async def leave(self,ctx):
        channel = ctx.author.voice.channel
        if (ctx.guild.voice_client) != None:
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I have left the voice channel!")

        else:
            await ctx.send("I am not in a channel.")


    #Initiallizing slash command 
    @slash_command(name="pause",description="Pauses the bots curretly playing audio.",guild_ids = guild_ids)
    async def pause(self,ctx):
        if ctx.guild.voice_client != None:
            voice = ctx.guild.voice_client
            voice.pause()
            await ctx.send("Pausing the song!")
        else:
            pass


    #Initiallizing slash command 
    @slash_command(name="resume",description="Resumes the bots currently playing audio.",guild_ids = guild_ids)
    async def resume(self,ctx):
        if ctx.guild.voice_client != None:
            voice = ctx.guild.voice_client
            voice.resume()
            await ctx.send("Resuming the song!")
        else:
            pass


    #Initiallizing slash command 
    @slash_command(name="endplay",description="Stops the bot from playing audio will need to search again if more audio is wanted.",guild_ids = guild_ids)
    async def stop(self,ctx):
        if ctx.guild.voice_client != None:
            voice = ctx.guild.voice_client
            voice.stop()
            await ctx.send("Stopping the song!")
        else:
            pass


    @slash_command(name="play",description="Searches youtube for terms and place first video's audio",guild_ids = guild_ids,options = [
		Option("searchterms","The search terms that you want to search on youtube for.",OptionType.STRING,required=True),
        Option("loop","Number of times you want to loop. Put 1 if you only want it to play once.",OptionType.STRING,required=False)])
    async def Play_Youtube_Video(self,ctx,searchterms,loop='1'):




        async def Play_Play(self,ctx,loop,searchterms):
            loop = loop.upper()
            search = searchterms
            channel = ctx.author.voice.channel
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}


            if (ctx.guild.voice_client) != None:
                await ctx.guild.voice_client.disconnect()
                vc = await channel.connect()
                if "http" in searchterms:
                    song = pafy.new(searchterms)  # creates a new pafy object
                    audio = song.getbestaudio()  # gets an audio source
                    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use
                    #await ctx.send("Now Playing "+searchterms)
                    vc.play(source)  # play the source
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 0.65
                    await asyncio.sleep(song.length)


                if "http" not in searchterms:
                    search = search.replace(" ","+")

                    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
                    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

                    song = pafy.new(video_ids[0])  # creates a new pafy object
                    audio = song.getbestaudio()  # gets an audio source
                    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS,)  # converts the youtube audio source into a source discord can use
                    #await ctx.send("Searched for "+searchterms+"\n"+"https://www.youtube.com/watch?v=" + video_ids[0])
                    vc.play(source)  # play the source
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 0.65
                    await asyncio.sleep(song.length)


            else:
                vc = await channel.connect()
                if "http" in searchterms:

                    #await ctx.send("Now Playing "+searchterms)

                    song = pafy.new(searchterms)  # creates a new pafy object
                    audio = song.getbestaudio()  # gets an audio source
                    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use\
                    vc.play(source)  # play the source
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 0.7
                    await asyncio.sleep(song.length)

                        
                elif "http" not in searchterms:

                    search = search.replace(" ","+")
                    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
                    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                    #await ctx.send("Searched for "+searchterms+"\n"+"https://www.youtube.com/watch?v=" + video_ids[0])

                    song = pafy.new(video_ids[0])  # creates a new pafy object
                    audio = song.getbestaudio()  # gets an audio source
                    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use\
                    vc.play(source)  # play the source
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 0.65
                    await asyncio.sleep(song.length)


        await ctx.send("Now Playing "+searchterms)
        for i in range (int(loop)):
            await Play_Play(self,ctx,loop,searchterms)

    @slash_command(name="playlistplay",description="plays a playlist",guild_ids = guild_ids,options = [
		Option("playlistname","The name of your playlist you want to play",OptionType.STRING,required=True)])
    async def Play_Playlist(self,ctx,playlistname):


        async def play_playlist_songs(self,ctx,playlistname):
            
            channel = ctx.author.voice.channel
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

            
            file = open('PlayLists/'+playlistname+".txt", "r")
            line_count = 0
            for line in file:
                if line != "\n":
                    line_count += 1
            file.close()
            file = open('PlayLists/'+playlistname+".txt", "r")
            content = file.read().splitlines()
            start = 0
            for i in range(line_count):
                if (ctx.guild.voice_client) != None:
                    song = pafy.new(content[start])  # creates a new pafy object
                    audio = song.getbestaudio()  # gets an audio source
                    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use\
                    vc.play(source)  # play the source
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 0.7
                    song_details ="Title: "+song.title+"\n"+"Author: "+song.author+"\n"+"Song_Duration: "+song.duration+"\n"+content[start]
                    if start ==0:
                        await ctx.send(song_details)
                    elif start >=1:
                        await ctx.edit(song_details)
                    await asyncio.sleep(song.length)
                    start += 1
                if (ctx.guild.voice_client) == None:
                    vc = await channel.connect()
                    song = pafy.new(content[start])  # creates a new pafy object
                    audio = song.getbestaudio()  # gets an audio source
                    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use\
                    vc.play(source)  # play the source
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 0.7
                    song_details ="Title: "+song.title+"\n"+"Author: "+song.author+"\n"+"Song_Duration: "+song.duration+"\n"+content[start]
                    if start ==0:
                        await ctx.send(song_details)
                    elif start <=1:
                        await ctx.edit(song_details)
                    await asyncio.sleep(song.length)
                    start += 1

        await play_playlist_songs(self,ctx,playlistname)




    @slash_command(name="createplaylist",description="Create a playlist with your choice of name",guild_ids = guild_ids,options = [
		Option("playlist_name","The Name of the playlist you want to add to.",OptionType.STRING,required=True)])
    async def Create_Blank_Playlist(self,ctx,playlist_name):
        justname = playlist_name
        name = playlist_name+".txt"
        f= open('PlayLists/'+name,"w+")
        f.close()
        await ctx.send("Created Blank Playlist Named: "+justname)

    @slash_command(name="addtoplaylist",description="Add a url to the playlist of your choice",guild_ids = guild_ids,options = [
		Option("playlist_name","The Name of the playlist you want to add to.",OptionType.STRING,required=True),
        Option("url","The url you want added to the playlist.",OptionType.STRING,required=True),])
    async def Add_To_Playlist(self,ctx,playlist_name,url):
        justplaylistname = playlist_name
        playlistname = playlist_name+".txt"
        f = open('PlayLists/'+playlistname,"a")
        f.write(url+"\n")
        f.close()
        await ctx.send("added "+url+" to "+justplaylistname+" playlist")

    # @slash_command(name="shuffleplaylist",description="shuffle a playlist of your choice.",guild_ids = guild_ids,options = [
	# 	Option("playlist_name","The Name of the playlist you want to add to.",OptionType.STRING,required=True)])
    # async def Add_To_Playlist(self,ctx,playlist_name):
    #     with open('PlayLists/'+playlist_name+'.txt','r') as source:
    #         data = [ (random.random(), line) for line in source ]
    #     data.sort()
    #     with open('PlayLists/'+playlist_name+'.txt','w') as target:
    #         for _, line in data:
    #             target.write( line )
    #         await ctx.send(playlist_name+" Has been shuffled.")

    @slash_command(name="removefromplaylist",description="removes a url from the playlist",guild_ids = guild_ids,options = [
		Option("playlist","The playlist you wish to edit",OptionType.STRING,required=True),
        Option("songurl","the song url you wish to remove to the playlist",OptionType.STRING,required=True)])
    async def Show_Queue(self,ctx,playlist,songurl):

        f = open('PlayLists/'+playlist+".txt","r")
        lines = f.readlines()
        f.close()
        f = open('PlayLists/'+playlist+".txt","w")
        for line in lines:
            if songurl not in line:
                f.write(line)

        await ctx.send(songurl+" Has been removed from the queue.")




    @slash_command(name="showplaylist",description="Shows the contents of the playlist of your choice",guild_ids = guild_ids,options = [
		Option("playlist_name","The Name of the playlist you want to add to.",OptionType.STRING,required=True)])
    async def Show_Queue(self,ctx,playlist_name):
        f = open('PlayLists/'+playlist_name+".txt")
        file_contents = f.read()
        await ctx.send(file_contents)
        f.close()




def setup(bot):
    bot.add_cog(Music(bot))
