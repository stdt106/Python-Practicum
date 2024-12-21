a = input()
a = a.split(' ')
p = int(input())
s = ''
for i in range(len(a)):
    s += str(int(a[i]) ** p) + " "
print(s)