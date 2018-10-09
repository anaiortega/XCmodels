#!/usr/bin/env python
import os


if 'MEDFILE_ROOT_DIR' not in os.environ:
  #os.system('source /opt/salome/KERNEL_7.5.1/salome.sh')
  print "you need to execute: "
  print 'source /opt/salome/KERNEL_7.5.1/salome.sh'
  exit(0)

import NeutralMeshDescription
from MEDLoader import MEDLoader


filename= "MeshPGE.med"

# Read the source meshes
meshNames= MEDLoader.GetMeshNames(filename)

# Set to True if the meshes and fields data must be loaded. Otherwise,
# only theire descriptions will be loaded.
READ_PHYSICAL_DATA=False

meshes= {}

for meshName in meshNames:
  print "Reading: ", meshName
  # At this step, one can load the mesh of name meshName (but it is
  # not an obligation to continue to explore the metadata)
  meshDimRelToMax = 0 # 0 = no restriction
  umesh = MEDLoader.ReadUMeshFromFile(filename,meshName,meshDimRelToMax)

  groupNames= MEDLoader.GetMeshGroupsNames(filename,meshName)
  print "groups= ", groupNames
  for grp in groupNames:
    grpMesh= MEDLoader.ReadUMeshFromGroups(filename,meshName,meshDimRelToMax,[grp])
    grpRec= NeutralMeshDescription.GroupRecord(grp,None,grpMesh);
    
    # families= MEDLoader.GetMeshFamiliesNamesOnGroup(filename,meshName,grp)
    # print "group: ", grp, " families: ", families
    # for f in families:
    #   fm= umesh.getFamily(f)
      
  mesh= NeutralMeshDescription.NeutralMeshData(umesh)
  #print mesh
  meshes[meshName]= mesh

outputfilename= "Mesh_1"
print "Dumping meshes into: ", outputfilename+'.pkl'  
NeutralMeshDescription.dumpMeshes(meshes,outputfilename)

  
