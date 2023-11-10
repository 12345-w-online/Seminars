import operator


def lavel(a):
    first = ['*', '/']
    second = ['+', '-']
    if a in first:
        return 1
    elif a in second:
        return 0
    
    
def my_list(s, reversed=False):
    my_new_list = []

    mydidgit = ''
    for i in s:
        if i.isdigit():
            mydidgit += i
        else:
            if mydidgit != '':               
                my_new_list.append(int(mydidgit))
                mydidgit = ''

            my_new_list.append(i)

    if mydidgit != '':               
                my_new_list.append(int(mydidgit))   

    if reversed:
        dict_of_caples = {'(': ')',
                          ')': '('
                          }
        
        my_new_list.reverse()
        my_new_list = list(map(lambda x: x if x != '(' and x != ')' else dict_of_caples[x], my_new_list))
    print(my_new_list)
    return my_new_list

            
def polska(a, reversed=False):
    if not(isinstance(a, list)):
        if reversed:
            a = my_list(a)
        else:
            a = my_list(a, reversed=True)
    
    first = ['*', '/']
    second = ['+', '-']
    s = []
    s_ = [0, 0]
    operrators = []

    for i in a:
        
        # start part working with ctaples
        if i == '(':
            s_ = polska(a[a.index('(') + 1::])
            if not(reversed):
                s = s + s_[0] 
            else:
                s = s_[0] + s

        if s_[1] != 0:
            s_[1] -= 1
            continue
                
        if i == ')':
            return [s + operrators[::-1], len(s + operrators[::-1]) + 2]
        # end part working with ctaples

        #start sorting station dijkstra

        if isinstance(i, int):
            s.append(i)
            
        if i in (first + second):
            if len(operrators) == 0 or lavel(i) > lavel(operrators[-1]):
                operrators.append(i)
            else:
                print(operrators)
                for j in range(len(operrators) - 1, -1, -1):
                    s.append(operrators[j])
                    operrators.pop(j)
                operrators.append(i)
    s = s + operrators
    # print("function done checkpoint")
    #end sorting station dijkstra

    print(reversed)
    if not(reversed):
        s.reverse()
    
    return s


def stack_calculation(iterable_list:'str'):
    ops = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv,  # use operator.div for Python 2
                '%': operator.mod,
                '^': operator.xor,
            }
    
    if not(isinstance(iterable_list, list)):
        iterable_list = list(iterable_list)

    my_stack = ['error']
    for elem in iterable_list:
        if elem.isdigit():
            my_stack.append(elem)
        else:
            if my_stack[-2] != 'error':
                a = my_stack.pop(-1)
                b = my_stack.pop(-1)    
                my_stack.append(ops[elem](int(b), int(a)))
            else:
                return 'error'

    return my_stack[-1]


a = input()
print(polska(a, reversed=True))
print("after polska function done")

b = input()
print(stack_calculation(b))
