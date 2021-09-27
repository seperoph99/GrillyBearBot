import json
import os
import platform
import sys
import re
import json
import mysql.connector

class Database:
	dbConnect = False
	db = False
	STARTCURRENCY = 150
	DAILYVAL = 100
	BALANCE = 2
	Columns = {"ID":0, "Username": 1, "Balance":2, "SlotPlays":3, "SlotWins":4, "Daily":5}
	CURRENCY = '₿₿' # Can Change this to emoji or other currency symbol | Bear Bucks
	CURRENCY_NAME = 'BearBucks'
	# BALANCE = 1
	# SLOTWINS = 2



	def __init__(self): # Class Constructor
		"""
		Call Constructor

		Initializes Database Connection and Database Cursor
		"""
		self.dbConnect = mysql.connector.connect(
			host="na01-sql.pebblehost.com",
			user="customer_189330_grillybear",
			password="VaNeeb2mn@GrN1fqtNFY",
			database="customer_189330_grillybear"
		)
		if self.dbConnect.is_connected() == True:
			self.db = self.dbConnect.cursor()
			print('Connection made. DB set to cursor.')
		else:
			print('There was an error connecting.')
		
	

	# ID and Users

	def getID(self, id):
		""" Get the entire row from the specified user ID
		
		Returns entire row if the user ID is found.
		Return 0 if ID is not found.
		"""
		try : # Search for given ID
			self.db.execute("SELECT * FROM Users WHERE ID = %s",(id,))
			return self.db.fetchall()
		except() : # Given ID Not Found in DB
			print('Error! User ID NOT FOUND!')
			return 0


	def createUser(self, member):
		"""
		Creates a new user in the database. Gets the ID to create a new line.

		Checks if user exists in database already and creates new user if not found in database.
		Prints error if user already exists in database.
		"""
		id = member.id
		name = str(member)
		if len(self.getID(id)) == 0: # Not found in DB - Free to create
			print('ID not found, creating new user.')
			sql = "INSERT INTO Users (ID,Username,Balance) VALUES (%s,%s,%s)"
			val = (id,name,self.STARTCURRENCY)
			self.db.execute(sql,val)
			self.dbConnect.commit()
			return True
		else:
			print('Error.')
			return False


	# Balance Prints

	def printCurrency(self, value):
		"""
		Prints value of given int with comma separated thousands.
		"""
		return self.CURRENCY + ' ' + '{:,}'.format(value)

	def printBalance(self, id):
		"""
		Prints out full currency in display format

		Format: self.Currency(Symbol) Balance Amount self.CurrencyName(Name)
		"""
		return f'{self.CURRENCY} ' + '{:,}'.format(self.getID(id)[0][self.BALANCE]) #+ f' {self.CURRENCY_NAME}'


	# Balance

	def getBal(self, id):
		"""
		Gets the balance of a user from the given user ID

		Returns int of user balance
		"""
		return self.getID(id)[0][self.Columns["Balance"]]

	def addMoney(self, id, amount):
		"""
		Adds amount given to balance of the given user ID

		Has no return.
		"""
		balance = self.getBal(id)
		addition = int(amount)
		addition = balance + addition

		update = "UPDATE Users SET Balance = %s WHERE ID = %s"
		self.db.execute(update,(addition,id))

		#Commiting the changes to the database
		self.dbConnect.commit()

	def subMoney(self, id, amount):
		"""
		Subtracts amount given to balance of given user ID if their balance is greater than the amount

		Amount should be positive.

		Returns False if the amount < users balance.
		Returns True and Subtracts amount from user balance if balance > amount.
		"""
		balance = self.getBal(id)

		if amount > balance: # User does not have enough money for action
			return False
		else: # User has enough money
			amount = 0 - amount 
			self.addMoney(id, amount)
			return True


	# Stats

	def addStat(self, id, stat):
		"""
		Adds to the selected stat of the given user ID
		"""
		statValue = self.Columns[stat]
		if statValue == self.Columns["SlotPlays"]: # Slot Plays Stat
			
			# Get stat value first
			self.db.execute("SELECT SlotPlays FROM Users WHERE ID = %s",(id,))
			results = self.db.fetchall()
			
			# Grab stat in int value & increment
			plays = int(results[0][0])
			plays += 1
			# Apply back into DB
			self.db.execute("UPDATE Users SET SlotPlays = %s WHERE ID = %s",(plays, id))

			# print('Added Slot Play')

		elif statValue == self.Columns["SlotWins"]: # Slot Wins Stat
			
			# Get stat value first
			self.db.execute("SELECT SlotWins FROM Users WHERE ID = %s",(id,))
			results = self.db.fetchall()

			# Grab stat in int value & increment
			wins = int(results[0][0])
			wins += 1
			# Apply back into DB
			self.db.execute("UPDATE Users SET SlotWins = %s WHERE ID = %s",(wins, id))

			# print('Added Slot Win')

		self.dbConnect.commit()

	def getStat(self, id, stat):
		"""
		"""
		stat = self.getBal(id)[0][self.Columns[stat]]
		return stat


	# Daily

	def claimDaily(self, id):
		"""
		Claims the daily pay for a user

		Checks if the user has already claimed their daily

		Returns True and adds daily amount to user.
		Returns False if the user has already claimed their daily.
		"""
		self.db.execute("SELECT Daily FROM Users WHERE ID = %s",(id,))
		daily = self.db.fetchall()[0][0]

		if daily == 0: # Claim Daily
			self.addMoney(id, self.DAILYVAL)
			self.db.execute("UPDATE Users SET Daily = 1 WHERE ID = %s",(id,))
			self.dbConnect.commit()
			return True
		else: # Already Claimed
			return False