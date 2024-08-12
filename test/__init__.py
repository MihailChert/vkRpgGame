from os import path
import sys
import unittest

file = __file__ if __file__ is not None else sys.args[0]
file = path.abspath(file)
while True:
	if path.basename(file) == 'textVkRPG':
		break
	file = path.split(file)[0]
sys.path.append(file)

def run_test():
	from .APITest import TestAdd

	unittest.main()
