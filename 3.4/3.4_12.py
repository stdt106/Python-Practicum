n = sorted(" ".join([input() for _ in range(int(input()))]).replace(",", "").split())
print("\n".join([f"{i}. {j}" for i, j in enumerate(n, 1)]))