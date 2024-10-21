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
		return cls.__instance

	def add_listener(self, command, handler):
		if isinstance(self.__listeners.get(command), list):
			self.__listeners[command].append(handler)
		else:
			self.__listeners[command] = [handler]

	def set_bot_sesion(self, bot_session):
		self._bot = bot_session

	def get_db_session(self):
		return self._db_session

	def listen(self, event):
		self._db_session = create_session()
		self.current_user = self._db_session.query(User).get(event.user_id)
		command = ''
		if self.current_user is None:
			self.current_user = event.user_id
			command = event.text
		else:
			command = self.current_user.last_command + event.text
		for handler in self.__listeners[command]:
			manager = handler(command, self.current_user)
			if manager.is_executable():
				manager.execute(event, command)
				break
		self._db_session.commit()
		self._db_session.close()

	def send(message, keys=None):
		self.resposns = {
		'user_id': self.current_user.Id,
		'message': message,
		'keys': keys
		}


BotApiMeta.__bot_command_controller__ = FakeApiController()
