list = {}

while True:
    try:
        product = input().upper()
        if product in list:
            list[product] += 1
        else:
            list[product] = 1
    except(EOFError):
        for i in sorted(list.keys()):
            print(list[i], i)
        break
