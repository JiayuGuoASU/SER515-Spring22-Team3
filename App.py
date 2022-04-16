from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import subprocess
from subprocess import call
import os, signal

from numpy import size

root = Tk()


def manual():
    try:
        subprocess.Popen(["xterm", "-e", "./script/manual.sh"])

    except:
        subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./manual.sh; read"])


def run():
    try:
        subprocess.Popen(["xterm", "-e", "./script/fullrun.sh"])

    except:
        subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./fullrun.sh; read"])
    button21.config(state=NORMAL)


def auto():
    try:
        subprocess.Popen(["xterm", "-e", "./script/automatic.sh"])

    except:
        subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./automatic.sh; read"])


def getSLAM():
    try:
        subprocess.Popen(["xterm", "-e", "./script/slam.sh"])

    except:
        subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./slam.sh; read"])
    button3.config(state=NORMAL)
    button22.config(state=NORMAL)


def downloadMap():
    try:
        subprocess.Popen(["xterm", "-e", "./script/downloadmap.sh"])

    except:
        subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./downloadmap.sh; read"])


def close():
    root.destroy()


def mapConfig():
    mapName = mapCombo.get() + ".sdf"
    call(["python3", "MapChoose.py", mapName])
    button12.config(state=NORMAL)


def roverConfig():
    call(["python3", "assemble_rover.py"])
    buttonSub.config(state=NORMAL)


def controlAlgorithm():
    algo = algoCombo.get()
    print("you select Algorithm: " + str(algo))
    subprocess.Popen(["python3", "algorithm.py", str(algo)])


root.geometry("550x850")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

labelMain = Label(frame, text="Anton control option", font=("Helvetica", 20))
labelMain.pack()

labelDiv1 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv1.pack()

labelSub = Label(frame, text="Step 1: Configuration", font=("Helvetica", 16))
labelSub.pack(padx=10, pady=10)

lablel11 = Label(frame, text="Choose a Map and build it:", font=("Helvetica", 12))
lablel11.pack(padx=10, pady=10)

mapList = ["RobotCupField", "GasStation", "Museum"]
mapCombo = Combobox(frame, values=mapList)
mapCombo.current(0)

mapCombo.state(["readonly"])
mapCombo.pack()

button11 = Button(frame, text="Build Map", command=mapConfig)
button11.pack(padx=10, pady=10)

label12 = Label(frame, text="Rover configuration:", font=("Helvetica", 12))
label12.pack(padx=10, pady=10)

button12 = Button(frame, text="Configure", command=roverConfig)
button12.pack()
# disable button
button12.config(state=DISABLED)

labelDiv2 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv2.pack()

label2 = Label(frame, text="Step 2: Build the project", font=("Helvetica", 16))
label2.pack(padx=10, pady=10)

buttonSub = Button(frame, text="Build & launch", command=run)
buttonSub.pack()
buttonSub.config(state=DISABLED)

labelDiv211 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv211.pack()

label21 = Label(frame, text="Step 3: Launch SLAM", font=("Helvetica", 16))
label21.pack(padx=10, pady=10)

button21 = Button(frame, text="Start Slam", command=getSLAM)
button21.pack()
button21.config(state=DISABLED)

button22 = Button(frame, text="Save map", command=downloadMap)
button22.pack()
button22.config(state=DISABLED)

labelDiv31 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv31.pack()

label31 = Label(frame, text="Step 4: Run the Robot with moving algorithm", font=("Helvetica", 16))
label31.pack(padx=10, pady=10)

algoList = ["Manual", "Automatic"]
algoCombo = Combobox(frame, values=algoList)
algoCombo.current(0)

algoCombo.state(["readonly"])
algoCombo.pack(padx=10, pady=4)


button3 = Button(frame, text="Select control", command=controlAlgorithm)
button3.pack(padx=5, pady=5)
button3.config(state=DISABLED)


labelDiv4 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv4.pack()

label4 = Label(frame, text="END", font=("Helvetica", 16))
label4.pack(padx=10, pady=10)


button4 = Button(frame, text="close", command=close)
button4.pack(padx=5, pady=5)

root.title("Autonomous rover control")
root.mainloop()
