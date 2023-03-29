month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").title()
        if "/" in date:
            date_month,date_day,date_year = date.split("/")
            if int(date_month) < 13 and int(date_day) < 32:
                if int(date_month) < 10:
                    date_month = date_month.zfill(2)
                if int(date_day) < 10:
                    date_day = date_day.zfill(2)
                print(date_year,date_month,date_day, sep = "-")
                break
        if "," in date:
            date = date.replace(",","")
            date_month,date_day,date_year = date.split(" ")
            if int(date_day) < 32:
                if date_month in month:
                    date_month = month.index(date_month)
                    date_month = int(date_month) + 1
                    date_month = str(date_month)
                if int(date_month) < 10:
                    date_month = date_month.zfill(2)
                if int(date_day) < 10:
                    date_day = date_day.zfill(2)
                print(date_year,date_month,date_day, sep = "-")
                break
    except(ValueError):
        break
