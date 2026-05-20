# agents/gambler_agent.py — Gambler Agent：赌徒/随机交易型

import random
from .base_agent import BaseAgent


class GamblerAgent(BaseAgent):
    """
    赌徒型交易者：
    - 完全随机决策
    - 高风险偏好（倾向交易而非持有）
    - BUY 40% / SELL 40% / HOLD 20%
    """

    def __init__(self):
        super().__init__(
            name="Gambler",
            personality="赌徒 / 高风险偏好 / 随机决策",
        )

    def decide(self, price, history):
        r = random.random()
        if r < 0.4:
            return "BUY"
        elif r < 0.8:
            return "SELL"
        else:
            return "HOLD"
