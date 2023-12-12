import datetime

import google_sheets.gsheets as gs
import database.db_querys as db
from config import TAMP_SHEET

def add_error(type, chat_id):
    query = db.execute_script('SELECT * FROM teachers WHERE chat_id = ?', (chat_id, ))
    teacher, crm_id = query[1], query[4]

    # Запрашиваем табличку
    table = TAMP_SHEET  # Указываем ссылку на таблицу таблицу
    name_list = 'Опоздания/Невыходы/Замены'  # Указываем название рабочего листа в таблице
    sheet = gs.get_sheet(table, name_list)  # Получаем объект таблицы
    col_date = sheet.get_col(1, include_tailing_empty=True)  # Запрос значений столбца

    now_date = str(datetime.date.today()).split('-')
    now_date = now_date[2] + '.' + now_date[1] + '.' + now_date[0]

    row = 1
    for date in col_date:

        if date == '':
            break
        row += 1

    addres = 'A' + str(row)
    cell = sheet.cell(addres)
    cell.set_value(now_date)

    addres = 'B' + str(row)
    cell = sheet.cell(addres)
    cell.set_value(str(crm_id) + ' | ' + str(teacher))

    addres = 'C' + str(row)
    cell = sheet.cell(addres)
    cell.set_value(type)
