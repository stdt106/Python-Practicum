def modern_print(sms):
    global s
    if sms not in s:
        s.add(sms)
        print(sms)


s = set()