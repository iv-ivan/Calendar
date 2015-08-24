from calendar import Calendar

def main():
    with Calendar("data.myCal") as newCal:
        newCal.draw()

if __name__ == "__main__":
    main()

