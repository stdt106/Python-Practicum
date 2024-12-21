tbl = {}
for i in range(n := int(input())):
    name, kasha = input().replace(' ', '*', 1).split("*")
    tbl[name] = kasha
want = input()
if ("\n".join(sorted([name for name, kasha in tbl.items() if want in kasha]))) == "":
    print("Таких нет")
    exit(0)
print("\n".join(sorted([name for name, kasha in tbl.items() if want in kasha])))
