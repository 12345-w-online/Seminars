def fibonachi(x, y, i, n):
    if i == n:
        return int(y)
    else:
        return fibonachi(y, x+y, i+1, n)


print(fibonachi(1, 1, 2, 10))
