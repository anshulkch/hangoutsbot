"""
Google search integration.
By: anshulkch & 997R8V10
"""

import logging
import plugins
import requests
import urllib
import json
from xml.etree import ElementTree

logger = logging.getLogger(__name__)

def _initialize(bot):
    plugins.register_user_command(['google'])

def _api_lookup(bot, type, code, num):
	apitype = ""
	if type=="i":
		apitype="&searchType=image"
	query = urllib.parse.urlencode({'q': code})
	youtube_api_key = bot.config.get_by_path(["spotify", "youtube"])
	sei = bot.config.get_by_path(["google", "search_engine_id"])
	url = 'https://www.googleapis.com/customsearch/v1?' + query + '&num=' + num + '&filter=1' + apitype + '&key=' + youtube_api_key + '&cx=' + sei
	logger.error(url)
	search_response = urllib.request.urlopen(url)
	search_results = search_response.read().decode("utf8")
	results = json.loads(search_results)
	return results

def google(bot, event, *args):
    if not args:
    	yield from bot.coro_send_message(event.conv_id, "You must pass in a search type: eg: ap google s <QUERY>.. s for web search, i for image search")
    	return
    command = args[0]
    if not command:
    	yield from bot.coro_send_message(event.conv_id, "You must pass in a search type: eg: ap google s <QUERY>.. s for web search, i for image search and the amount of results")
    	return
    num = args[1]
    if not num:
    	num = 1
    code = ' '.join(args[2:]).strip()
    if not code:
        yield from bot.coro_send_message(event.conv_id, "You need to enter the item to look for.")
        return
    
    results = _api_lookup(bot, command, code, num)
    data = results
    yield from bot.coro_send_message(event.conv_id, 'Total results: %s' % data['searchInformation']['totalResults'])
    hits = data['items']
    yield from bot.coro_send_message(event.conv_id, 'Top %d hits:' % len(hits))
    for h in hits:
    	yield from bot.coro_send_message(event.conv_id, "<b>" + h['title'] + "</b> | " + h['link'] + "<br />" + h['snippet'] + "<br/>")
    	
    return hits
