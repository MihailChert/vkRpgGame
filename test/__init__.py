import os
import sys
import unittest
import logging
import pdb
import atexit



file = __file__ if __file__ is not None else sys.args[0]
file = os.path.abspath(file)

while True:
	if os.path.basename(file) == 'textVkRPG':
		break
	file = os.path.split(file)[0]
sys.path.append(file)

def run_test():
	from .APITest import TestAdd
	from .LocationsTransitions import LocationTransitions

	logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
	pdb.set_trace()
	unittest.main()

run_test()
