# Class:        cse 111
# Group:        TEAMS GRP 19 (Wed 8pm MT)
# Date:         2024-23-10
# Descritpion:  Creating a UI using Tkinter to take input and calculate a result

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry
import math

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a Circle - Team 19")
    frm_main.pack(padx=2, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):

    # Line 1
    description = Label(frm_main, text="Calculate the area of a circle")

    # Line 2
    r = Label(frm_main , text="Enter radius cm (0.1 - 100.0):" )

    # Line 2 - Entry Box
    # Create an integer entry box where the user will enter her age.
    radius_ent = FloatEntry(frm_main, width=8, lower_bound=0.1, upper_bound=100)

    # Line 2
    measurment_type = Label(frm_main , text="(cm)" )

    # Line 3
    area_lbl = Label(frm_main , text="Area:" )

    # Line 3
    area = Label(frm_main, width=5)

    # Line 3
    cm_value = Label(frm_main, text="cm^2")

    # Clear Button
    btn_clear = Button(frm_main, text="Clear")

    description.grid( row=0, column=0, padx=3, pady=3)
    r.grid(row=1, column=0, padx=0, pady=3)
    radius_ent.grid(row=1,column=1, padx=10, pady=3)
    measurment_type.grid(row=1,column=2, padx=3, pady=3)
    area_lbl.grid(row=2,column=0, padx=3, pady=3)
    area.grid(row=2,column=1, padx=3, pady=3)
    cm_value.grid(row=2,column=2, padx=3, pady=3)

    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    def get_area(event):

        try:
            # Get the user's age.
            rad = radius_ent.get()

            # Compute the user's maximum heart rate.
            a = math.pi * ( rad**2 )

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            area.config(text=f'{a:.2f}')

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            area.config(text='')

    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        radius_ent.clear()
        area.config(text="")
        radius_ent.focus()

    radius_ent.bind("<KeyRelease>", get_area)
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    radius_ent.focus()



# If this file is executed like this:
# > python area_calculate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
