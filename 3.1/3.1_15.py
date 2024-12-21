a = input()
a = a.split(' ')
a = sorted(list(map(int, a)))
for i in range(a[0], 0, -1):
    c = 0
    for j in a:
        if j % i == 0:
            c += 1
    if c == len(a):
        print(i)
        break
