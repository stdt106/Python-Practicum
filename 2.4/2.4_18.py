s = ''
f = 0
c = 1
mxln = 0
n = int(input())
for i in range(1, n + 1):
    s += str(i) + " "
    k = len(s.split())
    if c == k:
        c += 1
        s += "\n"
        ln = len(s) - 2
        mxln = max(mxln, ln)
        s = ''
    if n == i and k != i:
        ln = len(s) - 1
        mxln = max(mxln, ln)

s = ''
f = 0
c = 1

for i in range(1, n + 1):
    s += str(i) + " "
    k = len(s.split())
    if c == k:
        c += 1
        s = s[:-1]
        print(f"{s: ^{mxln}}")
        s += "\n"
        s = ''
    if n == i and k != i:
        s = s[:-1]
        print(f"{s: ^{mxln}}")
