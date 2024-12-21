n = int(input())
m = []
st = ''
srch = ''
for i in range(n + 1):
    a = input()
    if i == n:
        srch = a
    m.append(a)
m.pop()
for i in range(len(m)):
    if srch.lower() in m[i].lower():
        print(m[i])