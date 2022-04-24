print('hello world')
import tkinter 
from tkinter import *
from tkinter.messagebox import *

host_files = {
    'Windows' :r"C:\Windows\System32\drivers\etc\hosts"

}
localhost ='127.0.0.1'

root = Tk()
root.title("Aloke's Awe-Inspiring Website Blocker")
root.geometry('500x400')
root.wm_resizable(True, True)

def block(win):
    print('entered this case')
    global img
    top = Toplevel()
    top.title('get blocked')
    img = tkinter.ImageTk.PhotoImage(Image.open("Pictures/Capture.png"))
    lbl = Label(top, image = img).pack()

Label(root, text="Aloke's Blocker of Websites", font=("Helvetica", 16)).place(x=45, y=0)
Label(root, text='What is you want', font=("Times New Roman", 16)).place(x=90, y=40)
Button(root,text='Block website', font=('Times',16), bg='SpringGreen4', command = lambda:
block(root)).place(x=110, y=100)
   
#Button(root,text='Block website', font=('Times',16), bg='SpringGreen4', command = lambda:
#unblock(root)).place(x=110, y=100)

