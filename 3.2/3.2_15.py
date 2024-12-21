m = []
for i in (s := input().split()):
    d = {}
    bin_digit = bin(int(i))[2:]
    d["digits"] = len(bin_digit)
    d["units"] = bin_digit.count("1")
    d["zeros"] = bin_digit.count("0")
    m.append(d)
print(m)