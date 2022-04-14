from abc import ABCMeta, abstractmethod


class rover_factory:
    def __init__(self, base, wheel, caster):
        self.base = base
        self.wheel = wheel
        self.caster = caster

    def config(self):
        self.base.config(self)
        self.wheel.config(self)
        self.caster.config(self)


class Base(metaclass=ABCMeta):
    @abstractmethod
    def config(self, rover):
        pass


class Base1(Base):
    def config(self, rover):
        print("<xacro:property name=base_width value=0.31/>")


class Base2(Base):
    def config(self, rover):
        print("<xacro:property name=base_width value=10/>")


class Base3(Base):
    def config(self, rover):
        print("<xacro:property name=base_width value=0.20/>")


class Wheel(metaclass=ABCMeta):
    @abstractmethod
    def config(self, rover):
        pass


class Wheel1(Wheel):
    def config(self, rover):
        print("<xacro:property name=wheel_radius value=0.10/>")


class Wheel2(Wheel):
    def config(self, rover):
        print("<xacro:property name=wheel_radius value=0.10/>")


class Wheel3(Wheel):
    def config(self, rover):
        print("<xacro:property name=wheel_radius value=0.10/>")


class Caster(metaclass=ABCMeta):
    @abstractmethod
    def config(self, rover):
        pass


class Caster1(Caster):
    def config(self, rover):
        print("<xacro:property name=caster_width value=0.15/>")


class Caster2(Caster):
    def config(self, rover):
        print("<xacro:property name=caster_length value=0.21/>")


class Caster3(Caster):
    def config(self, rover):
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
    base_factory = BaseFactory(base_type)
    base_object = base_factory.create_component()

    rover = rover_factory(base_object, wheal_object, caster_object)
    rover.config()


if __name__ == "__main__":
    main()