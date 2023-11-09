from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from data import *
from config import settings


dp = Dispatcher()
global_init('db/bot.db')
session = create_session()

bot = Bot(
    token=settings.bot_token,
    parse_mode=ParseMode.MARKDOWN_V2
    )

user_data = {}