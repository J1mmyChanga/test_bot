import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode

from config import settings
from create_bot import *


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    bot = Bot(
        token=settings.bot_token,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())