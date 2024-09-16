n = input()
c = int(input())
w = int(input())
money = int(input())
p1 = len('================Чек================')
pp1 = p1 - 6 - len(n)
print('================Чек================')
print('Товар:', ' ' * pp1, n, sep='')
pp2 = p1 - 5 - 11 - len(str(c)) - len(str(w))
print('Цена:', ' ' * pp2, w, 'кг * ', c, 'руб/кг', sep='')
pp3 = p1 - 6 - len(str(c * w)) - 3
print('Итого:', ' ' * pp3, c * w, 'руб', sep='')
pp4 = p1 - 8 - len(str(money)) - 3
print('Внесено:', ' ' * pp4, money, 'руб', sep='')
pp5 = p1 - 6 - len(str(money - c * w)) - 3
print('Сдача:', ' ' * pp5, money - c * w, 'руб', sep='')
print('===================================')