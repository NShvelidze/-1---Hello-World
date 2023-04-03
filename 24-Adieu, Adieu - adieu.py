import inflect
name_list = []
p = inflect.engine()

while True:
    try:
        name = input("Name: ")
        name_list.append(name)

    except(EOFError):
        print("")
        print("Adieu, adieu, to", p.join(name_list))
        break
    
