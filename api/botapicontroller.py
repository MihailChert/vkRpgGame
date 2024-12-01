import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from .render_message import RenderMessage
from db_model import User, create_session

class BotApiController:

	__instance = None

	def __new__(cls, *args, **kwargs):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
			cls.__instance.__listeners = {}
			cls.__instance.current_user = None
			cls.__instance._bot = None
			cls.__instance._db_session = None
			cls.__instance.__redirect = None
			cls.__instance.message_viewer = RenderMessage()
		return cls.__instance

	def add_listener(self, command, handler):
		if isinstance(self.__listeners.get(command), list):
			self.__listeners[command].append(handler)
		else:
			self.__listeners[command] = [handler]

	def get_message_viewer(self):
		return self.message_viewer

	def set_session(self, bot_session):
		self._bot = bot_session

	def get_db_session(self):
		return self._db_session

	def set_redirection(self, new_direct):
		self.__redirect = new_direct

	def listen(self, event):
		self._db_session = session = create_session()
		self.current_user = self._db_session.query(User).get(event.user_id)
		command = ''
		if self.current_user is None:
			command = event.text
		else:
			command = self.current_user.last_command + event.text

		self._execute_command(event, command)
		while self.__redirect is not None:
			command = self.__redirect
			self.__redirect = None
			self._execute_command(event, command)
		self._db_session.close()

	def _execute_command(self, event, command):
		namespace = command.split('/')[0]

		for handler in self.__listeners.get(namespace, self.__listeners['']):
			manager = handler(self.current_user, command)
			if manager.is_executable():
				manager.execute(event, command)
				break

	def send(self, message, keys=None):
		self._bot.messages.send(user_id=self.current_user.Id, message=message, keyboard=keys, random_id=vk_api.utils.get_random_id())
