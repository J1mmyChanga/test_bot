from aiogram import types


def get_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text='-1', callback_data='num_decr'),
         types.InlineKeyboardButton(text='+1',callback_data='num_incr')],
        [types.InlineKeyboardButton(text='Подтвердить',callback_data='num_finish')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard