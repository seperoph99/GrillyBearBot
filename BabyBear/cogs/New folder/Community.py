import os
import sys
import mysql.connector
import database
import discord
import asyncio
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


class Community(commands.Cog, name="community"):
	def __init__(self, bot):
		self.bot = bot




	@slash_command(name="vote",description="Creates a basic visual vote with emoji",guild_ids = guild_ids,
	options=[Option('vote','Describe what you are making a vote for.',OptionType.STRING)])
	async def VoteCommand(inter,ctx,vote):
		msg = await ctx.send(vote)
		await msg.add_reaction("✅")
		await msg.add_reaction("❌")

	@slash_command(name="gameservers",description="Lists avaliable game servers.",guild_ids = guild_ids)
	async def Game_Server_list(self,ctx):

		embed = discord.Embed(
			title = "Grilly Bear Game Servers.",
			description ="None Currently" ,
			color=config["success"],
		)
		await ctx.send(embed=embed)

	@slash_command(name="giveaway",description="Setup a give away with your description of choice.",guild_ids = guild_ids,options = [
		Option("itemname","what item you are using for the giveaway.",OptionType.STRING,required=True),
		Option("time","How many hours you want the giveaway to last before it draws.Integers only",OptionType.INTEGER,required=True)
		]
	)
	async def giveaway(self,ctx,itemname,time):
		inttime = time
		time = str(time)
		guild = ctx.guild
		giveaway = discord.utils.get(guild.roles,name="Giveaways")
		giveaway = (giveaway.id)
		giveaway = str(giveaway)
		
		roles = ctx.author.roles
		roles = str(roles)
		if '317781199709798410' in roles:
			if ctx.channel.id == 880903896686547004:
				embed = discord.Embed(
					title=" 🎉Giveaway hosted by "+ ctx.author.name+"🎉",
					description="Active Giveaway <@&"+giveaway+">",
					color=config["success"]
				)
				embed.add_field(name="prize",value = itemname,inline=False)
				embed.add_field(name="Giveaway End Time",value = "ends in "+time+" hours!")
				embed.add_field(name="How to enter",value = "simply react with 🐻 to this post and you will be automatically entered! ",inline=False)
				sendmsg = await ctx.send(embed=embed)
				await sendmsg.add_reaction("🐻")
				hostid = str(ctx.author.id)
				hostid = "<@"+hostid+">"
				time = int(time)*3600
				await asyncio.sleep(time)

				#Fetching the message
				msg1 = await sendmsg.channel.fetch_message(sendmsg.id)
				#Fetching the reactions and flattening to a readable list
				users = await msg1.reactions[0].users().flatten()
				#reading and writing the reaction list to giveawaylist.txt
				for user in users:
					userid = str(user)
					choices = open('giveawaylist.txt','a')
					choices.write(userid+"\n")
					choices.close()

				#Reading the giveawaylist.txt file
				f = open("giveawaylist.txt","r")
				lines = f.readlines()
				f.close()
				#writing to giveawylist.txt excluding any line that contains GrillyBear
				f = open("giveawaylist.txt","w")
				for line in lines:
					if "GrillyBear" not in line:
						f.write(line)
				f.close()
				#Reading Giveawylist one final time and picking a winner
				with open('giveawaylist.txt') as f:
					lines = f.readlines()
					winner = (random.choice(lines))
					if "GrillyBear#8983" in winner:
						winner = (random.choice(lines)) 



				embed2 = discord.Embed(
					title="🎉Giveaway hosted by "+ str(ctx.author.name)+"🎉",
					description="Closed Giveaway <@&"+giveaway+">",
					color=config["success"]
				)
				embed2.add_field(name="prize",value = itemname,inline=False)
				embed2.add_field(name="Giveaway ended",value = "This giveaway has ended.")
				embed2.add_field(name="Winner",value = "The winner is "+winner+"\n"+" DM "+hostid+" to receive your prize",inline=False)
				await sendmsg.edit(embed = embed2)
				open('giveawaylist.txt', 'w').close()
			else:
				await ctx.author.send("the giveaway command only works in the giveaway channel use it there only.")
		else:
			await ctx.send("You do not have permission to use this command.")


	@slash_command(name="giveaway-ping",description="Pings the giveaway role.",guild_ids = guild_ids)
	async def giveaway(inter,ctx):
		roles = ctx.author.roles
		roles = str(roles)
		if '317781199709798410' in roles:
			if ctx.channel.id == 880903896686547004:
				guild = ctx.guild
				giveaway = discord.utils.get(guild.roles,name="Giveaways")
				giveaway = (giveaway.id)
				giveaway = str(giveaway)
				await ctx.send("There is a new giveaway avaliable  <@&"+giveaway+">")
			else:
				await ctx.author.send("the giveaway-ping command only works in the giveaway channel use it there only.")
		else:
			await ctx.send("You do not have permission to use this command.")


def setup(bot):
	bot.add_cog(Community(bot))
