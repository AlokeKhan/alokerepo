print('hello world')
import tkinter 
from tkinter import *
from tkinter.messagebox import *
from tkinter.tix import IMAGETEXT
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

    blck = Toplevel()
    blck.title('get blocked')
    blck.geometry('400x300')

    Label(blck, text="Block a Site", font =("Impact", 15)).place(x=100,y=100)
    Label(blck, text="Type Website Name Below", font =("Impact", 15)).place(x=100,y=50)

    sites = Text(blck, width =30, height = 4)
    sites.place(x=100,y=140)

    block_btn = Button(blck, text="block", font =('Impact',12), bg ='MidnightBlue',fg='White', command = lambda:
 block_websites(sites.get('1.0',END)))
    block_btn.place(x=100,y=230)
    def block_websites(websites):
        global blck_sites
        with open('blocked_websites.txt', 'r+') as blocked_websites:
            blck_sites = blocked_websites.readlines()

        host_file= host_files['Windows']
        sites_to_block = list(websites.split(','))

        with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
            blocked_websites_txt.seek(0,2)
            for site in sites_to_block:
                blocked_websites_txt.write(site)

        with open(host_file, 'r+') as hostfile:
            content_in_file = hostfile.read()

            for site in sites_to_block:
                if site not in content_in_file:
                    hostfile.write(localhost + '\t' + site + '\n')
                    showinfo('Mission Accomplished', message = 'Websites have been blocked')
                else:
                    showinfo('Stoopid', message = 'The website already done been blocked')

def unblock(win):
    global unblock_btn
    ubwin= Toplevel(win)
    ubwin.title('unblock a website >:)')
    ubwin.geometry('500x200')

    Label(ubwin, text='Unblock the Websites you desire', font=('Helvetica',16)).place(x=80,y=0)
    Label(ubwin, text='Choose the desired website:', font=('Helvetica',16)).place(x=80,y=70)

    blck_sites_strvar = StringVar(ubwin)
    blck_sites_strvar.set(blck_sites[0])

    dropdown = OptionMenu(ubwin,blck_sites_strvar,*blck_sites)
    dropdown.config(width=20)
    dropdown.place(x=60,y=100)

    unblock_btn = Button(ubwin, text="unblock", font =('Impact',12), bg ='MidnightBlue',fg='Black', command = lambda:
  unblock_websites(blck_sites_strvar.get()))
    unblock_btn.place(x=100,y=200)
    def unblock_websites(websites_to_unblock):
        host_file= host_files('Windows')

        with open (host_file, 'r+') as hostfile:
            content_in_file = hostfile.readlines()
            hostfile.seek(0)

            for line in content_in_file:
                if not any(site in line for site in websites_to_unblock):
                    hostfile.write(line)

                hostfile.truncate()

        with open ('blocked_websites.txt', 'r+') as blocked_websites_txt:
            file_content = blocked_websites_txt.readlines()
            blocked_websites_txt.seek(0)

            for line in file_content:
                if not any(site in line for site in websites_to_unblock):
                    blocked_websites_txt.write(line)

                blocked_websites_txt.truncate()

        Label(ubwin, text='Website Blocked!', font=("Times", 13), bg='Aquamarine').place()

Label(root, text="Aloke's Blocker of Websites", font=("Helvetica", 16)).place(x=45, y=0)
Label(root, text='What is you want', font=("Times New Roman", 16)).place(x=90, y=40)
Button(root,text='Block website', font=('Times',16), bg='SpringGreen4', command = lambda:
block(root)).place(x=110, y=100)
   
Button(root,text='Unblock website', font=('Times',16), bg='SpringGreen4', command = lambda:
unblock(root)).place(x=110, y=150)

# you need to call root.update() and root.mainloop() to actually 
# open the window
root.update()
root.mainloop()
