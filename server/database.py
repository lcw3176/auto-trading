from __future__ import annotations
import sqlite3
import atexit
from typing import Any, Tuple


class DataBase:
    def __init__(self, db_name: str = 'main.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def run_query(self, query: str, params: Tuple[Any, ...] = ()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as error:
            print(f"Error: {error}")

    def run_query_with_cursor(self, query: str, params: Tuple[Any, ...] = ()):
        try:
            return self.cursor.execute(query, params)

        except sqlite3.Error as error:
            print(f"Error: {error}")
            return None

    def close_db(self):
        if self.conn:
            self.conn.close()


db = DataBase()


def mapped_key_value(rows):
    dic = {}
    for i in range(0, len(rows)):
        dic[rows.keys()[i]] = rows[i]

    return dic


atexit.register(db.close_db)


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
        CREATE TABLE IF NOT EXISTS trade_record (
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
        CREATE TABLE IF NOT EXISTS candle (
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

    db.run_query(query=user)
    db.run_query(query=trade_record)
    db.run_query(query=trade_in_progress)
    db.run_query(query=candle)


if __name__ == '__main__':
    init_db()
