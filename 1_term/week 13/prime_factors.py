def prime_factors(n, m, s, x):
    if n == 0:
        return 0
    if n < 0:
        raise ValueError('NO NEGATIVE NUMBERS')
    if isinstance(n, float):
        return ValueError('NO FLOAT VALUES')
    if m > x ** (1 / 2) + 1:
        return s + [x]
    elif n % m == 0:
        return prime_factors(n // m, m, s + [m], x)
    else:
        return prime_factors(n, m + 1, s, x)


def calling_function(n):
    return prime_factors(n, 2, [1], n)


if __name__ == '__main__':
    n = int(input())
    print(prime_factors(n, 2, [1], n))
