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
    with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : session started\n')

    while mins != 1:
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

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' :  time elapsed\n')





root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()