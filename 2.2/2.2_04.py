p = int(input())
v = int(input())
t = int(input())
if p > t > v:
    print("1. Петя")
    print("2. Толя")
    print("3. Вася")
if p > v > t:
    print("1. Петя")
    print("2. Вася")
    print("3. Толя")
if t > p > v:
    print("1. Толя")
    print("2. Петя")
    print("3. Вася")
if t > v > p:
    print("1. Толя")
    print("2. Вася")
    print("3. Петя")
if v > p > t:
    print("1. Вася")
    print("2. Петя")
    print("3. Толя")
if v > t > p:
    print("1. Вася")
    print("2. Толя")
    print("3. Петя")