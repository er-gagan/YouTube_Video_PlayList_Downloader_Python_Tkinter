from tkinter import *
from YTube import *
import urllib
from urllib.request import urlopen
from tkinter.messagebox import *

root=Tk()
root.geometry('1100x600')
root.resizable(0,0)

photo = PhotoImage(file = "./logo.png")
root.iconphoto(False,photo)

root.title("YouTube Playlist Downloader")

image1= PhotoImage(file="./banner.png")
label_for_image= Label(root, image=image1)
label_for_image.place(x=400, y=0)

search=StringVar()
path = StringVar()
URL = None

def CheckInternet():
    try:
        urlopen("https://www.google.com/")
        return True
    except urllib.error.URLError as Error:
        return False

def Search():
    if CheckInternet():
        global URL
        URL=search.get()
        if URL[0:33:]=="https://www.youtube.com/playlist?":
            e2.focus()
            l = playlistURL(URL)
            length = int(l[0])
            Info = f'''Number of Videos: {length}'''
            l1.config(text=Info)
            l2.config(text="List of Videos...")
            t1.config(state=NORMAL)
            for i in range(0,length):
                dd = f'''{l[1][i]}\n'''
                t1.insert(END,dd)
            t1.config(state=DISABLED)
        else:
            showerror("Error","Please Paste Youtube Playlist URL Only")
    else:
        showerror("Error","Your system is not connected to the internet")
        
def V360():
    global URL
    destinationPath = path.get()
    if destinationPath == "" or destinationPath == None or destinationPath[0::] in "                                                   ":
        showerror("Error","Please Enter Destination Path")
    else:
        set360(URL,destinationPath)
        l3.config(text="Downloading Completed")

def V720():
    global URL
    destinationPath = path.get()
    if destinationPath == "" or destinationPath == None or destinationPath[0::] in "                                                   ":
        showerror("Error","Please Enter Destination Path")
    else:
        set720(URL,destinationPath)
        l3.config(text="Downloading Completed")

Label(root,text="Paste YouTube Videos Playlist Link:",font=('ArialBlack',11)).place(x=10,y=68)

e1 = Entry(root,font=('Calibri',15),width=96,textvariable=search)
e1.focus()
e1.place(x=20,y=90)
Button(root,text="Search",font=('Calibri',15),command=Search).place(x=1000,y=83)

l1 = Label(root,font=('Calibribold',15))
l1.place(x=20,y=118)
# https://www.youtube.com/playlist?list=PLRvEAoctXa6dIz135lrQUnF6YUYR8zlAm
l2 = Label(root,font=('Calibribold',13))
l2.place(x=30,y=145)

t1=Text(root,height=10,width=100,font=('Calibri',15),bd=10)
t1.config(state=DISABLED)
t1.place(x=30,y=170)

Label(root,text="Enter Destination path to download video",font=('Calibriblack',13)).place(x=30,y=440)
e2=Entry(root,font=('Calibriblack',15),bd=3,width=92,textvariable=path)
e2.place(x=30,y=470)

Button(root,text="Download All Videos 360p",font=('Calibri',20),command=V360).place(x=100,y=530)
Button(root,text="Download All Videos 720p",font=('Calibri',20),command=V720).place(x=700,y=530)

l3 = Label(root,font=('Calibri',15))
l3.place(x=40,y=500)

root.mainloop()