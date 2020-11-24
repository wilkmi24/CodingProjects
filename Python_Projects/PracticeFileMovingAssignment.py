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
        self.master.geometry('{}x{}'.format(600, 300))
        self.master.title('Moving Files')
        self.master.config(bg = 'lightgray')
        self.varSource = StringVar()
        self.varDestination = StringVar()

        self.btnSource = Button(self.master,text='Browse... ', font=('Helvetica', 16), fg='black', bg = 'lightgray', command=self.BrowseSrc)
        self.btnSource.grid(row=0, column=0,padx=(30,0),pady=(30,0))
        
        self.btnDestination = Button(self.master,text='Browse... ', font=('Helvetica', 16), fg='black', bg = 'lightgray', command=self.BrowseDst)
        self.btnDestination.grid(row=1, column=0,padx=(30,0),pady=(30,0))

        self.lblDisplay = Label(self.master, text='', font=('Helvetica', 16),fg='black', bg = 'lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0),pady=(30,0))

        self.txtSource = Entry(self.master,text=self.varSource, font=("Helvetica", 16),fg = 'black', bg='white', width=30)
        self.txtSource.grid(row=0, column=1,padx=(30,0),pady=(30,0))

        self.txtDestination = Entry(self.master,text=self.varDestination, font=("Helvetica", 16),fg = 'black', bg='white', width=30)
        self.txtDestination.grid(row=1, column=1,padx=(30,0),pady=(30,0))

        self.btnCheck = Button(self.master, text="Check for Files", font=('Helvetica', 16), fg='black', bg = 'lightgray', command=self.Check)
        self.btnCheck.grid(row=2, column=0,padx=(30,0),pady=(30,0))

        self.btnClose = Button(self.master, text="Close Program", font=('Helvetica', 16), fg='black', bg = 'lightgray', command=self.CloseProgram)
        self.btnClose.grid(row=2, column=2,padx=(30,0),pady=(30,0))

    def BrowseSrc(self):
        filename = filedialog.askdirectory()
        e = self.txtSource
        e.delete(0,END)
        e.insert(0,filename)
        return

    def BrowseDst(self):
        filename = filedialog.askdirectory()
        e = self.txtDestination
        e.delete(0,END)
        e.insert(0,filename)
        
    def Check(self):
        src = '/Users/mindywilkens/Desktop/FolderA/'
        dst = '/Users/mindywilkens/Desktop/FolderB/'
        files = os.listdir(src)

        for i in files:
            shutil.move(src+i,dst)
     

    def CloseProgram(self):
        self.master.destroy()




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
   
