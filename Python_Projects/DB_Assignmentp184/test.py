
import sqlite3

conn = sqlite3.connect('trial.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_Name TEXT \
       )")
    conn.commit()
conn.close()


conn = sqlite3.connect('trial.db')

with conn:
    cur = conn.cursor()


    conn.commit()
    
conn.close()



conn = sqlite3.connect('trial.db')
with conn:
    cur = conn.cursor()
    cur.execute("Select * FROM tbl_files WHERE file_Name = '%txt' ")
    fileList = cur.fetchall()
    for i in fileList:
        files = 


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.dpf','myPhoto.jpg')

