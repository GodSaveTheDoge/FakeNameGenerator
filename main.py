import sys

if sys.version_info.major != 3:
    raise Exception("Python 2 is not supported! Please use Python 3 instead")

from pyrogram import Client
import logging

# logging.basicConfig(format='%(levelname)s in %(funcName)s: %(message)s')
logging.basicConfig(
    format="[%(levelname)s %(asctime)s] In module %(module)s, function %(funcName)s at line %(lineno)d -> %(message)s")

if sys.version_info.minor < 7:
    logging.warning("You should use python 3.7 or higher")

bot = Client(
    "FakeNameGenerator",
    config_file="config.ini"
)

bot.run()
