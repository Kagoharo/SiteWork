import math
from datetime import time
import psycopg2

def addUser(self, name, email, hpsw):
    try:
        self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE email LIKE '{email}'")
        res = self.__cur.fetchone()
        if res['count'] > 0:
            print("Пользователь с таким email уже существует")
            return False

        tm = math.floor(time.time())
        self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, ?)", (name, email, hpsw, tm))
        self.__db.commit()
    except psycopg2.Error as e:
        print("Ошибка добавления пользователя в БД " + str(e))
        return False

    return True