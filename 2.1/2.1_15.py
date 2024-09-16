ch = int(input())
mn = int(input())
vo = int(input())
fch = vo // 60
fmn = vo % 60
ch2 = fch % 24
m = (fmn + mn) % 60
hh = (fmn + mn) // 60
c = (ch2 + ch) % 24
if (c + hh) < 24:
    t1 = str(c + hh)
else:
    t1 = str(c + hh - 24)
t2 = str(m)
if len(t1) == 1:
    t1 = "0" + t1
if len(t2) == 1:
    t2 = "0" + t2
print(t1, ":", t2, sep='')
