from Tkinter import Tk, Label, Button
from Tkinter import *
import subprocess
import json
import csv
import datetime


class MyFirstGUI:


    with open('datalog.csv', 'a') as file:
        file.write('\n' + str(datetime.datetime.now()) + ' : NEW Participant creative\n')

    def __init__(self, master):
        self.master = master
        master.title("Creative Phrases")
	
        self.label = Label(master, text="Questions")
        self.label.pack()

        self.greet_button = Button(master, text="Why did you do that?", command=self.q1)
        self.greet_button.pack()

        self.greet_button = Button(master, text="What will you do next?", command=self.q2)
        self.greet_button.pack()

        self.greet_button = Button(master, text="What are you trying to make?", command=self.q3)
        self.greet_button.pack()

        self.greet_button = Button(master, text="How are you going to do that?", command=self.q4)
        self.greet_button.pack()

        self.label = Label(master, text="\n Creative Prompts")
        self.label.pack()

        self.greet_button = Button(master, text="Can you think of another way to do this?", command=self.c1)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Can you think of other things you can make the rover do?", command=self.c2)
        self.greet_button.pack()

        self.greet_button = Button(master, text="What else can you make the rover do when an object is near? ", command=self.c3)
        self.greet_button.pack()

        self.greet_button = Button(master, text="What new things can we use this for?", command=self.c4)
        self.greet_button.pack()

        self.greet_button = Button(master, text="There might be a better way to do that.", command=self.c5)
        self.greet_button.pack() 

        self.greet_button = Button(master, text="Make your own obstacle for the sensor", command=self.c7)
        self.greet_button.pack() 

        self.greet_button = Button(master, text="That is such a great idea.", command=self.c6)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Good job.", command=self.c8)
        self.greet_button.pack()

        # self.greet_button = Button(master, text="Make", command=self.c6)
        # self.greet_button.pack()         

        self.label = Label(master, text="\n FAQ")
        self.label.pack()

        self.greet_button = Button(master, text="Bluetooth", command=self.f1)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Batteries", command=self.f2)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Parts", command=self.f3)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Wrong Sesnor", command=self.f4)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Sensor before motor", command=self.f5)
        self.greet_button.pack()


        self.greet_button = Button(master, text="Red button to stop", command=self.f6)
        self.greet_button.pack()

        self.label = Label(master, text="\n Frequent Phrases")
        self.label.pack()


        self.greet_button = Button(master, text="Correct", command=self.correct)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Don't know", command=self.dontknow)
        self.greet_button.pack()

        self.greet_button = Button(master, text="I am Listening", command=self.listening)
        self.greet_button.pack()


        self.label = Label(master, text="\n \n")
        self.label.pack()


        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


    def q1(self):
        print("q1")
        subprocess.call('./test_jibo_anim.py scripts/speech.json q1', shell=True)
        
        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : q1\n')

    def q2(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json q2', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : q2\n')

    def q3(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json q3', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : q3\n')


    def q4(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json q4', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : q4\n')

    def c1(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c1', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : c1\n')

    def c2(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c2', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : c2\n')


    def c3(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c3', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : c3\n')

    def c4(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c4', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : c4\n')

    def c5(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c5', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : c5\n')


    def c6(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c6', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : c6\n')



    def c7(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c7', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : c7\n')


    def c8(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c8', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : c8\n')


    def f1(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json f1', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : f1\n')

    def f2(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json f2', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : f2\n')

    def f3(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json f3', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : f3\n')



    def f4(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json f4', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : f4\n')


    def f5(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json f5', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : f5\n')



    def f6(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json f6', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : f6\n')





    def good(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json good', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : good\n')


    def dontknow(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json dontknow', shell=True)


        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : dontknow\n')




    def correct(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json correct', shell=True)
    

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : correct\n')


    
    def listening(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json listening', shell=True)
    

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : listening\n')




root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
