from math import ceil
def sorterovka(a, key=lambda x: x):
    summ = 0
    if len(a) == 0:
        return []
    for i in range(len(a)):
            summ += key(a[i])

    sr = ceil(summ/len(a))
    eq = []
    minn = []
    maxx = []
    for i in range(len(a)):
        if key(a[i]) == sr:
            eq.append(a[i])
        elif key(a[i]) > sr:
            maxx.append(a[i])
        else:
            minn.append(a[i])
    return sorterovka(minn, key) + eq + sorterovka(maxx, key)


n = int(input())

my_list = []
for i in range(n):
    left, right = map(int, input().split())
    my_list.append([left, right])

my_list = sorterovka(my_list, key=lambda x: x[0])
print(my_list)
my_len = len(my_list)

now_right = my_list[0][1]
count = 1
for elem in my_list:
    if elem[0] > now_right:
        count += 1
        # print(elem)
        now_right = elem[1]
    elif elem[1] < now_right:
        now_right = elem[1]
    else:
        continue

print(count)