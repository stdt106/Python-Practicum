n = int(input())
for i in range(n):
    x = input()
    if "зайка" in x:
        print(x.index("зайка") + 1)
    else:
        print("Заек нет =(")