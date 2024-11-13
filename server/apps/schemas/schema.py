from pydantic import BaseModel
from datetime import datetime


class Users(BaseModel):
    id: int
    user_id: str
    user_pw: str
    strategy: str
    allow_sell_with_loss: bool
    is_trading: bool
    bet_money: int
    order_cancel_minute: int
    access_key: str
    secret_key: str


class TradeRecord(BaseModel):
    id: int
    user_id: int
    name: str
    company: str
    buyPrice: float
    sellPrice: float
    orderEndDate: datetime


class TradeInProgress(BaseModel):
    id: int
    user_id: int
    name: str
    company: str
    trade_price: float
    ordered_at: datetime
    volume: float
    buy_count: int
    in_order: bool
    order_complete: bool


class Candle(BaseModel):
    id: int
    company: str
    minute: str
    market: str
    date_kst: datetime
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: float
