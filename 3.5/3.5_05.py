from sys import stdin

lines, m = [], []
for line in stdin:
    lines.append(line.rstrip("\n"))
for line in lines:
    [m.append(i) for i in line.split() if i.lower() == i.lower()[::-1]]
print("\n".join(sorted(set(m))))