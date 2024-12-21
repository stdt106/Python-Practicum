ll = set()
el = set()
m = []
for i in range(n := int(input())):
    ll.add(input())
for i in range(int(input())):
    el.add(e := input())
    c = 0
    for j in range(s := int(input())):
        if (f := input()) in ll:
            c += 1
        else:
            c = 0
    if c == s:
        m.append(e)
if m:
    print("\n".join(sorted(m)))
else:
    print("Готовить нечего")