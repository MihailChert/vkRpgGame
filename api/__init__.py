import sys
import os
from os import path
import pdb

file = __file__ if __file__ is not None else sys.args[0]
file = path.abspath(file)
while True:
	if path.isdir(path.join(file, 'api')) and path.isfile(path.join(file, 'api', '__init__.py')):
		break
	file = path.split(file)[0]
if file not in sys.path:
	sys.path.append(file)

if not bool(os.environ.get('API_DEBUG', False)):
	from .botapicontroller import BotApiController
	from .abcbotapi import AbstractBotApi
	from .botstart import BotStart
