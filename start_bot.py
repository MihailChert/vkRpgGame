from secret_env import *
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from api import BotApiController

bot = VkApi(token=vk_bot_tocken)


listener = VkLongPoll(bot)
bot_controller = BotApiController()
bot_controller.set_session(bot.get_api())
for event in listener.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			bot_controlelr.listen(event)