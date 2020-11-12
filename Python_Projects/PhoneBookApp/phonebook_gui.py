
# Be sure to importt our other modules
# so we can have access to them
import phonebook_main
import phonebook_func

def load_gui(self):

    self.lbl_fname = tk.Label(self.master,text='First Name: ')
    self.lbl_fname.grid(row=0, column=0, padx=(27,0), pady(10,0), sticky=N+W)

    self.lbl_lname = tk.Label(self.master,text='Last Name: ')
    self.lbl_lname.grid(row=2, column=0, padx=(27,0), pady(10,0), sticky=N+W)

    self.lbl_phone = tk.Label(self.master,text='Phone Number: ')
    self.lbl_phone.grid(row=4, column=0, padx=(27,0), pady(10,0), sticky=N+W)

    self.lbl_email = tk.Label(self.master,text='Email Address: ')
    self.lbl_email.grid(row=6, column=0, padx=(27,0), pady(10,0), sticky=N+W)

    self.lbl_user = tk.Label(self.master,text='User: ')
    self.lbl_user.grid(row=0, column=2, padx=(0,0), pady(10,0), sticky=N+W)



    self.text_fname = tk.Entry(self.master,text='')
    self.text_fname.grid(row=1, column=0,rowspan=1, columnspan=2, padx=(30,40), pady(0,0), sticky=N+E+W)

    self.text_lname = tk.Entry(self.master,text='')
    self.text_lname.grid(row=3, column=0,rowspan=1, columnspan=2, padx=(30,40), pady(0,0), sticky=N+E+W)

    self.text_phone = tk.Entry(self.master,text='')
    self.text_phone.grid(row=5, column=0,rowspan=1, columnspan=2, padx=(30,40), pady(0,0), sticky=N+E+W)

    self.text_email = tk.Entry(self.master,text='')
    self.text_email.grid(row=7, column=0,rowspan=1, columnspan=2, padx=(30,40), pady(0,0), sticky=N+E+W)

    # Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.1stList1 = Listbox(self.master, exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.1stList1.bind('<<ListboxSelect>>',lambda event: phonebook_func.onSelect(self,event))
    self.scrollbar1.config(command=self.1stList1.yview)
    self.scrollbar1.grid(row=1, column=5,rowspan=7, columnspan=1, padx=(0,0), pady(0,0), sticky=N+E+S)
    self.1stList1.grid(row=1, column=2,rowspan=7, columnspan=3, padx=(0,0), pady(0,0), sticky=N+E+S+W)

    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: phonebook_func.addToList(self))
    self.btn_add.grid(row=5, column=0, padx=(25,0), pady(45,10), sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2text='Update'command=lambda:phonebook_func.onUpdate(self))
    self.btn_update.grid(row=8, column=1, padx=(15,0), pady(45,10), sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2text='Delete'command=lambda:phonebook_func.onDelete(self))
    self.btn_delete.grid(row=8, column=2, padx=(15,0), pady(45,10), sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2text='Close'command=lambda:phonebook_func.ask_quit(self))
    self.btn_close.grid(row=8, column=4, padx=(15,0), pady(45,10), sticky=E)

    phonebook_func.create_db(self)
    phonebook_func.onRefresh(self)

    

    