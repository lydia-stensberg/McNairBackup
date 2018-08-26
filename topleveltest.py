import tkinter
from tkinter import *

def topLevel():
    top=Toplevel()
    top.title("Listbox test")
    notiLabel = Label(top, text ="----test----", font=('Times', 20))
    notiLabel.grid(row=0,column=0, sticky=W)

    noti = Label(top, text ="----test----", font=('Times', 18))
    noti.grid(row=1,column=1, sticky=W)

    f = Label(top, text ="------test-----") # note the 'top' parameter
    # 'top' was your Toplevel widget
    f.grid(row=3,column=0, sticky=W)
    fa = Label(top)
    fa.grid(row=3,column=1, sticky=W)
    top.mainloop()


root=Tk()
root.title("Listbox test")

s = Label(text =">>>test<<<", font=(('Times'),20))
s.grid(row=2,column=0)


N = Label(text =">>>test<<<")
N.grid(row=3,column=0)


LB = Listbox(width=50, selectmode =SINGLE)
LB.grid(row=4, column=0)


TI = Button(text="b1", width =50, command=topLevel)
TI.grid(row=5, column=0)

root.mainloop()