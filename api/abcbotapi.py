from .botapicontroller import BotApiController
from abc import abstractmethod
from sqlalchemy.exc import SQLAlchemyError

class BotApiMeta(type):

	__bot_command_controller__ = BotApiController()

	def __init__(self, name, bases, attrs):
		try:
			if isinstance(attrs.get('namespace', False), str):
				BotApiMeta.__bot_command_controller__.add_listener(attrs['namespace'], self)
				self.controller = BotApiMeta.__bot_command_controller__
		except KeyError:
			pass
		super().__init__(name, bases, attrs)



class AbstractBotApi(metaclass=BotApiMeta):

	def __init__(self, user, request):
		self.current_user = user
		self.keys = None
		self.message = ''
		self._can_execute = self.may_execute_request(request)

	@abstractmethod
	def may_execute_request(self, request):
		pass

	def __getattribute__(self, item):
		item_obj = super().__getattribute__(item)
		if hasattr(item_obj, '__isabstractmethod__') and item_obj.__isabstractmethod__:
			raise TypeError(f'Can\'t instantiate abstract class {type(self)} without an implementation for abstract method \'{item}\'')
		if 'execute' == item and (not self._can_execute or self._can_execute is None):
			raise RuntimeError('Can\'t execute request. Move to next request manager.')
		return item_obj

	def is_executable(self):
		return self._can_execute

	@abstractmethod
	def execute(self, event, command):
		pass

	def try_commit_session(self, session):
		try:
			session.commit()
			return True
		except SQLAlchemyError as ex:
			session.rollback()  # TODO: add login for the alchemy error
			raise ex
			return False
