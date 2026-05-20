# agents/base_agent.py — Agent 基类：定义通用属性和接口

import config

class BaseAgent:
    """所有交易 Agent 的基类。"""

    def __init__(self, name, personality):
        self.name = name
        self.personality = personality  # 人格描述文字
        self.cash = config.INITIAL_CASH
        self.position = 0               # 持仓数量
        self.memory = []                # 记录每轮自己的行为 ("BUY"/"SELL"/"HOLD")

    def decide(self, price, history):
        """
        子类必须实现此方法。
        返回 "BUY" / "SELL" / "HOLD" 之一。
        """
        raise NotImplementedError

    def act(self, price, history):
        """执行决策并记录到 memory。"""
        action = self.decide(price, history)
        self.memory.append(action)

        # 更新持仓和资金（简化：每次交易 1 单位）
        if action == "BUY" and self.cash >= price:
            self.position += 1
            self.cash -= price
        elif action == "SELL" and self.position > 0:
            self.position -= 1
            self.cash += price

        return action

    def get_state(self):
        """返回 Agent 当前状态摘要。"""
        return {
            "name": self.name,
            "personality": self.personality,
            "cash": round(self.cash, 2),
            "position": self.position,
            "recent_actions": self.memory[-5:],
        }
