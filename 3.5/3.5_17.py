file_in = open("secret", encoding="UTF-8")
for line in file_in:
    for ch in line:
        print(chr(ord(ch) % 128), end="")