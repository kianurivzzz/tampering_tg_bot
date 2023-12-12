from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from google_sheets.insert_data import add_error

router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer('Опять работа?')


@router.message(Command('help'))
async def start_handler(msg: Message):
    await msg.answer('Список команд бота для менеджеров и тимлидеров:\n/chat_id – узнать айди чата\n/test_insert – тестовая запись в таблицу фиксации\n/delay – фиксация опоздания, проставлять если преподаватель вышел через 5-15 минут после начала урока\n/replacement – фиксация замены\n/skipping – фиксация невыхода на урок, проставлять после 15 минут ожидания')


@router.message(Command('chat_id'))
async def start_handler(msg: Message):
    await msg.answer(f'Chat ID: <code>{msg.chat.id}</code>')


@router.message(Command('test_insert'))
async def start_handler(msg: Message):
    add_error('тест', msg.chat.id)
    await msg.answer('<b>Тест</b> зафиксирован и добавлен в таблицу.')


@router.message(Command('delay'))
async def start_handler(msg: Message):
    add_error('опоздание', msg.chat.id)
    await msg.answer('<b>Опоздание</b> добавлено в таблицу.')


@router.message(Command('replacement'))
async def start_handler(msg: Message):
    add_error('замена', msg.chat.id)
    await msg.answer('<b>Замена</b> добавлена в таблицу.')


@router.message(Command('skipping'))
async def start_handler(msg: Message):
    add_error('невыход', msg.chat.id)
    await msg.answer('<b>Невыход</b> добавлен в таблицу.')

# @router.message()
# async def message_handler(msg: Message):
#     print(dict(msg))
#     await msg.answer(f'Инфо: {msg}')


# @router.message(F.new_chat_members)
# async def send_welcome(msg: types.Message):
#     bot_id = '6897378472'

#     for chat_member in msg.new_chat_members:
#         if chat_member.id == bot_id:
#             await msg.answer(f'Chat ID: {msg.chat.id}')
