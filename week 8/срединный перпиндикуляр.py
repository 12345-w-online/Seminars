n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

mean = sum([i[0] for i in data]) / len(data)
flag = True

for i in data:
    x = mean - (i[0] - mean)
    y = i[1]
    if not([x, y] in data):
        flag = False

if flag:
    print('Yes')
else:
    print('No')