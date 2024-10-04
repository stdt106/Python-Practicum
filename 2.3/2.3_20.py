n = int(input())
h = [0] * (n + 1)
c = 0
for i in range(1, n + 1):
    b = int(input())
    m = b // 256 ** 2
    r = (b // 256) % 256
    h[i] = b % 256
    if h[i] == (37 * (m + r + h[i - 1])) % 256 and h[i] < 100:
        h[i] = (37 * (m + r + h[i - 1])) % 256
    else:
        c = i
        print(i - 1)
        break
if c == 0:
    print(-1)