from tkinter import *
from tkcalendar import *
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from datetime import date
from calendar import monthrange
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.font as font1
import datetime
import requests
import os



def calendarApp():
	
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


def weatherApp():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    root=Tk()
    root.title('Weather')

    #getting screen width and height of display
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()

    #setting tkinter window size
    root.geometry("%dx%d" % (width, height))
    root.configure(bg="#b4e4e4")

    #Entry label
    label_we1=Label(root,text="Enter City-",font=("Quicksand semibold",35),bg="#b4e4e4",fg="Dark blue")
    label_we1.place(x=320,y=90)
    label_we2=""
    city1=StringVar()
    cityEntry= Entry(root, justify='center',font=("Quicksand semibold",30),width=23,fg="Dark blue",textvariable=city1)
    cityEntry.place(x=300,y=180)

    def weather():
            city=str(city1.get())
            city = str(city)+" weather"
            city = city.replace(" ", "+")
            res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            location = cityEntry.get() #soup.select('#wob_loc')[0].getText().strip()
            time = soup.select('#wob_dts')[0].getText().strip()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()
            display_weather(location,time,info,weather)

    def  display_weather(l,t,inf,wea):
            
            label_we2=Label(root,text=l+"\n"+t+"\n"+inf+"\n"+wea+"°C\nHave a Nice Day :)",font=("Quicksand semibold",30),width=30,fg="Dark blue",bg="#b4e4e4")
            label_we2.place(x=300,y=300)


    btnfont = font1.Font(family='Quicksand semibold', size=17)
    btn = Button(root, text=' Enter ', bd='5',width=5,height=1,command= weather,bg="#c8ffd4",font=btnfont)
    btn.place(x=870,y=178)

    root.mainloop()



def habitTrackerApp():
    # Making the Window
    root=Tk()
    root.title('Habit Tracker')
    root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
    root.configure(bg='#ccf2ff')

    title = Label(root, text = "Habit Tracker", font=('Quicksand semibold',25,'bold'), foreground='dark blue',
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
    b=0.3
    def newHab():
        nonlocal a,b
        nonlocal n
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
                d.config(bg='#f0f5f5')
        # Create a button widget and set the image
        dele = Button(root, image=image, command=clear)
        dele.place(relx=(0.3+0.021*n),rely=b)
        b=b+0.06

    # Add Habit Button
    add = Button(root, text='+ Add a Habit', font=('Quicksand semibold',10),bg='#006666', foreground='white',
            width=15,height=1,command=newHab)
    add.place(relx=0.457,rely=0.15)
    root.mainloop()



def moneyTrackerApp():
    root = Tk()
    root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("Money Tracker")
    root.configure(bg="#c8ffd4")

    title = Label(root,text='$ Money Tracker $', font=("Quicksand semibold",30,'bold'),bg="#c8ffd4",fg='dark blue')
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
        nonlocal a,b,s
        x = Label(root, text=' Total Incoming money',font=('Quicksand semibold',18),bg="#c8ffd4", fg='dark blue')
        x.place(relx=0.09,rely=0.27)
        e = Entry(root, justify='center', font=('Quicksand semibold',12), foreground='dark blue', width=22,
                highlightcolor='#668cff', highlightbackground='#668cff', highlightthickness=1)
        e.place(relx=a,rely=b, height=32)
        f = Entry(root, justify='center', font=('Quicksand semibold',12), foreground='dark blue', width=11,
                highlightcolor='#668cff', highlightbackground='#668cff', highlightthickness=1)
        f.place(relx=a+0.17,rely=b, height=32)
        y = Label(root, text=str(s),font=('Quicksand semibold',18), fg='dark blue',bg="#c8ffd4")
        y.place(relx=a+0.23, rely=0.27)

        def result():
            nonlocal s
            n=f.get()
            s=s+int(n)
            y = Label(root, text=str(s),font=('Quicksand semibold',18), fg='dark blue',bg="#c8ffd4")
            y.place(relx=a+0.23, rely=0.27)
        p = Button(root, text='>',font=('Quicksand semibold',12), fg='dark blue',bg="#B8E8FC", width=5, command=result)
        p.place(relx=a+0.27,rely=b-0.008)

        if b>0.79:
            g["state"]='disabled'
        b=b+0.08

    t=0
    c=0.61
    d=0.35
    def addE():
        nonlocal  c,d,t
        x = Label(root, text='Total Expenses',font=('Quicksand semibold',18), fg='dark blue',bg="#c8ffd4")
        x.place(relx=c,rely=0.27)
        e = Entry(root, justify='center', font=('Quicksand semibold',12), foreground='dark blue', width=22,
                highlightcolor='#668cff', highlightbackground='#668cff', highlightthickness=1)
        e.place(relx=c,rely=d, height=32)
        f = Entry(root, justify='center', font=('Quicksand semibold',12), foreground='dark blue', width=11,
                highlightcolor='#668cff', highlightbackground='#668cff', highlightthickness=1)
        f.place(relx=c+0.17,rely=d, height=32)
        y = Label(root, text=str(t),font=('Quicksand semibold',18), fg='dark blue',bg="#c8ffd4")
        y.place(relx=c+0.18, rely=0.27)

        def result():
            nonlocal t
            n=f.get()
            t=t+int(n)
            y = Label(root, text=str(t),font=('Quicksand semibold',18), fg='dark blue',bg="#c8ffd4")
            y.place(relx=c+0.18, rely=0.27)
        p = Button(root, text='>',font=('Quicksand semibold',12), fg='dark blue',bg="#B8E8FC", width=5, height=1, command=result)
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



def memoriesApp():

    def journal():
        nonlocal window
        window.destroy()
        global file
        def newFile():
            global file
            root.title("Journal")
            file = None
            TextArea.delete(1.0, END)


        def openFile():
            global file
            file = askopenfilename(defaultextension=".txt",
                                filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
            if file == "":
                file = None
            else:
                root.title(os.path.basename(file) + ":)")
                TextArea.delete(1.0, END)
                f = open(file, "r")
                TextArea.insert(1.0, f.read())
                f.close()

        def saveFile():
            global file
            if file == None:
                file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                                filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
                if file =="":
                    file = None
                else:
                    #Save as a new file
                    f = open(file, "w")
                    f.write(TextArea.get(1.0, END))
                    f.close()

                    root.title(os.path.basename(file) + ":)")
                    print("File Saved")
            else:
                # Save the file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

        def quitApp():
            root.destroy()

        def cut():
            TextArea.event_generate(("<>"))

        def copy():
            TextArea.event_generate(("<>"))

        def paste():
            TextArea.event_generate(("<>"))

        def about():
            showinfo("memories", "save your memories by date :)")

        if __name__ == '__main__':
            #Basic tkinter setup
            root = Tk()
            root.title("Journal")
            w=root.winfo_screenwidth()
            h=root.winfo_screenheight()
            x=(w/2)-(400)
            y=(h/2)-(250)
            root.geometry(f'800x500+{int(x)}+{int(y)}')

            #Add TextArea
            TextArea = Text(root, font="CenturyGothic 13")
            TextArea.configure(bg='#e6f5ff')
            file = None
            TextArea.pack(expand=True, fill=BOTH)

            # Lets create a menubar
            MenuBar = Menu(root)

            #File Menu Starts
            FileMenu = Menu(MenuBar, tearoff=0)
            # To open new file
            FileMenu.add_command(label="New", command=newFile)

            #To Open already existing file
            FileMenu.add_command(label="Open", command = openFile)

            # To save the current file
            FileMenu.add_command(label = "Save", command = saveFile)
            FileMenu.add_separator()
            FileMenu.add_command(label = "Exit", command = quitApp)
            MenuBar.add_cascade(label = "File", menu=FileMenu)
            # File Menu ends

            # Edit Menu Starts
            EditMenu = Menu(MenuBar, tearoff=0)
            #To give a feature of cut, copy and paste
            EditMenu.add_command(label = "Cut", command=cut)
            EditMenu.add_command(label = "Copy", command=copy)
            EditMenu.add_command(label = "Paste", command=paste)
            MenuBar.add_cascade(label="Edit", menu = EditMenu)
            # Edit Menu Ends

            # Help Menu Starts
            HelpMenu = Menu(MenuBar, tearoff=0)
            HelpMenu.add_command(label = "About Notepad", command=about)
            MenuBar.add_cascade(label="Help", menu=HelpMenu)
            # Help Menu Ends
            root.config(menu=MenuBar)

            #Adding Scrollbar using rules from Tkinter lecture no 22
            Scroll = Scrollbar(TextArea)
            Scroll.pack(side=RIGHT,  fill=Y)
            Scroll.config(command=TextArea.yview)
            TextArea.config(yscrollcommand=Scroll.set)
            root.mainloop()


    def photos():
        nonlocal window
        window.destroy()

        root = Tk()
        root.title("Photo Album")
        w=root.winfo_screenwidth()
        h=root.winfo_screenheight()
        x=(w/2)-(400)
        y=(h/2)-(250)
        root.geometry(f'800x500+{int(x)}+{int(y)}')
        root.configure(bg='#eff6fb')
        op=Entry(root, width=40)
        op.pack()

        def click():
            n=op.get()
            # Specify the directory containing the images
            filepath = "C:/Users/namri/Documents/nam/project/"
            # Get a list of all files in the directory
            contents = os.listdir(filepath)
            folder = filepath+n

            error = Label(root, text = '',font=('Quicksand semibold',10))
            error.place(relx=0.4,rely=0.2)
            if n not in contents:
                error.configure(text='this memory wasnt saved :(')
            else:
                # Get a list of all files in the directory
                files = os.listdir(folder)
                # Create an empty list to store the PhotoImage objects
                images = []
                # Iterate over the files in the directory
                for file in files:
                    # Check if the file is an image
                    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                        # Open the image file
                        img = Image.open(os.path.join(folder, file))
                        # Get the right size
                        ratio = img.width/img.height
                        newh = 400
                        neww = int(ratio*newh)
                        img = img.resize((neww,newh),Image.BICUBIC)
                        # Convert the image to a PhotoImage object
                        img = ImageTk.PhotoImage(img)
                        # Append the PhotoImage object to the list
                        images.append(img)
                title = Label(root, text=f'Your Pictures from {n}', font=('Quicksand semibold',10,'bold'))
                title.configure(bg='#eff6fb')
                title.place(relx=0.39,rely=0.88)
                op.destroy()
                b.destroy()
                # Create a variable to keep track of the current image index
                current_index = 0
                # Create a label for the current image
                current_img = Label(root, image=images[current_index])
                current_img.pack(anchor='center')

                # Define a function to display the next image
                def next_image():
                    nonlocal current_index
                    current_index += 1
                    # Check if the current index is out of bounds
                    if current_index >= len(images):
                        current_index = 0
                    # Update the label with the new image
                    current_img.configure(image=images[current_index])

                # Define a function to display the previous image
                def prev_image():
                    nonlocal current_index
                    current_index -= 1
                    # Check if the current index is out of bounds
                    if current_index < 0:
                        current_index = len(images) - 1
                    # Update the label with the new image
                    current_img.configure(image=images[current_index])

                # Create buttons to navigate between images
                prev_button = Button(root, text='<< Previous', font=('Quicksand semibold',10),command=prev_image)
                prev_button.pack(side=LEFT)
                next_button = Button(root, text='Next >>', font=('Quicksand semibold',10),command=next_image)
                next_button.pack(side=RIGHT)

        b=Button(root, text="enter", font=('Quicksand semibold',10))
        b['command']=click
        b.pack()
        root.mainloop()


    # My Memories page
    window= Tk()
    window.title("Memories")

    wid=window.winfo_screenwidth()
    hei=window.winfo_screenheight()
    x=(wid/2)-(250)
    y=(hei/2)-(250)
    window.geometry(f'500x500+{int(x)}+{int(y)}')
    window.config(bg='#c8ffd4')
    #window.config(bg='#eff6fb')

    ti = Label(window, text='Your Memories :)',font=("Quicksand semibold",25))
    ti.config(bg='#c8ffd4')
    ti.place(relx=0.25, rely=0.03)

    # Create a PhotoImage object
    img1 = Image.open("diary.png").resize((128,128))
    img1 = ImageTk.PhotoImage(img1)  
    jo = Label(window, image=img1)
    jo.place(relx=0.15, rely=0.29)

    jou = Button(window, text='  your journals  ', font=('Quicksand semibold',9), command=journal,bg='#006666', foreground='white')
    jou.place(relx=0.18, rely=0.6)

    # Create a PhotoImage object
    img2 = Image.open("photos.png").resize((120,120))
    img2 = ImageTk.PhotoImage(img2)  
    mm = Label(window, image=img2)
    mm.place(relx=0.6,rely=0.3)

    mem = Button(window, text='  your pictures  ', font=('Quicksand semibold',9), command=photos,bg='#006666', foreground='white')
    mem.place(relx=0.63, rely=0.6)
    window.mainloop()



def timerApp():
    # module required
    import time
    from tkinter import messagebox

    root=Tk()
    root.title('Timer')

    #getting screen width and height of display
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()

    #setting tkinter window size
    root.geometry("%dx%d" % (width, height))
    root.configure(bg="#C8FFD4")

    title = Label(root,text='Timer for Study Sessions',font=("Quicksand Semibold",40,'bold'),bg="#C8FFD4",fg="Dark blue")
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
    secondEntry= Entry(root,width=2,justify='center',font=("Quicksand Semibold",70 ),fg="Dark blue",textvariable=second)
    secondEntry.place(x=440,y=230)

    # Entry widget to get the value of "no"
    no_entry = Entry(root,width=4, font=("Quicksand Semibold", 21),justify='center', fg="Dark blue")
    no_entry.place(x=970, y=321)

    # Label to display the value of "no"
    no_label = Label(root, text="No. of Sessions:       ", font=("Quicksand Semibold", 20),bg="#C8FFD4",fg="Dark blue")
    no_label.place(x=700, y=320)

    st="00:00:00"
    do="0"
    i=0

    my_text='Study time-            '+st
    ses_text='Sessions Completed-  '+'_ /_'


    def update_session():
        nonlocal i
        i+=1 
        my_label2.configure(text='Sessions Completed-  '+str(int(do)+i)+'/'+no)

    my_label=Label(root,text=my_text,font=("Quicksand Semibold",20),bg="#C8FFD4",fg="Dark blue")
    my_label.place(x=700,y=220)

    my_label2=Label(root,text=ses_text,font=("Quicksand Semibold",20),bg="#C8FFD4",fg="Dark blue")
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



def home():
    home_window=Tk()
    width= home_window.winfo_screenwidth()
    height= home_window.winfo_screenheight()
    home_window.geometry("%dx%d" % (width, height))
    home_window.title("Home Page")
    home_window.configure(bg="#b8e8fc")

    Home_page=Label(home_window, background="#b8e8fc", foreground="dark blue", font=("Quicksand semibold", 30, "bold"), text="Home Page")
    Home_page.place(relx=0.45, rely=0.1)

    cal_button=Button(home_window, text="Calendar: To Do List", background="#c8ffd4", foreground="dark blue", width=17, height=7, font=("Quicksand semibold", 12, "bold"),
    command=calendarApp)
    cal_button.place(relx=0.45, rely=0.25)


    weather=Button(home_window, text="Weather", background="#c8ffd4", foreground="dark blue", width=17, height=7,font=("Quicksand semibold", 12, "bold"))
    weather.place(relx=0.3, rely=0.25)


    habit=Button(home_window, text="Habit Tracker", background="#c8ffd4", foreground="dark blue", width=17, height=7, font=("Quicksand semibold", 12, "bold"))
    habit.place(relx=0.3, rely=0.55)


    timer=Button(home_window, text="Timer", background="#c8ffd4", foreground="dark blue", width=17, height=7,font=("Quicksand semibold", 12, "bold"))
    timer.place(relx=0.45, rely=0.55)


    Money=Button(home_window, text="Money Tracker", background="#c8ffd4", foreground="dark blue", width=17, height=7, font=("Quicksand semibold", 12, "bold"),
    command=moneyTrackerApp)
    Money.place(relx=0.6, rely=0.55)


    Mem=Button(home_window, text="Memories", background="#c8ffd4", foreground="dark blue", width=17, height=7, font=("Quicksand semibold", 12, "bold"))
    Mem.place(relx=0.6, rely=0.25)

    home_window.mainloop()


home()
weatherApp()
home()
memoriesApp()
home()
memoriesApp()
home()
habitTrackerApp()
home()
timerApp()
home()
