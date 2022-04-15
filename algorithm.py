from abc import ABCMeta, abstractmethod
import subprocess
from subprocess import call
from tkinter import *
from tkinter.ttk import Combobox


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def strategy(self, parameters):
        pass


class ManuallyControl(Strategy):
    def strategy(self, parameters):
        # subprocess.call["gnome-terminal", "--", "bash", "-c", "cd script; ./manual.sh; read"]
        subprocess.Popen(["xterm", "-e","./script/manual.sh"])


class Navigation(Strategy):
    def strategy(self, parameters):
        print("navigation")


class AutoPilot(Strategy):
    def strategy(self, parameters):
        # subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./automatic.sh; read"])
        subprocess.Popen(["xterm", "-e","./script/automatic.sh"])


class Default(Strategy):
    def strategy(self, parameters):
        print("default")


class ContextFactory:
    def __init__(self, strategy, parameters):
        self.strategy = strategy
        self.parameter = parameters

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        if self.strategy == "Manual":
            strategy = ManuallyControl()
            strategy.strategy(self.parameter)
        elif self.strategy == "Automatic":
            strategy = AutoPilot()
            strategy.strategy(self.parameter)
        elif self.strategy == "navigation":
            strategy = Navigation()
            strategy.strategy(self.parameter)
        elif self.strategy == "run":
            strategy = Default()
            strategy.strategy(self.parameter)


def handle_button_click(strategy, parameters):
    context = ContextFactory(strategy, parameters)
    context.do_strategy()
    successLabel.config(text="Successfully executed " + strategy + " with parameters " + parameters)
    buttonSub.pack_forget()
    buttonClose.pack()


root = Tk()
root.geometry("500x300")
frame = Frame(root)
frame.pack()

controlList = ["Manual", "Automatic", "navigation", "run"]
combo = Combobox(root, values=controlList)
combo.current(0)
combo.pack()

buttonSub = Button(frame, text="Submit", command=handle_button_click(combo.get(), "parameters"))
buttonSub.pack()

successLabel = Label(frame, text="", fg="green")
successLabel.pack()

errorLabel = Label(frame, text="", fg="red")
errorLabel.pack()

buttonClose = Button(frame, text="Close", command=root.destroy)

root.title("Autonomous rover control")
root.mainloop()
