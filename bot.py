from aiogram import Bot, Dispatcher, types
import os
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def say_hello(message: types.Message):
    if message.text and message.text.lower() == "hi":
        await message.reply("Hello World!")
