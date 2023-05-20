from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID")
APP_ID2 = os.environ.get("APP_ID2")
APP_HASH = os.environ.get("APP_HASH")
APP_HASH2 = os.environ.get("APP_HASH2")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session = os.environ.get("TERMUX")
session2 = os.environ.get("TERMUX2")
SESSION = os.environ.get("TERMUX")
token = os.environ.get("TOKEN")
mitthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
mitthon2 = TelegramClient(StringSession(session2), APP_ID2, APP_HASH2)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()

