# library of useful functions on dates
# by Ryan Neubauer

def unpack_date(datestr):
    #get day, month, and year from datestr

    month, day, year = datestr.split("/")
    return int(day), int(month), int(year)


def pack_date(day, month, year):
    #produces date as a string
    
    return "{}/{}/{}".format(month, day, year)


def is_leap_year(year):
    #determines whether year is a leap year
    
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

def days_in_month(month, year):
    #returns number of days in a given month of a year

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if is_leap_year(year):
        return 29
    else:
        return 28

def is_valid_date(day, month, year):
    #determines whether date is valid

    if (day < 1) or (day > 31):
        return False
    elif days_in_month(month, year) <= 31 and month in [1,3,5,7,8,10,12]:
        return True
    elif days_in_month(month, year) <= 30 and month in [4, 6, 9, 11]:
        return True
    elif not(is_leap_year(year)) and day == 29:
        return False
    elif days_in_month(month, year) <= 29 and month == 2:
        return True
    else:
        return False

def days_in_year(year):
    #returns the number of days in the year
    
    if is_leap_year(year):
        return 366
    return 365

def day_number(day, month, year):
    #returns ordinal day number of date 


    if is_valid_date(day, month, year):
        day_num = 0
        month_count = 1
        while month_count != month:
            day_num += days_in_month(month_count, year)
            month_count += 1
        day_num += day
        return day_num

        


def elapsed_days(day1, month1, year1, day2, month2, year2):
    #returns the interval between two dates, in days
    
    if not(is_valid_date(day1,month1,year1)) or not(is_valid_date(day2, month2, year2)) or year2 < year1:
        return False
    else:
        year_count = year1
        days = 0
        while year_count != year2:
            days += days_in_year(year_count)
            year_count += 1
        days += day_number(day2, month2, year2) - day_number(day1, month1, year1)
    if days <= 0:
        return False
    return days
    
    

