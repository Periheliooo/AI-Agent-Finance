# simulation.py — 主模拟程序：驱动每轮仿真并输出日志

import config
from market import Market
from agents import FomoAgent, ValueAgent, GamblerAgent
from llm import generate_reason


def print_separator():
    print("-" * 40)


def print_agent_state(agent):
    state = agent.get_state()
    print(f"  [{state['name']}] {state['personality']}")
    print(f"    Cash: ${state['cash']} | Position: {state['position']} "
          f"| Recent: {state['recent_actions']}")


def run():
    # 初始化市场
    market = Market()

    # 初始化三个 Agent
    agents = [
        FomoAgent(),
        ValueAgent(),
        GamblerAgent(),
    ]

    print("=" * 40)
    print("  AI 金融市场 Agent 模拟系统")
    print("  资产: CoinX  |  初始价格: $100")
    print("=" * 40)
    print()

    for tick in range(1, config.MAX_TICKS + 1):
        old_price = round(market.get_price(), 2)

        # 收集每个 Agent 的决策
        actions = []
        for agent in agents:
            action = agent.act(market.get_price(), market.get_history())
            actions.append(action)

        # 根据买卖更新市场价格
        market.update(actions)

        new_price = round(market.get_price(), 2)

        # 输出本轮日志
        print(f"Tick {tick}")
        print(f"Price: ${old_price} -> ${new_price}")
        print()

        for agent in agents:
            last_action = agent.memory[-1]
            # 预留 LLM 接口
            reason = generate_reason(agent.name, last_action, new_price, market.get_history())
            print(f"  {agent.name}: {last_action}")
            if reason:
                print(f"    理由: {reason}")

        print_separator()
        print()

    # 最终总结
    print("=" * 40)
    print("  模拟结束 — 最终状态")
    print("=" * 40)
    print(f"  CoinX 最终价格: ${round(market.get_price(), 2)}")
    print()
    for agent in agents:
        state = agent.get_state()
        # 计算总资产 = 现金 + 持仓市值
        total = state["cash"] + state["position"] * market.get_price()
        print(f"  [{state['name']}] 总资产: ${round(total, 2)}")
        print(f"    现金: ${state['cash']} | 持仓: {state['position']} 单位")

    print()
    print("  (LLM 接口已预留，第二阶段接入真实 API)")


if __name__ == "__main__":
    run()
