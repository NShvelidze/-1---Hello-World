def insert_coin():

    amount_due = 50
    change_owed = 0
    print("Amount Due:",amount_due)
    while True:
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount_due -= coin
            if amount_due < 0:
                change_owed = amount_due + coin
                print("Change Owed:", change_owed)
                break
            elif amount_due == 0:
                 change_owed = 0
                 print("Change Owed:", change_owed)
                 break
            print("Amount Due:", amount_due)
        else:
            print("Please inster coin of different value")

insert_coin()
