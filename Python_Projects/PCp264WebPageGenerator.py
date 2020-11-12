

f = open("UpdateWebpage.html", "w")
f.write("<html>\n\t<body>\n\t\t<h1>\n\t\t\tStay tuned for our amazing summer sale!\n\t\t</h1>\n\t</body>\n\b</html>")
f.close()

f = open("UpdateWebpage.html", "r")
print(f.read())



import os
import sys

webrowser.open("UpdateWebpage.html")

def open_new_tab(url):
    """Open url in a new page ("tab") of the default browser.
    If not possible, then the behavior becomes equivalent to open_new().
    """
    return open(url, 2)
