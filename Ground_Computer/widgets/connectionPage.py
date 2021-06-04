import paramiko
import tkinter as tk
import time, os, sys
from paramiko.ssh_exception import (
    BadHostKeyException,
    AuthenticationException,
    SSHException,
)


class ConnectionPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="hostname: ")
        label2 = tk.Label(self, text="port name: ")
        label3 = tk.Label(self, text="username: ")
        label4 = tk.Label(self, text="password: ")
        self.hostnameEntry = tk.Entry(self, width="20")
        self.portEntry = tk.Entry(
            self,
            width="20",
        )
        self.usernameEntry = tk.Entry(
            self,
            width="20",
        )
        self.passwordEntry = tk.Entry(
            self,
            width="20",
        )
        self.var = tk.IntVar()
        self.testBool = tk.Checkbutton(self, text="Check if testing", variable=self.var)
        self.connectionButton = tk.Button(
            self, text="Connect", fg="white", bg="green", command=self.sshconnection
        )
        self.statusLabel = tk.Label(self, text="no connection", fg="red")

        self.portEntry.insert(0, "22")
        self.usernameEntry.insert(0, "pi")
        self.passwordEntry.insert(0, "P962qdjhAymHFZgy")

        self.portEntry.configure(state="readonly")
        self.usernameEntry.configure(state="readonly")
        self.passwordEntry.configure(state="readonly")

        label1.grid(column=0, row=0)
        label2.grid(column=0, row=1)
        label3.grid(column=0, row=2)
        label4.grid(column=0, row=3)
        self.hostnameEntry.grid(column=1, row=0, pady=10)
        self.portEntry.grid(column=1, row=1, pady=10)
        self.usernameEntry.grid(column=1, row=2, pady=10)
        self.passwordEntry.grid(column=1, row=3, pady=10)
        self.testBool.grid(column=1, row=4, pady=10)
        self.connectionButton.grid(column=1, row=5, pady=10)
        self.statusLabel.grid(column=1, row=6, pady=10)

    def sshconnection(self):
        # command = "cd Desktop/code/Telemetry/Raspberry Pi main.py"
        command = "cd Desktop/code/Telemetry/Raspberry Pi main.py"
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                self.hostnameEntry.get(),
                self.portEntry.get(),
                self.usernameEntry.get(),
                self.passwordEntry.get(),
            )
        except:
            self.statusLabel.configure(
                text="Error",
            )

        stdin, stdout, stderr = ssh.exec_command(command)
        try:
            for line in stdout.readlines():
                print(line)
        except (KeyboardInterrupt):
            ssh.close

        self.statusLabel.configure(text="Success", fg="green", bg="#233342")
