n = int(input())
m = int(input())
p = 7
v = 6
p -= 3
v += 3
p += 2
v -= 2
p += n
v += m
if v > p:
    print("Вася")
if p > v:
    print("Петя")