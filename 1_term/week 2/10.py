gl = ['а', 'е', 'и', 'о', 'у', 'ё', 'ю', 'я']

with open('input.txt', 'r+') as f:
    f1 = list(f.readlines())
    print(f1)
    for i in range(len(f1)):
        if (f1[i] in gl and i == 0) or (f1[i] in gl and not(f1[i-1] in gl)):
            f1.insert(i+1,'с' + f1[i])
    print(''.join(f1))