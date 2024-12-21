from itertools import permutations

s = sorted([x for x in " ".join([input() for _ in range(int(input()))]).replace(",", "").split()])
print("\n".join([" ".join(x) for x in list((permutations(s, 3)))]))