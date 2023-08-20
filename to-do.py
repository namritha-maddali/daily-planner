from tkinter import *
from tkcalendar import *
import os

cal_window=Tk()
cal_window.title("Monthly View")
cal_window.geometry("%dx%d" % (cal_window.winfo_screenwidth(), cal_window.winfo_screenheight()))
cal_window.configure(bg="#b8e8fc")

Title_window=Label(cal_window, text="Monthly View", font=('Quicksand semibold',25, "bold"), background="#b8e8fc", foreground="dark blue")
Title_window.pack(pady=5)

my_cal=Calendar(cal_window, date_pattern="dd.mm.yyyy", 
background="#c8ffd4", foreground="dark blue", bordercolor="dark blue", 
headersbackground="#c8ffd4", headersforeground="dark blue", 
selectbackground="dark blue", selectforeground="#c8ffd4", 
normalbackground="#c8ffd4",normalforeground="dark blue", 
weekendbackground="#c8ffd4",weekendforeground="dark blue",
font=('Quicksand semibold',20))


my_cal.pack()

	
def open_to_do():

	to_do_window=Tk()
	to_do_window.title("To Do List")
	to_do_window.geometry("%dx%d" % (to_do_window.winfo_screenwidth(), to_do_window.winfo_screenheight()))
	to_do_window.configure(bg="#b8e8fc")
	
	Title_todo=Label(to_do_window, text="To Do List", font=('Quicksand semibold',25,"bold"), background="#b8e8fc", foreground="dark blue")
	Title_todo.pack()
	
	date_title=Label(to_do_window, text=f"Date: {my_cal.get_date()}", font=('Quicksand semibold',20), background="#b8e8fc", foreground="dark blue")
	date_title.pack()

	to_do_frame=Frame(to_do_window)
	to_do_frame.pack()

	to_do_list=Listbox(to_do_frame, bg="#c8ffd4", selectbackground="dark blue", selectforeground="#c8ffd4",
activestyle="none", foreground="Dark blue",font=('Quicksand semibold',15) )
	to_do_list.pack(side=LEFT, fill=BOTH)


	to_do_enter=Entry(to_do_window, background="#c8ffd4", foreground="Dark blue",font=('Quicksand semibold',12))
	to_do_enter.pack(pady=5)


	def add_to_do():
		if (to_do_enter.get()).strip():
			f9=open(f"{my_cal.get_date()}.txt", "a+")
			items=f9.readlines()
			f9.close
			to_do_list.insert(END, to_do_enter.get())
			f=open(f"{my_cal.get_date()}.txt", "a")
			f.write(f"{to_do_enter.get()}\n")
			f.close
		
			to_do_enter.delete(0,END)
		else:
			pass


	def delete_to_do():
		f2=open(f"{my_cal.get_date()}.txt", "r")
		item=f2.readlines()
		f2.close
		for j in to_do_list.curselection():
			item.remove(to_do_list.get(j))
		f3=open(f"{my_cal.get_date()}.txt", "w")
		for k in item:
			f3.write(f"{k}")
		f3.close
		to_do_list.delete(ANCHOR)
		
		
		

	def strike():
		to_do_list.itemconfig(to_do_list.curselection(),fg="white", selectbackground="light grey")
		f4=open(f"{my_cal.get_date()}.txt", "r")
		items=f4.readlines()
		f4.close
		for j in to_do_list.curselection():
			items.remove(to_do_list.get(j))
		f5=open(f"{my_cal.get_date()}.txt", "w")
		for k in items:
			f5.write(f"{k}")
		f5.close

		
	def unstrike():
		
		f6=open(f"{my_cal.get_date()}.txt", "r")
		items=f6.readlines()
		f6.close
		for l in to_do_list.curselection():
			if to_do_list.get(l) not in items:
				items.append(to_do_list.get(l))
		f7=open(f"{my_cal.get_date()}.txt", "w")
		for m in items:
			f7.write(f"{m}")
		f7.close
		to_do_list.itemconfig(to_do_list.curselection(),fg="dark blue", selectbackground="dark blue")

	Add=Button(to_do_window, text="Add", command=add_to_do, font=('Quicksand semibold',10), 
background="#c8ffd4", foreground="dark blue")
	Add.pack(pady =3)
	Delete=Button(to_do_window, text="Delete", command=delete_to_do, font=('Quicksand semibold',10), 
background="#c8ffd4", foreground="dark blue")
	Delete.pack(pady=3)
	Done=Button(to_do_window, text="Mark as Done", command=strike, font=('Quicksand semibold',10), 
background="#c8ffd4", foreground="dark blue")
	Done.pack(pady=3)
	Undo=Button(to_do_window, text="Mark as Undone", command=unstrike, font=('Quicksand semibold',10), 
background="#c8ffd4", foreground="dark blue")
	Undo.pack(pady=3)

		
	save=Button(to_do_window, text="Save", command=to_do_window.destroy, bg="dark blue", fg="#b8e8fc", font=('Quicksand semibold',10))
	save.pack()

	
	to_do_scrollbar=Scrollbar(to_do_frame)
	to_do_scrollbar.pack(side=RIGHT, fill=BOTH)
	
	if os.path.exists(f"{my_cal.get_date()}.txt")==True:
		f1=open(f"{my_cal.get_date()}.txt", "r")
		data_todo=f1.readlines()
		f1.close
		for i in data_todo:
			to_do_list.insert(END,i)
	elif os.path.exists(f"{my_cal.get_date()}.txt")==False:
		pass
			

	to_do_window.mainloop()
	

button_get_date=Button(cal_window, text="Get the To Do List for Selected Date", command=open_to_do, font=('Quicksand semibold',12), 
background="#c8ffd4", foreground="dark blue")
button_get_date.pack(pady=5)


close=Button(cal_window, text="Close", command=cal_window.destroy, bg="dark blue", fg="#b8e8fc", font=('Quicksand semibold',12))
close.pack(pady=5)

cal_window.mainloop()