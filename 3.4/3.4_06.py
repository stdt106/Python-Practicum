from itertools import product

mast = ["пик", "треф", "бубен", "червей"]
mast.remove(input())
nom = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
print("\n".join(list([f"{x} {y}" for x, y in product(nom, mast)])))
