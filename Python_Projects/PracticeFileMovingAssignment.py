import shutil
import os
import time
from shutil import copytree
from tkinter import filedialog
from tkinter import *



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Moving Files')
        self.master.config(bg = 'lightgray')
        
        self.varSource = StringVar()
        self.varDestination = StringVar()

        self.lblSource = Label(self.master,text='Source Folder: ', font=('Helvetica', 16), fg='black', bg = 'lightgray')
        self.lblSource.grid(row=0, column=0,padx=(30,0),pady=(30,0))
        
        self.lblDestination = Label(self.master,text='Destination Folder: ', font=('Helvetica', 16), fg='black', bg = 'lightgray')
        self.lblDestination.grid(row=1, column=0,padx=(30,0),pady=(30,0))

        self.lblDisplay = Label(self.master, text='', font=('Helvetica', 16),fg='black', bg = 'lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0),pady=(30,0))

        self.txtSource = Entry(self.master,text=self.varSource, font=("Helvetica", 16),fg = 'black', bg='lightblue')
        self.txtSource.grid(row=0, column=1,padx=(30,0),pady=(30,0))

        self.txtDestination = Entry(self.master,text=self.varDestination, font=("Helvetica", 16),fg = 'black', bg='lightblue')
        self.txtDestination.grid(row=1, column=1,padx=(30,0),pady=(30,0))

        self.btnSearch = Button(self.master, text="Search", width=10, height=2, command=self.search)
        self.btnSearch.grid(row=2, column=1,padx=(0,0),pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90),pady=(30,0), sticky=NE)

    def search(self):
        filename = filedialog.askdirectory()
        print(filename)
        return filename
    

    def cancel(self):
        self.master.destroy()




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
   




root = Tk()
v = StringVar()
button2 = Button(text="Browse", command=browse_button).grid(row=0, column=3)

mainloop()

SECONDS_IN_DAY = 24 * 60 * 60

src = '/Users/mindywilkens/Desktop/FolderA/'
dst = '/Users/mindywilkens/Desktop/FolderB/'

now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(src):
    src_fname = os.path.join(src, fname)
    if last_mod_time(src_fname) > before:
        dst_fname = os.path.join(dst, fname)
        shutil.move(src_fname, dst_fname)
