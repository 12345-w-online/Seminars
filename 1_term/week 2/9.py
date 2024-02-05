with open('input.txt','r') as f:
    f1 = f.readlines()
deli = [".", "!", "?"]
f1 = ''.join(f1.split())
for i in deli:
    f1 = ' '.join(f1.split(i))

print(len(f1.split()))