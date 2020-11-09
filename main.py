from pyrogram import Client
import logging

# logging.basicConfig(format='%(levelname)s in %(funcName)s: %(message)s')
logging.basicConfig(
    format="[%(levelname)s %(asctime)s] In module %(module)s, function %(funcName)s at line %(lineno)d -> %(message)s"
)

bot = Client("FakeNameGenerator", config_file="config.ini")

bot.run()
