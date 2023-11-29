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

def my_h_index(s_list:list) -> int:
    my_h_ind = 0
    for elem, number in zip(reversed(s_list), range(1, len(s_list) + 1)):
        if elem >= number:
            my_h_ind += 1
        else:
            break
    return my_h_ind

def n_to_up_h_index(s_list:list) -> int:
    upping_h = my_h_index(s_list) + 1
    counter = 0
    for elem in s_list[-1: -upping_h - 1: -1]:
        if elem == upping_h - 1:
            counter += 1
        elif elem < upping_h:
            return -1
    return counter


n, l = map(int, input().split())
my_list = list(map(int, input().split()))
my_list = sorterovka(my_list)
# print(my_list)
needs_l = n_to_up_h_index(my_list)

if needs_l != -1 and needs_l <= l:
    print(my_h_index(my_list) + 1)
else:
    print(my_h_index(my_list))