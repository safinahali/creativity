from Tkinter import Tk, Label, Button
from Tkinter import *
import subprocess
import json
import csv
import datetime

class MyFirstGUI:


    def __init__(self, master):
        self.master = master
        master.title("Notes")



        c = Button(master, text="Close", command=master.quit)
        c.pack() 


        self.label = Label(master, text="\n Enter your notes here")
        self.label.pack()


	e = Entry(master)
	e.pack()
	e.focus_set()


	def callback():
	    print e.get()
	    textentry = e.get()
	    data = {
	    	"notes" :[[textentry]]
	    }

	    with open('data.json', 'w') as outfile:
    		json.dump(data, outfile)

            with open('datalog.csv', 'a') as file:
                file.write(str(datetime.datetime.now()) + " : [notes] : " + str(textentry) + "\n")

	    # subprocess.call('./test_jibo_anim.py data.json currentspeech', shell=True)

	b = Button(master, text="note", width=10, command=callback)
	b.pack()

	mainloop()
	e = Entry(master, width=50)

	# text = content.get()
	# content.set(text)
        




root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
