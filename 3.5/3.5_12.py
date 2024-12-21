ff, sf, tf, lf = input(), input(), input(), input()
f1, f2, f3 = '', '', ''
with open(ff, encoding='UTF-8') as ff:
    for ln in ff:
        l1 = [i for i in ln.split() if sum(int(k) % 2 == 0 for k in i) > sum(int(j) % 2 != 0 for j in i)]
        f1 += ' '.join(l1) + '\n'
        l2 = [i for i in ln.split() if sum(int(k) % 2 == 0 for k in i) < sum(int(j) % 2 != 0 for j in i)]
        f2 += ' '.join(l2) + '\n'
        l3 = [i for i in ln.split() if sum(int(k) % 2 == 0 for k in i) == sum(int(j) % 2 != 0 for j in i)]
        f3 += ' '.join(l3) + '\n'
with open(sf, "w", encoding='UTF-8') as sf:
    sf.write(f1)
with open(tf, "w", encoding='UTF-8') as tf:
    tf.write(f2)
with open(lf, "w", encoding='UTF-8') as lf:
    lf.write(f3)