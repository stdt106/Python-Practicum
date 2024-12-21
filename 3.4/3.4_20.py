from itertools import product

text = input().replace('(', '( ').replace(')', ' )')
p = [x for x in sorted(set(text.split())) if x.isupper()]
count = len(p)
text = text.replace('( ', '((((').replace(' )', '))))')
text = '(((' + text.replace('~', '))) == (((') + ')))'
text = '((' + text.replace('->', ')) <= ((') + '))'
text = '(' + text.replace('^', ') != (') + ')'
print(' '.join(p), 'F')
for i in product([0, 1], repeat=count):
    d = {k: v for (k, v) in zip(p, i)}
    print(' '.join([str(var) for var in i]), int(eval(text, d)))