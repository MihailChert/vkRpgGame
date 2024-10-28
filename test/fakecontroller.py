from db_model import User, create_session
from api.abcbotapi import BotApiMeta


class FakeApiController:

	__instance = None

	def __new__(cls, *args, **kwargs):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
			cls.__instance.current_user = None
			cls.__instance.__listeners = {}
			cls.__instance._bot = None
			cls.__instance.resposns = {}
			cls.__instance._db_session = None
			cls.__instance.__redirect = None
		return cls.__instance

	def add_listener(self, command, handler):
		self.__listeners[command] = handler

	def set_bot_sesion(self, bot_session):
		self._bot = bot_session

	def get_db_session(self):
		return self._db_session

	def set_redirection(self, new_direct):
		self.__redirect = new_direct

	def listen(self, event):
		self._db_session = create_session()
		self.current_user = self._db_session.query(User).get(event.user_id)
		command = ''
		if self.current_user is None:
			self.current_user = event.user_id
			command = event.text
		else:
			command = self.current_user.last_command + event.text
		self.__listeners[command].execute(event)
		while self.__redirect is not None:
			command = self.__redirect
			self.__redirect = None
			self.__listeners[command].execute(event)


		self._db_session.close()

	def send(message, keys=None):
		self.resposns = {
		'user_id': self.current_user.Id,
		'message': message,
		'keys': keys
		}


BotApiMeta.__bot_command_controller__ = FakeApiController()
