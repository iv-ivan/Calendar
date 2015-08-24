from calendar import Calendar

def main():
    with Calendar("data.txt") as newCal:
        newCal.draw()

main()

