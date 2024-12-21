import math
import os


rsm = ["б", "Б", "КБ", "МБ", "ГБ"]
c = 1
file_size = os.path.getsize(input())
while file_size > 1024:
    c += 1
    file_size /= 1024
print(math.ceil(file_size), rsm[c], sep='')