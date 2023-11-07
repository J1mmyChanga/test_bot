import asyncio
import logging
import sys
from contextlib import suppress
from random import randint

from aiogram import Bot, Dispatcher, types, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.enums import ParseMode
# from message_handlers import *
# from command_handlers import *

from config import settings

dp = Dispatcher()
user_data = {}


def get_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text='-1', callback_data='num_decr'),
         types.InlineKeyboardButton(text='+1',callback_data='num_incr')],
        [types.InlineKeyboardButton(text='Подтвердить',callback_data='num_finish')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@dp.message(CommandStart())
async def handle_command_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Кнопочка 1')],
        [types.KeyboardButton(text='Кнопочка 2')],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Выберите кнопку',
    )
    await message.answer(
        text=f'Вывожу какой от текст',
        reply_markup=keyboard,
    )


# @dp.message(CommandStart())
# async def handle_start(message: types.Message):
#     url = 'https://www.youtube.com/watch?v=x4vUsiZPi3w&list=RDZdpe65SBHUs&index=14'
#     await message.answer(
#         text=f'{markdown.hide_link(url)}Hello {markdown.hbold(message.from_user.full_name)}',
#         parse_mode=ParseMode.HTML,
#     )


@dp.message(Command('help'))
async def handle_command_help(message: types.Message):
    text = 'Я простой помощник\\-хелпер\\.\nЛомай *меня* полностью\\!'
    # entity_bold = types.MessageEntity(
    #     type='italic',
    #     offset=len('Я простой помощник-хелпер\nЛомай '),
    #     length=4,
    # )
    # entities = [entity_bold]
    # await message.answer(
    #     text=text,
    #     entities=entities,
    # )
    text = markdown.text(
        markdown.markdown_decoration.quote('Я простой помощник-хелпер.'),
        markdown.text(
            'Ломай',
            markdown.markdown_decoration.bold(
                markdown.text(
                    'меня',
                    markdown.underline('жестко,'),
                    markdown.strikethrough('жестко,'),
                    markdown.link('жестко и', 'https://www.youtube.com/watch?v=rrmsJhf89MY&list=RDZdpe65SBHUs&index=3'),
                    markdown.code('очень жестко!!!')
                )
            ),
            'полностью\\!'
        ),
        markdown.markdown_decoration.quote('Внимай, ссука!!!'),
        sep='\n'
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
    )


@dp.message(Command('code'))
async def handle_command_code(message: types.Message):
    text = markdown.text(
        'Пайтон БЛЯТЬ',
        '',
        markdown.markdown_decoration.pre_language(
            markdown.text(
                'print("Hello world!")',
                '\n',
                'def foo():',
                '   return "bar"',
                sep='\n'
            ),
            language='python'
        ),
        'и немножко жаваскрипта',
        '',
        markdown.markdown_decoration.pre_language(
            markdown.text(
                'console.log("Hello world!")',
                '\n',
                'function foo() {\n    return"bar"\n}',
                sep='\n'
            ),
            language='javascript'
        ),
        sep='\n'
    )
    await message.answer(text=text)


@dp.message(Command('but_builder'))
async def handle_command_but_buider(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 9):
        builder.add(types.KeyboardButton(text=f'Кнопка {i}'))
    builder.adjust(3)
    await message.answer(
        text='Выберите число:',
        reply_markup=builder.as_markup(resize_keyboard=True),
        input_field_placeholder='Выберите число',
    )


@dp.message(Command('special_buttons'))
async def handle_command_special_buttons(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Запросить геолокацию', request_location=True),
        types.KeyboardButton(text='Запросить контакт', request_contact=True),
    )
    builder.row(
        types.KeyboardButton(
            text='Выбрать премиум пользователя',
            request_user=types.KeyboardButtonRequestUser(
                request_id=1,
                user_is_premium=True
            ),
        ),
        types.KeyboardButton(
            text='Выбрать только канал',
            request_chat=types.KeyboardButtonRequestChat(
                request_id=2,
                chat_is_channel=True,
                chat_is_forum=False
            ),
        )
    )
    builder.row(
        types.KeyboardButton(
            text='Создать опрос',
            request_poll=types.KeyboardButtonPollType(),
        ),
    )
    await message.answer(
        text='Че хотите сделать?',
        reply_markup=builder.as_markup(resize_keyboard=True),
        input_field_placeholder='Че хотите сделать?',
    )


@dp.message(Command('inline_url'))
async def handle_command_inline_url(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text='Github',
            url='https://github.com/'
        )
    )
    builder.row(
        types.InlineKeyboardButton(
            text='Авито',
            url='https://www.avito.ru/'
        )
    )
    user_id = message.from_user.id
    chat_info = await message.bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(
            types.InlineKeyboardButton(
                text=f'User {user_id}',
                url=f'tg://user?id={user_id}'
            )
        )
    await message.answer(
        text='Выбери кнопочку',
        reply_markup=builder.as_markup(),
    )


@dp.message(Command('callback_but'))
async def handle_command_callback_but(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text='Получи данные',
            callback_data='value1'
        )
    )
    await message.answer(
        text='Жма на кнопку штоб число от 1 до 10 гетнуть',
        reply_markup=builder.as_markup(),
    )


@dp.message(Command("numbers"))
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard())


@dp.callback_query(F.data.startswith('num_'))
async def callbacks_num(callback: types.CallbackQuery):
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split('_')[-1]
    if action == 'incr':
        user_data[callback.from_user.id] = user_value + 1
        await update_num_text(callback.message, user_value + 1)
    elif action == 'decr':
        user_data[callback.message.from_user.id] = user_value - 1
        await update_num_text(callback.message, user_value - 1)
    else:
        await callback.message.edit_text(f'Итого: {user_value}')


@dp.callback_query(F.data == 'value1')
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(
        text=f'Вот твое число ебать {randint(1, 808)}'
    )
    # await callback.answer(
    #     text='Спасибо что воспользовались ботом',
    #     show_alert=True,
    #
    # )


async def update_num_text(message: types.Message, new_value: int):
    # with suppress(TelegramBadRequest):
        await message.edit_text(
            f'Укажите число: {new_value}',
            reply_markup=get_keyboard(),
            parse_mode=None
        )


@dp.message(F.text.lower().startswith('кноп'))
async def if_but2(message: types.Message):
    await message.reply('пока кнопочка', reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.chat_shared)
async def chat_is_shared(message: types.Message):
    await message.answer(
        text=markdown.text(
            f'Request ID: {message.chat_shared.request_id}',
            f'Chat ID: {message.chat_shared.chat_id}',
            sep='\n'
        ),
        parse_mode=None,
    )


@dp.message(F.user_shared)
async def user_is_shared(message: types.Message):
    await message.answer(
        text=markdown.text(
            f'Request ID: {message.user_shared.request_id}',
            f'User ID: {message.user_shared.user_id}',
            sep='\n'
        ),
        parse_mode=None,
    )


@dp.message()
async def echo_message(message: types.Message):
    await message.bot.send_message(
        chat_id=message.chat.id,
        text='Wait a second...',
        parse_mode=None
    )
    if message.text:
        await message.answer(
            text=message.text,
            entities=message.entities,
            parse_mode=None
        )
        return
    # await message.bot.send_message(
    #     chat_id=message.chat.id,
    #     text='Detected message...',
    #     reply_to_message_id=message.message_id
    # )
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Something new :)', parse_mode=None)
    # if message.text:
    #     await message.reply(text=message.text)
    # elif message.sticker:
    #     await message.reply_sticker(sticker=message.sticker.file_id)
    #     await message.bot.send_sticker(
    #         chat_id=message.chat.id,
    #         sticker=message.sticker.file_id,
    #         reply_to_message_id=message.message_id,
    #     )
    # elif message.photo:
    #     await message.reply_photo(photo=message.photo[-1].file_id)
    #     await message.bot.send_photo(
    #         chat_id=message.chat.id,
    #         photo=message.photo[-1].file_id,
    #         reply_to_message_id=message.message_id,
    #     )
    # else:
    #     await message.reply(text='hahhahah')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    bot = Bot(
        token=settings.bot_token,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())