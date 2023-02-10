# convet.py
# A program to convert Celsius to Farenheit
# by: Susan Computewell

def main():
    print("This program converts Celsius to Fahrenheit")
    celsius = eval(input("Enter temp in degrees Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit")
    input("Press <Enter> to quit.")

main()
