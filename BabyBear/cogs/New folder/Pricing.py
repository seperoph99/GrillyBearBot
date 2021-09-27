import os
import sys
import mysql.connector
import database
import discord
import yaml
import urllib.request
import json
from discord.ext import commands
from dislash import InteractionClient, Option, OptionType,slash_command, ActionRow, Button, ButtonStyle


guild_ids = [317357005687750657]

if not os.path.isfile("config.yaml"):
	sys.exit("'config.yaml' not found! Please add it and try again.")
else:
	with open("config.yaml") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)


class Pricing(commands.Cog, name="pricing"):
	def __init__(self, bot):
		self.bot = bot





	@slash_command(name="updateapp",description="Updates the app_id list from steam",guild_ids = guild_ids)
	async def Update_App_ID_List(self,ctx):
		request = urllib.request.Request('http://api.steampowered.com/ISteamApps/GetAppList/v0002/')
		response_body = urllib.request.urlopen(request).read()
		parsed = json.loads(response_body)
		parsedstring = json.dumps(parsed)
		jsonFile = open("appid_list.json", "w")
		jsonFile.write(parsedstring)
		jsonFile.close()
		await ctx.send("The Appid file has been updated")


	@slash_command(name="gamestats",description="shows how many players are currently online (Case sensitive and spelling needs to be accurate!)",guild_ids = guild_ids,
	options = [
		Option("game","the name of the game you want the player stats for.",OptionType.STRING,required=True)])
	async def Find_App_ID(self, ctx,game):
		f = open('appid_list.json',)
		data = json.load(f)
		data = data['applist']['apps']
		for x in data:
			keys = x.keys()
			values = x.values()
			if game in values:
				values = str(values)
				values = values.replace('dict_values',"")
				values = values.replace(game,"")
				values = values.replace("'","")
				values = values.replace('[',"")
				values = values.replace(']',"")
				values = values.replace('(',"")
				values = values.replace(')',"")
				values = values.replace(',',"")
				values = values.replace(' ',"")
				values = str(values)
				appid = values
				#Start of api call
				request = urllib.request.Request('https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?&appid='+appid)
				response_body = urllib.request.urlopen(request).read()
				parsed = json.loads(response_body)
				playercount = parsed['response']
				playercount = str(playercount)
				playercount = playercount.replace(", 'result': 1}","")
				playercount = playercount.replace("'","")
				playercount = playercount.replace("{player_count: ","")
				playercount = int(playercount)
				playercount = ('{:,}'.format(playercount))

				message ="```There is currently "+playercount+" Online for "+game+"```"
				await ctx.send(message)


	@slash_command(name="deals",description="Gets all prices for a game of your choosing(Spelling is important)",
	options=[Option('game','The Name of the game you want to search.',OptionType.STRING)],
	guild_ids = guild_ids)
	async def GameDealChecker(inter,ctx,game):
		key = 'a7a4795d8f5a4d0a82ab6a29098bc9a30d55713a'
		game = game
		# for word in args:
		# 	game += word
		title = game
		game = str(game)
		game = game.replace(" ","%20")
		
		results = None
		gameData = None
		try:
			# Plain Data
			request = urllib.request.Request('https://api.isthereanydeal.com/v02/game/plain/?key='+key+'&title='+game)
			response_body = urllib.request.urlopen(request).read()
			parsed = json.loads(response_body)
			game = parsed['data']['plain']

			# Price Data
			request = urllib.request.Request('https://api.isthereanydeal.com/v01/game/prices/?key='+key+'&plains='+game+'&exclude=voidu%2Citchio')
			response_body = urllib.request.urlopen(request).read()
			parsed = json.loads(response_body)
			
			results = parsed["data"][game]["list"]

			# Game Info
			request = urllib.request.Request('https://api.isthereanydeal.com/v01/game/info/?key='+key+'&plains='+game)
			response_body = urllib.request.urlopen(request).read()
			gameData = json.loads(response_body)
			gameData = gameData["data"][game]

			title = gameData["title"]
		
		except:
			pass

		if results is None: # Not Found

			embed = discord.Embed(
				title=f'{title} not found!',
				description='Check your spelling and try again.',
				color=config["error"]
			)
		elif len(results) == 0 :# Without Price Results

			embed = discord.Embed(
				title=f'No prices for {title} found.',
				description='',
				color=config["error"]
			)
		else: # Full Listing
			embed = discord.Embed(
				title=f'Prices for {title}',
				description=f'Original Price ${results[0]["price_old"]}',
				url=gameData["urls"]["game"],
				color=config["success"]
			)

			if gameData["image"] is not None:
				embed.set_thumbnail(url=gameData["image"])

			for store in results:
				embed.add_field(name=f'{store["shop"]["name"]}', value=f'[${"{:,.2f}".format(store["price_new"])}]({store["url"]}) ({"-" + str(store["price_cut"]) + "%" if (store["price_cut"] > 0) else (str(store["price_cut"]) + "%")})\n{store["drm"][0] if (len(store["drm"]) != 0) else ("")}')

		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Pricing(bot))
