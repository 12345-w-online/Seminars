import numpy as np
import math


def my_max(left, right):
    if left <= right:
        return right
    else:
        return left


def my_nod(left, right):
    while left != right:
        if left > right:
            left -= right
        else:
            right -= left
    return left


def create_max_table(n, s):
    table_maxes = np.zeros((int(math.log(n, 2)) + 1, n))
    table_maxes[0] = s
    for i in range(1, int(math.log(n, 2))+2):  # алгоритм для создания таблицы максимумов
        for j in range(n):
            if not ((2 ** (i - 1) + j) >= (n)) and table_maxes[i - 1][2 ** (i - 1) + j] != 0 and \
                    table_maxes[i - 1][j] != 0:
                max_elem = my_nod(table_maxes[i - 1][2 ** (i - 1) + j], table_maxes[i - 1][j])
                table_maxes[i][j] = max_elem
            else:
                break
    return table_maxes


def find_max_in_table_maxes(table_maxes, right, left):
    k = math.floor(math.log(right - left, 2))
    if table_maxes[k][left - 1] >= table_maxes[k][right - 2 ** k]:
        return table_maxes[k][left - 1]
    else:
        return table_maxes[k][right - 2 ** k]


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    table_maxes = create_max_table(n, s)
    print(table_maxes)

    list_answers = []
    k = int(input())
    for _ in range(k):
        left, right = map(int, input().split())
        list_answers.append(find_max_in_table_maxes(table_maxes, right, left))
    print(*list_answers)

'''
# Test
10
8 24 4 9 3 2 8 2 5 10
3
1 10
2 5
5 9
'''
