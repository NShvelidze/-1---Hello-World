while True:
        sequence = input("Fraction:")
        try:
            x = sequence.split("/")
            fraction = int(x[0]) / int(x[1])

            if fraction >= 1:
                fraction = int(fraction)
                print("F")
                break
            if fraction < 1 and fraction > 0:
                fraction = float(fraction)
                percentage = "{:.0%}".format(fraction)
                print(percentage)
                break
            if fraction == 0:
                print("E")
                break
        except(ValueError, ZeroDivisionError):
             continue
