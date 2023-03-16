def main():
    time = input("what time is it: ")
    time_transform = convert(time)
    if time_transform >= 7 and time_transform <= 8:
        print("breakfast time")
    elif time_transform >= 12 and time_transform <= 13:
        print("lunch time")
    elif time_transform >= 18 and time_transform <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    minute_transform = float(minutes) / 60
    return float(hours) + minute_transform

main()
