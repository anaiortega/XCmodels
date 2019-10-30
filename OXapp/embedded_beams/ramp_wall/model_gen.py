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
from postprocess import output_styles as outSty
from postprocess import output_handler as outHndl
from model.sets import sets_mng as sets
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc
from actions.earth_pressure import earth_pressure as ep

#home= '/home/ana/projects/XCmodels/OXapp/embedded_beams/ramp_wall/'
home= '/home/luis/Documents/XCmodels/OXapp/embedded_beams/ramp_wall/'
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

sty=outSty.OutputStyle()
out=outHndl.OutputHandler(modelSpace,sty)
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
#out.displayBlocks()
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
    
#out.displayBlocks()
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

beamSets=[beamXsteel,beamsYsteel,columnZsteel]
wallSets=[wallBasement,wallFirstFloor]
#out.displayFEMesh(setsToDisplay=beamSets+wallSets)
#out.displayLocalAxes()

#                       ***BOUNDARY CONDITIONS***

pntBase=gridGeom.getSetPntXYZRange(xyzRange=((xHall,0,foundElev),(xWestWall,LwallBasement,foundElev)),setName='pntBase')
lnBase=sets.get_lines_on_points(setPoints=pntBase, setLinName='lnBase', onlyIncluded=True)
for l in lnBase.lines:
    for n in l.getNodes:
        modelSpace.fixNode('000_FFF',n.tag)

pntBwall=gridGeom.getSetPntXYZRange(xyzRange=((xHall,0,foundElev),(xWestWall,0,firstFloorElev)),setName='pntBwall')
lnBwall=sets.get_lines_on_points(setPoints=pntBwall, setLinName='lnBwall', onlyIncluded=True)
#out.displayBlocks(lnBwall)
lnBwall.fillDownwards()
for n in lnBwall.getNodes:
    modelSpace.fixNode('000_FFF',n.tag)


#                       ***ACTIONS***
#selfweight
grav=9.81 #Gravity acceleration (m/s2)
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[wallBasement_mesh,wallFirstFloor_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))
'''
GselfWeight=lcases.LoadCase(preprocessor=prep,name="GselfWeight",loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])
modelSpace.addLoadCaseToDomain("GselfWeight")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("GselfWeight")
'''
#earth pressure
EastBasementWall=gridGeom.getSetSurfMultiXYZRegion(
    lstXYZRange=[((xHall,0,foundElev),(xHall,yHall,firstFloorElev)),
     ((xEastWall,yHall,foundElev),(xEastWall,LwallBasement,firstFloorElev)),
    ], nameSet='EastBasementWall')
EastBasementWall.fillDownwards()
WestBasementWall=gridGeom.getSetSurfMultiXYZRegion(
    lstXYZRange=[((xWestWall,0,foundElev),(xWestWall,LwallBasement,firstFloorElev))], nameSet='WestBasementWall')
WestBasementWall.fillDownwards()
soil_ramp=ep.EarthPressureSlopedWall(Ksoil=KearthPress, gammaSoil=grav*densSoil, zGroundPnt1=rampStartElev, XYpnt1=(xEastWall,0), zGroundPnt2=rampEndElev, XYpnt2=(xEastWall,LwallBasement))
earthPressEastwall=loads.EarthPressLoad(name= 'earthPressEastwall', xcSet=EastBasementWall,soilData=soil_ramp, vDir=xc.Vector([-1,0,0]))
earthPressWestwall=loads.EarthPressLoad(name= 'earthPressWestwall', xcSet=WestBasementWall,soilData=soil_ramp, vDir=xc.Vector([1,0,0]))

EarthPress=lcases.LoadCase(preprocessor=prep,name="EarthPress",loadPType="default",timeSType="constant_ts")
EarthPress.create()
EarthPress.addLstLoads([earthPressEastwall,earthPressWestwall])
modelSpace.addLoadCaseToDomain("EarthPress")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("EarthPress")

#Linear loads (dead, live, snow,wind)
pntE2F=gridGeom.getSetPntMultiXYZRegion(lstXYZRange=[
    ((xHall,0,secondFloorElev),(xHall,yHall,secondFloorElev)),
    ((xEastWall,yHall,secondFloorElev),(xEastWall,LwallBasement,secondFloorElev))]
    ,setName='pntE2F')
lnE2F=sets.get_lines_on_points(setPoints=pntE2F, setLinName='lnE2F', onlyIncluded=True)
out.displayBlocks(lnE2F)

pntW2F=gridGeom.getSetPntMultiXYZRegion(lstXYZRange=[
    ((xWestWall,0,secondFloorElev),(xWestWall,LwallBasement,secondFloorElev))]
    ,setName='pntW2F')
lnW2F=sets.get_lines_on_points(setPoints=pntW2F, setLinName='lnW2F', onlyIncluded=True)
out.displayBlocks(lnW2F)

lnEW2F=lnE2F+lnW2F
out.displayBlocks(lnEW2F)

Dead2F=loads.UniformLoadOnLines(name='Dead2F',xcSet=lnEW2F,loadVector=xc.Vector([0,0,-Dead_WE2F,0,0,0]))
Live2F=loads.UniformLoadOnLines(name='Live2F',xcSet=lnEW2F,loadVector=xc.Vector([0,0,-Live_WE2F,0,0,0]))
Snow2F=loads.UniformLoadOnLines(name='Snow2F',xcSet=lnEW2F,loadVector=xc.Vector([0,0,-Snow_WE2F,0,0,0]))
Wind2F=loads.UniformLoadOnLines(name='Wind2F',xcSet=lnEW2F,loadVector=xc.Vector([-Wind_WE2F,0,0,0,0,0]))

pntE1F=gridGeom.getSetPntMultiXYZRegion(lstXYZRange=[
    ((xHall,0,firstFloorElev),(xHall,yHall,firstFloorElev)),
    ((xEastWall,yHall,firstFloorElev),(xEastWall,LwallBasement,firstFloorElev))]
    ,setName='pntE1F')
lnE1F=sets.get_lines_on_points(setPoints=pntE1F, setLinName='lnE1F', onlyIncluded=True)
out.displayBlocks(lnE1F)
Dead1F=loads.UniformLoadOnLines(name='Dead1F',xcSet=lnE1F,loadVector=xc.Vector([0,0,-Dead_E1F,0,0,0]))
Live1F=loads.UniformLoadOnLines(name='Live1F',xcSet=lnE1F,loadVector=xc.Vector([0,0,-Live_E1F,0,0,0]))
Snow1F=loads.UniformLoadOnLines(name='Snow1F',xcSet=lnE1F,loadVector=xc.Vector([0,0,-Snow_E1F,0,0,0]))
Wind1F=loads.UniformLoadOnLines(name='Wind1F',xcSet=lnE1F,loadVector=xc.Vector([-Wind_E1F,0,0,0,0,0]))

Dead_LC=lcases.LoadCase(preprocessor=prep,name="Dead_LC",loadPType="default",timeSType="constant_ts")
Dead_LC.create()
Dead_LC.addLstLoads([Dead2F,Dead1F])
modelSpace.addLoadCaseToDomain("Dead_LC")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("Dead_LC")

Live_LC=lcases.LoadCase(preprocessor=prep,name="Live_LC",loadPType="default",timeSType="constant_ts")
Live_LC.create()
Live_LC.addLstLoads([Live2F,Live1F])
modelSpace.addLoadCaseToDomain("Live_LC")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("Live_LC")

Snow_LC=lcases.LoadCase(preprocessor=prep,name="Snow_LC",loadPType="default",timeSType="constant_ts")
Snow_LC.create()
Snow_LC.addLstLoads([Snow2F,Snow1F])
modelSpace.addLoadCaseToDomain("Snow_LC")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("Snow_LC")


Wind_LC=lcases.LoadCase(preprocessor=prep,name="Wind_LC",loadPType="default",timeSType="constant_ts")
Wind_LC.create()
Wind_LC.addLstLoads([Wind2F,Wind1F])
modelSpace.addLoadCaseToDomain("Wind_LC")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("Wind_LC")

