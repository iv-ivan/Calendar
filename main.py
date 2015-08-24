from calendar import Calendar

def main():
    with Calendar("data.myCal") as newCal:
        newCal.draw()

main()

