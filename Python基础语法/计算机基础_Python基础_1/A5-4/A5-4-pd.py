import pandas as pd

df = pd.read_csv('students.csv', encoding='utf-8')
average_score = df['分数'].mean()

print(f"全年级学生人数：{len(df)}")
print(f"全年级平均成绩：{average_score:.2f}")
