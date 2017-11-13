from __future__ import print_function
import csv
import pandas as pd
import time


from pymongo import MongoClient
import pymongo
import datetime
import pprint

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.chase
collection = db.checking6980
collection.create_index([("Datetime", pymongo.ASCENDING)], unique=True)

def strToUnix(date):
	return int(time.mktime(datetime.datetime.strptime(date, "%m/%d/%Y").timetuple()))
	
def toNone(row):
	for i,item in zip(range(len(row)),row):
		if((item == "") or (item == " ")):
			row[i] = None
	return row

chase = "Chase"
accountNum = "6980"
activity = "_Activity_20170731.CSV"

fileName = chase + accountNum + activity
print(fileName)

trans_template = {"Details": None,
					"Posting Date": None,
					"Description": None,
					"Amount": None,
					"Type": None,
					"Balance": None,
					"Check or Slip #": None,
					"Datetime": None
				}


with open(fileName, 'rb') as csvfile:
	transactions = csv.reader(csvfile, delimiter=',', quotechar='"')
	trans_list = list(transactions)
	trans_len = len(trans_list)
	
	prevDate = None
	dateCounter = 0
	for i in reversed(range(trans_len)):
		if(i == 0):
			continue
		else:
			row = trans_list[i]
			toNone(row)
			
			if(row[1] == prevDate):
				dateCounter+=1
			else:
				dateCounter = 0
				
			
			timestamp = strToUnix(row[1]) + dateCounter
			toInsert = {"Details": row[0],
					"Posting Date": row[1],
					"Description": row[2],
					"Amount": row[3],
					"Type": row[4],
					"Balance": row[5],
					"Check or Slip #": row[6],
					"Datetime": timestamp
				}
			prevDate = toInsert["Posting Date"]
			#pprint.pprint(toInsert)
			try:
				docId = collection.insert_one(toInsert).inserted_id
				print(docId)
			except(pymongo.errors.DuplicateKeyError):
				print(toInsert["Description"] + " already inserted.")
