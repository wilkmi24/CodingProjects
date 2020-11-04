
import sqlite3

conn = sqlite3.connect('practice.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
       )")
    conn.commit()
conn.close()


conn = sqlite3.connect('practice.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_fname) VALUES ('myMovie.mpg')"), \
    cur.execute("INSERT INTO tbl_files(col_fname) VALUES ('information.docx')"), \
    cur.execute("INSERT INTO tbl_files(col_fname) VALUES ('World.txt')"), \
    cur.execute("INSERT INTO tbl_files(col_fname) VALUES ('myImage.png')"), \
    cur.execute("INSERT INTO tbl_files(col_fname) VALUES ('data.pdf')"), \
    cur.execute("INSERT INTO tbl_files(col_fname) VALUES ('Hello.txt')"), \
    cur.execute("INSERT INTO tbl_files(col_fname) VALUES ('myPhoto.jpg')") \

    conn.commit()

conn.close()



conn = sqlite3.connect('practice.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_files WHERE col_fname = '%txt'")
    Results = cur.fetchall()

    
    print(Results)
