c = list("AHIMOTUVWXY18EJSZ3L25")
k = list('EJSZ')

d = {
    'E': '3',
    'J': 'L',
    'S': '2',
    'Z': '5'
}

s = input()
one_bool = True
for i in range(0, int(len(s)/2)+1):
    if s[i] != s[len(s)-i-1]:
        one_bool = False

for i in range(len(s)):
    if s[i] in k:
        s = s.replace(s[i], d[s[i]])

print(s)
two_bool = True
for i in range(0, int(len(s)/2)+2):
    if (s[i] != s[len(s)-i-1]) or not(s[i] in c):
        two_bool = False

if one_bool == 1 and two_bool == 1:
    print('mirrored polindrom')
elif one_bool == 1 and two_bool == 0:
    print('polindrom')
elif one_bool ==0 and two_bool == 1:
    print('mirrored')
else:
    print('no')