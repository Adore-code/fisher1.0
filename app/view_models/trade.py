"""
 Created by Tang on 2020/2/16 21:04
"""

class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self._parse(goods)


    def _parse(self, trades):
        self.total = len(trades)
        self.trades = [self._map_to_trade(gift) for gift in trades]

    def _map_to_trade(self, single):
        if single.create_datetime:
            time=single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            time = time,
            id=single.id
        )
