# month2.py
# A program to print the month abbreviation, given its number.
# by Ryan Neubauer

def main():
    # months is a list used as a lookup table
    months = ["January", "February", "March", "April", "May", "June",
            "  July", "August", "September", "October", "November", "December"]
    abbrv = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "  Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = int(input("Enter a month number (1-12): "))

    print("The month is", months[n-1] + ".")
    print("The abbreviation for the month is", abbrv[n-1] + ".")


main()
