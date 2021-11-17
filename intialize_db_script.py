import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
   connection = psycopg2.connect(user="postgres",
                                 password="123",
                                 host="127.0.0.1",
                                 port="5432",)
   connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
   cursor = connection.cursor()
   sql_create_database = 'create database site'
   cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection:
       cursor.close()
       connection.close()
       print("Соединение с PostgreSQL закрыто")

try:
    connection = psycopg2.connect(user="postgres",
                                      password="123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="site")
    cursor = connection.cursor()
    print("Вы подключены к - серверу")

    create_table_query = '''CREATE TABLE IF NOT EXISTS product_categories
                              (pcid SERIAL PRIMARY KEY,
                              category varchar(30) NOT NULL,
                              description varchar(500)); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица 'Категории товаров' успешно создана")

    create_table_query = '''CREATE TABLE IF NOT EXISTS product
                              (pid SERIAL PRIMARY KEY,
                              pcid INTEGER,
                              name varchar(50) NOT NULL CHECK (length(name) >=5),
                              description varchar(500),
                              price float NOT NULL CHECK (price > 0),
                              amount real NOT NULL,
                              image bytea DEFAULT NULL,
                              FOREIGN KEY (pcid) REFERENCES product_categories(pcid)); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица 'Товары' успешно создана")

    create_table_query = '''CREATE TABLE IF NOT EXISTS history
                              (hid SERIAL PRIMARY KEY,
                              pid INTEGER,
                              product_name varchar(50) NOT NULL,
                              product_amount real NOT NULL,
                              date_of_change timestamp NOT NULL,
                              FOREIGN KEY (pid) REFERENCES product (pid)); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица 'История изменений' успешно создана")

    create_table_query = '''CREATE TABLE IF NOT EXISTS login_credentials
                              (lcid SERIAL PRIMARY KEY,
                              email varchar(30),
                              password varchar(30)
                              ); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица 'Данные для авторизации' успешно создана")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")