#!/usr/bin/env python
import os, sys

inst_root= '/opt/salome'
python_version= '2.7'
med_root_dir= inst_root + '/MED_7.5.1'
#appli_root_dir= inst_root + '/salome_appli_7.5.1'
medfile_root_dir= inst_root + '/med-3.0.8'
pth= medfile_root_dir + '/bin'
pth+= ':' + med_root_dir+ '/bin/salome'
ld_library_path= medfile_root_dir + '/lib'
ld_library_path+= ':' + med_root_dir + '/lib/salome'
#ld_library_path+= ':' + appli_root_dir + '/lib/salome'
pythonpths= []
pythonpths.append(medfile_root_dir+ '/lib/python'+ python_version + '/site-packages')
pythonpths.append(med_root_dir + '/bin/salome')
pythonpths.append(med_root_dir + '/lib/salome')
pythonpths.append(med_root_dir + '/lib/python' + python_version + '/site-packages/salome')

sz= len(pythonpths)
pythonpath= pythonpths[0]
for i in range(1,sz):
  pythonpath+= ':' + pythonpths[i]

if 'PATH' not in os.environ:
  os.environ['PATH']= pth
else:
  os.environ['PATH']+= pth
print "PATH= ", os.environ['PATH']

if 'LD_LIBRARY_PATH' not in os.environ:
  os.environ['LD_LIBRARY_PATH']= ld_library_path
else:
  os.environ['LD_LIBRARY_PATH']+= ld_library_path
print "LD_LIBRARY_PATH= ", os.environ['LD_LIBRARY_PATH']

if 'PYTHONPATH' not in os.environ:
  os.environ['PYTHONPATH']= pythonpath
else:
  os.environ['PYTHONPATH']+= pythonpath

for pypth in pythonpths:
  sys.path.append(pypth)

#
# import yourmodule

# your program goes here

import med2xcUtils
os.execv('importMesh.py', sys.argv)

# filename= "Mesh_1.med"

# # Read the source meshes
# meshNames = MEDLoader.GetMeshNames(filename)

# # Set to True if the meshes and fields data must be loaded. Otherwise,
# # only theire descriptions will be loaded.
# READ_PHYSICAL_DATA=False

# for meshName in meshNames:
#   print "Reading: ", meshName
#   # At this step, one can load the mesh of name meshName (but it is
#   # not an obligation to continue to explore the metadata)
#   meshDimRelToMax = 0 # 0 = no restriction
#   mesh = MEDLoader.ReadUMeshFromFile(filename,meshName,meshDimRelToMax)
#   # Note that the read function required the parameter
#   # meshDimRelToMax. This parameter discreminates the meshdim you
#   # are interested to relatively to the maximal dimension of cells
#   # contained in the mesh in file (then its value could be 0, -1, -2
#   # or -3 depending on the max dimension of the mesh. 0 means "no
#   # restriction".

#   medMesh= MEDMesh(filename,meshName)
#   print medMesh
#   saveMeshForXC(medMesh,"xcMesh")
