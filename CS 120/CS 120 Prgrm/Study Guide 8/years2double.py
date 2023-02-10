# years2double.py
# by Ryan Neubauer

principal = 1

interest = float(input("Enter the annual interest as a decimal number: "))
bal = 1


year = 0
while bal < 2 * principal:
    bal = bal * (1 + interest)
    year = year + 1

print("The time it will take for this investment to double at this interest rate is", year, "years.")
input("Press <Enter> to quit.")
