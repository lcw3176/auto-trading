import pyupbit
import requests
import pandas as pd
from database import db
from functools import lru_cache
from apps.consts.candle_minute import upbit_candle_minute

@lru_cache(maxsize=200)
def get_all_tickers():
    base_headers = {"accept": "application/json"}

    url = "https://api.upbit.com/v1/market/all?is_details=false"
    res = requests.get(url, headers=base_headers)

    return res.json()


def get_backtest_info():
    korean_ticker = []

    for i in get_all_tickers():
        if 'KRW' in i['market']:
            korean_ticker.append(i['korean_name'])

    candle_minute = upbit_candle_minute.get_all_korean_to_list()

    return {
        "ticker": korean_ticker,
        "candle_minute": candle_minute
    }


def get_candle_data(ticker_kor, interval_kor, start_date, end_date):
    ticker = ''

    for i in get_all_tickers():
        if 'KRW' in i['market'] and i['korean_name'] == ticker_kor:
            ticker = i['market']
            break

    interval = upbit_candle_minute.find_by_korean(interval_kor)

    candle_data = pyupbit.get_ohlcv_from(ticker=ticker, interval=interval, fromDatetime=start_date, to=end_date)
    base_data = candle_data.reset_index()
    base_data["time"] = pd.to_datetime(base_data["index"]).dt.strftime(
        "%Y-%m-%dT%H:%M:%S"
    )

    base_data = base_data.drop(columns=["index"])
    base_data["time"] = pd.to_datetime(base_data["time"]).astype("int64") / 10 ** 9

    return base_data.to_dict(orient='records')