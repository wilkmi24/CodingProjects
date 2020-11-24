#set where the source of the files are
src = '/Users/mindywilkens/Desktop/FolderA/'

#set the destination path to folderB
dst = '/Users/mindywilkens/Desktop/FolderB/'
files = os.listdir(src)

for i in files:
    shutil.move(src+i, dst)




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


src = self.txtSource.get() + '/'
dst = self.txtDestination.get() + '/'

for i in files:
    absPath = os.path.join(src, i)
    shutil.copy(absPath, dst)


    import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%M %m/%d/%Y"
created = 'here'
dest = 'there'

for root, dirs,files in os.walk(created):  
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
            shutil.move(path, dest)
            # this is actual move

datetime.timedelta

os.path.getmtime(absPath)


SECONDS_IN_DAY = 24 * 60 * 60

src = "C:\Users\Student\Desktop\FolderA"
dst = "C:\Users\Student\Desktop\FolderB"

now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(src):
    src_fname = os.path.join(src, fname)
    if last_mod_time(src_fname) > before:
        dst_fname = os.path.join(dst, fname)
        shutil.move(src_fname, dst_fname)

timestamp = date.fromtimestamp(1326244364)

from datetime import datetime, date

mod_timestamp = datetime.datetime.fromtimestamp(path.getmtime(<YOUR_PATH_HERE>))
            
