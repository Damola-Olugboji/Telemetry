from tkinter import *
import math, sys, os

root = Tk()
root.title("Flight Computer")
root.geometry("300x300")
root.configure(bg="#233342")


def initialize_connection():
    connectionButton.configure(state="disabled")
    flight_control_screen()


connectionButton = Button(
    root,
    text="Initialize Connection",
    fg="white",
    bg="#B35340",
    command=initialize_connection,
)
connectionButton.pack(pady=100)


class flight_control_screen:
    def __init__(self):
        top = Toplevel()
        # app.geometry("1100x630+30+30")
        top.minsize(1100, 680)
        top.maxsize(1100, 680)


root.mainloop()