import unittest
import sys
import logging
from fakecontroller import FakeApiController
from fakeevent import FakeEvent
from api.abcbotapi import AbstractBotApi
import pdb

class StartRedirectPoint(AbstractBotApi):
	command = 'тест перенаправления'

	@classmethod
	def execute(cls, event):
		logging.debug('start redirect')
		cls.controller.set_redirection('перенапревление')

class EndRedirectPoint(AbstractBotApi):
	command = 'перенапревление'
	_ex = False

	@classmethod
	def execute(cls, event):
		logging.debug('redirect success')
		cls._ex = True
		return

class TestRedirectController(unittest.TestCase):
	def test_redirect(self):
		event = FakeEvent(0, 'тест перенаправления')
		controller = StartRedirectPoint.controller
		controller.listen(event)
		self.assertTrue(EndRedirectPoint._ex)