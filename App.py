from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import subprocess
from subprocess import call
import os, signal

from numpy import size

root = Tk()

processes = []


def manual():
    try:
        tmp = subprocess.Popen(["xterm", "-e", "./script/manual.sh"])
        processes.append(tmp.pid)
    except:
        tmp = subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./manual.sh; read"])
        processes.append(tmp)


def run():
    try:
        tmp = subprocess.Popen(["xterm", "-e", "./script/fullrun.sh"])
        processes.append(tmp)
    except:
        tmp = subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./fullrun.sh; read"])


def auto():
    try:
        tmp = subprocess.Popen(["xterm", "-e", "./script/automatic.sh"])
        processes.append(tmp)
    except:
        tmp = subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./automatic.sh; read"])
        processes.append(tmp)


def getSLAM():
    try:
        tmp = subprocess.Popen(["xterm", "-e", "./script/slam.sh"])
        processes.append(tmp)
    except:
        tmp = subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./slam.sh; read"])
        processes.append(tmp)


def downloadMap():
    try:
        tmp = subprocess.Popen(["xterm", "-e", "./script/download_map.sh"])
        processes.append(tmp)
    except:
        tmp = subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./download_map.sh; read"])
        processes.append(tmp)


def close():
    for process in processes:
        os.kill(process, signal.SIGINT)
    sys.exit(0)


def mapConfig():
    mapName = mapCombo.get() + ".sdf"
    call(["python3", "MapChoose.py", mapName])


def roverConfig():
    call(["python3", "assemble_rover.py"])


def controlAlgorithm():
    algo = algoCombo.get()
    print("you select Algorithm: " + str(algo))
    tmp = subprocess.Popen(["python3", "algorithm.py", str(algo)])
    processes.append(tmp.pid)
    # subprocess.Popen(["xterm", "-e","python3 algorithm.py"])


root.geometry("500x800")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

labelMain = Label(frame, text="Anton control option", font=("Helvetica", 20))
labelMain.pack(padx=10, pady=10)

labelDiv1 = Label(frame, text="_______________________________________", font=("Helvetica", 20))

labelDiv1.pack()
labelSub = Label(frame, text="First step: Configuration", font=("Helvetica", 16))
labelSub.pack(padx=10, pady=10)

lablel11 = Label(frame, text="Choose a Map and Click Build Map:", font=("Helvetica", 16))
lablel11.pack(padx=10, pady=10)

mapList = ["RobotCupField", "GasStation", "Museum"]
mapCombo = Combobox(frame, values=mapList)
mapCombo.current(0)

mapCombo.state(["readonly"])
mapCombo.pack()

bubtton11 = Button(frame, text="Build Map", command=mapConfig)
bubtton11.pack()

label12 = Label(frame, text="Rover configuration", font=("Helvetica", 16))
label12.pack(padx=10, pady=10)

bubtton12 = Button(frame, text="Rover configuration", command=roverConfig)
bubtton12.pack()

labelDiv2 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv2.pack()

label2 = Label(frame, text="Second step: Build the project", font=("Helvetica", 16))
label2.pack(padx=10, pady=10)

buttonSub = Button(frame, text="Build & launch", command=run)
buttonSub.pack()

bubtton4 = Button(frame, text="Start Slam", command=getSLAM)
bubtton4.pack()

labelDiv3 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv3.pack()

label3 = Label(frame, text="Third step: Run the Robot with moving algorithm", font=("Helvetica", 16))
label3.pack(padx=10, pady=10)

algoList = ["Manual", "Automatic"]
algoCombo = Combobox(frame, values=algoList)
algoCombo.current(0)

algoCombo.state(["readonly"])
algoCombo.pack(padx=10, pady=4)


button3 = Button(frame, text="Select control", command=controlAlgorithm)
button3.pack(padx=5, pady=5)


labelDiv4 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv4.pack()

label4 = Label(frame, text="END", font=("Helvetica", 16))
label4.pack(padx=10, pady=10)


button4 = Button(frame, text="close", command=close)
button4.pack(padx=5, pady=5)

root.title("Autonomous rover control")
root.mainloop()
