i = int(input())
n = int(input())
m = []
if i == n:
    print(i)
    exit()
while i <= n:
    m.append(i)
    if i == n:
        print(*m)
        exit()
    i += 1
while i >= n:
    m.append(i)
    if i == n:
        print(*m)
        exit()
    i -= 1