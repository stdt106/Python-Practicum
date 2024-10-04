ch = input()
n = ''
for i in ch:
    if int(i) % 2 != 0:
        n += i
print(n)