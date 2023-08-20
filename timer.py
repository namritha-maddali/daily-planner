# module required
import time
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Timer')

#getting screen width and height of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

#setting tkinter window size
root.geometry("%dx%d" % (width, height))
root.configure(bg="#C8FFD4")

title = Label(root,text='Timer for Study Sessions',font=("Quicksand Semibold",40),bg="#C8FFD4",fg="Dark blue")
title.place(x=320,y=70)

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry= Entry(root,width=2,justify='center',font=("Quicksand Semibold",70),fg="Dark blue",textvariable=hour)
hourEntry.place(x=200,y=230)
minuteEntry= Entry(root,width=2,justify='center',font=("Quicksand Semibold",70),fg="Dark blue",textvariable=minute)
minuteEntry.place(x=320,y=230)
secondEntry= Entry(root,width=2,justify='center',font=("Quicksand Semibold",70),fg="Dark blue",textvariable=second)
secondEntry.place(x=440,y=230)

# Entry widget to get the value of "no"
no_entry = Entry(root,width=4, font=("Quicksand Semibold", 21),justify='center', fg="Dark blue")
no_entry.place(x=970, y=321)

# Label to display the value of "no"
no_label = Label(root, text="No. of Sessions:       ", font=("Quicksand Semibold", 20), fg="Dark blue")
no_label.place(x=700, y=320)

st="00:00:00"
do="0"
i=0

my_text='Study time-            '+st
ses_text='Sessions Completed-  '+'_ /_'


def update_session():
     global i
     i+=1 
     my_label2.configure(text='Sessions Completed-  '+str(int(do)+i)+'/'+no)

my_label=Label(root,text=my_text,font=("Quicksand Semibold",20),fg="Dark blue")
my_label.place(x=700,y=220)

my_label2=Label(root,text=ses_text,font=("Quicksand Semibold",20),fg="Dark blue")
my_label2.place(x=700,y=420)


def divmod1(): 
    mins,secs = divmod(temp,60) #(temp//60,temp%60)
    hours=0
    if mins >60:
        hours, mins = divmod(mins, 60)
    return hours,mins,secs

def submit():
    
     j=int(do)
     global hour1,second1,minute1
     try:
             hour1=int(hour.get())
             minute1=int(minute.get())
             second1=int(second.get())
             global temp
             temp=hour1*3600+minute1*60+second1

             no1 = int(no_entry.get())
             global no
             no = str(no1)
             my_label2.configure(text='Sessions Completed-  '+str(int(do)+i)+'/'+no)
            
     except:
             print("Please input the right value")
            
     h,m,s=divmod1()
     global st
     st=str(h*3600)+":"+str(m*60)+":"+str(s)
     my_label.configure(text='Study time        '+st)

     if i!=no1: 
            while temp >-1:
                hours,mins,secs=divmod1()
                      
                # using format () method to store the value up to two decimal places
                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))
                        
                # updating the GUI window after decrementing the
                # temp value every time
                root.update()
                time.sleep(1)

                # when temp value = 0; then a messagebox pop's up
                # with a message:"Time's up"
                if (temp == 0) : 
                    messagebox.showinfo("Time Countdown", "Session Completed! ")
                    update_session()
                          
                          
                # after every one sec the value of temp will be decremented
                # by one
                temp -= 1
     else: 
            messagebox.showinfo("Time Countdown", "Hurray you have completed all the sessions! ")
          
# button widget
btn = Button(root, text='   Set Time Countdown  ',font=("Quicksand Semibold",10), bd='5',width=43,command= submit,bg="#B8E8FC")
btn.place(x=200,y=390)

root.mainloop()


