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
        self.visual['origin'] = origin
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

    def __init__(self, name, type, parent, child):
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
    
    def addOrigin(self, xyz, rpy):
        self.origin = {}
        self.origin['xyz'] = xyz
        self.origin['rpy'] = rpy


link = Link('link')
link.addInertial(1, 2, None)

link.addCollision(None, None, 2)
print(link.collision)

