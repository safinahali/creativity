import time
import ctypes 

from Tkinter import Tk, Label, Button
from Tkinter import *
import subprocess
import json
import csv
import datetime


run = raw_input("Type start when you begin the study >> ")

mins = 0
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins != 18:
        print "Minutes elapsed : ", mins
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1

    # Bring up the dialog box here
    class MyFirstGUI:

        def __init__(self, master):
            self.master = master
            master.title("STOP")


            self.label = Label(master, text="Time is up. \n Run the 'END' instruction in the 'Instructions' tab soon.", background = "red")
            self.label.pack()



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()