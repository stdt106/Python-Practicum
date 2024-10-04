a = int(input())
m = []
for i in range(2, a + 2):
    while a % i == 0:
        a = a // i
        m.append(i)
        m.append("*")
m.pop(-1)
print(*m)