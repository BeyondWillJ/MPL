# 统计文本文件中每个单词的出现频率，并将结果打印到终端
from collections import Counter
def word_frequency(input_file):
    # 读取文件内容
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # 转为小写

        # 去除标点符号
        for char in '.,!?;:()[]{}<>':
            text = text.replace(char, '')

    # 分割单词
    words = text.split()

    # 计算单词频率
    frequency = Counter(words)

    # 打印结果到终端
    for word, count in frequency.most_common():
        print(f"{word}: {count}")
# 使用示例
word_frequency('input.txt')