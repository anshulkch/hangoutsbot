import logging
import plugins
import requests
from xml.etree import ElementTree

logger = logging.getLogger(__name__)

def _initialize(bot):
    plugins.register_admin_command(['spam'])
    
def spam(bot, event, *args):
    if args is None:
    	yield from bot.coro_send_message(event.conv_id, "You need to enter the amount of times to spam and the spam text: eg: fs spam 100 SPAM")
    	return
    amt = args[0]
    code = ' '.join(args[1:]).strip()
    if not code:
    	yield from bot.coro_send_message(event.conv_id, "You need to enter the amount of times to spam and the spam text: eg: fs spam 100 SPAM")
    	return
    for x in range(0, int(amt)):
    	yield from bot.coro_send_message(event.conv_id, code)