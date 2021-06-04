import tkinter as tk
from tkinter import ttk
import threading
from widgets.graphs import RealtimeSensorGraph
from widgets.connectionPage import ConnectionPage


def quit():
    root.quit()


class TUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.graphButton = tk.Button(
            self, text="Graph", width=20, command=self.graphPage
        )
        self.exitButton = tk.Button(
            self, text="Exit", fg="white", bg="red", width=20, command=quit
        )
        self.statusLabel = tk.Label(self, text=" ")
        # self.display.grid(column = 0, row =1)
        self.attributeLabel = [
            "time",
            " latitude",
            "longitude",
            "altitude",
            "temperature",
            "accx",
            "accy",
            "accz",
            "pressure",
            "humidity",
        ]
        self.attributeUnit = [
            "unix",
            "",
            "",
            "meters",
            "celcius",
            "m/s^2",
            "m/s^2",
            "m/s^2",
            "pascal",
            "g/m^3",
        ]
        self.connectionFrame = ConnectionPage(self)

        self.grid_widgets()

    def grid_widgets(self):

        self.outputLabel = [None] * len(self.attributeLabel)
        self.outputTextbox = [None] * len(self.attributeLabel)

        self.graphButton.grid(column=0, row=0, pady=5)
        self.exitButton.grid(column=1, row=0, pady=5)
        self.statusLabel.grid(column=2, row=9, pady=5)
        self.connectionFrame.grid(
            column=5, row=1, rowspan=5, pady=(40, 0), padx=(30, 0)
        )

        for i in range(0, len(self.attributeLabel)):
            self.outputLabel[i] = tk.Label(
                self,
                fg="black",
                text=self.attributeLabel[i] + " (" + self.attributeUnit[i] + ")",
                font=("Times New Roman", 12),
            )
            self.outputTextbox[i] = tk.Label(
                self, bg="black", fg="#008000", width=20, height=3, text="Nan"
            )

            if i >= 3 and i < 6:
                self.outputLabel[i].grid(
                    column=i - 3, row=3, sticky="w", padx=(25, 5), pady=(5, 0)
                )
                self.outputTextbox[i].grid(
                    column=i - 3, row=4, sticky="w", padx=(25, 15), pady=(5, 0)
                )
                continue
            if i >= 6 and i < 9:
                self.outputLabel[i].grid(
                    column=i - 6, row=5, sticky="w", padx=(25, 5), pady=(5, 0)
                )
                self.outputTextbox[i].grid(
                    column=i - 6, row=6, sticky="w", padx=(25, 15), pady=(5, 0)
                )
                continue
            if i >= 9:
                self.outputLabel[i].grid(
                    column=i - 9, row=7, sticky="w", padx=(25, 5), pady=(5, 0)
                )
                self.outputTextbox[i].grid(
                    column=i - 9, row=8, sticky="w", padx=(25, 15), pady=(5, 0)
                )
                continue

            self.outputLabel[i].grid(
                column=i, row=1, sticky="w", padx=(25, 5), pady=(5, 0)
            )
            self.outputTextbox[i].grid(
                column=i, row=2, sticky="w", padx=(25, 15), pady=(5, 0)
            )

    def graphPage(self):
        pass
        graph_page = tk.Toplevel(self)
        graph_page.geometry("1100x700")
        graph_page.title("Sensor Graphs")

        exitButton = tk.Button(
            graph_page,
            text="exit",
            command=graph_page.destroy,
            fg="white",
            bg="red",
            width=20,
        )
        exitButton.grid(column=0, row=0, pady=25)

        widgets = [None] * len(self.attributeLabel)
        for i in range(0, len(widgets)):
            widgets[i] = RealtimeSensorGraph(
                graph_page, self.attributeLabel[i], self.attributeUnit[i], 0
            )
            if i >= 3 and i < 6:
                widgets[i].grid(column=1, row=i - 2, padx=(20, 0))
                continue
            if i >= 6 and i < 9:
                widgets[i].grid(column=2, row=i - 5, padx=(20, 0))
                continue
            if i > 9:
                widgets[i].grid(column=3, row=i - 8, padx=(20, 0))
                continue
            widgets[i].grid(column=0, row=i + 1, padx=(20, 0))

        graph_page.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(1100, 700)
    root.maxsize(1100, 700)
    root.title("Ground Computer")
    TUI(root).pack(side="top", fill="both", expand=True)
    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(1, weight=0)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    # root.bind('<Control-q>', quit)
    root.mainloop()
