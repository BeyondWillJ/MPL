def fibonacci(n):
    """计算斐波那契数列的前n项"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # 初始化前两项
    fib_sequence = [0, 1]

    # 计算后续项
    for i in range(2, n):
        next_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_num)

    return fib_sequence

def save_fibonacci(n, output_file):
    """计算斐波那契数列并保存到文件"""
    # 计算数列
    sequence = fibonacci(n)

    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, num in enumerate(sequence):
            f.write(f"F({i}) = {num}\n")
        # 添加统计信息
        f.write("\n")
        f.write(f"总项数：{len(sequence)}\n")
        if sequence:
            f.write(f"最大值：{max(sequence)}\n")
            f.write(f"总和：{sum(sequence)}\n")

    print(f"结果已保存到 {output_file}")
    # 也打印到终端
    print(f"前10项为：{sequence[:10]}")

save_fibonacci(20, 'fibonacci.txt')