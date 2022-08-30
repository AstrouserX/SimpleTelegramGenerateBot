import logging
import aiogram

def bot_conf():
  API_TOKEN = '<YOUR_BOT_API_TOKEN>'
  logging.basicConfig(level=logging.INFO)
  bot = aiogram.Bot(token=API_TOKEN)
  dp = aiogram.Dispatcher(bot)
  
  return bot, dp