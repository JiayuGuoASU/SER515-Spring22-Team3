from abc import ABCMeta, abstractmethod
import subprocess
from subprocess import call


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def strategy(self, parameters):
        pass


class ManuallyControl(Strategy):
    def strategy(self, parameters):
        subprocess.call["gnome-terminal", "--", "bash", "-c", "cd script; ./manual.sh; read"]


class Navigation(Strategy):
    def strategy(self, parameters):
        print("navigation")


class AutoPilot(Strategy):
    def strategy(self, parameters):
        subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd script; ./automatic.sh; read"])


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


parameter = "many parameters"
combo_get = "Manual"
context_factory = ContextFactory(combo_get, parameter)
context_factory.do_strategy()
