# convert2.py

def to_fahrenheit(c):
    return 9/5 * c + 32

def main():
    celsius = float(input("Enter Celsius Temp: "))
    fahrenheit = to_fahrenheit(celsius)
    print("The temp is,", to_fahrenheit(celsius),"F.")
    
    if fahrenheit > 85:
        print("Warning, it's hot out there!")

    if fahrenheit < 40:
        print("Bundle up! It's cold out there.")

main()
