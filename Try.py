import xml.etree.ElementTree as ET

from xml.dom import minidom
import os
print(os.getcwd())

class Rover:

	root = minidom.Document()
	rover = root.createElement('robot') 
	rover.setAttribute('name', 'Anton')
	root.appendChild(rover)

	def addLink(self, link):
        	self.rover.appendChild(link)

class Link:
	root = minidom.Document()
	link = root.createElement('link')

	def __init__(self, name):
		self.link.setAttribute('name', name)

	def addVisual(self, geometry, material):
		visual = self.root.createElement('visual')
		
		visual.appendChild(geometry)
		visual.appendChild(material)
		self.link.appendChild(visual)

class Material:
	root = minidom.Document()
	material = root.createElement('material')

	def __init__(self, name, color):
		self.name = name
		self.material.setAttribute('name', name)
		self.color = color
		colorEle = self.root.createElement('color')
		colorEle.setAttribute('rgba', color)
		self.material.appendChild(colorEle)

class Geometry:

	root = minidom.Document()
	geometry = root.createElement('geometry')

	def box(self, length, width, height):
		box = self.root.createElement('box')
		box.setAttribute('size', str(length) + ' ' + str(width) + ' ' + str(height))
		self.geometry.appendChild(box)

	def cylinder(self, radius, length):
		cylinder = self.root.createElement('cylinder')
		cylinder.setAttribute('radius', str(radius))
		cylinder.setAttribute('length', str(length))
		self.geometry.appendChild(cylinder)

	def sphere(self, radius):
		sphere = self.root.createElement('sphere')
		sphere.setAttribute('radius', str(radius))
		self.geometry.appendChild(sphere)


rover = Rover()
link = Link("testLink")

geo = Geometry()
geo.sphere(2)

mat = Material("Gray", "0.1 0.1 1.0 0.8")
link.addVisual(geo.geometry, mat.material)


rover.addLink(link.link)
xml_str = rover.root.toprettyxml(indent ="\t") 
print(xml_str)

