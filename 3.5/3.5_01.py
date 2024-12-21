from sys import stdin

text = stdin.read()
print([f"{x[0]}" for x in text.split()])