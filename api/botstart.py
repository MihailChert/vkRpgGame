from .abcbotapi import AbstractBotApi
from db_model import User, create_session


class BotStart(AbstractBotApi):

	command = 'Начать'

	@classmethod
	def execute(cls, event):
		new_user = User(Id=event.user_id, location_id=0)
		session = cls.controller.get_db_session()
		session.add(new_user)
		session.commit()
		session.close()
			
