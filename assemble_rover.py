# Copyright 4/9/22 LI ZHUORAN. All rights reserved.

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    def __init__(self, wheel, caster):
        self.wheel = wheel
        self.caster = caster

    @abstractmethod
    def config(self):
        pass


class Base1(Base):
    def config(self):
        print("<xacro:property name=base_width value=0.31/>")
        self.wheel.config(self)
        self.caster.config(self)


class Base2(Base):
    def config(self):
        print("<xacro:property name=base_width value=10/>")
        self.wheel.config(self)
        self.caster.config(self)


class Base3(Base):
    def config(self):
        print("<xacro:property name=base_width value=0.20/>")
        self.wheel.config(self)
        self.caster.config(self)


class Wheel(metaclass=ABCMeta):
    @abstractmethod
    def config(self, base):
        pass


class Wheel1(Wheel):
    def config(self, base):
        print("<xacro:property name=wheel_radius value=0.10/>")


class Wheel2(Wheel):
    def config(self, base):
        print("<xacro:property name=wheel_radius value=0.10/>")


class Wheel3(Wheel):
    def config(self, base):
        print("<xacro:property name=wheel_radius value=0.10/>")


class Caster(metaclass=ABCMeta):
    @abstractmethod
    def config(self, base):
        pass


class Caster1(Caster):
    def config(self, base):
        print("<xacro:property name=caster_width value=0.15/>")


class Caster2(Caster):
    def config(self, base):
        print("<xacro:property name=caster_length value=0.21/>")


class Caster3(Caster):
    def config(self, base):
        print("<xacro:property name=caster_xxx value=0.11/>")


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
    def __init__(self, component_name, wheel, caster):
        self.component_name = component_name
        self.wheel = wheel
        self.caster = caster

    def create_component(self):
        if self.component_name == "1":
            base1 = Base1(self.wheel, self.caster)
            base1.config()
        elif self.component_name == "2":
            base2 = Base2(self.wheel, self.caster)
            base2.config()
        elif self.component_name == "3":
            base3 = Base3(self.wheel,  self.caster)
            base3.config()


def main():
    print("1 : wheel1")
    print("2 : wheel2")
    print("3 : wheel3")
    print("4 : customize")
    wheel_type = input("option : ")
    wheel_factory = WheelFactory(wheel_type)
    wheal_object = wheel_factory.create_component()

    print("1 : caster1")
    print("2 : caster2")
    print("3 : caster3")
    print("4 : customize")
    caster_type = input("option : ")
    caster_factory = CasterFactory(caster_type)
    caster_object = caster_factory.create_component()

    print("1 : base1")
    print("2 : base2")
    print("3 : base3")
    print("4 : customize")
    base_type = input("option : ")
    base_factory = BaseFactory(base_type, wheal_object, caster_object)
    base_factory.create_component()


if __name__ == "__main__":
    main()
