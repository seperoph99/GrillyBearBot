import os
import sys
import mysql.connector
import database
import discord
import asyncpraw
from discord import Color
import random
import yaml
from discord.ext import commands
from dislash import InteractionClient, Option, OptionType,slash_command, ActionRow, Button, ButtonStyle


guild_ids = [317357005687750657]

if not os.path.isfile("config.yaml"):
	sys.exit("'config.yaml' not found! Please add it and try again.")
else:
	with open("config.yaml") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)


class Funny(commands.Cog, name="funny"):
	def __init__(self, bot):
		self.bot = bot

	@slash_command(name="reddit",description="Gets a random post from a subreddit of your choosing",guild_ids = guild_ids,options = [
		Option("subreddit","The subreddit to be used.",OptionType.STRING,required=True),
		])
	async def memegen(inter,ctx,subreddit):


		reddit = asyncpraw.Reddit(client_id='2ot5SpV0bf8ccw',
							client_secret='9xBNjTzsTCM9M-JWURV6-tYAWV9pmA',
							user_agent='XXXX')
		subname = subreddit
		subname = "Image Hosted from subreddit "+subname
		reddit = asyncpraw.Reddit(client_id='2ot5SpV0bf8ccw',
							client_secret='9xBNjTzsTCM9M-JWURV6-tYAWV9pmA',
							user_agent='XXXX')
		
		subreddit = await reddit.subreddit(subreddit)
		post = random.choice([post async for post in subreddit.hot(limit=25)])
		description = ""
		if 'soundcloud' in post.url:
			description = "No image here this is a audio post"
		embed = discord.Embed(
			title=post.title+"\n"+post.url,
			description=description,
			color=config["success"]
		)
		embed.set_image(url=post.url)
		embed.set_footer(text = subname)
		await ctx.send(embed=embed)

	@slash_command(name="sickness",description="Generates a random sickness good luck",guild_ids = guild_ids)
	async def Sickness_Generator(self,ctx):
		"""
		Random Sickness Generator
		"""
		Sickness = ['Faggot','Small Penis Syndrome','Tetanus','Parkinsons disease','Pediculosis capitis (Head lice)','Huntingtons disease','Reflex sympathetic dystrophy','Swine influenza','covid 19','Hepatitis B','AIDS','Yersinia pseudotuberculosis infection','Celiacs disease','NeoPlasm','Autoimmune dysautonomia','Hantavirus Pulmonary Syndrome']
		chance = [5,5,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
		results = random.choices(Sickness,chance,k=1)
		embed = discord.Embed(
			title=":nauseated_face: Your Sickness",
			description="Your Sickness is..."+"\n"+"\n"+":syringe: "+" "+(results[0]),
			color=config["success"]
		)
		await ctx.send(embed=embed)

	@slash_command(name="gayr8",description="Tells how gay you are LOL",guild_ids = guild_ids,
	options=[Option('target','who the target of the gayr8 is.',OptionType.USER)])
	async def Rate_Gay(inter,ctx,target):
		rated = str(random.randint(1,101))
		sentence = str(target)+' is '+rated+"% Gay :gay_pride_flag:"
		embed = discord.Embed(
			title = "Gay Rate Machine!",
			description=sentence,
			color= Color.magenta()
		)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Funny(bot))
