def lavel(a):
    first = ['*', '/']
    second = ['+', '-']
    if a in first:
        return 1
    elif a in second:
        return 0


def polska(a):
    first = ['*', '/']
    print(a)
    second = ['+', '-']
    a = list(a)
    s = []
    s_ = [0, 0]
    operrators = []
    for i in a:
        
        # start part working with ctaples
        if i == '(':
            s_ = polska(a[a.index('(') + 1::])
            s = s + s_[0]

        if s_[1] != 0:
            s_[1] -= 1
            continue
                
        if i == ')':
            return [s + operrators[::-1], len(s + operrators[::-1]) + 2]
        # end part working with ctaples

        #start sorting station dijkstra
        try:
            i = int(i)
        except:
            None
        if isinstance(i, int):
            s.append(i)
            
        if i in (first + second):
            if len(operrators) == 0 or lavel(i) > lavel(operrators[-1]):
                operrators.append(i)
            else:
                print(operrators)
                print('our list', s)
                s.reverse()
                print('our reversed list', s)
                for j in range(0, len(operrators) - 1, -1):
                    s.append(operrators[j])
                    operrators.pop(j)
                s.reverse()
                print('our list', s)
                operrators.append(i)
    s = s + operrators
    # print("function done checkpoint")
    #end sorting station dijkstra
    return s

a = input()
print(polska(a))
print("after polska function done")
