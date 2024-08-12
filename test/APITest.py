import unittest
from io import StringIO
import sys
import unittest.mock
from api import BotApiController, BotCommandStart


class event:
	text = 'start'
	user_id = '1'

class TestAdd(unittest.TestCase):

	def test_meta_rest(self):
		bt = BotApiController()._BotApiController__listeners
		self.assertTrue(isinstance(bt.get('start', False), type(BotCommandStart)))

	@unittest.mock.patch('sys.stdout', new_callable=StringIO)
	def assertStdout(self, expected_output, mock_stdout):
		BotApiController().listen(event)
		self.assertEqual(mock_stdout.getvalue(), expected_output)

	def test_bot(self):
		self.assertStdout('listener\n')

if __name__ == '__main__':
	unittest.main()
