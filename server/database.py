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
    user = '''
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

    trade_record = '''
        CREATE TABLE IF NOT EXISTS trade_records (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        company TEXT NOT NULL,
        buyPrice REAL NOT NULL,
        sellPrice REAL NOT NULL,
        orderEndDate DATETIME NOT NULL
    );'''

    trade_in_progress = '''
        CREATE TABLE IF NOT EXISTS trade_in_progress (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        company TEXT NOT NULL,
        trade_price REAL NOT NULL,
        ordered_at DATETIME NOT NULL,
        volume REAL NOT NULL,
        buy_count INTEGER NOT NULL,
        in_order BOOLEAN NOT NULL,
        order_complete BOOLEAN NOT NULL
    );'''

    candle = '''
        CREATE TABLE IF NOT EXISTS  Candle (
        id INTEGER PRIMARY KEY,
        company TEXT NOT NULL,
        minute TEXT NOT NULL,
        market TEXT NOT NULL,
        date_kst TEXT NOT NULL,
        open_price REAL NOT NULL,
        high_price REAL NOT NULL,
        low_price REAL NOT NULL,
        close_price REAL NOT NULL,
        volume REAL NOT NULL
    );'''

    DataBase.run_query(query=user)
    DataBase.run_query(query=trade_record)
    DataBase.run_query(query=trade_in_progress)
    DataBase.run_query(query=candle)


if __name__ == '__main__':
    init_db()
