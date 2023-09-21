n, s = map(str,input().split())
print(''.join([s[elem+int(n): elem: -1] for elem in range(0, len(s), int(n))]))