a = input()
staples_c = {")": "(", "]": "[", "}": "{"}
s = []
flag = 1
for i in a:
    if i in staples_c.keys():
        # print(staples_c[i], s[-1])
        if s[-1] == staples_c[i]:
            # print('check of end ctaples')
            s.pop(-1)
        else:
            flag = 0
    else:
        s.append(i)

if flag:
    print('Yes')
else:
    print('No')