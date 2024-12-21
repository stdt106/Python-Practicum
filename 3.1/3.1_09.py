a = input()
while a != '':
    if a.find("#") == 0:
        ...
    elif "#" in a:
        print(a[:(a.find("#"))])
    else:
        print(a)
    a = input()