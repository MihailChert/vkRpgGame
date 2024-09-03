import secret_env
import os
import vk_api
# import vk_api.utils
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from api import BotApiController

bot = vk_api.VkApi(token=os.environ['vk_bot_tocken'])

listener = VkLongPoll(bot)
bot_controller = BotApiController()
bot_controller.set_session(bot.get_api())

for event in listener.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			bot_controller.listen(event)