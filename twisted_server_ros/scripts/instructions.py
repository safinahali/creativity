from Tkinter import Tk, Label, Button
from Tkinter import *
import subprocess
import json
import csv
import datetime

class MyFirstGUI:

    def __init__(self, master):
        self.master = master
        master.title("Instructions")
	
        self.label = Label(master, text="Introduction")
        self.label.pack()

        self.greet_button = Button(master, text="Greeting", command=self.greet)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Intro", command=self.introduction)
        self.greet_button.pack()

        self.label = Label(master, text="Construction")
        self.label.pack()

        self.greet_button = Button(master, text="Parts", command=self.parts)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Attach Sensor", command=self.attachsensor)
        self.greet_button.pack()     

        self.greet_button = Button(master, text="Attach Sensor Wire", command=self.attachsensorwire)
        self.greet_button.pack()  

        self.label = Label(master, text="Programming")
        self.label.pack()

        self.greet_button = Button(master, text="Tablet Start", command=self.tablet)
        self.greet_button.pack()


        self.greet_button = Button(master, text="Bluetooth", command=self.bluetooth)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Interface Explain", command=self.interface)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Motor", command=self.motor)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Motor Value", command=self.motor2)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Sensor", command=self.sensor)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Sensor add before motor", command=self.sensor2)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Sensor orange button", command=self.sensor3)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Sensor try", command=self.sensor4)
        self.greet_button.pack()



        self.greet_button = Button(master, text="Explore", command=self.explore)
        self.greet_button.pack()

        self.label = Label(master, text="\n After 18-20 minutes \n")
        self.label.pack()

        self.end = Button(master, text="End speech", command=self.end)
        self.end.pack()

        self.label = Label(master, text="\n \n")
        self.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    

    def turn(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json turn', shell=True)


        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : turn\n')


    def time(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json time', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : time\n')



    def more(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json more', shell=True)


        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : more\n')
        

    def good(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json good', shell=True)

        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : good\n')



    def greet(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json greeting', shell=True)


    def introduction(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json introduction', shell=True)


    def parts(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json parts', shell=True)



    def attachsensor(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json attachsensor', shell=True)


    def attachsensorwire(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json attachsensorwire', shell=True)

    def tablet(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json tablet', shell=True)

    def bluetooth(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json f1', shell=True)

    def interface(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json interface', shell=True)

    def motor(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json motor', shell=True)

    def motor2(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json motor2', shell=True)

    def sensor(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json sensor', shell=True)

    def sensor2(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json sensor2', shell=True)

    def sensor3(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json sensor3', shell=True)

    def sensor4(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json sensor4', shell=True)


    def explore(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json explore', shell=True)

    def end(self):
        print("Greetings!")
        subprocess.call('./test_jibo_anim.py scripts/speech.json end', shell=True)


        with open('datalog.csv', 'a') as file:
            file.write(str(datetime.datetime.now()) + ' : end\n')



	



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
