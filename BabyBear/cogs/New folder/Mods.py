import os
import sys
import mysql.connector
import database
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


class moderation(commands.Cog, name="moderation"):
	def __init__(self, bot):
		self.bot = bot

	@commands.group(name="modcommands")
	async def Moderation_Commands(self, context):
		'''
		Lists all moderation commands
		'''
		embed = discord.Embed(
			title="__**Moderation Commands**__",
			description=" __**purge**__ - Purge purges x amount of messages purge [value] \n\
				__**dbcheck**__ - checks the status of the database connection.",
			color=config["success"]
		)
		await context.send(embed=embed)

	@slash_command(name="purge",description= "Removes messages by your request",guild_ids=guild_ids,options = [
		Option("number","the number of messages you would like to purge.",OptionType.STRING,required=True)])
	async def purge(self, context, number):
		"""
		Delete a number of messages.
		"""
		if context.message.author.id in config["owners"] or context.message.author.id in config["mods"]:
			try:
				number = int(number)
			except:
				embed = discord.Embed(
					title="Error!",
					description=f"`{number}` is not a valid number.",
					color=config["error"]
				)
				await context.send(embed=embed)
				return
			if number < 1:
				embed = discord.Embed(
					title="Error!",
					description=f"`{number}` is not a valid number.",
					color=config["error"]
				)
				await context.send(embed=embed)
				return
			purged_messages = await context.message.channel.purge(limit=number)
			embed = discord.Embed(
				title="Chat Cleared!",
				description=f"**{context.message.author}** cleared **{len(purged_messages)}** messages!",
				color=config["success"]
			)
			await context.send(embed=embed)
	@slash_command(name="dbcheck",description="Checks DataBase Connection.",guild_ids = guild_ids)
	async def DBCheck(self,context):
		"""
		Checks to make sure db connection is online
		"""

		#Getting the id of user
		id = context.author.id

		#Calling Connection to DB
		mydb = mysql.connector.connect(
			host="na01-sql.pebblehost.com",
			user="customer_189330_grillybear",
			password="VaNeeb2mn@GrN1fqtNFY",
			database="customer_189330_grillybear"
		)
		#Checking if db is connected if so print success message
		if mydb.is_connected() == True:
			dbcheck = "Database is online and connected"
			embed = discord.Embed(
				title="Database Connection Check",
				description=(dbcheck),
				color=config["success"]
			)
			await context.send(embed=embed)
		#Checking if db is connect if not printing error message
		if mydb.is_connected() == False:
			dbcheck = "Database is offline or not connected check provider"
			embed = discord.Embed(
				title="Database Connection Check",
				description=(dbcheck),
				color=config["error"]
			)
			await context.send(embed=embed)

	@slash_command(name="trophycase",description="Put your meme here.",guild_ids = guild_ids,options = [
		Option("meme","The meme or image you would like to vote for.",OptionType.STRING,required=True)])
	async def HouseCommand(self,ctx,*,meme):
		msg = await ctx.send(meme)
		await msg.add_reaction("🐻")


	@slash_command(name="postrules",description="Posts Rules with the agreement reaction.",guild_ids = guild_ids)
	async def giveaway(inter,ctx):
		if ctx.author.id == 205865007395766272:
			embed = discord.Embed(
				title="Grilliest Bears Rules",
				description=" ",
				color=config["success"]
			)
			embed.add_field(name = "Rule #1 ",value="Be respectful, civil, and welcoming.", inline=False)
			embed.add_field(name = "Rule #2 ",value="Any content that is NSFW must be posted in the appropriate channel and nowhere else.", inline=False)
			embed.add_field(name = "Rule #3 ",value="The primary language of this server is English.", inline=False)
			embed.add_field(name = "Rule #4 ",value="Don’t ping without legitimate reasoning behind them.", inline=False)
			embed.add_field(name = "Rule #5 ",value="Cat fishing, and Leaking personal information of others is forbidden", inline=False)
			embed.add_field(name = "Rule #6 ",value="Any harmful media (text, image, video or audio clip, ect) targeting specific groups/individuals is prohibited.", inline=False)
			embed.add_field(name = "Rule #7 ",value="Do not link scam websites.", inline=False)
			embed.add_field(name = "Rule #8 ",value="XP-Grinding is prohibited.", inline=False)
			embed.add_field(name = "Rule #9 ",value="Do not ping staff members for no reason.", inline=False)
			embed.add_field(name = "Rule #10 ",value="Do not play music or other audio through your microphone if you can help it.", inline=False)
			embed.add_field(name = "Rule #11 ",value="Fake or harmful links or links that harm the safety of others, and Threatening, bullying or harassing others is forbidden", inline=False)
			embed.add_field(name = "__**Agreement**__",value="By adding a reaction you agree to abide by the given rules and acknowledge Any infraction may result in a mute,kick or ban depending on severity of infraction.", inline=False)
			sendmsg = await ctx.send(embed=embed)
			await sendmsg.add_reaction("🤝")
		else:
			await ctx.send("You do not have permission for this command.")

def setup(bot):
	bot.add_cog(moderation(bot))
