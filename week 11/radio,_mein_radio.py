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


n, r = map(int, input().split())
r = r * 2
my_list = list(map(int, input().split()))

my_list = sorterovka(my_list)
# print(my_list)
my_right = my_list[0] + r
count = 1
for elem in my_list:
    # print(my_right)
    if elem > my_right:
        count += 1
        my_right = elem + r
    else:
        continue

print(count)