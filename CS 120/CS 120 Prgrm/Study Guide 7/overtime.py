# overtime.py
# by Ryan Neubauer
# This program calculates overtime pay

def computepay(hours, rate):
    if hours > 40:
        overtime = (hours - 40) * (rate * 1.5)
        regularhours = 40 * rate
        pay = overtime + regularhours
    else:
        pay = hours * rate

    return pay
    
def main():
    print("This program calculated your weekly pay.\n")
        
    hoursworked = float(input("Enter the number of hours worked: "))
    hourlyrate = float(input("How much to you make per hour? "))
        
    print("\nYour paycheck is:", computepay(hoursworked, hourlyrate))
    input("\nPress <Enter> to quit.")
if __name__ == "__main__":
    main()
