a = float(input())
s = 0
while a != 0:
    if a >= 500:
        s += 0.9 * a
    else:
        s += a
    a = float(input())
print(s)