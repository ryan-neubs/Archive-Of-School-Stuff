#ElapsedDays.py
#by Ryan Neubauer
#This program tells you the amount of days between your birthday and a given date.


from dates2 import *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

def main():
    print("This program calculates the amount of days between your birthday and the current date.")
    print()
    
    date1 = str(input("Please enter your birth date in the format of MM/DD/YYYY ===> "))
    date2 = str(input("Please enter the current date in the format of MM/DD/YYYY ===> "))
    day1, month1, year1 = unpack_date(date1)
    day2, month2, year2 = unpack_date(date2)
    
    if elapsed_days(day1, month1, year1, day2, month2, year2) == False:
        print()
        print("An error has occured: Please make sure the date is valid and comes after the birth date.")
        
    else:
        print()
        print("There are", elapsed_days(day1, month1, year1, day2, month2, year2), "day(s) between", date1, "and", date2 + ".")

    print()
    choice = str(input("Would you like to enter a new date? Type 'Yes' to continue or press [Enter] to quit: "))
    print()
    if choice == "Yes":
        main()
    
main()
