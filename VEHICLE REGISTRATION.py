from tkinter import *
from tkinter import messagebox
from tkinter import ttk

VRegistration = []

class Vehicles:

    def __init__(self, platenum, enginenum, chassisnum, maker, series, modyear, weight):
        self.platenum = platenum
        self.enginenum = enginenum
        self.maker = maker
        self.series = series
        self.modyear = modyear
        self.weight = weight

    # FUNCTIONS
 
def getplatenum(self):
    return self.platenum

def getmaker(self):
    return self.maker

def getseries(self):
    return self.series

def getmodyear(self):
    return self.modyear

def getweight(self):
    return self.weight

    #FRAME

frame = Tk()

    #LABELS
Label(frame, text='Plate Number:').grid(row=0,column=0, padx=10,pady=10)
Label(frame, text='Maker:').grid(row=0,column=2,padx=10,pady=10)
Label(frame, text='Series:').grid(row=0,column=4,padx=10,pady=10)
Label(frame, text='Model Year:').grid(row=1,column=2,padx=10,pady=10)
Label(frame, text='Weight:').grid(row=1,column=4,padx=10,pady=10)

    #ENTRIES
plnum = Entry(frame).grid(row=0,column=1,padx=10,pady=10)
mker = Entry(frame).grid(row=0,column=3,padx=10,pady=10)
srs = Entry(frame).grid(row=0,column=5,padx=10,pady=10)
modelyear = Entry(frame).grid(row=1,column=3,padx=10,pady=10)
weigh = Entry(frame).grid(row=1,column=5,padx=10,pady=10)

    #BUTTONS
btn_insert = Button(frame, text='Insert')
btn_insert.grid(row=2,column=5,padx=10,pady=10)

    #TREEVIEW
tview = ttk.Treeview(frame,column=("Plate Number", "Maker", "Series", "Model Year", "Weight"), show="headings")
tview.heading('#1', text='Plate Number')
tview.heading('#2', text='Maker')
tview.heading('#3', text='Series')
tview.heading('#4', text='Model Year')
tview.heading('#5', text='Weight')

tview.grid(row=7,column=0,columnspan=7)


frame.mainloop()

    


        
