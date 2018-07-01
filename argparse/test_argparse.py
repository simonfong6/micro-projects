import argparse

def main(args):
	print(args.port)
	print(args.debug)
	pass

if(__name__ == '__main__'):
	parser = argparse.ArgumentParser()
	parser.add_argument('-p','--port', help="Port that the server will run on.", type=int, default=8080)
	parser.add_argument('-d','--debug', help="Whether or not to run in debug mode.", default=False, action='store_true')
	args = parser.parse_args()
	main(args)