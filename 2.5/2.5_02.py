operation = input()
a, b = int(input()), int(input())
if "sum" in operation:
    print(a + b)
elif "sub" in operation:
    print(a - b)
elif "mult" in operation:
    print(a * b)
elif "div" in operation:
    print(a // b)