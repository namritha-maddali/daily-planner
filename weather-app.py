#in command prompt pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
from tkinter import *
import tkinter.font as font1
import datetime

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
        location = soup.select('#wob_loc')[0].getText().strip()
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
