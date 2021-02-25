import tkinter as tk
import paramiko
import math, sys, os
import config


class GroundComputer(tk.Frame):
    host = config.HOST
    port = config.PORT
    username = config.USERNAME
    password = config.PASSWORD

    @classmethod
    def main(cls):
        tk.NoDefaultRoot()
        root = tk.Tk()
        root.title("Ground Computer")
        root.geometry("1100x630+30+30")
        root.configure(bg="#233342")
        cls(root).grid(sticky="nsew")
        root.minsize(1100, 680)
        root.maxsize(1100, 680)
        root.mainloop()

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.connectionButton = StatefulButton(
            self,
            "Initialize Connection",
            self.initialize_connection,
        )
        self.statusLabel = tk.Label(self, text="", fg="red", bg="#233342")

        self.grid_widgets(padx=10, pady=10)

    def grid_widgets(self, **kw):
        self.connectionButton.grid(row=0, column=0, sticky="nsew", **kw)
        self.statusLabel.grid(row=0, column=1, **kw)

    def initialize_connection(self):
        self.connectionButton.configure(state="disabled")
        # command = "cd Desktop/code/python3 main.py"
        command = "ls"
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, self.port, self.username, self.password)
        except SSHExepction:
            statusLabel.configure(text="Error", fg="red", bg="#233342")

        stdin, stdout, stderr = ssh.exec_command(command)
        print("success")
        self.statusLabel.configure(text="Success", fg="green", bg="#233342")


class StatefulButton(tk.Button):
    def __init__(self, master, text, command, **kw):
        kw.update(text=text, command=self.__execute_command)
        super().__init__(master, **kw)
        self.configure(bg="#233342", fg="white")
        self.__command = command

    def __execute_command(self):
        self.__command = self.__command()


if __name__ == "__main__":
    GroundComputer.main()