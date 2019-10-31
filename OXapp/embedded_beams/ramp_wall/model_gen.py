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

home= '/home/ana/projects/XCmodels/OXapp/embedded_beams/ramp_wall/'
#home= '/home/luis/Documents/XCmodels/OXapp/embedded_beams/ramp_wall/'
execfile(home+'data.py')
execfile(home+'env_config.py')
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
EastBasementWall=gridGeom.genSurfMultiXYZRegion(
    [((xHall,0,foundElev),(xHall,yHall,firstFloorElev)),
     ((xHall,yHall,foundElev),(xEastWall,yHall,firstFloorElev)),
     ((xEastWall,yHall,foundElev),(xEastWall,LwallBasement,firstFloorElev))
    ],'EastBasementWall')
WestBasementWall=gridGeom.genSurfMultiXYZRegion(
    [((xWestWall,0,foundElev),(xWestWall,LwallBasement,firstFloorElev))
    ],'WestBasementWall')

East1FloorWall=gridGeom.genSurfMultiXYZRegion(
    [((xHall,0,firstFloorElev),(xHall,yHall,secondFloorElev)),
     ((xHall,yHall,firstFloorElev),(xEastWall,yHall,secondFloorElev)),
     ((xEastWall,yHall,firstFloorElev),(xEastWall,LwallFirstFloor,secondFloorElev)),
    ],'East1FloorWall')
South1FloorWall=gridGeom.genSurfMultiXYZRegion(
    [((xEastWall,LwallFirstFloor,firstFloorElev),(xWestWall,LwallFirstFloor,secondFloorElev))
    ],'South1FloorWall')

West1FloorWall=gridGeom.genSurfMultiXYZRegion(
    [((xWestWall,0,firstFloorElev),(xWestWall,LwallFirstFloor,secondFloorElev))
    ],'West1FloorWall')
     
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

EastBasementWall_mesh=fem.SurfSetToMesh(surfSet=EastBasementWall,matSect=wallBasement_mat,elemSize=eSize,elemType='ShellMITC4')
WestBasementWall_mesh=fem.SurfSetToMesh(surfSet=WestBasementWall,matSect=wallBasement_mat,elemSize=eSize,elemType='ShellMITC4')
East1FloorWall_mesh=fem.SurfSetToMesh(surfSet=East1FloorWall,matSect=wallFirstFloor_mat,elemSize=eSize,elemType='ShellMITC4')
South1FloorWall_mesh=fem.SurfSetToMesh(surfSet=South1FloorWall,matSect=wallFirstFloor_mat,elemSize=eSize,elemType='ShellMITC4')
West1FloorWall_mesh=fem.SurfSetToMesh(surfSet=West1FloorWall,matSect=wallFirstFloor_mat,elemSize=eSize,elemType='ShellMITC4')

EastBasementWall_mesh.generateMesh(prep)
East1FloorWall_mesh.generateMesh(prep)
South1FloorWall_mesh.generateMesh(prep)
WestBasementWall_mesh.generateMesh(prep)
West1FloorWall_mesh.generateMesh(prep)
fem.multi_mesh(preprocessor=prep,lstMeshSets=[beamXsteel_mesh,beamsYsteel_mesh,columnZsteel_mesh])     #mesh these sets

beamSets=[beamXsteel,beamsYsteel,columnZsteel]
wallSets=[EastBasementWall,East1FloorWall,South1FloorWall,WestBasementWall,West1FloorWall]
#out.displayFEMesh(setsToDisplay=beamSets+wallSets)
#out.displayLocalAxes()

walls=EastBasementWall+East1FloorWall+South1FloorWall+WestBasementWall+West1FloorWall
overallSet=beamSets+wallSets
#                       ***BOUNDARY CONDITIONS***

pntBase=gridGeom.getSetPntXYZRange(xyzRange=((xHall,0,foundElev),(xWestWall,LwallBasement,foundElev)),setName='pntBase')
lnBase=sets.get_lines_on_points(setPoints=pntBase, setLinName='lnBase', onlyIncluded=True)
for l in lnBase.lines:
    for n in l.getNodes:
        modelSpace.fixNode('000_FFF',n.tag)

pntBwall=gridGeom.getSetPntXYZRange(xyzRange=((xHall,0,foundElev),(xWestWall,0,firstFloorElev)),setName='pntBwall')
lnBwall=sets.get_lines_on_points(setPoints=pntBwall, setLinName='lnBwall', onlyIncluded=True)
#out.displayBlocks(lnBwall)
for l in lnBwall.lines:
    for n in l.getNodes:
        modelSpace.fixNode('000_FFF',n.tag)
#equal ux 2 floor
nodEast=sets.get_nodes_wire(setBusq=East1FloorWall, lstPtsWire=[geom.Pos3d(xEastWall,yHall,secondFloorElev),geom.Pos3d(xEastWall,LwallFirstFloor,secondFloorElev)], tol=0.01)
for n1 in nodEast:
    yn1=n1.get3dCoo[1]
    n2=West1FloorWall.getNodes.getNearestNode(geom.Pos3d(xWestWall,yn1,secondFloorElev))
    modelSpace.constraints.newEqualDOF(n1.tag,n2.tag,xc.ID([0]))

pnt=gridGeom.getSetPntXYZRange(xyzRange=((xWestWall,yDeck,firstFloorElev),(xWestWall,LwallBasement,firstFloorElev)),setName='pnt')
ln=sets.get_lines_on_points(setPoints=pnt, setLinName='ln', onlyIncluded=True)
for l in ln.lines:
    for n in l.getNodes:
        modelSpace.fixNode('0FF_FFF',n.tag)
        
pnt=gridGeom.getSetPntXYZRange(xyzRange=((xEastWall,LwallFirstFloor,firstFloorElev),(xEastWall,LwallBasement,firstFloorElev)),setName='pnt')
ln=sets.get_lines_on_points(setPoints=pnt, setLinName='ln', onlyIncluded=True)
for l in ln.lines:
    for n in l.getNodes:
        modelSpace.fixNode('0FF_FFF',n.tag)


#out.displayFEMesh()

#                       ***ACTIONS***
#selfweight
grav=9.81 #Gravity acceleration (m/s2)
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[EastBasementWall_mesh,East1FloorWall_mesh,South1FloorWall_mesh,WestBasementWall_mesh,West1FloorWall_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

#earth pressure
'''
EastBasementWall=gridGeom.getSetSurfMultiXYZRegion(
    lstXYZRange=[((xHall,0,foundElev),(xHall,yHall,firstFloorElev)),
     ((xEastWall,yHall,foundElev),(xEastWall,LwallBasement,firstFloorElev)),
    ], nameSet='EastBasementWall')
EastBasementWall.fillDownwards()
WestBasementWall=gridGeom.getSetSurfMultiXYZRegion(
    lstXYZRange=[((xWestWall,0,foundElev),(xWestWall,LwallBasement,firstFloorElev))], nameSet='WestBasementWall')
WestBasementWall.fillDownwards()
'''
soil_ramp=ep.EarthPressureSlopedWall(Ksoil=KearthPress, gammaSoil=grav*densSoil, zGroundPnt1=rampStartElev, XYpnt1=(xEastWall,0), zGroundPnt2=rampEndElev, XYpnt2=(xEastWall,LwallBasement))
earthPressEastwall=loads.EarthPressLoad(name= 'earthPressEastwall', xcSet=EastBasementWall,soilData=soil_ramp, vDir=xc.Vector([-1,0,0]))
earthPressWestwall=loads.EarthPressLoad(name= 'earthPressWestwall', xcSet=WestBasementWall,soilData=soil_ramp, vDir=xc.Vector([1,0,0]))

EarthPress=lcases.LoadCase(preprocessor=prep,name="EarthPress",loadPType="default",timeSType="constant_ts")
EarthPress.create()
EarthPress.addLstLoads([earthPressEastwall,earthPressWestwall])
modelSpace.addLoadCaseToDomain("EarthPress")
#out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("EarthPress")

#Linear loads (dead, live, snow,wind)
pntE2F=gridGeom.getSetPntMultiXYZRegion(lstXYZRange=[
    ((xHall,0,secondFloorElev),(xHall,yHall,secondFloorElev)),
    ((xEastWall,yHall,secondFloorElev),(xEastWall,LwallBasement,secondFloorElev))]
    ,setName='pntE2F')
lnE2F=sets.get_lines_on_points(setPoints=pntE2F, setLinName='lnE2F', onlyIncluded=True)

pntW2F=gridGeom.getSetPntMultiXYZRegion(lstXYZRange=[
    ((xWestWall,0,secondFloorElev),(xWestWall,LwallBasement,secondFloorElev))]
    ,setName='pntW2F')
lnW2F=sets.get_lines_on_points(setPoints=pntW2F, setLinName='lnW2F', onlyIncluded=True)

lnEW2F=lnE2F+lnW2F

Dead2F=loads.UniformLoadOnLines(name='Dead2F',xcSet=lnEW2F,loadVector=xc.Vector([0,0,-Dead_WE2F,0,0,0]))
Live2F=loads.UniformLoadOnLines(name='Live2F',xcSet=lnEW2F,loadVector=xc.Vector([0,0,-Live_WE2F,0,0,0]))
Snow2F=loads.UniformLoadOnLines(name='Snow2F',xcSet=lnEW2F,loadVector=xc.Vector([0,0,-Snow_WE2F,0,0,0]))
Wind2F=loads.UniformLoadOnLines(name='Wind2F',xcSet=lnEW2F,loadVector=xc.Vector([0,0,-Wind_WE2F,0,0,0]))
HWind2F=loads.UniformLoadOnLines(name='HWind2F',xcSet=lnE2F,loadVector=xc.Vector([WindH_E2F,0,0,0,0,0]))

pntE1F=gridGeom.getSetPntMultiXYZRegion(lstXYZRange=[
    ((xHall,0,firstFloorElev),(xHall,yHall,firstFloorElev)),
    ((xEastWall,yHall,firstFloorElev),(xEastWall,LwallBasement,firstFloorElev))]
    ,setName='pntE1F')
lnE1F=sets.get_lines_on_points(setPoints=pntE1F, setLinName='lnE1F', onlyIncluded=True)

Dead1F=loads.UniformLoadOnLines(name='Dead1F',xcSet=lnE1F,loadVector=xc.Vector([0,0,-Dead_E1F,0,0,0]))
Live1F=loads.UniformLoadOnLines(name='Live1F',xcSet=lnE1F,loadVector=xc.Vector([0,0,-Live_E1F,0,0,0]))
Snow1F=loads.UniformLoadOnLines(name='Snow1F',xcSet=lnE1F,loadVector=xc.Vector([0,0,-Snow_E1F,0,0,0]))
Wind1F=loads.UniformLoadOnLines(name='Wind1F',xcSet=lnE1F,loadVector=xc.Vector([0,0,-Wind_E1F,0,0,0]))
Earth1F=loads.UniformLoadOnLines(name='Earth1F',xcSet=lnE1F,loadVector=xc.Vector([Earth_E1F,0,0,0,0,0]))


Dead_LC=lcases.LoadCase(preprocessor=prep,name="Dead_LC",loadPType="default",timeSType="constant_ts")
Dead_LC.create()
Dead_LC.addLstLoads([selfWeight,Dead2F,Dead1F,Earth1F,earthPressEastwall,earthPressWestwall])
#modelSpace.addLoadCaseToDomain("Dead_LC")
#out.displayLoadVectors()
#modelSpace.removeLoadCaseFromDomain("Dead_LC")
'''
EarthP_LC=lcases.LoadCase(preprocessor=prep,name="EarthP_LC",loadPType="default",timeSType="constant_ts")
EarthP_LC.create()
EarthP_LC.addLstLoads([Earth1F,earthPressEastwall,earthPressWestwall])
modelSpace.addLoadCaseToDomain("EarthP_LC")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("EarthP_LC")
'''
Live_LC=lcases.LoadCase(preprocessor=prep,name="Live_LC",loadPType="default",timeSType="constant_ts")
Live_LC.create()
Live_LC.addLstLoads([Live2F,Live1F])
#modelSpace.addLoadCaseToDomain("Live_LC")
#out.displayLoadVectors()
#modelSpace.removeLoadCaseFromDomain("Live_LC")

Snow_LC=lcases.LoadCase(preprocessor=prep,name="Snow_LC",loadPType="default",timeSType="constant_ts")
Snow_LC.create()
Snow_LC.addLstLoads([Snow2F,Snow1F])
#modelSpace.addLoadCaseToDomain("Snow_LC")
#out.displayLoadVectors()
#modelSpace.removeLoadCaseFromDomain("Snow_LC")


Wind_LC=lcases.LoadCase(preprocessor=prep,name="Wind_LC",loadPType="default",timeSType="constant_ts")
Wind_LC.create()
Wind_LC.addLstLoads([Wind2F,Wind1F,HWind2F])
#modelSpace.addLoadCaseToDomain("Wind_LC")
#out.displayLoadVectors()
#modelSpace.removeLoadCaseFromDomain("Wind_LC")

#    ***LIMIT STATE COMBINATIONS***
combContainer= cc.CombContainer()  #Container of load combinations
# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
combContainer.ULS.perm.add('ELU01', '1.4*Dead_LC')
combContainer.ULS.perm.add('ELU02', '1.2*Dead_LC+1.6*Live_LC+0.5*Snow_LC')
combContainer.ULS.perm.add('ELU03', '1.2*Dead_LC+1.6*Snow_LC+0.5*Wind_LC')
combContainer.ULS.perm.add('ELU04', '1.2*Dead_LC+1.0*Live_LC+1.0*Wind_LC')
combContainer.ULS.perm.add('ELU05', '0.9*Dead_LC+1.0*Wind_LC')


from solution import predefined_solutions
modelSpace.removeAllLoadPatternsFromDomain()
modelSpace.addLoadCaseToDomain('Dead_LC')
analysis= predefined_solutions.simple_static_linear(FEcase)
result= analysis.analyze(1)
out.displayDispRot('uX')
out.displayIntForcDiag('My',beamXsteel)
out.displayIntForcDiag('Mz',beamXsteel)
out.displayIntForcDiag('My',beamsYsteel)
out.displayIntForcDiag('Mz',beamsYsteel)

