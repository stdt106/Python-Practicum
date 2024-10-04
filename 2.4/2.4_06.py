n = int(input())
m = []
c = 0
for i in range(n):
    a = int(input())
    m.append(a)
for i in range(mn := min(m), 0, -1):
    c = 0
    for j in m:
        if j % i == 0:
            c += 1
    if c == n:
        print(i)
        break