def my_max(s, m):
    fir_m = m
    s = list(map(int, list(str(s))))
    i = 0
    max_s = []
    while m != 0 and m < (len(s) - (i)):
        
        # print(s[i:m + i + 1], max(s[i:m + i + 1]))
        max_s.append(max(s[i:m + i + 1]))
        if max(s[i:m + i + 1]) != s[i]:
            # print(s[i::].index(max_s[-1]), i)
            m -= s[i::].index(max_s[-1]) 
        i = s[i::].index(max_s[-1]) + 1 + i
        # print(m, i, max_s)
            
    if len(max_s) < (len(s) - fir_m):
        # print(len(max_s), (len(s) - fir_m))
        return ''.join(map(str, max_s + s[i::]))
    return ''.join(map(str, max_s))


n, m  = map(int, input().split())
while n != 0 and m != 0:
    a = int(input())
    print(my_max(a, m))
    n, m = map(int, input().split())
    