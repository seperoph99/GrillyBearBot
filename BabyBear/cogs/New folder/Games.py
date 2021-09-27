import asyncio
import json
import os
import platform
import random
import sys
import math
import requests
import string
import re
import aiohttp
import discord
import yaml
from discord.ext import commands
from datetime import datetime
import database
from dislash import InteractionClient, Option, OptionType,slash_command, ActionRow, Button, ButtonStyle
guild_ids = [317357005687750657]

if not os.path.isfile("config.yaml"):
	sys.exit("'config.yaml' not found! Please add it and try again.")
else:
	with open("config.yaml") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)


class Games(commands.Cog, name="games"):
	def __init__(self, bot):
		self.bot = bot



	@slash_command(name="coinflip",description="Flips a coin for your pleasure",guild_ids = guild_ids)
	async def flipCoin(self,ctx):
		"""
		Flip A Coin
		"""
		image = ""
		coin = random.randint(0,1)
		if coin == 0:
			coin = "Heads"
			image = "https://i.imgur.com/xyFEyeW.png"
		else:
			coin = "Tails"
			image = "https://i.imgur.com/mXTdUs2.png"
		embed = discord.Embed(
			title = ":coin: Coin Flip" ,
			description = f'Landed on: {coin}',
			color=0xffd54f
		)
		embed.set_image(url = image)
		await ctx.send(embed=embed)

	@slash_command(name="8ball",description="Ask the magic 8 ball anything you may not like the response, No refunds!",guild_ids = guild_ids,options = [
		Option("question","The question you would like to ask the 8ball.",OptionType.STRING,required=True)])
	async def eight_ball(inter, ctx,question):
		"""
		Ask any question to the bot.
		"""
		input = ""
		for words in question:
			input += words + ' '

		answers = ['As long as my creators allow it', 'It is certain.', 'It is decidedly so.',
					'You may rely on it.', 'Without a doubt.',
					'Yes - definitely.', 'I\'m not sure if I\'m designed to answer something such as this', 'As I see, yes','Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
					'Currently in hibernation, please try again later.', 'Reply hazy, try again.', 'Ask again later.',
					'Better not tell you now.', 'Try asking Andrew, he might know.', 'Cannot predict now.',
					'Concentrate and ask again later.', 'Feeling a pretty strong Yes for this one.', 'Don\'t count on it.',
					'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
		embed = discord.Embed(
			#title="**My Answer:**",
			color=discord.Colour.random()
		)
		embed.set_author(name="8Ball", url="", icon_url="https://i.imgur.com/dKy8a0T.png")
		embed.add_field(name="Question:", value=f"{input}", inline=False)
		embed.add_field(name="Answer:", value=f"{answers[random.randint(0, len(answers))]}", inline=False)
		await ctx.send(embed=embed)
		


				#Rock Paper Scissors Disabled due to slash commands breaking deleting the message to put a new on in place.

	# @cog_ext.cog_slash(name="rps",description="Play Rock Paper Scissors with GrillyBear Who will win",guild_ids = guild_ids)
	# async def rock_paper_scissors(self, context):
	# 	"""
	# 	Game of Rock, Paper, Scissors
	# 	"""
	# 	choices = {
	# 		0: "rock",
	# 		1: "paper",
	# 		2: "scissors"
	# 	}
	# 	reactions = {
	# 		"🪨": 0,
	# 		"🧻": 1,
	# 		"✂": 2
	# 	}
	# 	embed = discord.Embed(title="Please choose", color=config["warning"])
	# 	embed.set_author(name=context.author.display_name, icon_url=context.author.avatar_url)
	# 	choose_message = await context.send(embed=embed)
	# 	for emoji in reactions:
	# 		await choose_message.add_reaction(emoji)

	# 	def check(reaction, user):
	# 		return user == context.message.author and str(reaction) in reactions

	# 	try:
	# 		reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check)

	# 		user_choice_emote = reaction.emoji
	# 		user_choice_index = reactions[user_choice_emote]

	# 		bot_choice_emote = random.choice(list(reactions.keys()))
	# 		bot_choice_index = reactions[bot_choice_emote]

	# 		result_embed = discord.Embed(color=config["success"])
	# 		result_embed.set_author(name=context.author.display_name, icon_url=context.author.avatar_url)
	# 		await choose_message.clear_reactions()

	# 		if user_choice_index == bot_choice_index:
	# 			result_embed.description = f"**That's a draw!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
	# 			result_embed.colour = config["warning"]
	# 		elif user_choice_index == 0 and bot_choice_index == 2:
	# 			result_embed.description = f"**You won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
	# 			result_embed.colour = config["success"]
	# 		elif user_choice_index == 1 and bot_choice_index == 0:
	# 			result_embed.description = f"**You won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
	# 			result_embed.colour = config["success"]
	# 		elif user_choice_index == 2 and bot_choice_index == 1:
	# 			result_embed.description = f"**You won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
	# 			result_embed.colour = config["success"]
	# 		else:
	# 			result_embed.description = f"**I won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
	# 			result_embed.colour = config["error"]
	# 			await choose_message.add_reaction("🇱")
	# 		await choose_message.edit(embed=result_embed)
	# 	except asyncio.exceptions.TimeoutError:
	# 		await choose_message.clear_reactions()
	# 		timeout_embed = discord.Embed(title="Too late", color=config["error"])
	# 		timeout_embed.set_author(name=context.author.display_name, icon_url=context.author.avatar_url)
	# 		await choose_message.edit(embed=timeout_embed)

	@slash_command(name="trivia",description="trivia testing",guild_ids = guild_ids,options = [
		Option("category","What Category",OptionType.STRING,required=True),
		Option("difficulty","What difficulty. (Easy = 1,Medium = 2,Hard = 3",OptionType.STRING,required=True),
		Option("questiontype","Multiple choice = 1 True/False = 2",OptionType.STRING,required=True)])
	async def trivia_play(self,ctx,category,difficulty,questiontype):
		if difficulty == "1":
			difficulty = "easy"
			color = 0x2ecc71
		if difficulty == "2":
			difficulty = "medium"
			color = 0xf1c40f
		if difficulty == "3":
			difficulty = "hard"
			color = 0x992d22
		if questiontype == "1":
			questiontype = "multiple"
		if questiontype == "2":
			questiontype = "boolean"
		url = "https://opentdb.com/api.php?amount=1&category="+category+"&difficulty="+difficulty+"&type="+questiontype
		difficulty = difficulty.capitalize()
		response = requests.get(url)
		data = response.json()
		category = data['results'][0]['category']
		question = data['results'][0]['question']
		question = question.replace("&","")
		question = question.replace(";","")
		question = question.replace("quot","''")
		question = question.replace(",","")
		question = question.replace("#039","")
		question = question.replace(";","")
		question = question.replace("cute","")
		if questiontype == 'multiple':
			choices = [data['results'][0]['incorrect_answers'][0],data['results'][0]['incorrect_answers'][1],data['results'][0]['incorrect_answers'][2],data['results'][0]['correct_answer']]
			print(data['results'][0]['correct_answer'])
			choices = sorted(choices,key=lambda k: random.random())
			choicea = "A. "+choices[0]+"\n"
			choicea.replace("&","")
			choicea.replace("#039","")
			choicea.replace(";","")
			choicea.replace("&amp","")
			choicea.replace(";","")
			choiceb = "B. "+choices[1]+"\n"
			choiceb.replace("&","")
			choiceb.replace("#039","")
			choiceb.replace(";","")
			choicec = "C. "+choices[2]+"\n"
			choicec.replace("&","")
			choicec.replace("#039","")
			choicec.replace(";","")
			choiced = "D. "+choices[3]+"\n"
			choiced.replace("&","")
			choiced.replace("#039","")
			choiced.replace(";","")
			msg1 = "__"+difficulty+" "+category+" trivia__ \n"+"- "+question+"\n\n"+choicea+choiceb+choicec+choiced
			embed = discord.Embed(
				title = "__Trivia__ - "+difficulty,
				description = category,
				color=color
			)
			#embed.add_field(name="__Difficulty__:", value=difficulty, inline=False)
			#embed.add_field(name="__Category__:", value=category, inline=False)
			embed.add_field(name="__Question__:", value=question, inline=False)
			embed.add_field(name="__Choices__:", value=choicea+choiceb+choicec+choiced, inline=False)
			embed.set_footer(text= "Trivia question for "+ctx.author.name+"You have 60 seconds. Go!")
			embed.set_thumbnail(url='https://t1.rbxcdn.com/f4e705c0b75a0fc2c24eeec820cd7362')
			row_of_buttons = ActionRow(
				Button(
					style=ButtonStyle.blurple,
					label="A",
					custom_id="A"
				),
				Button(
					style=ButtonStyle.blurple,
					label="B",
					custom_id="B"
				),
				Button(
					style=ButtonStyle.blurple,
					label="C",
					custom_id="C"
				),
				Button(
					style=ButtonStyle.blurple,
					label="D",
					custom_id="D"
				)
			)
			
			msg = await ctx.send(embed = embed,components =[row_of_buttons])
			on_click = msg.create_click_listener(timeout=600)
			

			msg2 = discord.Embed(
				title = "__Trivia__ - "+difficulty,
				description = category,
				color=color
			)
			#msg2.add_field(name="__Difficulty__:", value=difficulty, inline=False)
			#msg2.add_field(name="__Category__:", value=category, inline=False)
			msg2.add_field(name="__Question__:", value=question, inline=False)
			msg2.add_field(name="__Choices__:", value=choicea+choiceb+choicec+choiced, inline=False)
			msg2.set_footer(text= "Trivia question for "+ctx.author.name)
			msg3 = discord.Embed(
				title = "__Trivia__",
				color=color
			)
			#msg3.add_field(name="__Difficulty__:", value=difficulty, inline=False)
			#msg3.add_field(name="__Category__:", value=category, inline=False)
			msg3.add_field(name="__Question__:", value=question, inline=False)
			msg3.add_field(name="__Choices__:", value=choicea+choiceb+choicec+choiced, inline=False)
			msg3.set_footer(text= "Trivia question for "+ctx.author.name)
			
			#Checking if user that presses the button is the user that called the command otherwise posts a message only that user can see saying they are not the author.
			@on_click.not_from_user(ctx.author, cancel_others=True, reset_timeout=False)
			async def on_wrong_user(inter):
				await inter.reply("You're not the author", ephemeral=True)



			incorrect = "The correct answer was "'"'+data['results'][0]['correct_answer']+'"'+"You are incorrect"

			#Checking on click for button A
			xp = random.randint(1,3)
			@on_click.matching_id("A")
			async def Choice_A(inter):
				if choices[0] in (data['results'][0]['correct_answer']):
					msg2.add_field(name="Answer:", value="The Correct answer was "+'"'+data['results'][0]['correct_answer']+'"'+" You are correct and have been awarded "+str(xp)+" Experience!", inline=False)
					with open('users.json','r') as f:
						users = json.load(f)
						user = ctx.author
						users[str(user.guild.id)][str(user.id)]['experience'] += xp
						with open('users.json','w') as f:
							json.dump(users, f)
					await msg.edit(embed=msg2,components = [])
				else:
					msg3.add_field(name="Answer:", value="The correct answer was "'"'+data['results'][0]['correct_answer']+'"'+"You are incorrect", inline=False)
					await msg.edit(embed=msg3,components = [])

			#Checking on click for button B
			@on_click.matching_id("B")
			async def Choice_B(inter):
				if choices[1] in (data['results'][0]['correct_answer']):
					msg2.add_field(name="Answer:", value="The Correct answer was "+'"'+data['results'][0]['correct_answer']+'"'+" You are correct and have been awarded "+str(xp)+" Experience!", inline=False)
					with open('users.json','r') as f:
						users = json.load(f)
						user = ctx.author
						users[str(user.guild.id)][str(user.id)]['experience'] += xp
						with open('users.json','w') as f:
							json.dump(users, f)
					await msg.edit(embed=msg2,components = [])
				else:
					msg3.add_field(name="Answer:", value="The correct answer was "'"'+data['results'][0]['correct_answer']+'"'+"You are incorrect", inline=False)
					await msg.edit(embed=msg3,components = [])

			#Checking on click for button C
			@on_click.matching_id("C")
			async def Choice_C(inter):
				if choices[2] in (data['results'][0]['correct_answer']):
					msg2.add_field(name="Answer:", value="The Correct answer was "+'"'+data['results'][0]['correct_answer']+'"'+" You are correct and have been awarded "+str(xp)+" Experience!", inline=False)
					with open('users.json','r') as f:
						users = json.load(f)
						user = ctx.author
						users[str(user.guild.id)][str(user.id)]['experience'] += xp
						with open('users.json','w') as f:
							json.dump(users, f)
					await msg.edit(embed=msg2,components = [])
				else:
					msg3.add_field(name="Answer:", value="The correct answer was "'"'+data['results'][0]['correct_answer']+'"'+"You are incorrect", inline=False)
					await msg.edit(embed=msg3,components = [])

			#Checking on click for button D
			@on_click.matching_id("D")
			async def Choice_D(inter):
				if choices[3] in (data['results'][0]['correct_answer']):
					msg2.add_field(name="Answer:", value="The Correct answer was "+'"'+data['results'][0]['correct_answer']+'"'+" You are correct and have been awarded "+str(xp)+" Experience!", inline=False)
					with open('users.json','r') as f:
						users = json.load(f)
						user = ctx.author
						users[str(user.guild.id)][str(user.id)]['experience'] += xp
						with open('users.json','w') as f:
							json.dump(users, f)
					await msg.edit(embed=msg2,components = [])
				else:
					msg3.add_field(name="Answer:", value="The correct answer was "'"'+data['results'][0]['correct_answer']+'"'+"You are incorrect", inline=False)
					await msg.edit(embed=msg3,components = [])
		if questiontype == "boolean":
			embed = discord.Embed(
				title = "__Trivia__ - "+difficulty,
				description = category,
				color=color
			)
			#embed.add_field(name="__Difficulty__:", value=difficulty, inline=False)
			#embed.add_field(name="__Category__:", value=category, inline=False)
			embed.add_field(name="__Question__:", value=question, inline=False)
			embed.add_field(name="__Choices__:", value="True Or False", inline=False)
			embed.set_footer(text= "Trivia question for "+ctx.author.name)
			row_of_buttons = ActionRow(
				Button(
					style=ButtonStyle.blurple,
					label="True",
					custom_id="True"
				),
				Button(
					style=ButtonStyle.blurple,
					label="False",
					custom_id="False"
				))
			msg = await ctx.send(embed = embed,components = [row_of_buttons])
			on_click = msg.create_click_listener(timeout=60)
			@on_click.not_from_user(ctx.author, cancel_others=True, reset_timeout=False)
			async def on_wrong_user(inter):
				await inter.reply("You're not the author", ephemeral=True)
			msg2 = discord.Embed(
				title = "__Trivia__ - "+difficulty,
				description = category,
				color=color
			)
			#msg2.add_field(name="__Difficulty__:", value=difficulty, inline=False)
			#msg2.add_field(name="__Category__:", value=category, inline=False)
			msg2.add_field(name="__Question__:", value=question, inline=False)
			msg2.add_field(name="__Choices__:", value="True Or False", inline=False)
			msg2.set_footer(text= "Trivia question for "+ctx.author.name)
			msg3 = discord.Embed(
				title = "__Trivia__",
				color=color
			)
			#msg3.add_field(name="__Difficulty__:", value=difficulty, inline=False)
			#msg3.add_field(name="__Category__:", value=category, inline=False)
			msg3.add_field(name="__Question__:", value=question, inline=False)
			msg3.add_field(name="__Choices__:", value="True Or False", inline=False)
			msg3.set_footer(text= "Trivia question for "+ctx.author.name)
			incorrect = "The correct answer was "'"'+data['results'][0]['correct_answer']+'"'+"You are incorrect"
			msg3.set_footer(text = incorrect)
						#Checking on click for button A
			@on_click.matching_id("True")
			async def Choice_A(inter):
				if "True" in (data['results'][0]['correct_answer']):
					msg2.add_field(name="Answer:", value="The Correct answer was "+'"'+data['results'][0]['correct_answer']+'"'+" You are correct", inline=False)
					await msg.edit(embed=msg2,components = [])
				else:
					msg3.add_field(name="Answer:", value="The correct answer was "'"'+data['results'][0]['correct_answer']+'"'+"You are incorrect", inline=False)
					await msg.edit(embed=msg3,components = [])
					
			#Checking on click for button A
			@on_click.matching_id("False")
			async def Choice_A(inter):
				if "False" in (data['results'][0]['correct_answer']):
					msg2.add_field(name="Answer:", value="The Correct answer was "+'"'+data['results'][0]['correct_answer']+'"'+" You are correct", inline=False)
					await msg.edit(embed=msg2,components = [])
				else:
					msg3.add_field(name="Answer:", value="The correct answer was "'"'+data['results'][0]['correct_answer']+'"'+"You are incorrect", inline=False)
					await msg.edit(embed=msg3,components = [])

	@slash_command(name="trivia_category",description="Displays all trivia categories",guild_ids = guild_ids)
	async def trivia_category(self,ctx):
		categories = "9 = General Knowledge \n 10 = Books \n 11 = film \n 12 = music \n 13 = musicals & theatre \n 14 = television \n  15 = video games \n 16 = board games \n \
			17 = science and nature \n 18 = computers \n 19 = mathematics \n 20 = mythology \n 21 = sports \n 22 = geography \n 23 = history \n 24 = politics \n 25 = art \n \
				26 = celebrities \n 27 = animals \n 28 = vehicles \n 29 = comics \n 30 = gadgets \n 31 = japanese anime & manga \n 32 = cartoon & animations "
		embed = discord.Embed(
			title = "Trivia Categories " ,
			description=categories,
			color=config["success"])
		await ctx.send(embed=embed)
	
def setup(bot):
	bot.add_cog(Games(bot))
