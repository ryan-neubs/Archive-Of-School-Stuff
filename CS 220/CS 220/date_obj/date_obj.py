# library of useful functions and objects for dates

class Date:

    def __init__(self, datestr):
        """ create a date from month/day/year string
            post: creates a valid date object with int attributes
                  day, month, and year. Raises an exception if
                  datestr is ill-formed or an invalid date.
        """
        self.month, self.day, self.year = datestr.split("/")
        self.month, self.day, self.year = int(self.month), int(self.day), int(self.year)
        
        

    def _is_valid_date(self):
        """determine whether date is valid

        post: returns True self is a legal date, False otherwise.
        """
        return ( 1 <= self.month <= 12
            and 1 <= self.day <= days_in_month(self.month, self.year)
            and self.year > 1582)

    def __str__(self):
        """produce date as a string

        post: returns string in form 'month/day/year'
        """

        return "{}/{}/{}".format(self.month, self.day, self.year)
        
    def day_number(self):
        """return ordinal day number of date

        post: returns an int representing the "index" of the date in
              the year.
        note: January 1st is day 1, January 2nd is day 2, etc.
        """

        days = self.day
        for m in range(1, self.month):
            days += days_in_month(m, self.year)
        return days

    def __sub__(self, other):
        """return the interval between two dates, in days

        pre: other is a Date preceeding self.
        post: returns the number of days between the dates.
        note: for consecutive days, the answer is 1.
        """
        
        days = other.day_number() - self.day_number()
        for year in range(self.year, other.year):
            days += days_in_year(year)
        assert days > 0, "2nd date does not preceed birth date"
        return days
        

def is_leap_year(year):
    """ determine whether year is a leap year

    pre: year is an int representing a year
    post: returns True if year is a leap year, False otherwise.
    """
    return (year % 400 == 0
            or (year % 4 == 0 and year % 100 != 0))


def _month_lengths(year):
    """ construct a list of month lengths
    pre: year is an interval
    post: returns a list, lengths, where lengths[month] is the number of
          days in that month of year
    """

    lengths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        lengths[2] += 1
    return lengths


def days_in_month(month, year):
    """return number of days in a given month of a year

    pre: month is an int representing a valid month number
         and year is an int representing the year (e.g. 2021).
    post: returns an int of the number of days in the month
    """
    assert month in range(1, 13)
    return _month_lengths(year)[month]


def days_in_year(year):
    """return the number of days in year

    pre: year is an int representing a year (e.g. 2021)
    post: returns an int of the number of days in year
    """
    if is_leap_year(year):
        return 366
    return 365


def main():
    print("This program computes age in days.")

    birthday = Date(input("\nEnter a date of birth (month/day/year): "))
    today = Date(input("Enter today's date (month/day/year): "))

    print("\nif", birthday, "is your date of birth, and today is", today)
    print("then you are", birthday.__sub__(today), "days old.")


if  __name__ == "__main__":
    main()
