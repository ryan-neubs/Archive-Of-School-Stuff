# RPNCalculator.py
# by Ryan Neubauer and Gavin Roy

from Stack import *
from string import *

class Calculator:
    
    def __init__(self, userInput):
        self.equation = userInput.split()
        self.stack = Stack()

    def isOperator(self, symbol):
        return (symbol == "-" or symbol == "*" or symbol == "+"
                or symbol == "^" or symbol == "/")

    def isNum(self, num):
        return num.isnumeric()

    def calculate(self, num1, num2, operator):
        _num1 = int(num1)
        _num2 = int(num2)
        
        if operator == '-':
            return _num2 - _num1
        if operator == '*':
            return _num2 * _num1
        if operator == '^':
            return _num2 ** _num1
        if operator == '/':
            return _num2 / _num1
        if operator == '+':
            return _num2 + _num1

    def solve(self):
        try:
            while True:
                if self.isNum(self.equation[0]):
                    self.stack.push(self.equation.pop(0))
                if self.isOperator(self.equation[0]):
                    operator = self.equation.pop(0)
                    num1 = self.stack.pop()
                    num2 = self.stack.pop()
                    calc = self.calculate(num1, num2, operator)
                    self.stack.push(calc)
                if self.stack.isEmpty() or self.equation == []:
                    break
            assert self.stack.size() == 1
            return self.stack.pop()
        except:
            return "ERROR"

def main():
    print("Welcome to RPN Calculator.")
    print("")
    userInput = str(input("Please enter your equation: "))
    while userInput != "":
        equation = Calculator(userInput)
        print("")
        print("The answer is:", equation.solve())
        print("")
        userInput = str(input("Please enter your equation: "))
    print("")
    print("Thank you for using RPN calculator.")

if __name__ == "__main__":
    main()
    
        
            
    
