#imports
import time
import os
import sys
import signal

##########################################################################################

#delay print function
def delay_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.07)

#keyboard interrupt hanadler
def sigint_handler(signal, frame):
	delay_print('\nInterrupt caught \n')
	delay_print("cleaning stack traces... \n")
	sys.exit(0)
signal.signal(signal.SIGINT,sigint_handler)


##########################################################################################


#running code

