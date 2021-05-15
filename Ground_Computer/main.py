import tkinter as tk
import threading

from widgets.displayBox import DisplayBox

def quit():
    root.quit()

class TUI(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.initializeConnectionButton = tk.Button(self, text = "Initialize Connection", width = 20)
        self.exitButton = tk.Button(self, text = "Exit", fg= 'white', bg = 'red', width = 15)
        #self.display.grid(column = 0, row =1)
        



        self.grid_widgets()


    
    def grid_widgets(self):
        self.attributeLabel = ["time"," latitude", "longitude", "altitude", "temperature", "accx", "accy", "accz", "pressure", "humidity"]
        self.attributeUnit = ["unix", "", "", "meters", "celcius", "m/s^2", "m/s^2", "m/s^2", "pascal", "g/m^3"]
        self.displayBoxes = [None] * len(self.attributeLabel)
        self.initializeConnectionButton.grid(column = 0, row = 0)
        self.exitButton.grid(column = 1, row = 0)

        for i in range(0, len(self.attributeLabel)):
            self.displayBoxes[i] = DisplayBox(self, self.attributeLabel[i],"" ,self.attributeUnit[i])
            if i >= 3 and i <6 :
                self.displayBoxes[i].grid(row = 2, column = i-3, padx = 10, pady = 10, sticky = 'w')
                continue
            if i >=6:
                self.displayBoxes[i].grid(row = 3, column = i-6, padx = 10, pady = 10, sticky = 'w')
                continue
            if i >=9:
                print("got")
                self.displayBoxes[i].grid(row = 4, column = i-9, padx = 10, pady = 10, sticky = 'w')
                continue

            self.displayBoxes[i].grid(row = 1, column = i, padx = 10, pady = 10, sticky = 'w')



    


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(1100, 700)
    root.maxsize(1100, 700)
    TUI(root).pack(side="top", fill="both", expand=True)
    #root.grid_columnconfigure(0, weight = 1)
    #root.grid_columnconfigure(1, weight = 1)
    #root.grid_columnconfigure(0, weight = 1)
    #root.bind('<Control-q>', quit)
    root.mainloop()
