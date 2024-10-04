def prime(y):
    if y == 1:
        return False
    if y == 2:
        return True
    for i in range(2, int(y ** 0.5) + 1):
        if y % i == 0:
            return False
    return True


c = 0
n = int(input())
for i in range(n):
    a = int(input())
    if prime(a):
        c += 1
print(c)