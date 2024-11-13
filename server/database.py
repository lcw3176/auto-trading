from __future__ import annotations
import sqlite3
import atexit
from typing import Any, Tuple


class DataBase:
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    @classmethod
    def run_query(cls, query: str, params: Tuple[Any, ...] = ()):
        try:
            cls.cursor.execute(query, params)
            cls.conn.commit()

        except sqlite3.Error as error:
            print(error)

    @classmethod
    def run_query_with_result(cls, query: str, params: Tuple[Any, ...] = ()):
        try:
            cls.cursor.execute(query, params)
            yield from cls.cursor.fetchall()
        except sqlite3.Error as error:
            print(error)

    @classmethod
    def close_db(cls):
        if cls.conn:
            cls.conn.close()


atexit.register(DataBase.close_db)


def init_db():
    init_query = '''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id TEXT NOT NULL,
        user_pw TEXT NOT NULL,
        strategy TEXT NOT NULL,
        allow_sell_with_loss BOOLEAN NOT NULL,
        is_trading BOOLEAN NOT NULL,
        bet_money INTEGER NOT NULL,
        order_cancel_minute INTEGER NOT NULL,
        access_key TEXT NOT NULL,
        secret_key TEXT NOT NULL
    );'''

    DataBase.run_query(query=init_query)


if __name__ == '__main__':
    init_db()
