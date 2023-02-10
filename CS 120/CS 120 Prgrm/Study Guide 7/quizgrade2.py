# quizgrade2.py
def grade(score):
        
    if score == 5:
        return "A"
    elif score == 4:
        return "B"
    elif score == 3:
        return "C"
    elif score == 2:
        return "D"
    elif score < 2:
        return "F"
    
def main():
    print("Quiz Grader")
        
    s = int(input("Enter the score (0--5): "))
    print("Grade:", grade(s))
        
    input("\nPress <Enter> to quit.")
        
if __name__ == "__main__":
    main()
