class Link:

    def __init__(self, name):
        if name is None:
            raise Exception('Link name is None')
        self.name = name

    def addInertial(self, mass, inertia, origin):
        if mass is None or inertia is None:
            raise Exception('mass or inertia is None')

        self.inertial = {}
        self.inertial['mass'] = mass
        self.inertial['inertia'] = inertia
        self.inertial['origin'] = origin

    def addVisual(self, name, origin, geometry, material):
        if geometry is None:
            raise Exception('geometry is None for visual')

        self.visual = {}
        self.visual['name'] = name
        self.visual['origin'] = {}
        self.visual['origin']['xyz'] = origin.get('xyz', [0, 0, 0])
        self.visual['origin']['rpy'] = origin.get('rpy', [0, 0, 0])
        self.visual['geometry'] = geometry
        self.visual['material'] = material

    def addCollision(self, name, origin, geometry):
        if geometry is None:
            raise Exception('geometry is None for collision')

        self.collision = {}
        self.collision['name'] = name
        self.collision['origin'] = origin
        self.collision['geometry'] = geometry


class Joint:

    def __init__(self, name, type, parent, child, origin):
        allowedTypes = [
            'revolute', 'continuous', 'prismatic', 'fixed', 'floating', 'planar'
        ]
        if name is None:
            raise Exception('Joint name is None')

        if type not in allowedTypes:
            raise Exception('Joint type is not allowed')

        if parent is None or child is None:
            raise Exception('Parent or child Link is None')

        self.name = name
        self.type = type
        self.parent = parent
        self.child = child
        self.origin = {}
        self.origin['xyz'] = origin.get('xyz', [0, 0, 0])
        self.origin['rpy'] = origin.get('rpy', [0, 0, 0])


class Geometry:
    def __init__(self, type, config):
        if type is None:
            raise Exception('Geometry type is None')
        if type not in ['box', 'cylinder', 'sphere']:
            raise Exception('Geometry type is not allowed')
        self.type = type
        self.config(config)

    def config(self, config):
        if (self.type == 'box'):
            self.size = config.get('size')
        elif (self.type == 'cylinder'):
            self.radius = config.get('radius')
            self.length = config.get('length')
        elif (self.type == 'sphere'):
            self.radius = config.get('radius')


class Material:
    def __init__(self, name, color):
        if name is None:
            raise Exception('Material name is None')
        self.name = name
        self.color = color.get('rgba', "0 0 0 1")


link = Link('link')
link.addInertial(1, 2, None)
cylinder = Geometry('cylinder', {'radius': 1, 'length': 2})
link.addCollision(None, None, cylinder)
print(cylinder)
# print(link.collision['geometry'].radius)
