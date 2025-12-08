import random as r
def estimate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x = r.uniform(-1, 1)  # 生成[-1, 1]之间的随机数
        y = r.uniform(-1, 1)  # 生成[-1, 1]之间的随机数
        if x**2 + y**2 <= 1:       # 判断点是否在圆内
            inside_circle += 1
    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate
num_samples = 1000000  # 采样点数
pi_value = estimate_pi(num_samples)
print(f"估算的π值：{pi_value}")