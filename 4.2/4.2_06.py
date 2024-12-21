def order(*drink):
    global in_stock
    f = 0
    for ord in drink:
        if ord == "Эспрессо":
            if in_stock["coffee"] >= 1:
                in_stock["coffee"] -= 1
                return "Эспрессо"
            else:
                f += 1
        if ord == "Капучино":
            if in_stock["coffee"] >= 1 and in_stock["milk"] >= 3:
                in_stock["coffee"] -= 1
                in_stock["milk"] -= 3
                return "Капучино"
            else:
                f += 1
        if ord == "Макиато":
            if in_stock["coffee"] >= 2 and in_stock["milk"] >= 1:
                in_stock["coffee"] -= 2
                in_stock["milk"] -= 1
                return "Макиато"
            else:
                f += 1
        if ord == "Кофе по-венски":
            if in_stock["coffee"] >= 1 and in_stock["cream"] >= 2:
                in_stock["coffee"] -= 1
                in_stock["cream"] -= 2
                return "Кофе по-венски"
            else:
                f += 1
        if ord == "Латте Макиато":
            if in_stock["coffee"] >= 1 and in_stock["milk"] >= 2 and in_stock["cream"] >= 1:
                in_stock["coffee"] -= 1
                in_stock["milk"] -= 2
                in_stock["cream"] -= 1
                return "Латте Макиато"
            else:
                f += 1
        if ord == "Кон Панна":
            if in_stock["coffee"] >= 1 and in_stock["cream"] >= 1:
                in_stock["coffee"] -= 1
                in_stock["cream"] -= 1
                return "Кон Панна"
            else:
                f += 1
    if len(drink) == f:
        return "К сожалению, не можем предложить Вам напиток"