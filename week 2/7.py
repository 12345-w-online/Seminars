s = list(map(int,input().split()))
k = max([s.count(i) for i in s])
print((''.join(set([str(i)+' ' if s.count(i) == k else '' for i in s]))))