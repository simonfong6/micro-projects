myString = "temperature = 89, sound = 65, light = 355, heartrate = 85"

myList = myString.split(", ")

print myList

dataJSON = {}

for word in myList:
	print word
	key, equals, data = word.split(" ", 2)
	print key
	print equals
	print data
	dataJSON[key] = int(data)

print dataJSON


