m, n = int(input()), int(input())
print(", ".join([str(x) for x in range(n, m + 1, (n - m) % 10)]))
