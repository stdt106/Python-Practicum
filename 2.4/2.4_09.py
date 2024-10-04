n = int(input())
m = []
for i in range(n):
    a = input()
    a = max(map(int, a))
    m.append(a)
print(*m, sep='')