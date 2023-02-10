# dates2.py
# library of useful functions on dates
# by Ryan Neubauer

def unpack_date(datestr):
    """ get day, month, and year from datestr
    
    pre: datestr is in form 'month/day/year'
    post: returns day, month, year as ints
    """

    month, day, year = datestr.split("/")
    return int(day), int(month), int(year)


def pack_date(day, month, year):
    """produce date as a string
    
    post: returns string in form 'month/day/year'
    """

    return "{}/{}/{}".format(month, day, year)


def is_leap_year(year):
    """ determine whether year is a leap year
    
    pre: year is an int representing a year
    post: returns True if year is a leap year, False otherwise.
    """
    return (year % 400 == 0
            or (year % 4 == 0 and year % 100 != 0))

def month_lengths(year):
    """ construct a list of month lengths
    pre: year is an int
    post: returns a list, lengths, where lengths[month] is the number of
    days in that month of year
    """
    if is_leap_year(year):
        return [31, 29, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]
    
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_in_month(month, year):
    """return number of days in a given month of a year
    
    pre: month is an int representing a valid month number
         and year is an int representing the year (e.g. 2021).
    post: returns an int of the number of days in the month
    """
    assert month in range(1,13)
    return month_lengths(year)[month - 1]


def is_valid_date(day, month, year):
    """determine whether date is valid

    pre: day, month, and year are ints
    post: returns True if values indicate a legal date, 
          False otherwise.
    """

    return ( 1 <= month <= 12
            and 1 <= day <= days_in_month(month, year)
            and year > 1582)  
# dates2.py
# by Ryan Neubauer
def days_in_year(year):
    """return the number of days in year
    
    pre: year is an int representing a year (e.g. 2021)
    post: returns an int of the number of days in year
    """

    if is_leap_year(year):
        return 366
    return 365 

def day_number(day, month, year):
    """return ordinal day number of date 

    pre: day, month, and year are ints representing a valid date
    post: returns an int representing the "index" of the date in 
          the year. 
    note: January 1st is day 1, January 2nd is day 2, etc.
    """

    days = day
    for m in range(1, month):
        days += days_in_month(m, year)
    return days

def elapsed_days(day1, month1, year1, day2, month2, year2):
    """return the interval between two dates, in days

    pre: day1, month1, year1 are ints representing a valid date (date1)
         day2, month2, year2 are ints representing a valid date (date2)
         date2 comes after date1
    post: returns the number of days between the dates.
    note: for consecutive days, the answer is 1.
    """

    days = day_number(day2, month2, year2) - day_number(day1, month1, year1)
    for year in range(year1, year2):
        days += days_in_year(year)
    return days
