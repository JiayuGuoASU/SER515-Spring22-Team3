from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.geometry("400x200")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text="Pick a control option and submit")
label.pack()

label2 = Label(leftframe, text="Manual control")
label2.pack(padx=10, pady=10)


# button1 = Button(rightframe, text="Manual", command=lambda: print("Manual"))
# button1.pack(padx=3, pady=3)

# label3 = Label(leftframe, text="Automatic control")
# label3.pack(padx=10, pady=10)


# button1 = Button(rightframe, text="Automatic")
# button1.pack(padx=3, pady=3)

def manual():
    subprocess.call(['gnome-terminal', '-x', './automatic.sh'])
    return


def run():
    subprocess.call(['gnome-terminal', '-x', './fullrun.sh'])


def auto():
    subprocess.call(['gnome-terminal', '-x', './automatic.sh'])


def run1():
    if(Combo.get() == "Manual"):
        print("Manual")
        manual()
    elif(Combo.get() == "Automatic"):
        auto()
        print("Automatic")
    elif(Combo.get() == "Run"):
        print("Run")
        run()

    else:
        print("Random")


vlist = ["Run", "Random", "Automatic", "Manual"]

Combo = ttk.Combobox(frame, values=vlist)
Combo.set("Select")
Combo.pack(padx=5, pady=5)
button3 = Button(frame, text="Submit", command=run1)
button3.pack(padx=5, pady=5)

root.title("Autonomous rover control")
root.mainloop()
