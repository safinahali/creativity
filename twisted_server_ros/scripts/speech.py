from Tkinter import Tk, Label, Button
from Tkinter import *
import subprocess
import json
import csv
import datetime

class MyFirstGUI:


    def __init__(self, master):
        self.master = master
        master.title("Speech")

        self.label = Label(master, text="Animations")
        self.label.pack()


        self.greet_button = Button(master, text="Happy", command=self.happy)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Sad", command=self.sad)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Excited", command=self.excited)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Curious", command=self.curious)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Affection", command=self.affection)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Confused", command=self.confused)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Yep", command=self.yep)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Dance", command=self.dance)
        self.greet_button.pack()     

        self.greet_button = Button(master, text="Worried", command=self.worried)
        self.greet_button.pack() 


        self.greet_button = Button(master, text="Look Around", command=self.lookfront)
        self.greet_button.pack()  

        self.greet_button = Button(master, text="Look up", command=self.lookup)
        self.greet_button.pack()     

        self.greet_button = Button(master, text="Look Down", command=self.lookdown)
        self.greet_button.pack()      

        self.label = Label(master, text="Emoji")
        self.label.pack()

        self.greet_button = Button(master, text="Sample", command=self.sample)
        self.greet_button.pack()


        self.label = Label(master, text="\n \n")
        self.label.pack()


        

        c = Button(master, text="Close", command=master.quit)
        c.pack() 

            


        self.label = Label(master, text="\n Enter your text here")
        self.label.pack()


	e = Entry(master)
	e.pack()
	e.focus_set()


	def callback():
	    print e.get()
	    textentry = e.get()
	    data = {
	    	"currentspeech" :[[textentry]]
	    }
	    with open('data.json', 'w') as outfile:
    		json.dump(data, outfile)

            with open('datalog.csv', 'a') as file:
                file.write(str(datetime.datetime.now()) + " : [textentry] : " + str(textentry) + "\n")

	    subprocess.call('./test_jibo_anim.py data.json currentspeech', shell=True)

	b = Button(master, text="play", width=10, command=callback)
	b.pack()

	mainloop()
	e = Entry(master, width=50)

	# text = content.get()
	# content.set(text)
        


    def happy(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json happy', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : happy\n')

    def sad(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json sad', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : sad\n')

    def excited(self):
        print("Excited!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json excited', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : excited\n')

    def curious(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json curious', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : curious\n')

    def affection(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json affection', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : affection\n')

    def confused(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json confused', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : confused\n')

    def yep(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json yep', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : yep\n')


    def dance(self):
        print("Dance!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json dance', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : dance\n')


    def worried(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json worried', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : worried\n')


    def lookfront(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json lookfront', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : lookfront\n')


    def lookup(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json lookup', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : lookup\n')

    def lookdown(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json lookdown', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : lookdown\n')


    def sample(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json sample', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : emoji\n')




root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
