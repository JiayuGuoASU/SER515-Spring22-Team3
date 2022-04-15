import shutil
import sys

fileName = sys.argv[1]
original = r'./src/Anton_description/world/' + str(fileName)
target = r'./src/Anton_description/world/map.sdf'
shutil.copyfile(original, target)
print("Build " + fileName + " Successfully!")
