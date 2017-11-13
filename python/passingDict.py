
def changeDict(data):
	data["key1"] = 4

def main():
	data = {
		"key1": 1,
		"key2": 2,
		"key3": 3
	}
	print data
	changeDict(data)
	print data

if (__name__ == "__main__"):
	main()
