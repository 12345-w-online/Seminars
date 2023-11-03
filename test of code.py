def dorogi(s, t):
    doro = []
    doro.append(s[0])
    my_len = 0
    for i in range(1, len(s)):
        my_len += calc_my_len(s[i-1], s[i])
    my_len = my_len / (t - 1)
#     print(my_len, my_len ** (0.5))
    print(add_nul(s[0][0]), add_nul(s[0][1]))
    k = 0
    now_my_len = 0
    for i in range(t - 1):
        now_my_len = my_len + now_my_len
        while now_my_len > calc_my_len(s[k], s[k + 1]):
            now_my_len -= calc_my_len(s[k], s[k + 1])
            k += 1
        alfa = now_my_len / calc_my_len(s[k], s[k + 1])
        x = s[k][0] + (s[k + 1][0] - s[k][0]) * alfa
        y = s[k][1] + (s[k + 1][1] - s[k][1]) * alfa
        print(add_nul(round(x, 2)), add_nul(round(y, 2)))
        
def add_nul(a):
    if len(str(a).split('.')[1]) < 2:
        new_a = (str(str(a).split('.')[0]) + '.' + (str(str(a).split('.')[1]) + '00')[0:2:])
        return new_a
    else:
        return a

def calc_my_len(t1, t2):
    
    return (((t2[0] - t1[0]) ** 2) + ((t2[1] - t1[1]) ** 2)) ** (0.5)

def enter(k):
    a = []
    for j in range(k):
        a.append(list(map(float, input().split())))
    return a

n = int(input())

for i in range(n):
    print(f"Road #{i + 1}:")
    a, b = map(int, input().split())
    s = enter(a)
    dorogi(s, b)