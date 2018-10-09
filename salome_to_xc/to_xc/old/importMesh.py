#!/usr/bin/env python

import med2xcUtils

filename= "Mesh_1.med"

# Read the source meshes
meshNames = MEDLoader.GetMeshNames(filename)

# Set to True if the meshes and fields data must be loaded. Otherwise,
# only theire descriptions will be loaded.
READ_PHYSICAL_DATA=False

for meshName in meshNames:
  print "Reading: ", meshName
  # At this step, one can load the mesh of name meshName (but it is
  # not an obligation to continue to explore the metadata)
  meshDimRelToMax = 0 # 0 = no restriction
  mesh = MEDLoader.ReadUMeshFromFile(filename,meshName,meshDimRelToMax)
  # Note that the read function required the parameter
  # meshDimRelToMax. This parameter discreminates the meshdim you
  # are interested to relatively to the maximal dimension of cells
  # contained in the mesh in file (then its value could be 0, -1, -2
  # or -3 depending on the max dimension of the mesh. 0 means "no
  # restriction".

  medMesh= med2xcUtils.MEDMesh(filename,meshName)
  print medMesh
  med2xcUtils.saveMeshForXC(medMesh,"xcMesh")
