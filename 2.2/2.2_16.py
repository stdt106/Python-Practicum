p = int(input())
v = int(input())
t = int(input())
if p > t > v:
    print("          Петя          ")
    print("  Толя")
    print("                  Вася")
    print("   II      I      III   ")
if p > v > t:
    print("          Петя          ")
    print("  Вася")
    print("                  Толя")
    print("   II      I      III   ")
if t > p > v:
    print("          Толя          ")
    print("  Петя")
    print("                  Вася")
    print("   II      I      III   ")
if t > v > p:
    print("          Толя          ")
    print("  Вася")
    print("                  Петя")
    print("   II      I      III   ")
if v > p > t:
    print("          Вася          ")
    print("  Петя")
    print("                  Толя")
    print("   II      I      III   ")
if v > t > p:
    print("          Вася          ")
    print("  Толя")
    print("                  Петя")
    print("   II      I      III   ")
