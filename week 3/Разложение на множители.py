def mnoj(n, m, s, x):
    if m > x**(1/2)+1:
        return s + [x]
    elif n % m == 0:
        return mnoj(n//m, m, s + [m], x)
    else:
        return mnoj(n, m+1, s, x)


n = int(input())

print(mnoj(n, 2, [1], n))