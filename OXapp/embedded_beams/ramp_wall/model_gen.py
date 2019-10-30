# -*- coding: utf-8 -*-

import os
import xc_base
import geom
import xc
import math
from model import predefined_spaces
from model.geometry import grid_model as gm
from materials import typical_materials as tm
from model.mesh import finit_el_model as fem

home= '/home/ana/projects/XCmodels/OXapp/embedded_beams/ramp_wall/'
execfile(home+'data.py')
#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the

#grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)
# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()

#lines

beamXsteel=gridGeom.genLinMultiXYZRegion([((xHall,yCantilv,secondFloorElev),(xWestWall,yCantilv,secondFloorElev))],'beamXsteel')

beamsYsteel=gridGeom.genLinMultiXYZRegion([
    ((xHall,yCantilv,secondFloorElev),(xHall,0,secondFloorElev)),
    ((xEastWall,yCantilv,secondFloorElev),(xEastWall,yHall,secondFloorElev)),
    ((xWestWall,yCantilv,secondFloorElev),(xWestWall,0,secondFloorElev))
     ],'beamsYsteel')

columnZsteel=gridGeom.genLinMultiXYZRegion([
     ((xEastWall,0,firstFloorElev),(xEastWall,0,secondFloorElev)),
     ],'columnZsteel')

#surfaces
wallBasement=gridGeom.genSurfMultiXYZRegion(
    [((xHall,0,foundElev),(xHall,yHall,firstFloorElev)),
     ((xHall,yHall,foundElev),(xEastWall,yHall,firstFloorElev)),
     ((xEastWall,yHall,foundElev),(xEastWall,LwallBasement,firstFloorElev)),
     ((xWestWall,0,foundElev),(xWestWall,LwallBasement,firstFloorElev))
    ],'wallBasement')

wallFirstFloor=gridGeom.genSurfMultiXYZRegion(
    [((xHall,0,firstFloorElev),(xHall,yHall,secondFloorElev)),
     ((xHall,yHall,firstFloorElev),(xEastWall,yHall,secondFloorElev)),
     ((xEastWall,yHall,firstFloorElev),(xEastWall,LwallFirstFloor,secondFloorElev)),
     ((xWestWall,0,firstFloorElev),(xWestWall,LwallFirstFloor,secondFloorElev)),
     ((xEastWall,LwallFirstFloor,firstFloorElev),(xWestWall,LwallFirstFloor,secondFloorElev))
    ],'wallFirstFloor')
    
#                         *** MATERIALS *** 
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())
# Steel material-section

beamXsteel_mat= ASTMmat.WShape(steel=A992,name='W16X40')
beamXsteel_mat.defElasticShearSection3d(preprocessor,A992)
beamsYsteel_mat= ASTMmat.WShape(steel=A992,name='W16X40')
beamsYsteel_mat.defElasticShearSection3d(preprocessor,A992)
columnZsteel_mat= ASTMmat.HSSShape(steel=A992,name='HSS22X22X3/4')
columnZsteel_mat.defElasticShearSection3d(preprocessor,A992)

# Isotropic elastic section-material appropiate for plate and shell analysis
wallBasement_mat=tm.DeckMaterialData(name='wallBasement_mat',thickness= wallThBasement,material=concrProp)
wallBasement_mat.setupElasticSection(preprocessor=prep)   #creates the section-material
wallFirstFloor_mat=tm.DeckMaterialData(name='wallFirstFloor_mat',thickness= wallThFirstFloor,material=concrProp)
wallFirstFloor_mat.setupElasticSection(preprocessor=prep)   #creates the section-material
modelSpace.displayBlocks()

#Mesh
#Steel elements: local Z-axis corresponds to weak axis of the steel shape
beamXsteel_mesh=fem.LinSetToMesh(linSet=beamXsteel,matSect=beamXsteel_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
beamsYsteel_mesh=fem.LinSetToMesh(linSet=beamsYsteel,matSect=beamsYsteel_mat,elemSize=eSize,vDirLAxZ=xc.Vector([1,0,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
columnZsteel_mesh=fem.LinSetToMesh(linSet=columnZsteel,matSect=columnZsteel_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')

wallBasement_mesh=fem.SurfSetToMesh(surfSet=wallBasement,matSect=wallBasement_mat,elemSize=eSize,elemType='ShellMITC4')
wallFirstFloor_mesh=fem.SurfSetToMesh(surfSet=wallFirstFloor,matSect=wallFirstFloor_mat,elemSize=eSize,elemType='ShellMITC4')

wallBasement_mesh.generateMesh(prep)
wallFirstFloor_mesh.generateMesh(prep)
fem.multi_mesh(preprocessor=prep,lstMeshSets=[beamXsteel_mesh,beamsYsteel_mesh,columnZsteel_mesh])     #mesh these sets


modelSpace.displayFEMesh()
modelSpace.displayLocalAxes()
