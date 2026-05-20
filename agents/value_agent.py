# agents/value_agent.py — Value Agent：价值投资型

import config
from .base_agent import BaseAgent


class ValueAgent(BaseAgent):
    """
    价值投资者：
    - 当前价格 < 均价 → 低估 → BUY
    - 当前价格 > 均价 → 高估 → SELL
    - 价格接近均价 → HOLD
    """

    def __init__(self):
        super().__init__(
            name="Value",
            personality="价值投资 / 低买高卖 / 厌恶风险",
        )

    def decide(self, price, history):
        if len(history) < 3:
            return "HOLD"

        # 计算移动均价
        avg_price = sum(history) / len(history)
        threshold = avg_price * 0.02  # 2% 阈值避免频繁交易

        if price < avg_price - threshold:
            return "BUY"   # 低估买入
        elif price > avg_price + threshold:
            return "SELL"  # 高估卖出
        else:
            return "HOLD"
