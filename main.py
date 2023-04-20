#!/usr/bin/env python3

import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

Bot = Client("TestWebApp", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

web_app = WebAppInfo(url="https://alexandr0856.github.io/")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Site", web_app=web_app)]
    ],
    resize_keyboard=True
)


@Bot.on_message(filters.command("start"))
def qr_analyzer(client, message):
    Bot.send_message(message.chat.id, 'Analyze QR code', reply_markup=keyboard)


if __name__ == '__main__':
    Bot.run()
