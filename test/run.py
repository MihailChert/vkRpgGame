import logging
import os
import sys
import unittest
import pdb


os.environ['db_config_path'] = 'sqlite:///:memory:'

test_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
api_dir = os.path.split(test_dir)[0]
sys.path.append(api_dir)

discover = unittest.defaultTestLoader.discover(test_dir, 'test_*.py')
testRunner = unittest.runner.TextTestRunner()

logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)


if __name__ == '__main__':
	testRunner.run(discover)