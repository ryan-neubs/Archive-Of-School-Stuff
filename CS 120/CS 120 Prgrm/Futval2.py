# futval_graph2.py

from graphics import *

def main():
    # Introduction
    print("This program plots the growth of a 20-year investment.")

    # Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 21.5, 20400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)
    Text(Point(-1, 12500), '12.5K').draw(win)
    Text(Point(-1, 15000), '15.0K').draw(win)
    Text(Point(-1, 17500), '17.5K').draw(win)
    Text(Point(-1, 20000), '20.0K').draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    # Draw a bar for each subsequent year
    for year in range(1, 21):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()

main()
