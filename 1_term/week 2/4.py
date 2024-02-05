s = list(map(int,input().split()))
print([s[i+1] if i%2 == 0 else s[i-1] for i in range(len(s)-1)]+[s[len(s)-1]])