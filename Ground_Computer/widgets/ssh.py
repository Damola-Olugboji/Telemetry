import paramiko
import sys

results = []


def sshconnection():
    command = "ls"

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect("192.168.1.13", username="pi", password="P962qdjhAymHFZgy")

    stdin, stdout, stderr = client.exec_command(
        "python Desktop/code/Telemetry/Pi/main.py"
    )
    print(f'STDOUT: {stdout.read().decode("utf8")}')
    print(f"Return code: {stdout.channel.recv_exit_status()}")


sshconnection()
