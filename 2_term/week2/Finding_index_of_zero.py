n = int(input())
s = list(map(int, input().split()))
index_zero = 0
for i in range(len(s)):
    if s[i] == 0:
        s[i] = [s[i], index_zero]
        index_zero += 1
index_previos_zero = None
list_index_zeros = []
for i in range(len(s) - 1, -1, -1):
    if isinstance(s[i], list):
        index_previos_zero = i
        list_index_zeros.append(i)
    else:
        s[i] = index_previos_zero
list_index_zeros.reverse()
# print(s)
# print(list_index_zeros)

list_answers = []
m = int(input())
for _ in range(m):
    left, right, k = map(int, input().split())
    left_i = left - 1
    right_i = right - 1
    if isinstance(s[left_i], list):
        index_need_z = s[left_i][1]
    elif s[left_i] is None:
        index_need_z = None
    else:
        index_need_z = s[s[left_i]][1]
    if index_need_z is not None:
        if (k - 1 + index_need_z) < len(list_index_zeros):
            list_answers.append(list_index_zeros[k - 1 + index_need_z])
        else:
            list_answers.append(None)
    else:
        list_answers.append(None)

print(*list_answers)
'''
12
0 1 0 0 1 1 0 1 1 0 1 1
3
1 5 2
2 7 3
1 12 5
'''
