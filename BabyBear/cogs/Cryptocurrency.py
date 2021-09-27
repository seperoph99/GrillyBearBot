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


class cryptocurrency(commands.Cog, name="cryptocurrency"):
	def __init__(self, bot):
		self.bot = bot

	# BITCOIN
	@slash_command(name="cryptobitcoin",description="Displays current bitcoin prices",guild_ids = guild_ids)
	async def bitcoin(self, context):
		"""
		Price of Bitcoin.
		"""
		url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true"
		# Async HTTP request
		async with aiohttp.ClientSession() as session:
			raw_response = await session.get(url)
			response = await raw_response.text()
			response = json.loads(response)

			price = response['bitcoin']['usd']
			if price < 1:
				price = '{:,.6f}'.format(price)
			else:
				price = '{:,}'.format(price)
			change = response['bitcoin']['usd_24h_change']
			valType = ''
			if change > 0:
				valType = '+'

			embed = discord.Embed(
				title="Bitcoin (BTC)",
				color=0xf7931a #discord.Colour.from_rgb(247, 147, 26) #f7931a
			)
			embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@9ab8d6934b83a4aa8ae5e8711609a70ca0ab1b2b/128/color/btc.png")
			embed.add_field(name='USD', value=f"${price} ({valType}{change:.2f}%)",inline=False)
			embed.add_field(name="URL", value="https://www.coingecko.com/en/coins/bitcoin",inline=False)
			Command_Log = ctx.author.name+"ran Command Crypto_Bitcoin"
			f = open("Console_Log.txt","a")
			f.write(Command_Log)
			f.close
			await context.send(embed=embed)

	# DOGECOIN
	@slash_command(name="cryptodoge",description="Displays current DogeCoin prices",guild_ids = guild_ids)
	async def dogecoin(self, context):
		"""
		Price of Dogecoin.
		"""
		url = "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd&include_24hr_change=true"
		# Async HTTP request
		async with aiohttp.ClientSession() as session:
			raw_response = await session.get(url)
			response = await raw_response.text()
			response = json.loads(response)

			price = response['dogecoin']['usd']
			if price < 1:
				price = '{:,.6f}'.format(price)
			else:
				price = '{:,}'.format(price)
			change = response['dogecoin']['usd_24h_change']
			valType = ''
			if change > 0:
				valType = '+'

			embed = discord.Embed(
				title="Dogecoin (DOGE)",
				color=0xc3a634 #discord.Colour.from_rgb(195, 166, 52) #c3a634
			)
			embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@9ab8d6934b83a4aa8ae5e8711609a70ca0ab1b2b/128/color/doge.png")
			embed.add_field(name='USD', value=f"${price} ({valType}{change:.2f}%)",inline=False)
			embed.add_field(name="URL", value="https://www.coingecko.com/en/coins/dogecoin",inline=False)
			Command_Log = ctx.author.name+"ran Command CryptoDoge"
			f = open("Console_Log.txt","a")
			f.write(Command_Log)
			f.close
			await context.send(embed=embed)

	# ETHEREUM
	@slash_command(name="cryptoethereum",description="Displays current Ethereum prices",guild_ids = guild_ids)
	async def ethereum(self, context):
		"""
		Price of Ethereum.
		"""
		url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_24hr_change=true"
		# Async HTTP request
		async with aiohttp.ClientSession() as session:
			raw_response = await session.get(url)
			response = await raw_response.text()
			response = json.loads(response)
			price = response['ethereum']['usd']
			if price < 1:
				price = '{:,.6f}'.format(price)
			else:
				price = '{:,}'.format(price)
			change = response['ethereum']['usd_24h_change']
			valType = ''
			if change > 0:
				valType = '+'

			embed = discord.Embed(
			title="Ethereum (ETH)",
			color=0x62688f
		)
			embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/279/large/ethereum.png")
			embed.add_field(name='USD', value=f"${price} ({valType}{change:.2f}%)",inline=False)
			embed.add_field(name="URL", value="https://www.coingecko.com/en/coins/ethereum",inline=False)
			await context.send(embed=embed)

	# CUMROCKET
	@slash_command(name="cryptoecum",description="Displays current CumRocket prices",guild_ids = guild_ids)
	async def cumrocket(self, context):
		"""
		Price of CumRocket.
		"""
		url = "https://api.coingecko.com/api/v3/simple/price?ids=cumrocket&vs_currencies=usd&include_24hr_change=true"
		# Async HTTP request
		async with aiohttp.ClientSession() as session:
			raw_response = await session.get(url)
			response = await raw_response.text()
			response = json.loads(response)
			price = response['cumrocket']['usd']
			if price < 1:
				price = '{:,.6f}'.format(price)
			else:
				price = '{:,}'.format(price)
			change = response['cumrocket']['usd_24h_change']
			valType = ''
			if change > 0:
				valType = '+'

			embed = discord.Embed(
			title="CumRocket (CUMMIES)",
			color=0xe1498b
		)
			embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/15088/large/logo-2_%282%29.png")
			embed.add_field(name='USD', value=f"${price} ({valType}{change:.2f}%)",inline=False)
			embed.add_field(name="URL", value="https://www.coingecko.com/en/coins/cumrocket",inline=False)
			await context.send(embed=embed)

	# LITECOIN
	@slash_command(name="cryptolite",description="Displays current LiteCoin prices",guild_ids = guild_ids)
	async def litecoin(self, context):
		"""
		Price of Litecoin.
		"""
		url = "https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd&include_24hr_change=true"
		# Async HTTP request
		async with aiohttp.ClientSession() as session:
			raw_response = await session.get(url)
			response = await raw_response.text()
			response = json.loads(response)
			price = response['litecoin']['usd']
			if price < 1:
				price = '{:,.6f}'.format(price)
			else:
				price = '{:,}'.format(price)
			change = response['litecoin']['usd_24h_change']
			valType = ''
			if change > 0:
				valType = '+'

			embed = discord.Embed(
			title="Litecoin (LTC)",
			color=0xbfbbbb
		)
			embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@9ab8d6934b83a4aa8ae5e8711609a70ca0ab1b2b/128/color/ltc.png")
			embed.add_field(name='USD', value=f"${price} ({valType}{change:.2f}%)",inline=False)
			embed.add_field(name="URL", value="https://www.coingecko.com/en/coins/litecoin",inline=False)
			await context.send(embed=embed)

	# MONERO
	@slash_command(name="cryptoxmr",description="Displays current Monero prices",guild_ids = guild_ids)
	async def monero(self, context):
		"""
		Price of Monero.
		"""
		url = "https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd&include_24hr_change=true"
		# Async HTTP request
		async with aiohttp.ClientSession() as session:
			raw_response = await session.get(url)
			response = await raw_response.text()
			response = json.loads(response)
			price = response['monero']['usd']
			if price < 1:
				price = '{:,.6f}'.format(price)
			else:
				price = '{:,}'.format(price)
			change = response['monero']['usd_24h_change']
			valType = ''
			if change > 0:
				valType = '+'

			embed = discord.Embed(
			title="Monero (XMR)",
			color=0xff6600
		)
			embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@9ab8d6934b83a4aa8ae5e8711609a70ca0ab1b2b/128/color/xmr.png")
			embed.add_field(name='USD', value=f"${price} ({valType}{change:.2f}%)",inline=False)
			embed.add_field(name="URL", value="https://www.coingecko.com/en/coins/monero",inline=False)
			await context.send(embed=embed)

	# PUSSY FINANCIAL
	@slash_command(name="cryptopus",description="Displays current Pussy Financial prices",guild_ids = guild_ids)
	async def pussyfin(self, context):
		"""
		Price of Pussy Financial.
		"""
		url = "https://api.coingecko.com/api/v3/simple/price?ids=pussy-financial&vs_currencies=usd&include_24hr_change=true"
		# Async HTTP request
		async with aiohttp.ClientSession() as session:
			raw_response = await session.get(url)
			response = await raw_response.text()
			response = json.loads(response)
			price = response['pussy-financial']['usd']
			if price < 1:
				price = '{:,.6f}'.format(price)
			else:
				price = '{:,}'.format(price)
			change = response['pussy-financial']['usd_24h_change']
			valType = ''
			if change > 0:
				valType = '+'

			embed = discord.Embed(
			title="Pussy Financial (PUSSY)",
			color=0xffb1a4
		)
			embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/15213/large/pussytoken.png")
			embed.add_field(name='USD', value=f"${price} ({valType}{change:.2f}%)",inline=False)
			embed.add_field(name="URL", value="https://www.coingecko.com/en/coins/pussy-financial",inline=False)
			await context.send(embed=embed)

def setup(bot):
	bot.add_cog(cryptocurrency(bot))
