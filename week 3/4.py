a, b = input().split()
[print(b * i) if i <= int(a) // 2 +1 else print(b * (int(a) + 1 - i)) for i in range(1, int(a) + 1)]
