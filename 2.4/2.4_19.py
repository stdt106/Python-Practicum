s = int(input())
q = [[0] * s for _ in range(s)]
for ch in range((s + 1) // 2):
    for i in range(ch, s - ch):
        q[ch][i] = ch + 1
    for i in range(ch + 1, s - ch):
        q[i][s - ch - 1] = ch + 1
    for i in range(ch, s - ch):
        q[s - ch - 1][s - i - 1] = ch + 1
    for i in range(ch + 1, s - ch - 1):
        q[s - i - 1][ch] = ch + 1
max_s = (s + 1) // 2
w = len(str(max_s))
for r in q:
    print(" ".join(f"{num: >{w}}" for num in r))