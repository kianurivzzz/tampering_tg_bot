import sqlite3

from config import DB_PATH

def execute_script(script, tup):                         # Выполняем script
    conn = sqlite3.connect(DB_PATH)           # Подключаемся к базе
    cur = conn.cursor()                                  # Создаём курсор
    cur.execute(script, tup)                             # Выполняем скрипт
    result = cur.fetchall()                              # Сохраняем результат
    conn.commit()                                        # Подтверждаем изменения
    conn.close()                                         # Закрываем подключение
    if result:                                           # Если есть результат
        return result[0]

def execute_script_all(script, tup):                     # Выполняем script
    conn = sqlite3.connect(DB_PATH)           # Подключаемся к базе
    cur = conn.cursor()                                  # Создаём курсор
    cur.execute(script, tup)                             # Выполняем скрипт
    result = cur.fetchall()                              # Сохраняем результат
    conn.commit()                                        # Подтверждаем изменения
    conn.close()                                         # Закрываем подключение
    if result:                                           # Если есть результат
        return result
