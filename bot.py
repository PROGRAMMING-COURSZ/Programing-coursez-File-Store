import os
import logging
import logging.config
from pyrogram.errors import BadMsgNotification
# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import time
time.time()  # forces Python to sync system time
from pyromod import listen
from pyrogram import Client
from config import *

def main():
    plugins = dict(root="plugins")
    app = Client("FileStore",
                 bot_token=BOT_TOKEN,
                 api_id=API_ID,
                 api_hash=API_HASH,
                 plugins=plugins,
                 workers=100)

    while True:
    try:
        app.run()
        break
    except BadMsgNotification:
        print("Time sync issue, retrying in 10 seconds...")
        time.sleep(10)


if __name__ == "__main__":
    main()
