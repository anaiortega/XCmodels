
# -*- coding: utf-8 -*-

import os
import xc_base
import geom
import xc
import math
from model import predefined_spaces
from model.geometry import grid_model as gm
from model.mesh import finit_el_model as fem
from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets
from materials import typical_materials as tm
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc
from actions.earth_pressure import earth_pressure as ep
#Auxiliary data
 #Geometry
deckTh=0.40
wallTh=0.45
baseSlabTh=0.60
vertIntHeigCrochy=413.37-405.5+baseSlabTh  #vertical internal height Cochy side
intSpan=0.5+3+3+1.5
totalHeightCrochy=vertIntHeigCrochy+deckTh/2.0+baseSlabTh/2.0
totalwidth=intSpan+wallTh
trSlope=0.025     #transversal slope of the deck
lnSlope=0.029     #longitudinal slope of the foundation slab
  #Actions
asphaltDens=2400    #mass density of asphalt (kg/m3)
asphaltTh=0.12      #thickness of asphalt on the deck (m)
guardRailWght=500      #weight of the guard rail (N/m)
firad=math.radians(31)  #internal friction angle (radians)                   
KearthPress=(1-math.sin(firad))/(1+math.sin(firad))     #Active coefficient of pressure considered 
#soil= fs.FrictionalSoil(phi= firad)
#KearthPress= soil.K0Jaky() #Earth pressure at rest (see OFROU bridge manual chapter C03). 
densSoil=2200       #mass density of the soil (kg/m3)
densWater=1000      #mass density of the water (kg/m3)
   #traffic loads
     # adjustment coefficients (tableau 1 SIA-269) portée 5.3-10m
alphQ1act=0.6
alphQ2act=0.4
alphq1act=0.4
alphq2act=0.4
alphq3act=0.4
alphqract=0.4

Qk1=300e3          #(N in each axle)
Qk1wheel=300e3/2   #(N in each wheel)
Qk2=200e3          #(N in each axle)
Qk2wheel=Qk2/2     #(N in each wheel)
qk1=9e3            #(N/m2)
qk2=2.5e3          #(N/m2)
qk3=2.5e3          #(N/m2)
qkr=2.5e3          #(N/m2)

brakingQact=0.8*Qk1+0.07*qk1*3*totalwidth

#Winkler foundation model data
winkMod03=20e7         #Winkler modulus of subgrade reaction obtained from 0.3 m plate bearing test [N/m3] (20 kp/cm3)
fslabWidth=6
fslabLength=12
# KsSquareSlab=winkMod03*((fslabWidth+0.3)/(2*fslabWidth))**2 # Terzaghi formula that gives the subgrade reaction modulus for square slab foundations on sandy soils
KsSquareSlab=winkMod03*(0.3)/(fslabWidth) # Terzaghi formula that gives the subgrade reaction modulus for square slab foundations on clay soils
winkMod=KsSquareSlab*(1+0.5*fslabWidth/fslabLength)/1.5 # Extrapolation of Terzagi formula for rectangular foundation slabs.
coefHorVerSprings=0.25  #ratio between horizontal and vertical stiffness of springs

eSize= 0.4

#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3

# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)

# coordinates in global X,Y,Z axes for the grid generation
xList=[0,0.2*totalwidth,0.8*totalwidth,totalwidth]
yList=[0,0.38,0.58,0.78,3.78,6.78,9.78,12.08,12.28,12.66]
zList=[0,0.2*totalHeightCrochy,0.8*totalHeightCrochy,totalHeightCrochy]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()
#Displacements of the grid points in a range
for i in range(1,len(xList)):
    r= gm.IJKRange((i,0,lastZpos),(i,lastYpos,lastZpos))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,-trSlope*xList[i]]))

for j in range(1,len(yList)):
    r=gm.IJKRange((0,j,0),(lastXpos,j,0))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,lnSlope*yList[j]]))


#Ranges for lines and surfaces
foundExtSlab_rg= [ gm.IJKRange([0,0,0],[1,lastYpos,0]), gm.IJKRange([2,0,0],[lastXpos,lastYpos,0]) ]
foundIntSlab_rg= [ gm.IJKRange([1,0,0],[2,lastYpos,0])]
leftWall_rg= [ gm.IJKRange([0,0,0],[0,lastYpos,lastZpos])]
rightWall_rg= [gm.IJKRange([lastXpos,0,0],[lastXpos,lastYpos,lastZpos])]
deckExtSlab_rg= [ gm.IJKRange([0,0,lastZpos],[1,lastYpos,lastZpos]), gm.IJKRange([2,0,lastZpos],[lastXpos,lastYpos,lastZpos]) ]
deckIntSlab_rg= [ gm.IJKRange([1,0,lastZpos],[2,lastYpos,lastZpos])]
#Surfaces generation
foundExtSlab=gridGeom.genSurfMultiRegion(lstIJKRange=foundExtSlab_rg,setName='foundExtSlab')
foundIntSlab=gridGeom.genSurfMultiRegion(lstIJKRange=foundIntSlab_rg,setName='foundIntSlab')
leftWall=gridGeom.genSurfMultiRegion(lstIJKRange=leftWall_rg,setName='leftWall')
rightWall=gridGeom.genSurfMultiRegion(lstIJKRange=rightWall_rg,setName='rightWall')
deckExtSlab=gridGeom.genSurfMultiRegion(lstIJKRange=deckExtSlab_rg,setName='deckExtSlab')
deckIntSlab=gridGeom.genSurfMultiRegion(lstIJKRange=deckIntSlab_rg,setName='deckIntSlab')

#                         *** MATERIALS *** 
#*Auxiliary data
fcmDeck=36.5e6
EcDeck=8500*(fcmDeck/1e6)**(1/3.0)*1e6
fcmWalls=42.5e6
EcWalls=8500*(fcmWalls/1e6)**(1/3.0)*1e6
fcmFound=36.5e6
EcFound=8500*(fcmFound/1e6)**(1/3.0)*1e6
cpoish=0.2                #Poisson's coefficient of concrete
densh= 2500 #specific mass of concrete (kg/m3)

concrDeck=tm.MaterialData(name='concrDeck',E=EcDeck,nu=cpoish,rho=densh)
concrWalls=tm.MaterialData(name='concrWalls',E=EcWalls,nu=cpoish,rho=densh)
concrFound=tm.MaterialData(name='concrFound',E=EcFound,nu=cpoish,rho=densh)

# Isotropic elastic section-material appropiate for plate and shell analysis
deck_mat= tm.DeckMaterialData(name= 'deck_mat', thickness= deckTh,material=concrDeck)
deck_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
wall_mat= tm.DeckMaterialData(name= 'wall_mat', thickness= wallTh,material=concrWalls)
wall_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
found_mat= tm.DeckMaterialData(name= 'found_mat', thickness= baseSlabTh,material=concrFound)
found_mat.setupElasticSection(preprocessor=prep)   #creates de section-material

#                         ***FE model - MESH***

foundExtSlab_mesh=fem.SurfSetToMesh(surfSet=foundExtSlab,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)
foundIntSlab_mesh=fem.SurfSetToMesh(surfSet=foundIntSlab,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)
leftWall_mesh=fem.SurfSetToMesh(surfSet=leftWall,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)
rightWall_mesh=fem.SurfSetToMesh(surfSet=rightWall,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)
deckExtSlab_mesh=fem.SurfSetToMesh(surfSet=deckExtSlab,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)
deckIntSlab_mesh=fem.SurfSetToMesh(surfSet=deckIntSlab,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)

fem.multi_mesh(preprocessor=prep,lstMeshSets=[foundExtSlab_mesh,foundIntSlab_mesh,leftWall_mesh,rightWall_mesh,deckExtSlab_mesh,deckIntSlab_mesh])

#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
#foundationElasticSupports=
from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets
from materials import typical_materials as tm
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc
from actions.earth_pressure import earth_pressure as ep
#Auxiliary data
 #Geometry
deckTh=0.40
wallTh=0.45
baseSlabTh=0.60
vertIntHeigCrochy=413.37-405.5+baseSlabTh  #vertical internal height Cochy side
intSpan=0.5+3+3+1.5
totalHeightCrochy=vertIntHeigCrochy+deckTh/2.0+baseSlabTh/2.0
totalwidth=intSpan+wallTh
trSlope=0.025     #transversal slope of the deck
lnSlope=0.029     #longitudinal slope of the foundation slab
  #Actions
asphaltDens=2400    #mass density of asphalt (kg/m3)
asphaltTh=0.12      #thickness of asphalt on the deck (m)
guardRailWght=500      #weight of the guard rail (N/m)
firad=math.radians(31)  #internal friction angle (radians)                   
KearthPress=(1-math.sin(firad))/(1+math.sin(firad))     #Active coefficient of pressure considered 
#soil= fs.FrictionalSoil(phi= firad)
#KearthPress= soil.K0Jaky() #Earth pressure at rest (see OFROU bridge manual chapter C03). 
densSoil=2200       #mass density of the soil (kg/m3)
densWater=1000      #mass density of the water (kg/m3)
   #traffic loads
     # adjustment coefficients (tableau 1 SIA-269) portée 5.3-10m
alphQ1act=0.6
alphQ2act=0.4
alphq1act=0.4
alphq2act=0.4
alphq3act=0.4
alphqract=0.4

Qk1=300e3          #(N in each axle)
Qk1wheel=300e3/2   #(N in each wheel)
Qk2=200e3          #(N in each axle)
Qk2wheel=Qk2/2     #(N in each wheel)
qk1=9e3            #(N/m2)
qk2=2.5e3          #(N/m2)
qk3=2.5e3          #(N/m2)
qkr=2.5e3          #(N/m2)

brakingQact=0.8*Qk1+0.07*qk1*3*totalwidth

#Winkler foundation model data
winkMod03=20e7         #Winkler modulus of subgrade reaction obtained from 0.3 m plate bearing test [N/m3] (20 kp/cm3)
fslabWidth=6
fslabLength=12
# KsSquareSlab=winkMod03*((fslabWidth+0.3)/(2*fslabWidth))**2 # Terzaghi formula that gives the subgrade reaction modulus for square slab foundations on sandy soils
KsSquareSlab=winkMod03*(0.3)/(fslabWidth) # Terzaghi formula that gives the subgrade reaction modulus for square slab foundations on clay soils
winkMod=KsSquareSlab*(1+0.5*fslabWidth/fslabLength)/1.5 # Extrapolation of Terzagi formula for rectangular foundation slabs.
coefHorVerSprings=0.25  #ratio between horizontal and vertical stiffness of springs

eSize= 0.4

#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3

# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)

# coordinates in global X,Y,Z axes for the grid generation
xList=[0,0.2*totalwidth,0.8*totalwidth,totalwidth]
yList=[0,0.38,0.58,0.78,3.78,6.78,9.78,12.08,12.28,12.66]
zList=[0,0.2*totalHeightCrochy,0.8*totalHeightCrochy,totalHeightCrochy]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()
#Displacements of the grid points in a range
for i in range(1,len(xList)):
    r= gm.IJKRange((i,0,lastZpos),(i,lastYpos,lastZpos))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,-trSlope*xList[i]]))

for j in range(1,len(yList)):
    r=gm.IJKRange((0,j,0),(lastXpos,j,0))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,lnSlope*yList[j]]))


#Ranges for lines and surfaces
foundExtSlab_rg= [ gm.IJKRange([0,0,0],[1,lastYpos,0]), gm.IJKRange([2,0,0],[lastXpos,lastYpos,0]) ]
foundIntSlab_rg= [ gm.IJKRange([1,0,0],[2,lastYpos,0])]
leftWall_rg= [ gm.IJKRange([0,0,0],[0,lastYpos,lastZpos])]
rightWall_rg= [gm.IJKRange([lastXpos,0,0],[lastXpos,lastYpos,lastZpos])]
deckExtSlab_rg= [ gm.IJKRange([0,0,lastZpos],[1,lastYpos,lastZpos]), gm.IJKRange([2,0,lastZpos],[lastXpos,lastYpos,lastZpos]) ]
deckIntSlab_rg= [ gm.IJKRange([1,0,lastZpos],[2,lastYpos,lastZpos])]
#Surfaces generation
foundExtSlab=gridGeom.genSurfMultiRegion(lstIJKRange=foundExtSlab_rg,setName='foundExtSlab')
foundIntSlab=gridGeom.genSurfMultiRegion(lstIJKRange=foundIntSlab_rg,setName='foundIntSlab')
leftWall=gridGeom.genSurfMultiRegion(lstIJKRange=leftWall_rg,setName='leftWall')
rightWall=gridGeom.genSurfMultiRegion(lstIJKRange=rightWall_rg,setName='rightWall')
deckExtSlab=gridGeom.genSurfMultiRegion(lstIJKRange=deckExtSlab_rg,setName='deckExtSlab')
deckIntSlab=gridGeom.genSurfMultiRegion(lstIJKRange=deckIntSlab_rg,setName='deckIntSlab')

#                         *** MATERIALS *** 
#*Auxiliary data
fcmDeck=36.5e6
EcDeck=8500*fcmDeck/1e6**(1/3.0)*1e6
fcmWalls=42.5e6
EcWalls=8500*fcmWalls/1e6**(1/3.0)*1e6
fcmFound=36.5e6
EcFound=8500*fcmFound/1e6**(1/3.0)*1e6
cpoish=0.2                #Poisson's coefficient of concrete
densh= 2500 #specific mass of concrete (kg/m3)

concrDeck=tm.MaterialData(name='concrDeck',E=EcDeck,nu=cpoish,rho=densh)
concrWalls=tm.MaterialData(name='concrWalls',E=EcWalls,nu=cpoish,rho=densh)
concrFound=tm.MaterialData(name='concrFound',E=EcFound,nu=cpoish,rho=densh)

# Isotropic elastic section-material appropiate for plate and shell analysis
deck_mat= tm.DeckMaterialData(name= 'deck_mat', thickness= deckTh,material=concrDeck)
deck_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
wall_mat= tm.DeckMaterialData(name= 'wall_mat', thickness= wallTh,material=concrWalls)
wall_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
found_mat= tm.DeckMaterialData(name= 'found_mat', thickness= baseSlabTh,material=concrFound)
found_mat.setupElasticSection(preprocessor=prep)   #creates de section-material

#                         ***FE model - MESH***

foundExtSlab_mesh=fem.SurfSetToMesh(surfSet=foundExtSlab,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)
foundIntSlab_mesh=fem.SurfSetToMesh(surfSet=foundIntSlab,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)
leftWall_mesh=fem.SurfSetToMesh(surfSet=leftWall,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)
rightWall_mesh=fem.SurfSetToMesh(surfSet=rightWall,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)
deckExtSlab_mesh=fem.SurfSetToMesh(surfSet=deckExtSlab,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)
deckIntSlab_mesh=fem.SurfSetToMesh(surfSet=deckIntSlab,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)

fem.multi_mesh(preprocessor=prep,lstMeshSets=[foundExtSlab_mesh,foundIntSlab_mesh,leftWall_mesh,rightWall_mesh,deckExtSlab_mesh,deckIntSlab_mesh])

#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
foundationElasticSupports=sprbc.ElasticFoundation(wModulus=winkMod,cRoz=coefHorVerSprings)
found=foundExtSlab+foundIntSlab
foundationElasticSupports.generateSprings(xcSet=found)

#                       ***ACTIONS***
#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
selfWeight= loads.InertialLoad(name='selfWeight', lstMeshSets=[leftWall_mesh,rightWall_mesh,foundIntSlab_mesh,foundExtSlab_mesh,deckIntSlab_mesh,deckExtSlab_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

# Uniform loads applied on shell elements
#    name:       name identifying the load
#    xcSet:     set that contains the surfaces
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)

#  Dead load.
AsphaltSet_rg=gm.IJKRange([0,2,lastZpos],[lastXpos,lastYpos-2,lastZpos])
GuardrailSet_rg=[gm.IJKRange([0,1,lastZpos],[lastXpos,2,lastZpos]),gm.IJKRange([0,lastYpos-2,lastZpos],[lastXpos,lastYpos-1,lastZpos])]
Lane1Sit1Set_rg=gm.IJKRange([0,3,lastZpos],[lastXpos,4,lastZpos])
Lane1Sit2Set_rg=gm.IJKRange([0,5,lastZpos],[lastXpos,6,lastZpos])
Lane2Set_rg=gm.IJKRange([0,4,lastZpos],[lastXpos,5,lastZpos])
Lane3Sit1Set_rg=Lane1Sit2Set_rg
Lane3Sit2Set_rg=Lane1Sit1Set_rg
RestSet_rg=[gm.IJKRange([0,2,lastZpos],[lastXpos,3,lastZpos]),gm.IJKRange([0,6,lastZpos],[lastXpos,7,lastZpos])]

AsphaltSet=gridGeom.getSetSurfOneRegion(ijkRange=AsphaltSet_rg,setName='alphaltSet')
GuardrailSet=gridGeom.getSetSurfMultiRegion(lstIJKRange=GuardrailSet_rg,setName='GuardrailSet')
Lane1Sit1Set=gridGeom.getSetSurfOneRegion(ijkRange=Lane1Sit1Set_rg,setName='Lane1Sit1Set')
Lane1Sit2Set=gridGeom.getSetSurfOneRegion(ijkRange=Lane1Sit2Set_rg,setName='Lane1Sit2Set')
Lane2Set=gridGeom.getSetSurfOneRegion(ijkRange=Lane2Set_rg,setName='Lane2Set')
Lane3Sit1Set=gridGeom.getSetSurfOneRegion(ijkRange=Lane3Sit1Set_rg,setName='Lane3Sit1Set')
Lane3Sit2Set=gridGeom.getSetSurfOneRegion(ijkRange=Lane3Sit2Set_rg,setName='Lane3Sit2Set')
RestSet=gridGeom.getSetSurfMultiRegion(lstIJKRange=RestSet_rg,setName='RestSet')

        
            
deadLoadAsphalt= loads.UniformLoadOnSurfaces(name= 'deadLoadAsphalt',xcSet=AsphaltSet,loadVector= xc.Vector([0,0,-grav*asphaltDens*asphaltTh]))
deadLoadGuardrail=loads.UniformLoadOnSurfaces(name= 'deadLoadGuardrail',xcSet=GuardrailSet,loadVector= xc.Vector([0,0,-guardRailWght/(yList[2]-yList[1])]))
trafLoadSit1Lane1=loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Lane1',xcSet=Lane1Sit1Set,loadVector= xc.Vector([0,0,-alphq1act*qk1]))
trafLoadSit1Lane2=loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Lane2',xcSet=Lane2Set,loadVector= xc.Vector([0,0,-alphq2act*qk2]))
trafLoadSit1Lane3=loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Lane3',xcSet=Lane3Sit1Set,loadVector= xc.Vector([0,0,-alphq3act*qk3]))
trafLoadSit1Rest=loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Rest',xcSet=RestSet,loadVector= xc.Vector([0,0,-alphqract*qkr]))
trafLoadSit2Lane1=loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Lane1',xcSet=Lane1Sit2Set,loadVector= xc.Vector([0,0,-alphq1act*qk1]))
trafLoadSit2Lane2=loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Lane2',xcSet=Lane2Set,loadVector= xc.Vector([0,0,-alphq2act*qk2]))
trafLoadSit2Lane3=loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Lane3',xcSet=Lane3Sit2Set,loadVector= xc.Vector([0,0,-alphq3act*qk3]))
trafLoadSit2Rest=loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Rest',xcSet=RestSet,loadVector= xc.Vector([0,0,-alphqract*qkr]))

# Load acting on one or several nodes
#     name:       name identifying the load
#     lstNod:     list of nodes  on which the load is applied
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#auxilary fuction
def CoordTrainLoads(xmin,ymin,z):
  xmax=xmin+1.20
  ymax=ymin+2.0
  points=[geom.Pos3d(xmin,ymin,z),geom.Pos3d(xmin,ymax,z),geom.Pos3d(xmax,ymin,z),geom.Pos3d(xmax,ymax,z)]
  return sets.get_lstNod_from_lst3DPos(prep,points)
#

trafQLoadLane1Sit1a=loads.NodalLoad(name='trafQLoadLane1Sit1a',lstNod=CoordTrainLoads(0.2,yList[3]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1act*Qk1wheel,0,0,0]))
trafQLoadLane2Sit1a=loads.NodalLoad(name='trafQLoadLane2Sit1a',lstNod=CoordTrainLoads(0.2,yList[4]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2act*Qk2wheel,0,0,0]))
trafQLoadLane1Sit1b=loads.NodalLoad(name='trafQLoadLane1Sit1b',lstNod=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[3]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1act*Qk1wheel,0,0,0]))
trafQLoadLane2Sit1b=loads.NodalLoad(name='trafQLoadLane2Sit1b',lstNod=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[4]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2act*Qk2wheel,0,0,0]))
trafQLoadLane1Sit2a=loads.NodalLoad(name='trafQLoadLane1Sit2a',lstNod=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[5]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1act*Qk1wheel,0,0,0]))
trafQLoadLane2Sit2a=loads.NodalLoad(name='trafQLoadLane2Sit2a',lstNod=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[4]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2act*Qk2wheel,0,0,0]))
trafQLoadLane1Sit2b=loads.NodalLoad(name='trafQLoadLane1Sit2b',lstNod=CoordTrainLoads(0.5,yList[5]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1act*Qk1wheel,0,0,0]))
trafQLoadLane2Sit2b=loads.NodalLoad(name='trafQLoadLane2Sit2b',lstNod=CoordTrainLoads(0.5,yList[4]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2act*Qk2wheel,0,0,0]))

points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[3]+yList[4])/2.0,zList[lastZpos])]
trafBrakingSit1=loads.NodalLoad(name='trafBrakingSit1',lstNod=sets.get_lstNod_from_lst3DPos(prep,points),loadVector=xc.Vector([brakingQact,0,0,0,0,0]))
points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[5]+yList[6])/2.0,zList[lastZpos])]
trafBrakingSit2=loads.NodalLoad(name='trafBrakingSit2',lstNod=sets.get_lstNod_from_lst3DPos(prep,points),loadVector=xc.Vector([brakingQact,0,0,0,0,0]))


# Earth pressure applied to shell elements
#     Attributes:
#     name:       name identifying the load
#     xcSet:      set that contains the surfaces to be loaded
#     EarthPressureModel: instance of the class EarthPressureModel, with 
#                 the following attributes:
#                   K:Coefficient of pressure
#                   zGround:global Z coordinate of ground level
#                   gammaSoil: weight density of soil 
#                   zWater: global Z coordinate of groundwater level 
#                           (if zGroundwater<minimum z of model => there is no groundwater)
#                   gammaWater: weight density of water
#     vDir: unit xc vector defining pressures direction

soil01=ep.EarthPressureModel(zGround=zList[lastZpos],zBottomSoils=[-10],KSoils=[KearthPress], gammaSoils=[densSoil*grav], zWater=-10.0, gammaWater=densWater*grav)

earthPressLoadleftWall= loads.EarthPressLoad(name= 'earthPressLoadleftWall', xcSet=leftWall, soilData=soil01,vDir=xc.Vector([1,0,0]))
earthPressLoadrightWall= loads.EarthPressLoad(name= 'earthPressLoadrightWall',xcSet=rightWall, soilData=soil01, vDir=xc.Vector([-1,0,0]))

#    ***LOAD CASES***
GselfWeight= lcases.LoadCase(preprocessor=prep,name='GselfWeight',loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])
GdeadLoad= lcases.LoadCase(preprocessor=prep,name='GdeadLoad',loadPType="default",timeSType="constant_ts")
GdeadLoad.create()
GdeadLoad.addLstLoads([deadLoadAsphalt,deadLoadGuardrail])
GearthPress=lcases.LoadCase(preprocessor=prep,name='GearthPress',loadPType="default",timeSType="constant_ts")
GearthPress.create()
GearthPress.addLstLoads([earthPressLoadleftWall,earthPressLoadrightWall])
QtrafSit1a= lcases.LoadCase(preprocessor=prep,name='QtrafSit1a',loadPType="default",timeSType="constant_ts")
QtrafSit1a.create()
QtrafSit1a.addLstLoads([trafLoadSit1Lane1,trafLoadSit1Lane2,trafLoadSit1Lane3,trafLoadSit1Rest,trafQLoadLane1Sit1a,trafQLoadLane2Sit1a,trafBrakingSit1])
QtrafSit1b= lcases.LoadCase(preprocessor=prep,name='QtrafSit1b',loadPType="default",timeSType="constant_ts")
QtrafSit1b.create()
QtrafSit1b.addLstLoads([trafLoadSit1Lane1,trafLoadSit1Lane2,trafLoadSit1Lane3,trafLoadSit1Rest,trafQLoadLane1Sit1b,trafQLoadLane2Sit1b,trafBrakingSit1])
QtrafSit2a= lcases.LoadCase(preprocessor=prep,name='QtrafSit2a',loadPType="default",timeSType="constant_ts")
QtrafSit2a.create()
QtrafSit2a.addLstLoads([trafLoadSit2Lane1,trafLoadSit2Lane2,trafLoadSit2Lane3,trafLoadSit2Rest,trafQLoadLane1Sit2a,trafQLoadLane2Sit2a,trafBrakingSit2])
QtrafSit2b= lcases.LoadCase(preprocessor=prep,name='QtrafSit2b',loadPType="default",timeSType="constant_ts")
QtrafSit2b.create()
QtrafSit2b.addLstLoads([trafLoadSit2Lane1,trafLoadSit2Lane2,trafLoadSit2Lane3,trafLoadSit2Rest,trafQLoadLane1Sit2b,trafQLoadLane2Sit2b,trafBrakingSit2])

QtrafSit1unif= lcases.LoadCase(preprocessor=prep,name='QtrafSit1unif',loadPType="default",timeSType="constant_ts")
QtrafSit1unif.create()
QtrafSit1unif.addLstLoads([trafLoadSit1Lane1,trafLoadSit1Lane2,trafLoadSit1Lane3,trafLoadSit1Rest]) #defined only for the purpose of displaying
QtrafSit2unif= lcases.LoadCase(preprocessor=prep,name='QtrafSit2unif',loadPType="default",timeSType="constant_ts")
QtrafSit2unif.create()
QtrafSit2unif.addLstLoads([trafLoadSit2Lane1,trafLoadSit2Lane2,trafLoadSit2Lane3,trafLoadSit2Rest]) #defined only for the purpose of displaying

#LOAD COMBINATIONS
combContainer= cc.CombContainer()  #Container of load combinations

# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
    # name:        name to identify the combination
    # rare:        combination for a rare design situation
    # freq:        combination for a frequent design situation
    # qp:          combination for a quasi-permanent design situation
    # earthquake:  combination for a seismic design situation
#Characteristic combinations.
combContainer.SLS.rare.add('ELSR01', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafSit1a')
combContainer.SLS.rare.add('ELSR02', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafSit1b')
combContainer.SLS.rare.add('ELSR03', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafSit2a')
combContainer.SLS.rare.add('ELSR04', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafSit2b')
#Frequent combinations.
combContainer.SLS.freq.add('ELSF01', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+0.75*QtrafSit1a')
combContainer.SLS.freq.add('ELSF02', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+0.75*QtrafSit1b')
combContainer.SLS.freq.add('ELSF03', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+0.75*QtrafSit2a')
combContainer.SLS.freq.add('ELSF04', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+0.75*QtrafSit2b')
#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP01', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELU01', '1.2*GselfWeight+1.2*GdeadLoad+0.9*GearthPress+1.5*QtrafSit1a')
combContainer.ULS.perm.add('ELU02', '0.9*GselfWeight+0.9*GdeadLoad+1.2*GearthPress+1.5*QtrafSit1a')
combContainer.ULS.perm.add('ELU03', '1.2*GselfWeight+1.2*GdeadLoad+0.9*GearthPress+1.5*QtrafSit1b')
combContainer.ULS.perm.add('ELU04', '0.9*GselfWeight+0.9*GdeadLoad+1.2*GearthPress+1.5*QtrafSit1b')
combContainer.ULS.perm.add('ELU05', '1.2*GselfWeight+1.2*GdeadLoad+0.9*GearthPress+1.5*QtrafSit2a')
combContainer.ULS.perm.add('ELU06', '0.9*GselfWeight+0.9*GdeadLoad+1.2*GearthPress+1.5*QtrafSit2a')
combContainer.ULS.perm.add('ELU07', '1.2*GselfWeight+1.2*GdeadLoad+0.9*GearthPress+1.5*QtrafSit2b')
combContainer.ULS.perm.add('ELU08', '0.9*GselfWeight+0.9*GdeadLoad+1.2*GearthPress+1.5*QtrafSit2b')

#Fatigue.
combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+ 1.00*QtrafSit1a')

shellElements=foundExtSlab+foundIntSlab+leftWall+rightWall+deckExtSlab+deckIntSlab

foundation=foundExtSlab+foundIntSlab
foundation.name='foundation'
foundation.description='fondation'
walls=leftWall+rightWall
walls.name='walls'
walls.description='murs'
deck=deckExtSlab+deckIntSlab
deck.name='deck'
deck.description='dalle'
foundDeck=foundExtSlab+foundIntSlab+deckExtSlab+deckIntSlab
foundDeck.name='foundDeck'
foundDeck.description='dalle et fondation'

overallSet=prep.getSets.getSet('total')
