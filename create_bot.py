from aiogram import Bot
from aiogram import Dispatcher
from config import *
import logging


bot_token = os.getenv('AutoBookingPlacesBot')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher()
