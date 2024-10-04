i = input()
n = 0
while i != "Приехали!":
    if "зайка" in i:
        n += 1
    i = input()
print(n)