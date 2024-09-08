class FakeEvent:

	def __init__(self, user_id, text):
		self.user_id = user_id
		self.text = text

	@classmethod
	def bot_start(self, user_id, text):
		e = cls(user_id, text)
		return e