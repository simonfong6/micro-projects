from __future__ import print_function
import csv
import pandas as pd

class Transaction:
	total = 0
	def __init__(self, details, posting_date, description, amount, 
		transaction_type, balance, check_slip_num):
		self.details = details
		self.posting_date = posting_date
		self.description = description
		self.amount = amount
		self.transaction_type = transaction_type
		self.balance = balance
		self.check_slip_num = check_slip_num
		self.total += float(amount)

from pymongo import MongoClient
import pymongo
import datetime
import pprint

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.chase
collection = db.checking6980

pprint.pprint(collection.find())
