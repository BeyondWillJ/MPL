"""生成学生信息 CSV 文件

生成 1000 行数据，字段为：学号, 姓名, 班级, 分数
- 学号格式：2025XXXXX（5 位顺序数字，不重复）
- 姓名：常见中文姓名，随机生成且不重复
- 班级：在 25_1 .. 25_8 中随机分配
- 分数：混合分布 — 以概率 low_prob(默认 0.02) 分配为 3~10 的极低分（模拟极端低分学生），其余服从均值 80（可配置，默认 std=20）的正态分布，取整并截断到 3 ~ 100 的整数

输出文件：students.csv（UTF-8-sig，方便在 Windows/Excel 打开）
"""

import csv
import random
from typing import List


def generate_unique_names(n: int) -> List[str]:
	# 常用姓氏（取一部分常见姓氏）
	surnames = [
		"王", "李", "张", "刘", "陈", "杨", "赵", "黄", "周", "吴",
		"徐", "孙", "朱", "马", "胡", "郭", "何", "高", "林", "罗",
		"郑", "梁", "谢", "宋", "唐", "许", "韩", "冯", "邓", "曹",
		"彭", "曾", "肖", "田", "董", "潘", "袁", "于", "余", "叶",
		"蒋", "杜", "苏", "魏", "程", "吕", "丁", "沈", "任", "姚",
	]

	# 常见名字用字（单字），会随机组合成1或2个字的名
	name_chars = list(
		"伟芳秀英华明静丽强磊军洋勇杰娟涛超玲慧辉磊鑫敏淑燕佳峰鑫诚晓宁欣宇俊佳倩宁洁嘉辉志豪文斌雅婷志强瑞丽鹏翔晨昊诗琪晨曦")

	names = set()
	while len(names) < n:
		s = random.choice(surnames)
		k = random.choice([1, 2])  # 名字长度：1 或 2
		g = ''.join(random.choices(name_chars, k=k))
		name = s + g
		names.add(name)

	return list(names)


def generate_students(n: int = 1000, out_file: str = "students.csv", mean: float = 80.0, std: float = 20.0, low_prob: float = 0.02) -> None:
	# 生成不重复的学号：2025 + 5 位数字
	ids = [f"2025{num:05d}" for num in random.sample(range(100000), n)]

	# 生成不重复的姓名
	names = generate_unique_names(n)
	random.shuffle(names)

	# 随机分配班级与分数（混合分布：部分极低分 + 正态分布）
	classes = [f"25_{random.randint(1, 8)}" for _ in range(n)]
	# 以概率 low_prob 生成 3~10 的极低分，剩余样本服从 N(mean, std)
	scores = []
	for _ in range(n):
		if random.random() < low_prob:
			s = random.randint(3, 10)
		else:
			s = int(round(random.gauss(mean, std)))
			s = max(3, min(100, s))
		scores.append(s)

	# 写入 CSV，使用 utf-8-sig 以便 Excel 正确识别
	with open(out_file, "w", newline="", encoding="utf-8-sig") as f:
		writer = csv.writer(f)
		writer.writerow(["学号", "姓名", "班级", "分数"])
		for i in range(n):
			writer.writerow([ids[i], names[i], classes[i], scores[i]])

	print(f"已生成 {n} 条学生记录，保存到 {out_file}")


if __name__ == "__main__":
	generate_students(3000, "students.csv")

