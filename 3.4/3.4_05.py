s = list(input().split() + input().split() + input().split())
for x, y in enumerate(sorted(" ".join([x.replace(",", "") for x in s]).split()), 1):
    print(f"{x}. {y}")