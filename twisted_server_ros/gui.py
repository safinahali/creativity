
from Tkinter import Tk, Label, Button
from Tkinter import *
import subprocess
import json



class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
	
        self.label = Label(master, text="control")
        self.label.pack()


        self.greet_button = Button(master, text="Start", command=self.greet)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Intro", command=self.introduction)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Your Turn", command=self.turn)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Time", command=self.time)
        self.greet_button.pack()

        self.greet_button = Button(master, text="More", command=self.more)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Good", command=self.good)
        self.greet_button.pack()	

        self.label = Label(master, text="creative")
        self.label.pack()

        self.greet_button = Button(master, text="Pic1", command=self.c1)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Pic2", command=self.c2)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Pic3", command=self.c3)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Pic4", command=self.c4)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Pic5", command=self.c5)
        self.greet_button.pack()        

        self.label = Label(master, text="Non creative")
        self.label.pack()

        self.greet_button = Button(master, text="Pic1", command=self.n1)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Pic2", command=self.n2)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Pic3", command=self.n3)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Pic4", command=self.n4)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Pic5", command=self.n5)
        self.greet_button.pack()   

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

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

	    subprocess.call('./test_jibo_anim.py data.json currentspeech', shell=True)

	b = Button(master, text="get", width=10, command=callback)
	b.pack()

	mainloop()
	e = Entry(master, width=50)

	text = content.get()
	content.set(text)





    def greet(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json greeting', shell=True)

    def introduction(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json introduction', shell=True)

    def turn(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json turn', shell=True)

    def time(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json time', shell=True)

    def c1(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json c1', shell=True)

    def c2(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json c2', shell=True)

    def c3(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json c3', shell=True)

    def c4(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json c4', shell=True)

    def c5(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json c5', shell=True)

    def n1(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json n1', shell=True)

    def n2(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json n2', shell=True)

    def n3(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json n3', shell=True)

    def n4(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json n4', shell=True)

    def n5(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json n5', shell=True)

    def more(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json more', shell=True)

    def good(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py speech.json good', shell=True)





	



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
