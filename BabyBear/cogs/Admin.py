import os
import sys
import mysql.connector
import database
import random
import discord
import yaml
import json
from discord.ext import commands
from dislash import InteractionClient, Option, OptionType,slash_command, ActionRow, Button, ButtonStyle
guild_ids = [317357005687750657]

if not os.path.isfile("config.yaml"):
	sys.exit("'config.yaml' not found! Please add it and try again.")
else:
	with open("config.yaml") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)


class owner(commands.Cog, name="owner"):
	def __init__(self, bot):
		self.bot = bot





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



	@slash_command(name="logfile",description="(Admin Only)Sends you a copy of the current chat history.",guild_ids = guild_ids,options = [
		Option("yourname","The user you want to send the log file to.",OptionType.USER,required=True)])
	async def Posts(self, context,yourname:discord.User):
		if context.author.id == 307234299164360704 or context.author.id ==205865007395766272:

			with open("ChatLog.txt", "rb") as file:
				await yourname.send(context.author,file=discord.File(file,"ChatLog.txt"))
			with open("Voice_Log.txt", "rb") as file:
				await yourname.send(context.author,file=discord.File(file,"VoiceLog.txt"))
			await context.send("I sent you a copy.")
		else:
			await context.send("You are not permitted to do this action, contact a developer if this is a mistake.")


	@slash_command(name="createreactionroles",description="Creates Reaction Roles message",guild_ids = guild_ids)
	async def giveaway(self,ctx):
		if ctx.author.id == 205865007395766272:
			embed = discord.Embed(
				title="Reaction Roles",
				description="React with 🎉 to be given the giveaway role.\n\n React with 🏆 to be notifed of trophy case voting sessions.",
				color=config["success"]
			)
			sendmsg = await ctx.send(embed=embed)
			await sendmsg.add_reaction("🎉")
			await sendmsg.add_reaction("🏆")
		else:
			await ctx.send("You do not have permission for this command.")


def setup(bot):
	bot.add_cog(owner(bot))
