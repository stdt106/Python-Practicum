from itertools import combinations

print("\n".join([f"{x[0]} - {x[1]}" for x in combinations([input() for _ in range(int(input()))], 2)]))