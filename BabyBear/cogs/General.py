import json
import os
import platform
import random
import asyncio
import sys
import math
import re
import aiohttp
import requests
import discord
from discord import Color
import yaml
from discord.ext import commands
import mysql.connector
from PIL import Image,ImageDraw,ImageFont,ImageOps
from io import BytesIO
from discord.ext.commands import Bot
import database
import asyncpraw
from trello import TrelloApi
import urllib.request
import random
from dislash import InteractionClient, Option, OptionType,slash_command, ActionRow, Button, ButtonStyle
guild_ids = [317357005687750657]

if not os.path.isfile("config.yaml"):
	sys.exit("'config.yaml' not found! Please add it and try again.")
else:
	with open("config.yaml") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)



class general(commands.Cog, name="general"):
	def __init__(self, bot):
		self.bot = bot

	intents=discord.Intents.all()
	bot = Bot(command_prefix=config["bot_prefix"], intents=intents)










	@slash_command(name="information",description="Displays some usefull information a bout the bot",guild_ids = guild_ids)
	async def info(self, ctx):
		"""
		Get some useful information about the bot.
		"""
		embed = discord.Embed(
			description="Created By Seperoph#1399 and AkaBaka#4654",
			color=config["success"]
		)
		embed.set_author(
			name="Bot Information"
		)
		embed.add_field(
			name="Head Programmers:",
			value="Seperoph#1399 and AkaBaka#4654",
			inline=True
		)
		embed.add_field(
			name="Python Version:",
			value=f"{platform.python_version()}",
			inline=True
		)
		await ctx.respond(embed=embed)


	@slash_command(name = 'randomnumbergenerator',description = "get a random number from your choice of numbers.",guild_ids = guild_ids,options = [
		Option("minnumber","The Minimum Number to be used.",OptionType.INTEGER,required=True),
		Option("maxnumber","The Maximum Number to be used.",OptionType.INTEGER,required=True)
		]
	)
	async def Random_Number_Generator(inter,ctx,minnumber,maxnumber):
		startnum = minnumber
		endnum = maxnumber
		randomnumber = random.randrange(startnum,endnum)
		msg = "Your random number between "+str(startnum)+" and "+str(endnum)+" is "+str(randomnumber)
		await ctx.send(msg)



	# @cog_ext.cog_slash(name="topbalance",description="Displays the users with the highest 3 balance",guild_ids = guild_ids)
	# async def CardCommand(self,ctx):

	# 	mydb = mysql.connector.connect(
	# 		host="na01-sql.pebblehost.com",
	# 		user="customer_189330_grillybear",
	# 		password="VaNeeb2mn@GrN1fqtNFY",
	# 		database="customer_189330_grillybear"
	# 		)
	# 	Top10 = mydb.cursor()
	# 	Top10.execute("SELECT UserName,Balance FROM Users ORDER BY Balance DESC LIMIT 3")
	# 	Top10 = Top10.fetchall()
	# 	Top1 = str(Top10[0][0])
	# 	Top1Split = Top1.split("#",1)
	# 	SubTop1 = Top1Split[0]
	# 	Top1Bal = int(Top10[0][1])
	# 	Top1Bal = int(Top1Bal)
	# 	Top1Bal = "{:,}".format(Top1Bal)
	# 	Top2 = str(Top10[1][0])
	# 	Top2Split = Top2.split("#",1)
	# 	SubTop2 = Top2Split[0]
	# 	Top2Bal = str(Top10[1][1])
	# 	Top2Bal = int(Top2Bal)
	# 	Top2Bal = "{:,}".format(Top2Bal)
	# 	Top3 = str(Top10[2][0])
	# 	Top3Split = Top3.split("#",1)
	# 	SubTop3 = Top3Split[0]
	# 	Top3Bal = str(Top10[2][1])
	# 	Top3Bal = int(Top3Bal)
	# 	Top3Bal = "{:,}".format(Top3Bal)
	# 	#Embeding results into discord
	# 	embed = discord.Embed(
	# 		 title="💰Top Users : Balance💰",
	# 		 description= "```"+"First- "+SubTop1+" "+"₿₿ "+Top1Bal+"\n"+"\n"+"Second- "+SubTop2+" "+"₿₿ "+Top2Bal+"\n"+"\n"+"Third- "+SubTop3+" "+"₿₿ "+Top3Bal+"```",
	# 		color=config["success"]
	# 	)
	# 	await ctx.send(embed=embed)



	# @cog_ext.cog_slash(name="poll",description="Creates a basic poll with emoji up to 10 options",guild_ids = guild_ids)
	# async def Create_Poll(self,ctx,option1 = "",option2 = "",option3 = "",option4 = "",option5 = "",option6 = "",option7 = "",option8 = "",option9 = "",option10 = ""):
	# 	if option1 == "": option1 = ""
	# 	else:option1 = option1+"  1️⃣"+"\n"
	# 	if option2 == "": option2 = ""
	# 	else:option2 = option2+"  2️⃣"+"\n"
	# 	if option3 == "": option3 = ""
	# 	else:option3 = option3+"  3️⃣"+"\n"
	# 	if option4 == "": option4 = ""
	# 	else:option4 = option4+"  4️⃣"+"\n"
	# 	if option5 == "": option5 = ""
	# 	else:option5 = option5+"  5️⃣"+"\n"
	# 	if option6 == "": option6 = ""
	# 	else:option6 = option6+"  6️⃣"+"\n"
	# 	if option7 == "": option7 = ""
	# 	else:option7 = option7+"  7️⃣"+"\n"
	# 	if option8 == "": option8 = ""
	# 	else:option8 = option8+"  8️⃣"+"\n"
	# 	if option9 == "": option9 = ""
	# 	else:option9 = option9+"  9️⃣"+"\n"
	# 	if option10 == "": option10 = ""
	# 	else:option10 = option10+"  🔟"+"\n"
	# 	embed = discord.Embed(
	# 		title = "Click the emoji that corrosponds to the answer you want.",
	# 		description =option1+option2+option3+option4+option5+option6+option7+option8+option9+option10,
	# 		color=config["success"],
	# 	)
	# 	msg = await ctx.send(embed=embed)
	# 	await msg.add_reaction("1️⃣")
	# 	if option2 != "":await msg.add_reaction("2️⃣")
	# 	if option3 != "":await msg.add_reaction("3️⃣")
	# 	if option4 != "":await msg.add_reaction("4️⃣")
	# 	if option5 != "":await msg.add_reaction("5️⃣")
	# 	if option6 != "":await msg.add_reaction("6️⃣")
	# 	if option7 != "":await msg.add_reaction("7️⃣")
	# 	if option8 != "":await msg.add_reaction("8️⃣")
	# 	if option9 != "":await msg.add_reaction("9️⃣")
	# 	if option10 != "":await msg.add_reaction("🔟")




	@slash_command(name="feedback",description="Post feedback here",guild_ids = guild_ids,options = [
		Option("feedbacktitle","The title of the feedback card giving a very brief description of the feedback.",OptionType.STRING,required=True),
		Option('feedback','explain your feedback as well as you can. max character of 16,000',OptionType.STRING,required=True)
		]
	)

	async def Trello(self,ctx,feedbacktitle,feedback):
		user = ctx.author.name
		type = feedbacktitle+" Feedback By "+user

		TRELLO_APP_KEY = "7e808f098450d695776f6ec9db72beb8"
		TOKEN = "993e1631788e8a29574caf7393ed00ddcd120d43a058a513db740240308afcfe"
		listID = "60ff65e0c8b59135e64dead0"
		cardPos = "top"

		trello = TrelloApi(TRELLO_APP_KEY, TOKEN)
		newCard = trello.cards.new(type, idList=listID, desc=feedback, pos=cardPos)

		await ctx.send(user+" your feedback has been sent!")




	@slash_command(name="say",description="Makes the bot say what you say",guild_ids = guild_ids,options = [
		Option("message","The words you want the bot to say.",OptionType.STRING,required=True)])
	async def say(self, context,message):
		"""
		The bot will say anything you want.
		"""
		await context.send(message)


	@slash_command(name="cb",description="Make bot put your text into a codeblock",guild_ids = guild_ids,options = [
		Option("message","The words you want the bot to say.",OptionType.STRING,required=True)])
	async def Codeblock(self, context,message):
		"""
		The bot will say anything you want but in a code block.
		"""
		embed = discord.Embed(
			description="```"+ message + "```",
			color=config["success"]
		)
		await context.send(embed=embed)

	@slash_command(name="embed",description="Make bot put your text into a embed",guild_ids = guild_ids,options = [
		Option("message","The words you want the bot to say.",OptionType.STRING,required=True)])
	async def embed(self, context,message):
		"""
		The bot will say anything you want but embeded.
		"""
		embed = discord.Embed(
			description=message,
			color=config["success"]
		)
		await context.send(embed=embed)


	@slash_command(name="help",description="Displays Help",guild_ids = guild_ids)
	async def helpcommand(inter,ctx):
		await ctx.send("For any help with commands and what they do visit our dedicated webpage\nhttp://grillybear.42web.io")





def setup(bot):
	bot.add_cog(general(bot))
