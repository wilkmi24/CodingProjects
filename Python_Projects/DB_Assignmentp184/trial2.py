
import sqlite3

conn = sqlite3.connect('trial2.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.dpf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileList TEXT \
       )")
    conn.commit()
conn.close()



conn = sqlite3.connect('practice.db')

with conn:
    cur = conn.cursor()
    conn.commit()
    
conn.close()


