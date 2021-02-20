from tkinter import *
import math, sys, os

root = Tk()
root.title("Flight Computer")
root.geometry("300x300")
root.configure(bg="#233342")


class initialize_connection:
    def __init__(self, num):
        pass


connectionButton = Button(
    root,
    text="Initialize Connection",
    fg="white",
    bg="#B35340",
)
connectionButton.pack(pady=100)

root.mainloop()