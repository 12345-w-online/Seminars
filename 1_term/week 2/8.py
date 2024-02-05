s = list(map(int,input().split()))
   # for j in (s[:s.index(i)] + s[s.index(i)+1]) for i in s
for i in s:
   k, l =0, 0
   for j in (s[:s.index(i):] + s[s.index(i)+1::]):
      if i > j:
         k+=1
      else:
         l+=1
   if k == l:
      print(i)