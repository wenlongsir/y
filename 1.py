def sqrt(n):
    x = n
    while True:
        y = (x + n / x) / 2
        if abs(y - x) < 0.0001:
            return round(y, 2)
        x = y

for i in range(1, 101):
    print(f"The square root of {i} is {sqrt(i)}")
