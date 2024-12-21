from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
for line in lines:
    if line[0] == "#":
        pass
    elif "#" in line:
        slice = line.find("#")
        line = line[:slice]
        print(line)
    else:
        print(line)