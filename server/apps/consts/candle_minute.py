class UpbitCandleMinute:
    def __init__(self):
        self.five_m = {"minute": "minute5", "ko": "5분"}
        self.fifth_m = {"minute": "minute15", "ko": "15분"}
        self.thirty_m = {"minute": "minute30", "ko": "30분"}
        self.one_h = {"minute": "minute60", "ko": "1시간"}
        self.four_h = {"minute": "minute240", "ko": "4시간"}
        self.one_d = {"minute": "day", "ko": "1일"}
        self.one_w = {"minute": "week", "ko": "1주"}

    def get_all_korean_to_list(self):
        dict = self.__dict__
        lst = []

        for k, v in dict.items():
            lst.append(v['ko'])

        return lst

    def find_by_korean(self, ko):
        dict = self.__dict__

        for k, v in dict.items():
            if v["ko"] == ko:
                return v["minute"]

        return ""

upbit_candle_minute = UpbitCandleMinute()