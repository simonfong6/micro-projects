import random

numCorrect = 0
numTrials = 0

done = False
while(not done):
	prizeDoor = random.randint(0,2)

	doors = {0:False, 1:False, 2:False}
	doors[prizeDoor] = True

	initialGuess = int(raw_input("Which door do you think the prize is behind? [0,1,2]:"))

	notPrize = 0
	while((notPrize == prizeDoor) or (notPrize == initialGuess)):
		notPrize += 1

	print "It is not in door " + str(notPrize)
	guess = int(raw_input("What would you like to change your guess to?:"))	
	if(guess == prizeDoor):
		print "You win, it was behind door " + str(prizeDoor)
		numCorrect += 1
	else:
		print "You lose, it was behind door " + str(prizeDoor)

	numTrials += 1
	if((guess == 4) or (initialGuess == 4)):
		done = True
		numTrials -= 1
		print "In " + str(numTrials) + " rounds, you got " + str(numCorrect) + " correct"
