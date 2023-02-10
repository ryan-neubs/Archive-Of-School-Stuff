# ConvertKm.py
# By Ryan Neubauer
# This program converts Kilometers to Miles



from graphics import *

def main():
    win = GraphWin("Kilometer to Miles", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(1,3), "Distance in kilometers:").draw(win)
    Text(Point(1,1), "     Distance in Miles:").draw(win)
    inputText = Entry(Point(2.25,3), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25,1),"")
    outputText.draw(win)
    button = Text(Point(1.5,2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Conversion to Miles
    kilometers = float(inputText.getText())
    miles = kilometers * 0.62

    # Display output and change button
    outputText.setText(round(miles,2))
    button.setText("Quit")

    # Mouseclick to quit
    win.getMouse()
    win.close()


main()
