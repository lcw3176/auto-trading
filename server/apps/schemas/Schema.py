from pydantic import BaseModel


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





