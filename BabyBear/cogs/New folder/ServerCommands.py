import os
import sys
from discord import client
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




class Server_Commands(commands.Cog, name="Server_Commands"):
	def __init__(self, bot):
		self.bot = bot


	@slash_command(name="ping",description="Checks the status of the bot",guild_ids = guild_ids)
	#@commands.command(name="ping")
	async def ping(self, context):
		embed = discord.Embed(
			color=config["success"]
		)
		embed.add_field(
			name="Bot Check",
			value="I am fully functional!",
			inline=True
		)
		await context.send(embed=embed)


	# @commands.command(name="server")
	# async def server(self, context):
	# 	 """
	# 	 Get the invite link of the grillybear server.
	# 	 """
	# 	 await context.send("I sent you a private message!")
	# 	 await context.author.send("Join my discord server by clicking here: https://discord.gg/aYAcKbrFJs")

	



def setup(bot):
	bot.add_cog(Server_Commands(bot))