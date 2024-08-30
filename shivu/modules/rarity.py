from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from itertools import groupby
import math
from html import escape 
import random

from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler

from shivu import collection, user_collection, application

RARITY_MAP = {
    "1": "🔵 Common",
    "2": "🟣 Rare",
    "3": "🍄 Special",
    "4": "🔮 Premium",
    "5": "⚗ Limited",
}

selected_rarity = None

async def rarity(update: Update, context: CallbackContext) -> None:
    global selected_rarity
    query = update.callback_query
    data = query.data

    _, rarity_key = data.split(':')
    selected_rarity = RARITY_MAP[rarity_key]

    await update.message.reply_text(f'Rarity dipilih: {selected_rarity}')

async def harem(update: Update, context: CallbackContext, page=0) -> None:
    global selected_rarity
    # ... (isi fungsi harem Anda di sini, dengan modifikasi untuk memeriksa selected_rarity)

RARITY_HANDLER = CommandHandler('rarity', rarity, block=False)
application.add_handler(RARITY_HANDLER)
