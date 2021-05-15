import tkinter as tk



class DisplayBox(tk.Frame):
    def __init__(self, parent, info, output, units):
        tk.Frame.__init__(self, parent)
        if output == "":
            output = "default"
        info += ":"
        outputString = tk.StringVar()
        outputString.set(output)
        self.infoLabel = tk.Label(self, text = info, anchor = 'w',font = ('Times New Roman', 13))
        self.outputInformation = tk.Entry(self, textvariable = outputString, state = tk.DISABLED, width = '10')
        self.unitLabel = tk.Label(self, text = units,font = ('Times New Roman', 13))

        self.infoLabel.grid(column = 0, row = 0, padx = 2.5, pady = 2.5)
        self.outputInformation.grid(column = 1, row =0, padx = 2.5, pady = 2.5)
        self.unitLabel.grid(column = 2, row = 0, padx = 2.5, pady = 2.5)

    def updateInformation(self, new):
        self.outputInformation.configure(text = new)

    def getValue(self):
        return self.output
        