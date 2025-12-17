import csv

# 总分
total_score = 0
# 学生人数
count = 0

# 建议涉及文件操作时，预先定义好文件路径
csv_path = 'students.csv'

# 打开 csv 文件
# 注意编码问题 一般使用utf-8即可
# 尽量使用with语句管理文件上下文 避免忘记关闭文件
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader) # 跳过第一行 表头
    # 逐行读取数据
    for row in reader:
        score = float(row[3])  # 第4列是分数
        total_score += score
        count += 1

# 计算平均分
average_score = total_score / count

print(f"全年级学生人数：{count}")
print(f"全年级平均成绩：{average_score:.2f}")