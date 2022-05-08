import pyttsx3
import os

import pypdf2
import datetime
from tkinter.filedialog import *
book=askopenfilename()
pdfreader=pypdf2.pdffilereader(book)
pages=pdfreader.numpages

for num in range(0,pages):
    page=pdfreader.getpage(num)
    text=page.extracttext()
    print("pdf content is:",text)
    player=pyttsx3.init()
    player.say(text)
    player.runandwait()
strtime=datetime.datetime.now().strftime("%h:%m:%s")
f=open(r"c:\users\hp\desktop\pdfrhistory.txt","r+")
z=[]
r=[]
r.append(book)
r.append(strtime)
z.append(r)

f.write(str(book)+str(strtime)+str("   ***   "))
s=f.readlines()
print("your activity:",r)

