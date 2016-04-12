"""
Flights Plugin. Get's various information on Flight Simulator.
By: 997R8V10
"""

import logging
import plugins
import requests
from xml.etree import ElementTree
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

def _initialize(bot):
	plugins.register_user_command(['zulu', 'weather', 'avweather'])

def _api_lookup(type, iaco):
	api_url = "http://avwx.rest/api/metar.php?station{0}&options=info,translate,summary".format(iaco)
	r= requests.get(api_url)
	try:
		root = ElementTree.fromstring(r.content)
		raw = root.findall('METAR/{}/raw_text'.format(type))
	except ElementTree.ParseError as e:
		logger.info("METAR Error: {}".format(e))
		return None
	return raw

def zulu(bot, event, *args):
	data = datetime.now(timezone.utc).strftime("%H%Mz")
	yield from bot.coro_send_message(event.conv_id, "It is currently " + data)

def weather(bot, event, *args):
    """Display the current interpreted weather report for the supplied ICAO airport code.
<b>/bot metar <ICAO airport code></b>
ICAO Airport Codes: https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code
METAR source: http://aviationweather.gov"""
	code = ''.join(args).strip()
	if not code:
		yield from bot.coro_send_message(event.conv_id, "You need to enter the ICAO airport code you wish the look up, https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code .")
		return

	data = _api_lookup('METAR',code)
    
	sendstr = ""

	if data is None:
		yield from bot.coro_send_message(event.conv_id, "There was an error retrieving the METAR information.")
	elif not data or len(data) == 0:
		yield from bot.coro_send_message(event.conv_id, "The response did not contain METAR information, check the ICAO airport code and try again.")
	else:
		sendstr+=data.findall('METAR/Info/Name') + " airport information at " + data.findall('METAR/Time')
		sendstr+=". Wind " + data.findall('METAR/Info/Translations/Wind') + ". Visibility " + data.findall('METAR/Info/Translations/Visibility')
		sendstr+=". " + data.findall('METAR/Info/Translations/Clouds') + ". " + data.findall('METAR/Info/Translations/Other')
		sendstr+=". Temperature " + data.findall('METAR/Info/Translations/Temperature') + ", Dewpoint " + data.findall('METAR/Info/Translations/Dewpoint')
		sendstr+=". Altimeter " + data.findall('METAR/Info/Translations/Altimeter')
		yield from bot.coro_send_message(event.conv_id, sendstr)

def avweather(bot, event, *args):
    """Display the current interpreted weather report for the supplied ICAO airport code.
<b>/bot metar <ICAO airport code></b>
ICAO Airport Codes: https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code
METAR source: http://aviationweather.gov"""
	code = ''.join(args).strip()
	if not code:
		yield from bot.coro_send_message(event.conv_id, "You need to enter the ICAO airport code you wish the look up, https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code .")
		return

	data = _api_lookup('METAR',code)
    
	sendstr = ""

	if data is None:
		yield from bot.coro_send_message(event.conv_id, "There was an error retrieving the METAR information.")
	elif not data or len(data) == 0:
		yield from bot.coro_send_message(event.conv_id, "The response did not contain METAR information, check the ICAO airport code and try again.")
	else:
		sendstr+=data.findall('METAR/Info/Name') + " airport information at " + data.findall('METAR/Time')
		sendstr+=". " + data.findall('METAR/Summary') + ". " + data.findall('METAR/Flight-Rules') + " approaches in use. " + data.findall('METAR/Remarks')
		yield from bot.coro_send_message(event.conv_id, sendstr)