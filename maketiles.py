#!/usr/bin/python

# from qgis.core import *
from qgis.core import QgsApplication, QgsVectorLayer

print ('lala')

# Supply path to qgis install location
QgsApplication.setPrefixPath("/usr", True)

print ('lalaf')

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()



# Write your code here to load some layers, use processing
# algorithms, etc.

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()

print('end')