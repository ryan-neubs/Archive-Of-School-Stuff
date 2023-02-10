# gui.py


import tkinter as tk
import sys
sys.path.insert(0, '..')  # fix to allow imorts from paystation module

from paystation.domain import (PayStation,
                               AlphaTownFactory,
                               BetaTownFactory,
                               GammaTownFactory,
                               TripoliFactory
                               )

from paystation.guiview import PayStationGUIview

# Configuration of PayStations to appear in the GUI
FACTORIES = [AlphaTownFactory(), BetaTownFactory(),
             GammaTownFactory(), TripoliFactory()]


class MultiPayStationModel:
    """ Model for PayStationGUIApp"""


class PayStationGUIApp:
    """ Presenter for the PayStation GUI """

    def __init__(self, root, model, view):
        self.root = root
        self.model = model
        self.view = view

    def run(self):
        self.root.title("Paystation Simulator")
        self.root.deiconify()
        self.root.mainloop()


def main():
    root = tk.Tk()
    view = PayStationGUIview(root)
    model = MultiPayStationModel()
    for factory in FACTORIES:
        model.add_paystation(factory)
    PayStationGUIApp(root, model, view).run()


if __name__ == "__main__":
    main()
