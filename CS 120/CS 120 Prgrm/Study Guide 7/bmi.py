# bmi.py
def bmi(weight, height):
    
    return weight*720 / height**2

def bmirange(bmi):
    
    if 26 > bmi > 18:
        return "in"
    elif bmi < 19:
        return "below"
    elif bmi > 25:
        return "above"
    
    # Returns "above", "in", or "below" based on BMI
    
def main():
    
    print("This program evaluates your body mass index (BMI)\n")
    
    weight = float(input("Enter your weight (in pounds): "))
    height = float(input("Enter your height (in inches): "))
    
    index = bmi(weight, height)
    
    print("Your BMI is", index)
    print("You are", bmirange(index), "the healthy range.")
    
    input("\nPress <Enter> to quit.")
    
main()
