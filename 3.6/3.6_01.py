n = int(input())
for _ in range(n):
    s, a, b = input().split('^')
    a = int(a)
    b = int(b)
    if len(s) % 4 != 0:
        sh = len(s) % 4
    else:
        sh = 4
    print(s[a:b:sh])