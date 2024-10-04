s = int(input())
w = int(input())


def c(s, w):
    return '-' * (s * (w + 1) - 1)


for i in range(1, s + 1):
    if i > 1:
        print(c(s, w))
    row = '|'.join(f"{i * j:^{w}}" for j in range(1, s + 1))
    print(row)
