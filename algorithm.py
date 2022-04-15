from abc import ABCMeta, abstractmethod
import subprocess
from subprocess import call
from tkinter import *
from tkinter.ttk import Combobox
import sys

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def strategy(self):
        pass


class ManuallyControl(Strategy):
    def strategy(self):
        # subprocess.call["gnome-terminal", "--", "bash", "-c", "cd script; ./manual.sh; read"]
        subprocess.Popen(["xterm", "-e","./script/manual.sh"])


class Navigation(Strategy):
    def strategy():
        print("navigation")


class AutoPilot(Strategy):
    def strategy(self):
        # subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./automatic.sh; read"])
        subprocess.Popen(["xterm", "-e","./script/automatic.sh"])


class Default(Strategy):
    def strategy(self):
        print("default")


class ContextFactory:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        if self.strategy == "Manual":
            strategy = ManuallyControl()
            strategy.strategy()
        elif self.strategy == "Automatic":
            strategy = AutoPilot()
            strategy.strategy()
        elif self.strategy == "navigation":
            strategy = Navigation()
            strategy.strategy()
        elif self.strategy == "run":
            strategy = Default()
            strategy.strategy()

algo = sys.argv[1]
context_factory = ContextFactory(algo)
context_factory.do_strategy()
