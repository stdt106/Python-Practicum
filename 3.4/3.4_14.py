from itertools import permutations

s = sorted([input() for _ in range(int(input()))])
print("\n".join(", ".join(j) for j in [x for x in list(permutations(s, 3))]))