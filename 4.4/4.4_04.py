def counter(text):
    d = {}
    for i in text:
        if i not in d:
            if i.isalpha():
                d[i] = text.count(i)
    r = sorted(list((k, v) for k, v in d.items()), key=lambda x: x[0])
    for i in r:
        yield i