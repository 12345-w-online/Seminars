s = list(map(int,input().split()))
b = [i + 1 for i in range(int(s[0]))]
print(b)
print([item for item in b if item not in s[1::]][0])
