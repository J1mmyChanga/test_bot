from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.enums import ParseMode
from create_dispatcher import *
from misc import get_keyboard


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