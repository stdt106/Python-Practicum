with open("numbers.num", "rb") as f:
    rec = f.read()
print(sum([int.from_bytes(rec[i:i + 2], "big") for i in range(0, len(rec), 2)]) % 2 ** 16)