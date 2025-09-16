# bot.py
from aiogram import Bot, Dispatcher, types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(lambda message: message.text and message.text.lower() == "hi")
async def say_hello(message: types.Message):
    await message.reply("Hello World!")
