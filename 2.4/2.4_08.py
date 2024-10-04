n = int(input())
m = []
for i in range(n):
    a = input()
    ch = input()
    m.append(a)
    m.append(ch)
s = sm = 0
ind = ''
for j in range(1, n * 2 + 1, 2):
    s = sum(map(int, m[j]))
    if sm <= s:
        sm = s
        ind = m[j - 1]
print(ind)