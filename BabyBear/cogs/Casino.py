import asyncio
import json
import os
import platform
import random
import sys
import math
import string
import re
import aiohttp
import discord
import yaml
from discord.ext import commands
from datetime import datetime
import database
from dislash import InteractionClient, Option, OptionType,slash_command, ActionRow, Button, ButtonStyle


if not os.path.isfile("config.yaml"):
	sys.exit("'config.yaml' not found! Please add it and try again.")
else:
	with open("config.yaml") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)


class Casino(commands.Cog, name="casino"):
	def __init__(self, bot):
		self.bot = bot


	JACKPOT = 10000

	@commands.group(name="casino")
	async def Casino_Commands(self, context):
		'''
		Lists all casino commands
		'''
		embed = discord.Embed(
			title="Casino Commands",
			description=" slots - play the casino slots \n pay - checks the payout of all casino games.",
			color=config["success"]
		)
		await context.send(embed=embed)


	@commands.command(name="slots")
	async def slots(self, context):
		"""
		Slot machine
		"""
		
		if context.invoked_subcommand is None:
			PRICE = 15
			DB = database.Database()
			ID = context.author.id
			#			  0		1	  2      3     4      5     6      7     8     9     10     11    12    13     14    15    16
			pictures = ["🍒", "🔔", "🍋", "🍉", "7️⃣", "🐻", "🍒", "🍋", "🔔", "🍒", "🍉", "🍋", "🔔", "🍒", "7️⃣", "🔔", "🍉"]
			values = {"🍒":0, "🔔":1, "🍋":2, "🍉":3, "7️⃣":4, "🐻":5}
			amount = [35, 80, 175, 450, 1200, self.JACKPOT]

			rarityLow = [[0, 6, 9, 13], [1, 8, 12, 15]] # Cherries & Bells
			rarityMid = [2, 7, 11] # Lemons
			rarityHigh = [3, 10, 16] # Melons
			rarityRare = [4, 14] # Sevens
			rarityUltra = [5] # Bear

			value = 0
			playing = True


			# Amount Wager ?
			# Default Amount -


			# Output Info
			state = ""
			output = ""
			win = ""
			
			# Remove command call
			await context.message.delete()

			# Full Play
			def pull():

				slots = [0, 0, 0]

				rowPay = ["", "", ""]

				# Initialize Random
				random.seed(datetime.now())
				rand1 = random.randint(1, 10)
				rand2 = random.randint(0, 1000)
				rand3 = random.randint(0, 100)

				# rand1 1 - 4 = match 2
				# rand1 6 - 10 = full random roll
				if rand1 < 4: # 30%
					# Match
					self.state = "2"
					if rand2 < 497: # 49.7% | 0 - 497
						# Cherries / Bells
						pick = random.randint(0,1)
						slots[0] = rarityLow[pick][random.randint(0, (len(rarityLow[pick])-1))]
						slots[1] = rarityLow[pick][random.randint(0, (len(rarityLow[pick])-1))]
						value = pick
					elif rand2 < 737: # 23.9% | 498 - 737
						# Lemons
						slots[0] = rarityMid[random.randint(0, (len(rarityMid)-1))]
						slots[1] = rarityMid[random.randint(0, (len(rarityMid)-1))]
						value = 2
					elif rand2 < 918: # 18% | 738 - 918
						# Melons
						slots[0] = rarityHigh[random.randint(0, (len(rarityHigh)-1))]
						slots[1] = rarityHigh[random.randint(0, (len(rarityHigh)-1))]
						value = 3
					elif rand2 < 989: # 7% | 919 - 989
						# Sevens
						slots[0] = rarityRare[random.randint(0, (len(rarityRare)-1))]
						slots[1] = rarityRare[random.randint(0, (len(rarityRare)-1))]
						value = 4
					else: # 1% | 990 - 1000
						# Bear Jackpot
						slots[0] = pictures[rarityUltra[0]]
						slots[1] = pictures[rarityUltra[0]]
						value = 5

							
					rowPay[0] = pictures[slots[0]]
					rowPay[1] = pictures[slots[1]]
					if rand3 > 50: # 50% | Match Third
						slots[2] = slots[0]
						self.state += "W"
					else:
						slots[2] = random.randint(0, len(pictures)-1)
						self.state += "R"

					rowPay[2] = pictures[slots[2]]
				else:
					# Full Random
					self.state = "R"
					slots[0] = random.randint(0, (len(pictures)-1))
					slots[1] = random.randint(0, (len(pictures)-1))
					slots[2] = random.randint(0, (len(pictures)-1))
					rowPay[0] = pictures[slots[0]]
					rowPay[1] = pictures[slots[1]]
					rowPay[2] = pictures[slots[2]]
					value = values[rowPay[2]]


				# Align Columns
				rowTop = [(slots[0] - 1), (slots[1] - 1), (slots[2] - 1)]
				rowBtm = [(slots[0] + 1), (slots[1] + 1), (slots[2] + 1)]

				# Correct out of range
				for i in range (3):
					if (slots[i]-1) < 0:
						rowTop[i] = pictures[len(pictures)-1]
					else:
						rowTop[i] = pictures[slots[i]-1]

				for i in range(3):
					if (slots[i]+1) > (len(pictures)-1):
						rowBtm[i] = pictures[0]
					else:
						rowBtm[i] = pictures[slots[i]+1]

				#
				# Add Win Amount!
				#
				# Win / Lose
				if rowPay[0] == rowPay[1] and rowPay[1] == rowPay[2]:
					winnings = amount[value]
					DB.addMoney(context.author.id, winnings)
					DB.addStat(ID, "SlotWins")
					self.win = f"You Win ${winnings}!" # + Amount
					
				else:
					self.win = "You Lose. Better Luck Next Time!"

				self.output = f"\u200B\n   |  {rowTop[0]}  |  {rowTop[1]}  |  {rowTop[2]}  |\n>|  {rowPay[0]}  |  {rowPay[1]}  |  {rowPay[2]}  |< Payline\n   |  {rowBtm[0]}  |  {rowBtm[1]}  |  {rowBtm[2]}  |"


			embed = discord.Embed(title = "Bear Slots",description = "")

			# Start of execute
			if DB.subMoney(context.author.id, PRICE) == True: # Check Balance before play
				playing = True
				self.JACKPOT += 5
				DB.addStat(ID, "SlotPlays")
				pull()
				embed.description = f"{context.author.display_name} spent ${PRICE} to spin!"
				embed.set_thumbnail(url="https://upld.im/images/9poT2q.png")
				embed.add_field(name=self.output, value="\u200B")
				embed.color = discord.Color.random()
				embed.set_footer(text=f"{self.win} {self.state}")

			else: # Not Enough Balance
				playing = False
				embed.description = f"You don't have enough money to play!"
				embed.color(0xAA0000)

				await context.send(embed=embed)

			gameOutput = await context.send(embed=embed)

			# Check for matching emoji & user command caller
			def check(reaction, user):
				return user == context.message.author and str(reaction) == "🎰"

			while(playing):
				
				await gameOutput.add_reaction("🎰")

				try:
					reaction, user = await self.bot.wait_for("reaction_add", timeout=15, check=check)
					await gameOutput.clear_reactions()
					if DB.subMoney(context.author.id, PRICE) == True:
						playing = True
						self.JACKPOT += 5
						DB.addStat(ID, "SlotPlays")
						pull()

						embed = discord.Embed(
							title = "Bear Slots" ,
							description = f"{context.author.display_name} spent ${PRICE} to spin again!",
							color = discord.Colour.random(),
						)
						embed.set_thumbnail(url="https://upld.im/images/9poT2q.png")
						embed.add_field(name=self.output, value="\u200B")
						embed.color = discord.Color.random()
						embed.set_footer(text=f"{self.win} {self.state}")

					else:
						playing = False
						embed = discord.Embed(
						title = "Bear Slots" ,
						description = f"You don't have enough money to play!",
						color = 0xAA0000
						)

					await gameOutput.edit(embed=embed)

				except:
					await gameOutput.clear_reactions()
					playing = False



	@commands.command(name="slotspay")
	async def slots_pay(self, context):
		"""
		View the payouts
		"""
		
		stuff = None
		embed = discord.Embed(
			title = "Slot Machine Payouts",
			description = "You can win *sometimes*™",
			color = config["success"]
		)
		#embed.set_thumbnail(url="🎰")
		embed.add_field(name="🍒🍒🍒", value="35")
		embed.add_field(name="🔔🔔🔔", value="80")
		embed.add_field(name="🍋🍋🍋", value="175")
		embed.add_field(name="🍉🍉🍉", value="450")
		embed.add_field(name="7️⃣7️⃣7️⃣", value="1200")
		#embed.add_field(name="\u200B", value="\u200B", inline=False)
		embed.add_field(name="🐻🐻🐻", value=f"Jackpot: {'{:,}'.format(self.JACKPOT)}", inline=False)
		await context.message.delete()
		await context.send(embed=embed)

		

	
def setup(bot):
	bot.add_cog(Casino(bot))
