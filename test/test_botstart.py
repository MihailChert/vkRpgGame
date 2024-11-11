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
		event = FakeEvent(1, 'Начать')
		controller.listen(event)
		query = controller.get_db_session().query(User)
		query = query.all()
		logging.debug(query)

		self.assertTrue(len(query) >= 2)
		for i in query:
			logging.debug(i)
			self.assertTrue(i.Id)

	def test_create_user(self):
		controller = FakeApiController()
		event = FakeEvent(19, 'Начать')
		controller.listen(event)
		event.text = 'Женский'
		controller.listen(event)
		event.text = 'Подтвердить'
		controller.listen(event)
		event.text = 'Анахоэль Де'
		controller.listen(event)
		event.text = 'Изменить'
		controller.listen(event)
		event.text = 'event name'
		controller.listen(event)
		query = controller.get_db_session().query(User).get(event.user_id)
		self.assertEqual('f', query.sex)
		self.assertEqual('event name', query.nicname)
		self.assertEqual('Начать/Имя/Подтверждение/', query.last_command)
		event.text = 'Подтвердить'
		controller.listen(event)
		query = controller.get_db_session().query(User).get(event.user_id)
		self.assertEqual('', query.last_command)
		logging.debug(query)
