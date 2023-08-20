from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def journal():
    global window
    window.destroy()
    global file
    def newFile():
        global file
        root.title("Memories - Journal")
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
            root.title(os.path.basename(file) + " - Journal")
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

                root.title(os.path.basename(file) + " - Journal")
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
        root.title("Memories - Journal")
        w=root.winfo_screenwidth()
        h=root.winfo_screenheight()
        x=(w/2)-(400)
        y=(h/2)-(250)
        root.geometry(f'800x500+{int(x)}+{int(y)}')

        #Add TextArea
        TextArea = Text(root, font="CenturyGothic")
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
        HelpMenu.add_command(label = "About Journals", command=about)
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
    global window
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
            title = Label(root, text=f'Your Memories From {n}', font=('Quicksand semibold',11,'bold'))
            title.place(relx=0.365,rely=0.875)
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
            prev_button = Button(root, text='<< Previous', command=prev_image)
            prev_button.pack(side=LEFT)
            next_button = Button(root, text='Next >>', command=next_image)
            next_button.pack(side=RIGHT)

    b=Button(root, text="enter")
    b['command']=click
    b.pack()
    root.mainloop()

# My Memories page
window = Tk()
window.title("memories")

wid=window.winfo_screenwidth()
hei=window.winfo_screenheight()
x=(wid/2)-(250)
y=(hei/2)-(250)
window.geometry(f'500x500+{int(x)}+{int(y)}')
window.config(bg='#eff6fb')

ti = Label(window, text='Your Memories :)',font=("Quicksand semibold",25))
ti.place(relx=0.25, rely=0.03)

# Create a PhotoImage object
img1 = Image.open("diary.png").resize((128,128))
img1 = ImageTk.PhotoImage(img1)   
jo = Label(window, image=img1)
jo.place(relx=0.15, rely=0.29)

jou = Button(window, text='  your journals  ',command=journal)
jou.place(relx=0.19, rely=0.6)


# Create a PhotoImage object
img2 = Image.open("photos.png").resize((120,120))
img2 = ImageTk.PhotoImage(img2)   
mm = Label(window, image=img2)
mm.place(relx=0.6,rely=0.3)

mem = Button(window, text='  your pictures  ',command=photos)
mem.place(relx=0.64, rely=0.6)
window.mainloop()


