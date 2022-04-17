import os

from .commands import encode_string
from pyrogram import Client, filters
from config import *

@Client.on_message(filter.command(['link', 'store']) & ~filters.edited)
async def storefile(bot, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply('hmm')
    file_type = replied.media
    if file_type not in ["photo", "video", 'audio', 'document']:
        return await message.reply('Hm')
    bot = await c.get_me()
    base64_string = await encode_string(f"{m.chat.id}_{msg.message_id}")
    url = f"https://t.me/{bot.username}?start={base64_string}"
    await message.reply(f"Here is Link : {url}")
