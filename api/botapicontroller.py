import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from db_model import User, create_session

class BotApiController:

	__instance = None

	def __new__(cls, *args, **kwargs):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
			cls.__instance.__listeners = {}
			cls.__instance.current_user = None
			cls.__instance._bot = None
		return cls.__instance

	def add_listener(self, command, handler):
		self.__listeners[command] = handler

	def set_session(self, bot_session):
		self._bot = bot_session

	def listen(self, event):
		session = create_session()
		self.current_user = session.query(User).get(event.user_id)
		print(self.current_user)
		session.close()
		if self.current_user is None:
			self.current_user = event.user_id
		self.__listeners[event.text].execute(event)

	def send(message, keys=None):
		self._bot.message.send(user_id=self.current_user, message=message, keyboard=keys, random_id=vk_api.utils.get_random_id())
