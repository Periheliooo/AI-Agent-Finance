# agents/fomo_agent.py — FOMO Agent：追涨杀跌型

import random
from .base_agent import BaseAgent


class FomoAgent(BaseAgent):
    """
    恐惧与贪婪驱动的交易者：
    - 连续上涨 → 倾向 BUY（害怕踏空）
    - 连续下跌 → 倾向 SELL（恐慌抛售）
    - 趋势不明 → HOLD
    """

    def __init__(self):
        super().__init__(
            name="FOMO",
            personality="追涨杀跌 / 害怕踏空 / 容易恐慌",
        )

    def decide(self, price, history):
        if len(history) < 3:
            return "HOLD"

        # 最近 3 轮价格趋势
        recent = history[-3:]
        up_count = sum(1 for i in range(1, len(recent)) if recent[i] > recent[i - 1])
        down_count = sum(1 for i in range(1, len(recent)) if recent[i] < recent[i - 1])

        if up_count == 2:
            # 连续上涨 → 80% 追买
            return "BUY" if random.random() < 0.8 else "HOLD"
        elif down_count == 2:
            # 连续下跌 → 80% 恐慌卖出
            return "SELL" if random.random() < 0.8 else "HOLD"
        else:
            return "HOLD"
