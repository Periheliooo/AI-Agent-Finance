# market.py — 市场模块：维护价格、价格历史、根据买卖单更新价格

import config

class Market:
    """虚拟金融市场，维护 CoinX 的价格和历史记录。"""

    def __init__(self):
        self.price = config.INITIAL_PRICE
        self.history = [self.price]  # 每轮价格快照

    def update(self, actions):
        """
        根据 Agent 的买卖行为更新价格。
        actions: list[str]，如 ["BUY", "SELL", "HOLD"]
        公式: price_next = price * (1 + alpha * (buy_count - sell_count) / N)
        """
        buy_count = actions.count("BUY")
        sell_count = actions.count("SELL")
        n = len(actions)

        delta = config.ALPHA * (buy_count - sell_count) / n
        new_price = self.price * (1 + delta)
        # 防止价格跌到 0 以下
        self.price = max(new_price, 0.01)
        self.history.append(self.price)

    def get_price(self):
        return self.price

    def get_history(self):
        return self.history
