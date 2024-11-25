from .abcbotapi import AbstractBotApi
from db_model import User, create_session
import pdb


class BotStart(AbstractBotApi):

	namespace = ''
	view = 'messages_start'

	def may_execute_request(self, request):
		return 'Начать' in request

	def execute(self, event, command):
		command = command.split('/')
		if len(command) == 1:
			self._create_player(event)
			return

		match command[1]:
			case 'Пол': self._sex_defenition(event, command)
			case 'Имя': self._name_definition(event, command)


	def _create_player(self, event):
		new_user = User(Id=event.user_id, location_id=0, last_command='Начать/Пол/')
		session = self.controller.get_db_session()
		session.add(new_user)

		keys = self._keys_for_sex_choise()
		self.controller.current_user = new_user
		viewer = self.controller.get_message_viewer()
		text, keys = viewer.get_message(self.view, event.text, None, user=new_user)
		self.controller.send(text, keys=keys)
		text, keys = viewer.get_message(self.view, 'Начать/Пол/', None, user=new_user)
		self.controller.send(text, keys=keys)
		self.try_commit_session(session)


	def confirmation(self, ansver, next_route, prev_route):
		new_route = None
		user_unsver = None
		if ansver == 'Изменить':
			new_route = prev_route
			user_unsver = 'change'
		elif ansver == 'Подтвердить':
			new_route = next_route 
		else:
			new_route = self.current_user.last_command
			user_unsver = 'error'
		session = self.controller.get_db_session()
		if new_route != self.current_user.last_command:
			self.current_user.last_command = new_route
			session.add(self.current_user)
		viewer = self.controller.get_message_viewer()
		try:
			text, keys = viewer.get_message(self.view, new_route, user_unsver, user=self.current_user)
			self.controller.send(text, keys=keys)
		except NameError as ex:
			if next_route == '':
				self.controller.set_redirection(next_route)
			else:
				raise ex

		self.try_commit_session(session)


	def _sex_defenition(self, event, command_splited):
		session = self.controller.get_db_session()
		if(command_splited[2] == 'Подтверждение'):
			self.confirmation(event.text, 'Начать/Имя/', 'Начать/Пол/')
			return

		sex = 'f' if event.text == 'Женский' else ('m' if event.text == 'Мужской' else 'error')
		if sex == 'error':
			keys = self._keys_for_sex_choise()
			viewer = self.controller.get_message_viewer()
			text, keys = viewer.get_message(self.view, '/'.join(command_splited), 'error', user=self.current_user)
			self.controller.send(text, keys=keys)
			return
		self.current_user.sex = sex
		self.current_user.last_command = 'Начать/Пол/Подтверждение/'
		viewer = self.controller.get_message_viewer()
		text, keys = viewer.get_message(self.view, self.current_user.last_command, None, user=self.current_user)
		self.controller.send(text, keys)
		session.add(self.current_user)
		self.try_commit_session(session)

	def _keys_for_sex_choise(self):
		return None

	def _name_definition(self, event, command_splited):
		session = self.controller.get_db_session()
		if command_splited[2] == 'Подтверждение':
			self.confirmation(event.text, '', 'Начать/Имя/')
			return

		self.current_user.nicname = event.text
		self.current_user.last_command = 'Начать/Имя/Подтверждение/'
		viewer = self.controller.get_message_viewer()
		text, keys = viewer.get_message(self.view, self.current_user.last_command, None, user=self.current_user)
		self.controller.send(text, keys=keys)
		session.add(self.current_user)
		self.try_commit_session(session)

			
