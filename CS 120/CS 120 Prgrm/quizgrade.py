# quizgrade.py

def grade(score):
    letter_grade = "FFDCBA"[score]
    return letter_grade

def main():
    print("Quiz Grader")

    s = int(input("Enter score (0-5): "))
    print("Grade:", grade(s))

main()
input("Press <Enter> to quit.")
