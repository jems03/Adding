from tkinter import *  
from tkinter import ttk

EmployeeInfo = []

class Adds:
    

    def __init__(self, name, department, position, rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate

def get_info(self):
    return self.name + self.department + self.position + self.rate

def thanks():
    th = "Employee Added"
    messagebox.showinfo("Notification", th)
    th2 = en1.get() + d1.get() + p1.get() + er1.get()
    messagebox.showinfo("Notification", th2)

def info():
    global EmployeeInfo
    name = en1.get()
    dept = d1.get()
    pos = p1.get()
    erate = er1.get()
    EmployeeInfo.append(Adds(name,dept,pos,erate))
    for a in EmployeeInfo:
        print(a.name, a.department, a.position, a.rate)
        

def clear():
    en1.delete(0, END)
    d1.delete(0, END)
    p1.delete(0, END)
    er1.delete(0, END)

fr = Tk()
Label(fr, text='Employee Name:').grid(row=0,padx=20,pady=10)
Label(fr, text='Department:').grid(row=1,padx=20,pady=10)
Label(fr, text='Position:').grid(row=2,padx=20,pady=10)
Label(fr, text='Employee Rate:').grid(row=3,padx=20,pady=10)

en1 = Entry(fr)
d1 = Entry(fr)
p1 = Entry(fr)
er1 = Entry(fr)

en1.grid(row=0,column=1,padx=20,pady=10)
d1.grid(row=1,column=1,padx=20,pady=10)
p1.grid(row=2,column=1,padx=20,pady=10)
er1.grid(row=3,column=1,padx=20,pady=10)

btn1 = Button(fr, text='Insert', command=lambda:[thanks(),info(),clear()])
btn1.grid(row=4,column=1,padx=20,pady=10)

tview = ttk.Treeview(fr,column=("Name", "Department", "Position", "Rate"), show="headings")
tview.heading('#1', text='Name')
tview.heading('#2', text='Department')
tview.heading('#3', text='Position')
tview.heading('#4', text='Rate')
tview.grid(row=5,column=0,columnspan=5)


        
fr.mainloop()
