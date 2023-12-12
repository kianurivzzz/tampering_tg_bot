import google_sheets.gsheets as gs
import database.db_querys as db
from config import DB_SHEET


def update_teachers():
    table = DB_SHEET # Указываем ссылку на таблицу
    name_sheet = 'Преподаватели' # Указываем индекс рабочего листа в таблице
    sheet = gs.get_sheet(table, name_sheet) # Получаем объект таблицы

    names = sheet.get_col(2, include_tailing_empty=True) # Запрос значений столбца
    mails = sheet.get_col(4, include_tailing_empty=True) # Запрос значений столбца
    tg_usernames = sheet.get_col(5, include_tailing_empty=True) # Запрос значений столбца
    crm_ids = sheet.get_col(1, include_tailing_empty=True) # Запрос значений столбца
    chat_ids = sheet.get_col(19, include_tailing_empty=True) # Запрос значений столбца

    i = 2
    for elem in names:
        if names[i] == None or names[i] == '':
            continue

        teacher_info = [int(crm_ids[i]) if crm_ids[i] != '' else crm_ids[i], names[i], mails[i], tg_usernames[i], int(chat_ids[i]) if chat_ids[i] != '' else chat_ids[i]]
        print(teacher_info)

        query = db.execute_script('SELECT * FROM teachers WHERE tg_username=?', (teacher_info[3], ))

        if query != None:
            db.execute_script('UPDATE teachers SET name=?, mail=?, tg_username=?, crm_id=?, chat_id=? WHERE tg_username=?', (teacher_info[1], teacher_info[2], teacher_info[3], teacher_info[0], teacher_info[4], teacher_info[3]))

        else:
            db.execute_script('INSERT INTO teachers (name, mail, tg_username, crm_id, chat_id) VALUES (?, ?, ?, ?, ?)', (teacher_info[1], teacher_info[2], teacher_info[3], teacher_info[0], teacher_info[4]))

        i += 1


update_teachers()
