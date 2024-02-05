s = list(map(int,input().split()))
print(''.join([str(i)+' ' if s.count(i) == 1 else '' for i in s]))