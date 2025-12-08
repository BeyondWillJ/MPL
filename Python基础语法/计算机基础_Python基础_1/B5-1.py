import random as r

def monty_hall(switch):
	doors = [0, 1, 2]
	prize = r.choice(doors)
	choice = r.choice(doors)

	# 主持人随机打开一扇既不是玩家选的门也不是奖品的门
	possible_to_open = [d for d in doors if d != choice and d != prize]
	opened = r.choice(possible_to_open)

	if switch:
		remaining = [d for d in doors if d != choice and d != opened]
		new_choice = remaining[0] # 只有一扇门剩下
		return new_choice == prize
	else:
		return choice == prize


# 不换
trials = 10000
wins_without_switch = sum(monty_hall(switch=False) for _ in range(trials))
print(f"不换门赢的概率: {wins_without_switch / trials:.2%}")
# 换
wins_with_switch = sum(monty_hall(switch=True) for _ in range(trials))
print(f"换门赢的概率: {wins_with_switch / trials:.2%}")