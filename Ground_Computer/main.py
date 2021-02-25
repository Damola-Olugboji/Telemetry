from tkinter import *
import paramiko
import math, sys, os
import config

root = Tk()
root.title("Flight Computer")
root.geometry("300x300")
root.configure(bg="#233342")


def initialize_connection():
    connectionButton.configure(state="disabled")
    host = "192.168.1.11"
    port = 22
    username = "pi"
    password = config.PASSWORD

    command = "cd Desktop/code/"
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
    except SSHExepction:
        statusLabel.configure(text="Error", fg="red", bg="#233342")

    stdin, stdout, stderr = ssh.exec_command(command)
    flight_control_screen()


connectionButton = Button(
    root,
    text="Initialize Connection",
    fg="white",
    bg="#B35340",
    command=initialize_connection,
)
connectionButton.pack(pady=100)
statusLabel = Label(text="", bg="#233342")
statusLabel.pack(pady=25)


class flight_control_screen:
    def __init__(self):
        top = Toplevel()
        # app.geometry("1100x630+30+30")
        top.minsize(1100, 680)
        top.maxsize(1100, 680)
    
    def 


root.mainloop()