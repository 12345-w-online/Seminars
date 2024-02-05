n = int(input())
dict = {}
for u in range(n):
    name, i, j = map(str, input().split())
    dict[name] = [int(i), int(j)]

a = input()
while a != '0':
    s = []
    a = list(a)
    for u in range(len(a)):
        s.append(dict[a[u]])
    # print(s)
    for k in range(len(s) - 1):
        if s[k][1] != s[k + 1][0]:
            print('error')
            break
    else:
        if len(s) == 1:
            print(0)
        else:
            m = min(list(map(lambda x: x[1], s[:-1])))
            sum = 0
            for i in s:
                if i[0] != m and i[1] != m:
                    sum += i[0] * i[1]
            sum += s[0][0] * s[len(s) - 1][1]
            # print(m)
            print(sum * m)
    
    a = input()
# print(s)
