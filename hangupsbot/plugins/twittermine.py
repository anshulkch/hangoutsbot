"""
API for Twitter
"""

import logging
import plugins
import requests
from xml.etree import ElementTree

logger = logging.getLogger(__name__)

def _initialize(bot):
    plugins.register_user_command(['lcps','nuf'])

def _api_lookup(handle, keytext):
    return ""

def lcps(bot, event, *args):
    """Displays closing information for LCPS"""
    """Not currently implemented"""

def nuf(bot, event, *args):
    """Displays information for Nuf's class"""
    """yield from bot.coro_send_message(event.conv_id, "You need to enter the ICAO airport code you wish the look up, https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code .")"""
    
