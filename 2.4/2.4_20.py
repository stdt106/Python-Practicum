def f(n):
    m = 0
    b = 2
    for k in range(2, 11):
        d = []
        t = n
        while t > 0:
            d.append(t % k)
            t //= k
            s = sum(d)
            if s > m:
                m = s
                b = k
    return b


n = int(input())
print(f(n))

