import xml.dom.minidom
import sys
from pathlib import Path
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class RenderMessage:

	FILE_PATH = sys.path.copy()

	def __init__(self, add_new_os_path=None):
		self.view = None
		self.path = None
		self.ansver = None
		self.os_path = self.FILE_PATH
		if add_new_os_path is not None:
			self.add_path(add_new_os_path)

	def _validate_path(self, path, ansver):
		if ansver is None:
			return path
		if ansver in path:
			path = path[:-len(ansver)]
		return path

	def add_path(self, new_path):
		self.os_path.append(new_path)

	@classmethod
	def add_path(cls, new_path):
		cls.FILE_PATH.append(new_path)

	def _find_path(self):
		for path in self.os_path:
			path = Path(path) / Path('bot_view') / Path(self.view+'.xml')
			if path.is_file():
				return path
		raise ValueError(f'The {self.view}.xml is not file or not exist in paths.')

	@staticmethod
	def _find_element_by_name_and_attr(dom, element_name, element_attr_name, element_attr_value):
		elems = dom.getElementsByTagName(element_name)
		for elem in elems:
			if elem.attributes.get(element_attr_name) is not None and elem.attributes.get(element_attr_name).value == element_attr_value:
				return elem
		raise NameError(f'Can\'t find element with name: {element_name} and attribute name: {element_attr_name} with value: {element_attr_value}.')

	def get_text(self, kwargs):
		path = self._find_path()
		doc = None
		with open(path) as f:
			doc = xml.dom.minidom.parse(f)
		doc = self._find_element_by_name_and_attr(doc, 'message', 'path', self.path)
		if self.ansver is None:
			formated_text = doc.getElementsByTagName('text')[0].firstChild.data
			formated_data = doc.getElementsByTagName('formates')
		else:
			formated_text = self._find_element_by_name_and_attr(doc, 'text', 'ansver', self.ansver).firstChild.data
			formated_data = self._find_element_by_name_and_attr(doc, 'formates', 'ansver', self.ansver)
		formated_text = formated_text.replace('\t', '')
		formated_data = self._process_format_data(doc, kwargs)
		return formated_text.format(**formated_data)

	def _process_format_data(self, formated_data_elem, parameters_execution):
		formated_data = {}
		for elem in formated_data_elem.getElementsByTagName('parameter'):
			if not elem.attributes.get('name') and not elem.attributes['replace']:
				raise ValueError('Parameter tag mast have attributes name and replace.')
			formated_data[elem.attributes.get('name').value] = elem.attributes.get('replace').value
		for replace_parameter_name in formated_data:
			replace_parameter = formated_data[replace_parameter_name]
			replace_parameter = replace_parameter.split(';')[0]
			if not parameters_execution.get(replace_parameter.split('.')[0]):
				raise NameError('Can\'t find attribute')
			replace_parameter = replace_parameter.split('.')
			value = eval(f'parameters_execution[replace_parameter[0]].{'.'.join(replace_parameter[1:])}')
			formated_data[replace_parameter_name] = value
		return formated_data
	
	def get_keys(self):
		path = self._find_path()
		doc = None
		with open(path) as f:
			doc = xml.dom.minidom.parse(f)
		doc = self._find_element_by_name_and_attr(doc, 'message', 'path', self.path)
		if self.ansver is None:
			buttons_elem = doc.getElementsByTagName('buttons')
			if(isinstance(buttons_elem, list) and len(buttons_elem)):
				buttons_elem = buttons_elem[0]
		else:
			try:
				buttons_elem = self._find_element_by_name_and_attr(doc, 'buttons', 'ansver', self.ansver)
			except:
				return VkKeyboard.get_empty_keyboard()
		if not buttons_elem:
			return VkKeyboard.get_empty_keyboard()
		keys = VkKeyboard(one_time=(buttons_elem.getAttribute('one_time') == 'True'), inline=(buttons_elem.getAttribute('inline') == 'True'))
		for button in buttons_elem.getElementsByTagName('button'):
			key_color = button.attributes.get('color', 'secondary').value
			keys.add_button(button.firstChild.data, getattr(VkKeyboardColor, key_color.upper()))
		return keys.get_keyboard()

	def get_message(self, view, command, ansver, **kwargs):
		self.view = view
		self.path = self._validate_path(command, ansver)
		self.ansver = ansver
		return self.get_text(kwargs), self.get_keys()

