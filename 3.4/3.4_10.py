n = int(input())
print("А Б В")
s = [f"{i} {j} {g}" for i in range(1, n + 1) for j in range(1, n + 1) for g in range(1, n + 1) if i + j + g == n]
print("\n".join(s))