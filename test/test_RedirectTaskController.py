import unittest
import sys
import logging
from fakecontroller import FakeApiController
from fakeevent import FakeEvent
from api.abcbotapi import AbstractBotApi
import pdb

class StartRedirectPoint(AbstractBotApi):
	namespace = ''

	def may_execute_request(self, request):
		return request == 'тест перенаправления'
	
	def execute(self, event, command):
		logging.debug('start redirect')

		self.controller.set_redirection('перенапревление')

class EndRedirectPoint(AbstractBotApi):
	namespace = ''
	_ex = False

	def may_execute_request(self, request):
		return request == 'перенапревление'

	
	def execute(self, event, command):
		logging.debug('redirect success')
		self.__class__._ex = True
		return

class TestRedirectController(unittest.TestCase):

	def test_redirect(self):
		event = FakeEvent(0, 'тест перенаправления')
		controller = StartRedirectPoint.controller
		controller.listen(event)
		self.assertTrue(EndRedirectPoint._ex)

	@classmethod
	def tearDownClass(self):
		controller = StartRedirectPoint.controller
		listeners = getattr(controller, f'_{type(controller).__name__}__listeners')['']
		listeners.remove(StartRedirectPoint)
		listeners.remove(EndRedirectPoint)