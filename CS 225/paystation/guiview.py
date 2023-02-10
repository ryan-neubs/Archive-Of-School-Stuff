# guiview.py

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


class PayStationGUIview:

    def __init__(self, parent=None):
        self.parent = parent
        frame = ttk.Frame(parent)
        frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.variant_selector = ttk.Menubutton(frame,
                                               text="Variant Selection")
        self.variant_selector.grid(row=0, column=0, columnspan=4,
                                   sticky=(tk.W, tk.E))
        self.variant_menu = tk.Menu(self.variant_selector, tearoff=0)
        self.variant_selector["menu"] = self.variant_menu

        self.b_5_c = ttk.Button(frame, text="5 c")
        self.b_5_c.grid(row=1, column=4, sticky=(tk.E), pady=5, padx=5)
        self.b_10_c = ttk.Button(frame, text="10 c")
        self.b_10_c.grid(row=2, column=4, sticky=(tk.E), pady=5, padx=5)
        self.b_25_c = ttk.Button(frame, text="25 c")
        self.b_25_c.grid(row=3, column=4, sticky=(tk.E), pady=5, padx=5)

        self.b_cancel = ttk.Button(frame, text="Cancel")
        self.b_cancel.grid(row=4, column=1, pady=3, padx=5)
        self.b_buy = ttk.Button(frame, text="Buy")
        self.b_buy.grid(row=4, column=3, pady=3, padx=5)

        self.display = ttk.Label(frame, text="0030",
                                 font=("sans", 40),
                                 relief="sunken",
                                 anchor=tk.CENTER)
        self.display.grid(row=1, column=0,
                          columnspan=4, rowspan=3,
                          padx=5, pady=5,
                          sticky="nesw")
        self._configure_buttons()

    def _configure_buttons(self):
        # example button configuration
        self.b_5_c["command"] = lambda: self._controller.coin(5)

    def set_labels(self, labels):
        # This one is complete because it was "tricky."
        menu = self.variant_menu
        for label in labels:
            def command(label=label):
                self.controller.select_paystation(label)
            menu.add_command(label=label, command=command)

    def set_state(self, state):
        # example setting widget state

        if state["accept_select_paystation"]:
            self.variant_selector["state"] = "normal"
        else:
            self.variant_selector["state"] = "disabled"

    def show_receipt(self, receipt, id=None):
        # completed for visual test
        win = tk.Toplevel()     # create new top-level window
        win.geometry("500x180")
        win.title("Receipt")
        frame = ttk.Frame(win)
        frame.grid()
        msg = ttk.Label(frame, text=receipt,
                        font=("courier", 12), justify=tk.LEFT)
        msg.grid(row=0)
        ttk.Button(win, text="OK", command=win.destroy).grid(row=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PayStation GUI Visual Test")
    view = PayStationGUIview(root)
    view.set_labels(["Alphatown", "Betatown"])
    receipt_lines = ["-"*50]*6
    receipt = "\n".join(receipt_lines)
    view.show_receipt(receipt)
    root.mainloop()
