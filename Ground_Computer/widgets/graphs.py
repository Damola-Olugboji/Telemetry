import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk


class RealtimeSensorGraph(tk.Frame):
    def __init__(self,parent, ouputLabel, outputUnit, data):
        tk.Frame.__init__(self, parent)
        
        f = Figure(figsize = (1,1), dpi = 100)
        a = f.add_subplot(211)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        

    def animate(i):
        pullData = open("sampleText.txt","r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xList.append(int(x))
                yList.append(int(y))

        a.clear()
        a.plot(xList, yList)



    
