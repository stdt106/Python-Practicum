d = input()
y = 0
x = 0
n = int(input())
while d != "СТОП":
    if d == "СЕВЕР" or d == "ЮГ":
        if d == "СЕВЕР":
            y += n
        if d == "ЮГ":
            y -= n
    if d == "ВОСТОК" or d == "ЗАПАД":
        if d == "ВОСТОК":
            x += n
        if d == "ЗАПАД":
            x -= n
    d = input()
    if d == "СТОП":
        break
    n = int(input())
print(y)
print(x)
