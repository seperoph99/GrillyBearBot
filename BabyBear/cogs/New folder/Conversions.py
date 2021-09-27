import json
import os
import platform
import random
import sys
import math
import re
import aiohttp
import discord
import yaml
from discord.ext import commands
from dislash import InteractionClient, Option, OptionType,slash_command, ActionRow, Button, ButtonStyle
guild_ids = [317357005687750657]

if not os.path.isfile("config.yaml"):
	sys.exit("'config.yaml' not found! Please add it and try again.")
else:
	with open("config.yaml") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)


class conversion(commands.Cog, name="conversion"):
	def __init__(self, bot):
		self.bot = bot

		
	@slash_command(name="convertfahrenheit",description="converts your value from fahrenheit to celcius ",guild_ids = guild_ids,options = [
		Option("fvalue","value to convert from fahrenheit to celcius.",OptionType.STRING,required=True)])
	async def convert_f(self,context,fvalue):
		msg = str(fvalue)
		num = float(str(re.search('\d+(.\d+)?',msg).group(0)))
		conv = ((num - 32) * 5/9)
		output = str(conv) + ' ℃'
		Command_Log = ctx.author.name+"ran Command Convert_Fahrenheit"
		f = open("Console_Log.txt","a")
		f.write(Command_Log)
		f.close

		embed = discord.Embed(
			title = "Fahrenheit To Celcius" ,
			description = str(num)+" ℉"+" converts to"+"\n"+output,
			color = config["success"]
		)
		await context.send(embed=embed)

	@slash_command(name="convertcelcius",description="converts your value from celcius to fahrenheit ",guild_ids = guild_ids,options = [
		Option("cvalue","value to convert from celcius to fahrenheit.",OptionType.STRING,required=True)])
	async def convert_c(self,context,cvalue):
		msg = str(cvalue)
		num = float(str(re.search('\d+(.\d+)?',msg).group(0)))
		conv = (num * 9/5) + 32
		output = str(conv) + ' ℉'
		Command_Log = ctx.author.name+"ran Command Convert_Celcius"
		f = open("Console_Log.txt","a")
		f.write(Command_Log)
		f.close

		embed = discord.Embed(
			title = "Celcius To Fahrenheit" ,
			description = str(num)+" ℃"+" converts to"+"\n"+output,
			color = config["success"]
		)
		await context.send(embed=embed)

	@slash_command(name="convertfeet",description="converts your value from feet to meters ",guild_ids = guild_ids,options = [
		Option("fvalue","value to convert from feet to meters.",OptionType.STRING,required=True)])
	async def convert_feet(self,context,fvalue):
		msg = str(fvalue)
		num = float(str(re.search('\d+(.\d+)?',msg).group(0)))
		conv = num * 0.3048
		output = str(conv) + ' Meters'
		Command_Log = ctx.author.name+"ran Command Convert_Feet"
		f = open("Console_Log.txt","a")
		f.write(Command_Log)
		f.close

		embed = discord.Embed(
			title = "Feet To Meters" ,
			description = str(num)+" Feet"+" converts to"+"\n"+output ,
			color = config["success"]
		)
		await context.send(embed=embed)

	@slash_command(name="convertmeter",description="converts your value from meters to feet ",guild_ids = guild_ids,options = [
		Option("mvalue","value to convert from meters to feet.",OptionType.STRING,required=True)])
	async def convert_meters(self,context,mvalue):
		msg = str(mvalue)
		num = float(str(re.search('\d+(.\d+)?',msg).group(0)))
		conv = num * 3.28084
		output = str(conv) + ' Feet'
		Command_Log = ctx.author.name+"ran Command Convert_Meter"
		f = open("Console_Log.txt","a")
		f.write(Command_Log)
		f.close

		embed = discord.Embed(
			title = "Meters to Feet" ,
			description = str(num)+" Meters"+" converts to"+"\n"+output ,
			color = config["success"]
		)
		await context.send(embed=embed)

	@slash_command(name="convertmile",description="converts your value from miles to kilometers ",guild_ids = guild_ids,options = [
		Option("mivalue","value to convert from miles to kilometers.",OptionType.STRING,required=True)])
	async def convert_miles(self,context,mivalue):
		msg = str(mivalue)
		num = float(str(re.search('\d+(.\d+)?',msg).group(0)))
		conv = num * 1.609344
		output = str(conv) + ' Kilometers'
		Command_Log = ctx.author.name+"ran Command Convert_Mile"
		f = open("Console_Log.txt","a")
		f.write(Command_Log)
		f.close

		embed = discord.Embed(
			title = "Miles to Kilometers" ,
			description = str(num)+" Miles"+" converts to"+"\n"+output ,
			color = config["success"]
		)
		await context.send(embed=embed)


	@slash_command(name="convertkilometer",description="converts your value from kilometers to miles ",guild_ids = guild_ids,options = [
		Option("kmvalue","value to convert from kilometers to miles.",OptionType.STRING,required=True)])
	async def convert_killometers(self,context,kmvalue):
		msg = str(kmvalue)
		num = float(str(re.search('\d+(.\d+)?',msg).group(0)))
		conv = num * 0.6214
		output = str(conv) + ' Miles'
		Command_Log = ctx.author.name+"ran Command Convert_Kilometer"
		f = open("Console_Log.txt","a")
		f.write(Command_Log)
		f.close

		embed = discord.Embed(
			title = "Kilometers to Miles",
			description = str(num)+" Kilometers"+" converts to"+"\n"+output,
			color = config["success"]
		)
		await context.send(embed=embed)
	

def setup(bot):
	bot.add_cog(conversion(bot))
