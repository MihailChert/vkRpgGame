import unittest
import sys
import logging
from fakecontroller import FakeApiController
from fakeevent import FakeEvent
from api.botstart import BotStart
from db_model import User
import logging
import pdb

class TestStart(unittest.TestCase):

	def test_controller(self):
		self.assertTrue(isinstance(BotStart.controller, FakeApiController))

	def test_start(self):
		controller = FakeApiController()
		event = FakeEvent(1, BotStart.command)
		controller.listen(event)
		query = controller.get_db_session().query(User)
		query = query.all()
		self.assertTrue(len(query) >= 2)
		for i in query:
			logging.debug(i)
			self.assertTrue(i.Id)


