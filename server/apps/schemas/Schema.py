from abc import *

class Schema(metaclass=ABCMeta):

    @abstractmethod
    def get_schema(self) -> dict:
        pass


class User(Schema):
    def __init__(self, user_id, user_pw, strategy, allow_sell_with_loss, is_trading, bet_money, order_cancel_minute, access_key, secret_key) -> None:
        self.user_id = user_id
        self.user_pw = user_pw
        self.strategy = strategy
        self.allow_sell_with_loss = allow_sell_with_loss
        self.is_trading = is_trading
        self.bet_money = bet_money
        self.order_cancel_minute = order_cancel_minute
        self.access_key = access_key
        self.secret_key = secret_key


    def get_schema(self) -> dict:
        return {
            "user_id" : self.user_id,
            "user_pw" : self.user_pw
        }


