
import sqlite3

conn = sqlite3.connect('trial.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_Name TEXT \
       )")
    conn.commit()


conn = sqlite3.connect('trial.db')



fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.dpf','myPhoto.jpg')

for x in fileList:
            if x.endswith('.txt'):
                with conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO tbl_files (file_Name) Values (?)", (x,))
                        
conn.close()

