n = int(input())
c = 0
for j in range(n):
    p = input()
    pp = ''
    for i in p:
        pp = i + pp
    if p == pp:
        c += 1
print(c)
