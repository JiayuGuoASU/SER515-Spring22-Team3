
from xml.dom import minidom


class Rover:

    root = minidom.Document()
    rover = root.createElement('robot')
    rover.setAttribute('name', 'Anton')
    root.appendChild(rover)

    def addLink(self, link):
        self.rover.appendChild(link.link)

    def addJoint(self, joint):
        self.rover.appendChild(joint.joint)


class Link:
    name = None
    inertial = None
    visual = None
    conflict = None
    
    def __init__(self, name, root):
        self.root = root
        self.link = self.root.createElement('link')
        self.collisionEle = self.root.createElement('collision')
        self.name = name
        self.link.setAttribute('name', name)
        self.root.appendChild(self.link)

    def addVisual(self, geometry, material):
        visualEle = self.root.createElement('visual')
        visualEle.appendChild(geometry)
        visualEle.appendChild(material)
        self.link.appendChild(visualEle)

    def addCollision(self, geometry):
        self.collisionEle = self.root.createElement('collision')
        self.collisionEle.appendChild(geometry)
        self.link.appendChild(self.collisionEle)

    def addInertia(self, inertial):
        self.link.appendChild(inertial)

    def addSurfaceToConflict(self, val):
        surfaceEle = self.root.createElement('surface')
        frictionEle = self.root.createElement('friction')
        odeEle = self.root.createElement('ode')

        muEle = self.root.createElement('mu')
        mu = self.root.createTextNode(str(val))
        muEle.appendChild(mu)
        mu2Ele = self.root.createElement('mu2')
        mu2 = self.root.createTextNode(str(val))
        mu2Ele.appendChild(mu2)

        odeEle.appendChild(muEle)
        odeEle.appendChild(mu2Ele)
        frictionEle.appendChild(odeEle)
        surfaceEle.appendChild(frictionEle)
        self.collisionEle.appendChild(surfaceEle)


class Material:

    def __init__(self, name, color, root):
        self.root = root
        self.material = self.root.createElement('material')
        self.name = name
        self.material.setAttribute('name', name)
        self.color = color
        colorEle = self.root.createElement('color')
        colorEle.setAttribute('rgba', color)
        self.material.appendChild(colorEle)


class Geometry:

    inertiaList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    def __init__(self, m, root):
        self.m = m
        self.root = root
        self.geometry = self.root.createElement('geometry')
        self.inertialEle = root.createElement('inertial')

    def box(self, length, width, height):
        m = self.m
        self.type = "box"
        box = self.root.createElement('box')
        box.setAttribute(
            'size', str(length) + ' ' + str(width) + ' ' + str(height)
            )
        self.geometry.appendChild(box)
        self.inertiaList[0] = m / 12 * (height * height + length * length)
        self.inertiaList[3] = m / 12 * (length * length + width * width)
        self.inertiaList[5] = m / 12 * (height * height + width * width)

    def cylinder(self, radius, length):
        m = self.m
        self.type = "cylinder"
        cylinder = self.root.createElement('cylinder')
        cylinder.setAttribute('radius', str(radius))
        cylinder.setAttribute('length', str(length))
        self.geometry.appendChild(cylinder)
        self.inertiaList[0] = m / 12 * (3 * radius * radius + length * length)
        self.inertiaList[3] = m / 12 * (3 * radius * radius + length * length)
        self.inertiaList[5] = m / 2 * radius * radius

    def sphere(self, radius):
        m = self.m
        self.type = "sphere"
        sphere = self.root.createElement('sphere')
        sphere.setAttribute('radius', str(radius))
        self.geometry.appendChild(sphere)
        self.inertiaList[0] = (2/5) * m * (radius * radius)
        self.inertiaList[3] = (2/5) * m * (radius * radius)
        self.inertiaList[5] = (2/5) * m * (radius * radius)

    def generateInertia(self):
        massEle = self.root.createElement('mass')
        massEle.setAttribute('value', self.m)
        inertiaEle = self.root.createElement('inertia')
        inertiaEle.setAttribute('ixx', str(self.inertiaList[0]))
        inertiaEle.setAttribute('ixy', str(self.inertiaList[1]))
        inertiaEle.setAttribute('ixz', str(self.inertiaList[2]))
        inertiaEle.setAttribute('iyy', str(self.inertiaList[3]))
        inertiaEle.setAttribute('iyz', str(self.inertiaList[4]))
        inertiaEle.setAttribute('izz', str(self.inertiaList[5]))
        self.inertialEle.appendChild(inertiaEle)


class Joint:
    # root = minidom.Document()
    # joint = minidom.Document().createElement('joint')
    allowedTypes = [
        'revolute', 'continuous', 'prismatic', 'fixed', 'floating', 'planar'
        ]
    type = None

    def __init__(self, name, type, parentLink, childLink, root):
        if type not in self.allowedTypes:
            raise NameError("Type not allowed")
        self.root = root
        self.joint = self.root.createElement('joint')
        self.joint.setAttribute('name', name)
        self.joint.setAttribute('type', type)
        parentEle = self.root.createElement('parent')
        parentEle.setAttribute('link', parentLink.name)
        self.joint.appendChild(parentEle)
        
        childEle = self.root.createElement('child')
        childEle.setAttribute('link', childLink.name)
        self.joint.appendChild(childEle)


rover = Rover()
link = Link("testLink", rover.root)
geo = Geometry(5, rover.root)
geo.sphere(2)
geo.generateInertia()
mat = Material("Gray", "0.1 0.1 1.0 0.8", rover.root)
link.addVisual(geo.geometry, mat.material)
# link.addSurfaceToConflict(0.5)
link.addCollision(geo.geometry)
link.addInertia(geo.inertialEle)
# rover.addLink(link)

link2 = Link("testLink2", rover.root)
geo2 = Geometry(5, rover.root)
geo2.box(3, 4, 5)
geo2.generateInertia()
mat2 = Material("Yellow", "0.1 0.1 1.0 0.8", rover.root)
link2.addVisual(geo2.geometry, mat2.material)
# link2.addSurfaceToConflict(0.5)
link2.addCollision(geo2.geometry)
link2.addInertia(geo2.inertialEle)
# rover.addLink(link2)

joint = Joint("testJoint", "fixed", link, link2, rover.root)
rover.addJoint(joint)

joint2 = Joint("testJoint2", "fixed", link2, link, rover.root)
rover.addJoint(joint2)

xml_str = rover.root.toprettyxml(indent="\t")


# root = minidom.Document()
# tree = root.createElement('root')
# tree.setAttribute('name', 'Anton')
# root.appendChild(tree)

# lst = root.createElement('lst')
# lst.setAttribute('name', 'lst')
# tree.appendChild(lst)

# lst2 = root.createElement('lst')
# lst2.setAttribute('name', 'lst2')
# tree.appendChild(lst2)
# str = root.toprettyxml(indent="\t")
print(xml_str)
print(rover.root.__str__)
