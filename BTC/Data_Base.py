import sqlite3

class Base:

    contact = sqlite3.connect('btc.db')
    cur = contact.cursor()


    def insert_to_base(self, dictionary):
        '''Записывает новые данные в базу'''

        self.connection = self.cur
        self.cur.execute("CREATE TABLE IF NOT EXISTS historical (date TEXT UNIQUE, price REAL)")
        for k, v in dictionary.items():
            self.cur.execute("INSERT OR IGNORE INTO historical (date, price) VALUES (?, ?)",
                        (k, v))
        self.contact.commit()

    def execute_rest_to_base(self, start, end):
        '''Проверка наличия данных за указанный период в базе'''

        self.connection = self.cur
        self.cur.execute("SELECT * FROM historical WHERE date BETWEEN ? AND ?", (start, end))
        result = self.cur.fetchall()
        return result
        self.contact.commit()

    def check_base_rest(self, date):
        '''Проверка данных за конкретную дату в базе для формирования интервалов запроса'''

        self.connection = self.cur
        self.cur.execute("CREATE TABLE IF NOT EXISTS historical (date TEXT UNIQUE, price REAL)")  # Для самого первого запроса, когда базы еще нет
        self.cur.execute("SELECT * FROM historical WHERE date == ?", (date,))
        result = self.cur.fetchall()
        return result
        self.contact.commit()

BTC= Base()