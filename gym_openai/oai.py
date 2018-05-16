#!/usr/bin/python
import gym
import sys
import os
RENDER = True
try:
	test = str(sys.argv[1])
	env = gym.make(test)
	env.monitor.start('/tmp/{0}-1'.format(test[2:]))
	env.reset()
	counter = 0
	while 1:
    		tick = counter + 1
    		counter = tick
		if RENDER == True:
    			env.render()
		if RENDER == False:
			print "No render needed"
    		action = env.action_space.sample() # take a random action
    		observation, reward, done, info = env.step(action)
    		print observation
    		if done:
			apikey = file('APIKey', 'r').read()
			print "Episode {0} finished".format(counter)
			env.monitor.close()
			writeup = os.popen("gist OpenAI").read()
			gym.upload('/tmp/{0}-1'.format(test[2:]), writeup=writeup,api_key=str(apikey).strip("\n"))
        		break
except KeyboardInterrupt:
	env.monitor.close()
	sys.exit()
except IndexError:
	print "Error! Missing Test."
	print "Please run: "
	print "{0} Test-v0".format(sys.argv[0])
	sys.exit()
except gym.error.UnregisteredEnv:
	print "Test not found!"
	sys.exit()	
except gym.error.UnsupportedMode:
	print "This doesnt support render mode!"
	RENDER = False
