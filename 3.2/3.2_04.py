n, m = int(input()), int(input())
nn = []
mm = []
c = 0
for i in range(n + m):
    if i < n:
        nn.append(input())
    else:
        mm.append(input())
for i in nn:
    for j in mm:
        if i == j:
            c += 1
if c == 0:
    print("Таких нет")
else:
    print(c)