symbol = input("Write any text: ")
symbol = symbol.replace(" ","")  #if you need to count a text length without whitespace's

if len(symbol) == 0:
    print("please write at last one symbol")
else:
    print(len(symbol))
