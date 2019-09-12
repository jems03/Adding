from tkinter import *
from tkinter import messagebox
from tkinter import ttk

VRegistration = []

class Vehicles:

    def __init__(self, platenum, maker, series, modyear, weight):
        self.platenum = platenum
        self.maker = maker
        self.series = series
        self.modyear = modyear
        self.weight = weight

    def getplatenum(self):
        return self.platenum

    def getmaker(self):
        return self.getmaker

    def getseries(self):
        return self.series

    def getmodyear(self):
        return self.modyear

    def getweight(self):
        return self.weight
        
    # FUNCTIONS

def add_vehicle():
    global VRegistration
    plt = plnum.get()
    mkr = mker.get()
    series = srs.get()
    mdyr = modelyear.get()
    wght = weigh.get()
    VRegistration.append(Vehicles(plt,mkr,series,mdyr,wght))
    thanks()
    view_vehicles()
    reset_entry()

def thanks():
    th = 'Vehicle Added!'
    messagebox.showinfo('Notification',th)
    
def view_vehicles():
    global Vregistration
    global tview
    for i in tview.get_children():
        tview.delete(i)
    for j in VRegistration:
        print(j.platenum, j.maker, j.series, j.modyear, j.weight)
        tview.insert('','end',values=(j.platenum, j.maker, j.series, j.modyear, j.weight))

def reset_entry():
    plnum.delete(0,'end')
    mker.delete(0,'end')
    srs.delete(0,'end')
    modelyear.delete(0,'end')
    weigh.delete(0,'end')
    
    #FRAME
frame = Tk()
frame.title("SIMPLE VEHICLE REGISTRATION SYSTEM")

    #LABELS
Label(frame, text='Plate Number:').grid(row=0,column=0, padx=10,pady=10)
Label(frame, text='Maker:').grid(row=0,column=2,padx=10,pady=10)
Label(frame, text='Series:').grid(row=0,column=4,padx=10,pady=10)
Label(frame, text='Model Year:').grid(row=1,column=2,padx=10,pady=10)
Label(frame, text='Weight:').grid(row=1,column=4,padx=10,pady=10)

    #ENTRIES
plnum = Entry(frame)
mker = Entry(frame)
srs = Entry(frame)
modelyear = Entry(frame)
weigh = Entry(frame)

plnum.grid(row=0,column=1,padx=10,pady=10)
mker.grid(row=0,column=3,padx=10,pady=10)
srs.grid(row=0,column=5,padx=10,pady=10)
modelyear.grid(row=1,column=3,padx=10,pady=10)
weigh.grid(row=1,column=5,padx=10,pady=10)

    #BUTTONS
btn_insert = Button(frame, text='Insert', command=add_vehicle)
btn_insert.grid(row=2,column=5,padx=10,pady=10)

    #TREEVIEW
tview = ttk.Treeview(frame,column=("Plate Number", "Maker", "Series", "Model Year", "Weight"), show="headings")
tview.heading('#1', text='Plate Number')
tview.heading('#2', text='Maker')
tview.heading('#3', text='Series')
tview.heading('#4', text='Model Year')
tview.heading('#5', text='Weight')

tview.grid(row=6,column=0,columnspan=6)


frame.mainloop()

    


        
