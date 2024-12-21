s = " ".join([input()for i in range(int(input()))]).split()
n = int(input())
print("\n".join([f"{x[0]}" for x in list(zip(s * n, [x for x in range(1, n + 1)]))]))