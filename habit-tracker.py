from tkinter import *
from PIL import Image, ImageTk
from datetime import date
from calendar import monthrange

# Making the Window
root=Tk()
root.title('habit tracker')
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
'''can = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
big = Image.open("bg.png")
big = big.convert("RGBA")
big.putalpha(175)
big = ImageTk.PhotoImage(big)
can.create_image(0, 0, anchor=NW, image=big)
can.pack()'''
root.configure(bg='#ccf2ff')

title = Label(root, text = "Habit Tracker", font=('Century Gothic',25,'bold'), foreground='dark blue',
            bg='#ccf2ff')
title.place(relx=0.4267, rely=0.03)


# To set the Habit tracker to the Current Month
m = date.today().month
if m==1:
    month = Label(root, text='January '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.455, rely=0.10)
elif m==2:
    month = Label(root, text='February '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.4515, rely=0.10)
elif m==3:
    month = Label(root, text='March '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.4634, rely=0.10)
elif m==4:
    month = Label(root, text='April '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.47, rely=0.10)
elif m==5:
    month = Label(root, text='May '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.4705, rely=0.10)
elif m==6:
    month = Label(root, text='June '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.467, rely=0.10)
elif m==7:
    month = Label(root, text='July '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.47, rely=0.10)
elif m==8:
    month = Label(root, text='August '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.459, rely=0.10)
elif m==9:
    month = Label(root, text='September '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.445, rely=0.10)
elif m==10:
    month = Label(root, text='October '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.454, rely=0.10)
elif m==11:
    month = Label(root, text='November '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.446, rely=0.10)
else:
    month = Label(root, text='December '+str(date.today().year), font=('Quicksand semibold',15))
    month.configure(bg='#ccf2ff', foreground='dark blue')
    month.place(relx=0.445, rely=0.10)

# Heading of the Habit Tracker Table
habits = Label(root, text='Habits to keep track of', font=('Quicksand semibold',10,'bold'), bg='#ccffd7',width=35, 
            height=2,borderwidth=0.5, relief='solid', foreground='dark blue')
habits.place(relx=0.035, rely=0.22)
n = monthrange(date.today().year,date.today().month)[1]
x=0.26
for i in range(1, n+1):
    day = Label(root, text=str(i), font=('Quicksand semibold',10), bg='#ccffd7', width=3, height=2, 
            borderwidth=0.5, relief='solid', foreground='dark blue')
    x=x+0.021
    day.place(relx=x,rely=0.22)

# Create a PhotoImage object
image = Image.open("del.png").resize((25,27))
image = ImageTk.PhotoImage(image)

# To change colour of the cell when clicked 
def change(d):
    d.configure(bg='#009999')

# Creating a Habit Column
a=0.035
b=0.31
def newHab():
    global a,b,n
    hab = Entry(root, justify='center', font=('Quicksand semibold',10), foreground='dark blue', 
            width=35, highlightcolor='#006080', highlightbackground='#006080', highlightthickness=1)
    hab.place(relx=a,rely=b, height=32) 
    if b>0.84:
        add["state"]='disabled'
    
    c=0.26
    e=[]
    for i in range(n):
        cal = Button(root, text='', bg='#f0f5f5', padx=10.5, pady=5, borderwidth=1, relief='solid',
                highlightbackground='white')
        c=c+0.021
        cal['command']= lambda d=cal:change(d)
        cal.place(relx=c,rely=b)
        e.append(cal)

    def clear():
        for d in e:
            d.configure(bg='#f0f5f5')
    # Create a button widget and set the image
    dele = Button(root, image=image, command=clear)
    dele.place(relx=(0.3+0.021*n),rely=b)

    b=b+0.06

# Add Habit Button
add = Button(root, text='+ Add a Habit', font=('Quicksand semibold',10),bg='#006666', foreground='white',
        width=15,height=1,command=newHab)
add.place(relx=0.457,rely=0.151)

root.mainloop()