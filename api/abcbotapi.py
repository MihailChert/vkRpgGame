from .botapicontroller import BotApiController
from abc import abstractmethod

class BotApiMeta(type):

	__bot_command_controller__ = BotApiController()

	def __init__(self, name, bases, attrs):
		try:
			if (not hasattr(attrs['execute'], '__isabstractmethod__') or not attrs['execute'].__isabstractmethod__) and attrs.get('command') is not None:
				BotApiMeta.__bot_command_controller__.add_listener(attrs['command'], self)
				self.controller = self
		except KeyError:
			pass
		super().__init__(name, bases, attrs)


class AbstractBotApi(metaclass=BotApiMeta):

	def __init__(self):
		self.current_user = None
		self.keys = None
		self.message = ''

	@classmethod
	@abstractmethod
	def execute(cls, event):
		pass

	def send(self):
		self.controller.send_message(self.message, self.keys)
