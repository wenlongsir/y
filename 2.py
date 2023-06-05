import random

n = 1000000  # 抛点次数
count = 0  # 落在圆内的点数

for i in range(n):
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        count += 1

pi = 4 * count / n
print(f"The estimated value of pi is {pi:.2f}")
