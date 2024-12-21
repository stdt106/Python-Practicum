kk = {}
for j in range(int(input())):
    x, y = input().split()
    i = (x[:-1], y[:-1])
    kk[i] = kk.get(i, 0) + 1
print(max(kk.values()))