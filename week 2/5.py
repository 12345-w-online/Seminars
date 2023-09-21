s = list(map(int,input().split()))
print([s[len(s)-1]]+s[:len(s)-1])