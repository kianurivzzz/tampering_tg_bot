from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from google_sheets.insert_data import add_error
from database.update_teachers import update_teachers

router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer('Опять работа?')


@router.message(Command('update_teachers'))
async def update_db_handler(msg: Message):
    await msg.answer('Запускаю обновление преподавателей')
    update_teachers()
    await msg.answer('Обновил преподавателей')


@router.message(Command('help'))
async def help_handler(msg: Message):
    await msg.answer('Список команд бота для менеджеров и тимлидеров:\n/chat_id – узнать айди чата\n/test_insert – тестовая запись в таблицу фиксации\n/delay – фиксация опоздания, проставлять если преподаватель вышел через 5-15 минут после начала урока\n/replacement – фиксация замены\n/skipping – фиксация невыхода на урок, проставлять после 15 минут ожидания')


@router.message(Command('chat_id'))
async def chat_id_handler(msg: Message):
    await msg.answer(f'Chat ID: <code>{msg.chat.id}</code>')


@router.message(Command('test_insert'))
async def test_handler(msg: Message):
    add_error('тест', msg.chat.id)
    await msg.answer('<b>Тест</b> зафиксирован и добавлен в таблицу.')


@router.message(Command('delay'))
async def delay_handler(msg: Message):
    add_error('опоздание', msg.chat.id)
    await msg.answer('<b>Опоздание</b> добавлено в таблицу.')


@router.message(Command('replacement'))
async def replacement_handler(msg: Message):
    add_error('замена', msg.chat.id)
    await msg.answer('<b>Замена</b> добавлена в таблицу.')


@router.message(Command('skipping'))
async def skipping_handler(msg: Message):
    add_error('невыход', msg.chat.id)
    await msg.answer('<b>Невыход</b> добавлен в таблицу.')
