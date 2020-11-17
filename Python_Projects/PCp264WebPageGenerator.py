

f = open("UpdateWebpage.html", "w")
f.write("<html>\n\t<body>\n\t\t<h1>\n\t\t\tStay tuned for our amazing summer sale!\n\t\t</h1>\n\t</body>\n\b</html>")
f.close()

f = open("UpdateWebpage.html", "r")
print(f.read())


import webbrowser

webbrowser.open_new_tab('UpdateWebpage.html')
webbrowser.open_new('UpdateWebpage.html')    


import tkinter
from tkinter import *


win = Tk('UpdatetoWebpage')
f = Frame(win)
l = Label(win, text='Please enter your message here')
l.pack()
f.pack()
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()
b1 = Button(f, text='Submit')
b1.pack()
v.get()

def submitButton():
    print(v.get())


b1.configure(command=submitButton)






    
