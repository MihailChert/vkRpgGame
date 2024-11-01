from .abcbotapi import AbstractBotApi
from db_model import User, create_session


class BotStart(AbstractBotApi):

	namespace = ''

	def may_execute_request(self, request):
		return True

	def execute(cls, event, command):
		new_user = User(Id=event.user_id, location_id=0)
		session = cls.controller.get_db_session()
		session.add(new_user)
		session.commit()
			
