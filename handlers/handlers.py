from random import randint

from aiogram import types, F
from aiogram.utils import markdown
from create_bot import *
from ..misc import get_keyboard



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