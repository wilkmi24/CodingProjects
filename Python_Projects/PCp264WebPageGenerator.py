import tkinter
from tkinter import *
import webbrowser






   


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Updating Webpage')
        self.master.config(bg = 'lightgray')
        
        self.varMessage = StringVar()
        
        self.lblSource = Label(self.master,text='Enter your message here: ', font=('Helvetica', 16), fg='black', bg = 'lightgray')
        self.lblSource.grid(row=0, column=0,padx=(30,0),pady=(30,0))
        
        self.lblDisplay = Label(self.master, text='', font=('Helvetica', 16),fg='black', bg = 'lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0),pady=(30,0))

        self.txtMessage = Entry(self.master,text=self.varMessage, font=("Helvetica", 16),fg = 'black', bg='white')
        self.txtMessage.grid(row=0, column=1,padx=(30,0),pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submitButton)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0),pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.Cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90),pady=(30,0), sticky=NE)

    
    def submitButton(self):
        f = open("UpdateWebpage.html", "w")
        f.write("<html>\n\t<body>\n\t\t<h1>\n\t\t\tStay tuned for our amazing summer sale!\n {} \t\t</h1>\n\t</body>\n\b</html>".format(self.txtMessage.get()))
        f.close()
        webbrowser.open_new_tab('UpdateWebpage.html')
        print('test')
         

    def Cancel(self):
        self.master.destroy()




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()






    
