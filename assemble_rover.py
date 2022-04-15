from abc import ABCMeta, abstractmethod
import subprocess
import os


class rover_factory:
    def __init__(self, base, wheel, caster):
        self.base = base
        self.wheel = wheel
        self.caster = caster

    def config(self):
        file = open("./src/Anton_description/urdf/Anton.xacro", "w")
        file.write('<?xml version="1.0"?>\n')
        file.write('\n<robot name="Anton" xmlns:xacro="http://www.ros.org/wiki/xacro">\n')
        base = self.base.config(self)
        wheel = self.wheel.config(self)
        caster = self.caster.config(self)
        file.write("\t")
        file.write(base)
        file.write("\n")
        file.write("\t")
        file.write(wheel)
        file.write("\n")
        file.write("\t")
        file.write(caster)
        file.write("\n")
        file.write(
            '\t<xacro:include filename="./chasis.xacro"/>\n\t<xacro:include '
            'filename="./wheels.xacro"/>\n\t<xacro:include filename="./caster.xacro"/>\n\t<xacro:include '
            'filename="./laser.xacro"/>\n\t<xacro:include filename="./camera.xacro"/>\n\t<xacro:include '
            'filename="./AntonPlugins.xacro"/>\n</robot>'
        )
        os.popen("xacro ./src/Anton_description/urdf/Anton.xacro > ./src/Anton_description/urdf/Anton.urdf")
        # subprocess.call(["cd src, cd Anton_description, cd urdf; xacro Anton.xacro > Anton.urdf; read"])
        # subprocess.call(["gnome-terminal", "--", "bash", "-c", "source /opt/ros/foxy/setup.bash; read"])
        # subprocess.call(["gnome-terminal", "--", "bash", "-c", "cd src; cd Anton_description; cd urdf; xacro Anton.xacro > Anton.urdf; read"])


class Base(metaclass=ABCMeta):
    @abstractmethod
    def config(self, rover):
        pass


class Base1(Base):
    def config(self, rover):
        base_dimensions = '<xacro:include filename="./chasis_dimension_1.xacro"/>'
        return base_dimensions


class Base2(Base):
    def config(self, rover):
        base_dimensions = '<xacro:include filename="./chasis_dimension_2.xacro"/>'
        return base_dimensions


class Base3(Base):
    def config(self, rover):
        base_dimensions = '<xacro:include filename="./chasis_dimension_3.xacro"/>'
        return base_dimensions


class Wheel(metaclass=ABCMeta):
    @abstractmethod
    def config(self, rover):
        pass


class Wheel1(Wheel):
    def config(self, rover):
        wheel_dimensions = '<xacro:include filename="./wheels_dimension_1.xacro"/>'
        return wheel_dimensions


class Wheel2(Wheel):
    def config(self, rover):
        wheel_dimensions = '<xacro:include filename="./wheels_dimension_2.xacro"/>'
        return wheel_dimensions


class Wheel3(Wheel):
    def config(self, rover):
        wheel_dimensions = '<xacro:include filename="./wheels_dimension_3.xacro"/>'
        return wheel_dimensions


class Caster(metaclass=ABCMeta):
    @abstractmethod
    def config(self, rover):
        pass


class Caster1(Caster):
    def config(self, rover):
        caster_dimensions = '<xacro:include filename="./caster_dimension_1.xacro"/>'
        return caster_dimensions


class Caster2(Caster):
    def config(self, rover):
        caster_dimensions = '<xacro:include filename="./caster_dimension_2.xacro"/>'
        return caster_dimensions


class Caster3(Caster):
    def config(self, rover):
        caster_dimensions = '<xacro:include filename="./caster_dimension_3.xacro"/>'
        return caster_dimensions


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_component(self):
        pass


class CasterFactory(Factory):
    def __init__(self, component_name):
        self.component_name = component_name

    def create_component(self):
        if self.component_name == "1":
            caster1 = Caster1()
            return caster1
        elif self.component_name == "2":
            caster2 = Caster2()
            return caster2
        elif self.component_name == "3":
            caster3 = Caster3()
            return caster3


class WheelFactory(Factory):
    def __init__(self, component_name):
        self.component_name = component_name

    def create_component(self):
        if self.component_name == "1":
            wheel1 = Wheel1()
            return wheel1
        elif self.component_name == "2":
            wheel2 = Wheel2()
            return wheel2
        elif self.component_name == "3":
            wheel3 = Wheel3()
            return wheel3


class BaseFactory(Factory):
    def __init__(self, component_name):
        self.component_name = component_name

    def create_component(self):
        if self.component_name == "1":
            base1 = Base1()
            return base1
        elif self.component_name == "2":
            base2 = Base2()
            return base2
        elif self.component_name == "3":
            base3 = Base3()
            return base3


from curses.ascii import isdigit
from tkinter import *

root = Tk()
from tkinter.ttk import Combobox


def main():
    def handleValues():
        wheel_type = wheelCombo.get()
        caster_type = casterCombo.get()
        base_type = baseCombo.get()
        print(wheel_type, caster_type, base_type)
        successLabel.config(text="Success! You have selected: " + wheel_type + " " + caster_type + " " + base_type)
        successLabel.pack()
        buttonSub.pack_forget()

        wheel_factory = WheelFactory(wheel_type)
        wheal_object = wheel_factory.create_component()
        caster_factory = CasterFactory(caster_type)
        caster_object = caster_factory.create_component()
        base_factory = BaseFactory(base_type)
        base_object = base_factory.create_component()

        rover = rover_factory(base_object, wheal_object, caster_object)
        rover.config()

        buttonClose.pack()

    root.geometry("350x250")
    frame = Frame(root)
    frame.pack()

    label1 = Label(frame, text="Select wheel configuration:")
    label1.pack(padx=10, pady=4)

    wheelList = ["1", "2", "3"]
    wheelCombo = Combobox(frame, values=wheelList)
    wheelCombo.current(0)

    wheelCombo.state(["readonly"])
    wheelCombo.pack(padx=10, pady=4)

    label2 = Label(frame, text="Select caster configuration:")
    label2.pack(padx=10, pady=4)

    casterList = ["1", "2", "3"]
    casterCombo = Combobox(frame, values=casterList)
    casterCombo.current(0)

    casterCombo.state(["readonly"])
    casterCombo.pack(padx=10, pady=4)

    label3 = Label(frame, text="Select base configuration:")
    label3.pack(padx=10, pady=4)

    baseList = ["1", "2", "3"]
    baseCombo = Combobox(frame, values=baseList)
    baseCombo.current(0)

    baseCombo.state(["readonly"])
    baseCombo.pack(padx=10, pady=4)

    buttonSub = Button(frame, text="Submit", command=handleValues)
    buttonSub.pack()

    successLabel = Label(frame, text="", fg="green")
    successLabel.pack()

    errorLabel = Label(frame, text="", fg="red")
    errorLabel.pack()

    buttonClose = Button(frame, text="Close", command=root.destroy)

    root.title("Rover customization")
    root.mainloop()


if __name__ == "__main__":
    main()
