# futval.py
#  A program to compute the value of an investment
#  Carried multiple years into the future

def main():
    print("This program calculates the future value")
    print("of a multi-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years to invest: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, "years is:", principal)

    input("Press <Enter> to quit.")


main()
