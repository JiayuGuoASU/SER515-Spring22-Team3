from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import subprocess
from subprocess import call
import os
# import algorithm

from numpy import size

root = Tk()


def manual():
    # cmd = ["gnome-terminal", "--", "bash", "-c", "cd script; ./manual.sh; read"]
    subprocess.Popen(["xterm", "-e","./script/manual.sh"])
    # proc = subprocess.Popen(cmd)


def run():
    subprocess.Popen(["xterm", "-e","./script/fullrun.sh"])
    subprocess.Popen(["xterm", "-e","./script/manual.sh"])

def auto():
    subprocess.Popen(["xterm", "-e","./script/automatic.sh"])


def getSLAM():
    subprocess.Popen(["xterm", "-e","./script/downloadmap.sh"])


def downloadMap():
    subprocess.Popen(["xterm", "-e","./script/downloadmap.sh"])

def close():
    os.system("kill -9 " + str(PPID))

def mapConfig():
    call(["python3", "MapChoose.py"])


def roverConfig():
    call(["python3", "assemble_rover.py"])


def controlAlgorithm():
    algo = algoCombo.get()
    print("you select Algorithm: " + str(algo))
    call(["python3", "algorithm.py", str(algo)])
    # subprocess.Popen(["xterm", "-e","python3 algorithm.py"])

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

# bubtton12 = Button(frame, text="Download map", command=downloadMap)
# bubtton12.pack()

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
    frame, text="Third step: Run the Robot with moving algorithm", font=("Helvetica", 16)
)
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

label4 = Label(frame, text="Get the resultant map", font=("Helvetica", 16))
label4.pack(padx=10, pady=10)

bubtton4 = Button(frame, text="Result", command=getSLAM)
bubtton4.pack()

button4 = Button(frame, text="close", command=close)
button4.pack(padx=5, pady=5)

root.title("Autonomous rover control")
root.mainloop()
