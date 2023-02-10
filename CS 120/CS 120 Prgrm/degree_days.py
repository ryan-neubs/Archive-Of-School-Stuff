# degree_days.py
# by Ryan Neubauer


def average(line):
    high, low = line.split()
    high = int(high)
    low = int(low)
    avg_temp = (high + low)/2
    return avg_temp

def main():
    print("This program computes Heating and Cooling Degree Days\nfrom a series of daily high and low temperatures.")
    print("")
    hdd = 0
    cdd = 0
    line = input("Enter the high and low temp for the day (<Enter to quit): ")
    while line != (""):
        avg = average(line)
        if avg < 65:
            hdd = (65 - avg) + hdd
        else:
            cdd = (avg - 65) + cdd
        line = input("Enter the high and low temp for the day (<Enter to quit>): ")
    print("")
    print("Heating Degree Days:", hdd)
    print("Cooling Degree Days:", cdd)
    print("Total Degree Days:", hdd + cdd)
    print("")
    input("Press <Enter> to quit.")


main()


