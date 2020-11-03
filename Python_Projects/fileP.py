
import os
import datetime
def modification_date(test):
    t = os.path.getmtime(test)
    return datetime.datetime.fromtimestamp(t)
