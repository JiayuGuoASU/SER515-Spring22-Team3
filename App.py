from cProfile import label
from tkinter import *
from tkinter import ttk
import subprocess
from subprocess import call
import os
import algorithm

from numpy import size

root = Tk()


def manual():
    cmd = ["gnome-terminal", "--", "bash", "-c", "cd script; ./manual.sh; read"]
    proc = subprocess.Popen(cmd)


def run():
    subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./fullrun.sh; read"])
    subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./slam.sh; read"])
    gazeboProcess = subprocess.Popen("./script/fullrun.sh", stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)


def auto():
    subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./automatic.sh; read"])


def getSLAM():
    subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./downloadmap.sh; read"])


def downloadMap():
    subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./downloadmap.sh; read"])


def close():
    os.system("kill -9 " + str(PPID))


def run1():
    if Combo.get() == "Manual":
        print("Manual")
        run1.ppid = manual()
        print(run1.ppid)
    elif Combo.get() == "Automatic":
        auto()
        print("Automatic")
    elif Combo.get() == "Run":
        print("Run")
        run()


def mapConfig():
    # run MapWindow.py
    call(["python3", "Map.py"])


def roverConfig():
    # run MapWindow.py
    call(["python3", "assemble_rover.py"])


def controlAlgorithm():
    # run MapWindow.py
    call(["python3", "alogrithm.py"])


root.geometry("500x700")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

labelMain = Label(frame, text="Pick a control option", font=("Helvetica", 20))
labelMain.pack(padx=10, pady=10)

labelDiv1 = Label(frame, text="_______________________________________", font=("Helvetica", 20))

labelDiv1.pack()
labelSub = Label(frame, text="First step: Configuration", font=("Helvetica", 16))
labelSub.pack(padx=10, pady=10)

lablel11 = Label(frame, text="Map configuration:", font=("Helvetica", 16))
lablel11.pack(padx=10, pady=10)

bubtton12 = Button(frame, text="Download map", command=downloadMap)
bubtton12.pack()

bubtton11 = Button(frame, text="Map configuration", command=mapConfig)
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


labelDiv3 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv3.pack()

label3 = Label(
    frame, text="Third step: Run the project\n Two options: \n *Manual \n *Automatic", font=("Helvetica", 16)
)
label3.pack(padx=10, pady=10)

button3 = Button(frame, text="Select control", command=controlAlgorithm)
button3.pack(padx=5, pady=5)


labelDiv4 = Label(frame, text="_______________________________________", font=("Helvetica", 20))
labelDiv4.pack()

label4 = Label(frame, text="Get the resultant map", font=("Helvetica", 16))
label4.pack(padx=10, pady=10)

bubtton4 = Button(frame, text="Result", command=getSLAM)
bubtton4.pack()

button4 = Button(frame, text="close", command=close)
button4.pack(padx=5, pady=5)

root.title("Autonomous rover control")
root.mainloop()
