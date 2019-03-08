from Tkinter import Tk, Label, Button
from Tkinter import *
import subprocess
import json
import csv
import datetime


class MyFirstGUI:
    def __init__(self, master):

        with open('datalog.csv', 'a') as file:
            file.write('\n' + str(datetime.datetime.now()) + ' : NEW Participant noncreative\n')

        self.master = master
        master.title("Non Creative Phrases")   

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


        self.label = Label(master, text="\n \n")
        self.label.pack()


        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


    def q1(self):
        print("Greetings!")
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


    def c1(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c1', shell=True)

    def c2(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c2', shell=True)

    def c3(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c3', shell=True)

    def c4(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c4', shell=True)

    def c5(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c5', shell=True)


    def c6(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json c6', shell=True)

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
