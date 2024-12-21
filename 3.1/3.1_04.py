a = " "
while a != '':
    a = input()
    if a[len(a) - 3:len(a) + 1] == "@@@":
        continue
    if a[0:2] == "##":
        print(a[2:])
    else:
        print(a)