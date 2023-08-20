from tkinter import *

root = Tk()
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(bg="#e6eeff")

title = Label(root,text='$ Money Tracker $', font=("Quicksand semibold",30,'bold'),bg="#e6eeff",fg='dark blue')
title.place(relx=0.36,rely=0.03)

gain = Label(root,text='Incoming money', font=("Quicksand semibold",17,'italic'),bg="#B8E8FC",fg='dark blue', width=20,
    height=2, borderwidth=0.5, relief='solid')
gain.place(relx=0.1,rely=0.15)

loss = Label(root,text='Expenses', font=("Quicksand semibold",17,'italic'),bg="#B8E8FC",fg='dark blue', width=20,
    height=2, borderwidth=0.5, relief='solid')
loss.place(relx=0.61,rely=0.15)

s=0
a=0.1
b=0.35

def addI():
    global a,b
    x = Label(root, text=' Total Incoming money',font=('Quicksand semibold',18),bg="#e6eeff", fg='dark blue')
    x.place(relx=0.09,rely=0.27)
    e = Entry(root, justify='center', font=('Quicksand semibold',12), foreground='dark blue', width=22,
            highlightcolor='#668cff', highlightbackground='#668cff', highlightthickness=1)
    e.place(relx=a,rely=b, height=32)
    f = Entry(root, justify='center', font=('Quicksand semibold',12), foreground='dark blue', width=11,
            highlightcolor='#668cff', highlightbackground='#668cff', highlightthickness=1)
    f.place(relx=a+0.17,rely=b, height=32)

    def result():
        global s
        n=f.get()
        s=s+int(n)
        y = Label(root, text=str(s),font=('Quicksand semibold',18), fg='dark blue',bg="#e6eeff")
        y.place(relx=a+0.23, rely=0.27)
    p = Button(root, text='>',font=('Quicksand semibold',12), fg='dark blue', width=5, command=result)
    p.place(relx=a+0.27,rely=b-0.008)

    if b>0.79:
        g["state"]='disabled'
    b=b+0.08

t=0
c=0.61
d=0.35
def addE():
    global  c,d
    x = Label(root, text='Total Expenses',font=('Quicksand semibold',18), fg='dark blue',bg="#e6eeff")
    x.place(relx=c,rely=0.27)
    e = Entry(root, justify='center', font=('Quicksand semibold',12), foreground='dark blue', width=22,
            highlightcolor='#668cff', highlightbackground='#668cff', highlightthickness=1)
    e.place(relx=c,rely=d, height=32)
    f = Entry(root, justify='center', font=('Quicksand semibold',12), foreground='dark blue', width=11,
            highlightcolor='#668cff', highlightbackground='#668cff', highlightthickness=1)
    f.place(relx=c+0.17,rely=d, height=32)

    def result():
        global t
        n=f.get()
        t=t+int(n)
        y = Label(root, text=str(t),font=('Quicksand semibold',18), fg='dark blue',bg="#e6eeff")
        y.place(relx=c+0.18, rely=0.27)
    p = Button(root, text='>',font=('Quicksand semibold',12), fg='dark blue', width=5, height=1, command=result)
    p.place(relx=c+0.27,rely=d-0.008)

    if d>0.79:
        l["state"]='disabled'
    d=d+0.08

g=Button(root, text=" +  ", font=("Quicksand semibold",21,'italic'),width=4,height=1,bg='#B8E8FC', fg='dark blue', borderwidth=0.5,
        relief='solid', command=addI)
g.place(relx=0.325,rely=0.151)
l=Button(root, text=" +  ", font=("Quicksand semibold",21,'italic'),width=4,height=1,bg='#B8E8FC', fg='dark blue', borderwidth=0.5,
        relief='solid', command=addE)
l.place(relx=0.835,rely=0.151)

root.mainloop()