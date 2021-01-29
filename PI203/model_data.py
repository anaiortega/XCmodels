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

# Ouvrage 203 - PI 1 echangeur Ecublens
#Auxiliary data
 #Geometry
upDeckTh=1.0
downDeckTh=1.0
upWallTh=0.7
downWallTh=1.0
midWallTh=0.7
baseSlabTh=1.1
maxVertIntHeig=9.10  #maximum vertical internal height
minVertIntHeig=5.65  #minimum vertical internal height
intSpan=1+3.75+3.75+3.50+1
totalmaxHeight=baseSlabTh/2.0+maxVertIntHeig+upDeckTh/2.0
totalminHeight=baseSlabTh/2.0+minVertIntHeig+downDeckTh/2.0
totalwidth=intSpan+downWallTh
zPosDownDeck=3

  #Actions
asphaltDens=2400    #mass density of asphalt (kg/m3)
asphaltTh=0.12      #thickness of asphalt on the deck (m)
guardRailWght=500      #weight of the guard rail (N/m)
firad=math.radians(31)  #internal friction angle (radians)                   
KearthPress=(1-math.sin(firad))/(1+math.sin(firad))     #Active coefficient of pressure considered 
densSoil=2200       #mass density of the soil (kg/m3)
densWater=1000      #mass density of the water (kg/ms)
   #traffic loads
     # adjustment coefficients 
alphQ1hw=0.9
alphQ2hw=0.9
alphq1hw=0.9
alphq2hw=0.9
alphq3hw=0.9
alphqrhw=0.9
alphQ1sr=0.65
alphq1sr=0.65

Qk1=300e3          #(N in each axle)
Qk1wheel=300e3/2   #(N in each wheel)
Qk2=200e3          #(N in each axle)
Qk2wheel=Qk2/2     #(N in each wheel)
qk1=9e3            #(N/m2)
qk2=2.5e3          #(N/m2)
qk3=2.5e3          #(N/m2)
qkr=2.5e3          #(N/m2)

#Y positions of traffic lanes in highway and subsidiary road
YposLane1HwSit1=[8,9]
YposLane2HwSit1=[7,8]
YposLane3HwSit1=[6,7]
YposRestHwSit1=[5,7]
YposLane1HwSit2=[7,8]
YposLane2HwSit2=[6,7]
YposLane3HwSit2=[5,6]
YposRestHwSit2=[8,9]
YposLane1Sr=[3,4]

fleetAngle=math.radians(25)
totalObliqWidth=totalwidth/math.sin(fleetAngle)

#Exceptional transport (model 3)
YposAxe=8    
excentr=0.5
distTrWheels=3
distLnWheels=1.8
xminTruck=1
QwheelExcTr=100e3     #load/wheel [N]
alphQExcTr=1.00   

      #Braking load
brakingQhw=min(1.2*alphQ1hw*Qk1+0.1*alphq1hw*qk1*3*totalObliqWidth,900e3)  #in highway
brakingQsr=min(1.2*alphQ1sr*Qk1+0.1*alphq1sr*qk1*3*totalObliqWidth,900e3)  #in subsidiary road
    #Road sub-base thickness
subbThSr=2.5         #mean sub-base thickness under the subsidiary road
gammaSubb=2e3        #mass density (kg/m3) of the sub-base material

#Winkler foundation model data
winkMod03=20e7         #Winkler modulus of subgrade reaction obtained from 0.3 m plate bearing test [N/m3] (2 kp/cm3)
fslabWidth=13        
fslabLength=20
# KsSquareSlab=winkMod03*((fslabWidth+0.3)/(2*fslabWidth))**2 # Terzaghi formula that gives the subgrade reaction modulus for square slab foundations on sandy soils
KsSquareSlab=winkMod03*(0.3)/(fslabWidth) # Terzaghi formula that gives the subgrade reaction modulus for square slab foundations on clay soils
winkMod=KsSquareSlab*(1+0.5*fslabWidth/fslabLength)/1.5 # Extrapolation of Terzagi formula for rectangular foundation slabs.
coefHorVerSprings=0.1  #ratio between horizontal and vertical stiffness of springs

#Materials
fcmDeck=30e6
EcDeck=8500*(fcmDeck/1e6)**(1/3.0)*1e6
fcmWalls=30e6
EcWalls=8500*(fcmWalls/1e6)**(1/3.0)*1e6
fcmFound=30e6
EcFound=8500*(fcmFound/1e6)**(1/3.0)*1e6
cpoish=0.2                #Poisson's coefficient of concrete
densh= 2500 #specific mass of concrete (kg/m3)

eSize= 1

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
yList=[0,0.35,0.7,5.1,12.9,15.3,22.2,29.1,36,42.9,45.5,45.85,46.2]
zList=[0,0.2*totalminHeight,0.8*totalminHeight,totalminHeight,0.8*totalmaxHeight,totalmaxHeight]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)


# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Points' generation
gridGeom.generatePoints()

#Displacements of the grid points in a range
for i in range(1,len(xList)):
  r= gm.IJKRange((i,0,0),(i,lastYpos,lastZpos))
  gridGeom.movePointsRange(r,xc.Vector([0.0,xList[i]/math.tan(fleetAngle),0.0]))

#Ranges for lines and surfaces
foundExtSlab_rg= [ gm.IJKRange([0,0,0],[1,lastYpos,0]), gm.IJKRange([2,0,0],[lastXpos,lastYpos,0]) ]
foundIntSlab_rg= [ gm.IJKRange([1,0,0],[2,lastYpos,0])]
leftDownWall_rg= [ gm.IJKRange([0,0,0],[0,lastYpos,3])]
leftUpWall_rg= [ gm.IJKRange([0,5,3],[0,lastYpos,lastZpos])]
rightDownWall_rg= [gm.IJKRange([lastXpos,0,0],[lastXpos,lastYpos,3])]
rightUpWall_rg= [gm.IJKRange([lastXpos,5,3],[lastXpos,lastYpos,lastZpos])]
midWall_rg= [gm.IJKRange([0,5,3],[lastXpos,5,lastZpos])]
upDeckExtSlab_rg= [ gm.IJKRange([0,5,lastZpos],[1,lastYpos,lastZpos]), gm.IJKRange([2,5,lastZpos],[lastXpos,lastYpos,lastZpos]) ]
upDeckIntSlab_rg= [ gm.IJKRange([1,5,lastZpos],[2,lastYpos,lastZpos])]
downDeckIntSlab_rg= [ gm.IJKRange([1,0,3],[2,5,3])]
downDeckExtSlab_rg= [ gm.IJKRange([0,0,3],[1,5,3]), gm.IJKRange([2,0,3],[lastXpos,5,3]) ]
#Surfaces generation
foundExtSlab=gridGeom.genSurfMultiRegion(lstIJKRange=foundExtSlab_rg,setName='foundExtSlab')
foundIntSlab=gridGeom.genSurfMultiRegion(lstIJKRange=foundIntSlab_rg,setName='foundIntSlab')
leftDownWall=gridGeom.genSurfMultiRegion(lstIJKRange=leftDownWall_rg,setName='leftDownWall')
leftUpWall=gridGeom.genSurfMultiRegion(lstIJKRange=leftUpWall_rg,setName='leftUpWall')
rightDownWall=gridGeom.genSurfMultiRegion(lstIJKRange=rightDownWall_rg,setName='rightDownWall')
rightUpWall=gridGeom.genSurfMultiRegion(lstIJKRange=rightUpWall_rg,setName='rightUpWall')
midWall=gridGeom.genSurfMultiRegion(lstIJKRange=midWall_rg,setName='midWall')
upDeckExtSlab=gridGeom.genSurfMultiRegion(lstIJKRange=upDeckExtSlab_rg,setName='upDeckExtSlab')
upDeckIntSlab=gridGeom.genSurfMultiRegion(lstIJKRange=upDeckIntSlab_rg,setName='upDeckIntSlab')
downDeckExtSlab=gridGeom.genSurfMultiRegion(lstIJKRange=downDeckExtSlab_rg,setName='downDeckExtSlab')
downDeckIntSlab=gridGeom.genSurfMultiRegion(lstIJKRange=downDeckIntSlab_rg,setName='downDeckIntSlab')


#                         *** MATERIALS *** 

concrDeck=tm.MaterialData(name='concrDeck',E=EcDeck,nu=cpoish,rho=densh)
concrWalls=tm.MaterialData(name='concrWalls',E=EcWalls,nu=cpoish,rho=densh)
concrFound=tm.MaterialData(name='concrFound',E=EcFound,nu=cpoish,rho=densh)


# Isotropic elastic section-material appropiate for plate and shell analysis

upDeck_mat= tm.DeckMaterialData(name= 'upDeck_mat',thickness= upDeckTh,material=concrDeck)
upDeck_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
downDeck_mat= tm.DeckMaterialData(name= 'downDeck_mat', thickness= downDeckTh,material=concrDeck)
downDeck_mat.setupElasticSection(preprocessor=prep)
upWall_mat= tm.DeckMaterialData(name= 'upWall_mat',thickness= upWallTh,material=concrWalls)
upWall_mat.setupElasticSection(preprocessor=prep)
midWall_mat=tm.DeckMaterialData(name= 'midWall_mat', thickness= midWallTh,material=concrWalls)
midWall_mat.setupElasticSection(preprocessor=prep)
downWall_mat= tm.DeckMaterialData(name= 'downWall_mat', thickness= downWallTh,material=concrWalls)
downWall_mat.setupElasticSection(preprocessor=prep)
found_mat= tm.DeckMaterialData(name= 'found_mat', thickness= baseSlabTh,material=concrFound)
found_mat.setupElasticSection(preprocessor=prep)

#                         ***FE model - MESH***

    # Types of surfaces to be discretized from the defined 
    # material, type of element and size of the elements.
    # Parameters:
    #   name:     name to identify the type of surface
    #   material: name of the material that makes up the surface
    #   elemType: element type to be used in the discretization
    #   elemSize: mean size of the elements
    #   ranges:   lists of grid ranges to delimit the surfaces of 
    #             the type in question
foundExtSlab_mesh=fem.SurfSetToMesh(surfSet=foundExtSlab,matSect=found_mat,elemType='ShellMITC4',elemSize= eSize)
foundIntSlab_mesh=fem.SurfSetToMesh(surfSet=foundIntSlab,matSect=found_mat,elemType='ShellMITC4',elemSize= eSize)

leftDownWall_mesh=fem.SurfSetToMesh(surfSet=leftDownWall,matSect=downWall_mat,elemType='ShellMITC4',elemSize= eSize)
leftUpWall_mesh=fem.SurfSetToMesh(surfSet=leftUpWall,matSect=upWall_mat,elemType='ShellMITC4',elemSize= eSize)
rightDownWall_mesh=fem.SurfSetToMesh(surfSet=rightDownWall,matSect=downWall_mat,elemType='ShellMITC4',elemSize= eSize)
rightUpWall_mesh=fem.SurfSetToMesh(surfSet=rightUpWall,matSect=upWall_mat,elemType='ShellMITC4',elemSize= eSize)
midWall_mesh=fem.SurfSetToMesh(surfSet=midWall,matSect=midWall_mat,elemType='ShellMITC4',elemSize= eSize)
upDeckExtSlab_mesh=fem.SurfSetToMesh(surfSet=upDeckExtSlab,matSect=upDeck_mat,elemType='ShellMITC4',elemSize= eSize)
upDeckIntSlab_mesh=fem.SurfSetToMesh(surfSet=upDeckIntSlab,matSect=upDeck_mat,elemType='ShellMITC4',elemSize= eSize)
downDeckExtSlab_mesh=fem.SurfSetToMesh(surfSet=downDeckExtSlab,matSect=downDeck_mat,elemType='ShellMITC4',elemSize= eSize)
downDeckIntSlab_mesh=fem.SurfSetToMesh(surfSet=downDeckIntSlab,matSect=downDeck_mat,elemType='ShellMITC4',elemSize= eSize)

allSurfList=[foundExtSlab_mesh,foundIntSlab_mesh,leftDownWall_mesh,leftUpWall_mesh,midWall_mesh,rightDownWall_mesh,rightUpWall_mesh,upDeckExtSlab_mesh,upDeckIntSlab_mesh,downDeckExtSlab_mesh,downDeckIntSlab_mesh]
fem.multi_mesh(preprocessor=prep,lstMeshSets=allSurfList)



#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
foundationElasticSupports=sprbc.ElasticFoundation(wModulus=winkMod,cRoz=coefHorVerSprings)
found=foundExtSlab+foundIntSlab
foundationElasticSupports.generateSprings(xcSet=found)


# ***** ACTIONS *****

#                       ***ACTIONS***
#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
gravSets=[stm.primitiveSet for stm in allSurfList]
selfWeight= loads.InertialLoad(name='selfWeight', lstSets=gravSets, vAccel=xc.Vector( [0.0,0.0,-grav]))


# Uniform loads applied on shell elements
#    name:       name identifying the load
#    xcSet:     set that contains the surfaces
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)




deadLoadAsphalt_rg= [gm.IJKRange([0,3,zPosDownDeck],[lastXpos,4,zPosDownDeck]),gm.IJKRange([0,5,lastZpos],[lastXpos,9,lastZpos])]
deadLoadSubbSr_rg=gm.IJKRange([0,2,zPosDownDeck],[lastXpos,5,zPosDownDeck])
deadLoadGuardrail_rg=[gm.IJKRange([0,1,zPosDownDeck],[lastXpos,2,zPosDownDeck]),gm.IJKRange([0,lastYpos-2,lastZpos],[lastXpos,lastYpos-1,lastZpos])]
trafLoadSit1Lane1Hw_rg=gm.IJKRange([0,YposLane1HwSit1[0],lastZpos],[lastXpos,YposLane1HwSit1[1],lastZpos])
trafLoadSit1Lane2Hw_rg=gm.IJKRange([0,YposLane2HwSit1[0],lastZpos],[lastXpos,YposLane2HwSit1[1],lastZpos])
trafLoadSit1Lane3Hw_rg=gm.IJKRange([0,YposLane3HwSit1[0],lastZpos],[lastXpos,YposLane3HwSit1[1],lastZpos])
trafLoadSit1RestHw_rg=gm.IJKRange([0,YposRestHwSit1[0],lastZpos],[lastXpos,YposRestHwSit1[1],lastZpos])
trafLoadSit2Lane1Hw_rg=gm.IJKRange([0,YposLane1HwSit2[0],lastZpos],[lastXpos,YposLane1HwSit2[1],lastZpos])
trafLoadSit2Lane2Hw_rg=gm.IJKRange([0,YposLane2HwSit2[0],lastZpos],[lastXpos,YposLane2HwSit2[1],lastZpos])
trafLoadSit2Lane3Hw_rg=gm.IJKRange([0,YposLane3HwSit2[0],lastZpos],[lastXpos,YposLane3HwSit2[1],lastZpos])
trafLoadSit2RestHw_rg=gm.IJKRange([0,YposRestHwSit2[0],lastZpos],[lastXpos,YposRestHwSit2[1],lastZpos])
trafLoadSit12Lane1Sr_rg=gm.IJKRange([0,YposLane1Sr[0],zPosDownDeck],[lastXpos,YposLane1Sr[1],zPosDownDeck])

deadLoadAsphaltSet=gridGeom.getSetSurfMultiRegion(lstIJKRange=deadLoadAsphalt_rg,setName='deadLoadAsphaltSet')
deadLoadSubbSrSet=gridGeom.getSetSurfOneRegion(ijkRange=deadLoadSubbSr_rg,setName='deadLoadSubbSrSet')
deadLoadGuardrailSet=gridGeom.getSetSurfMultiRegion(lstIJKRange=deadLoadGuardrail_rg,setName='deadLoadGuardrailSet')
trafLoadSit1Lane1HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit1Lane1Hw_rg,setName='trafLoadSit1Lane1HwSet')
trafLoadSit1Lane2HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit1Lane2Hw_rg,setName='trafLoadSit1Lane2HwSet')
trafLoadSit1Lane3HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit1Lane3Hw_rg,setName='trafLoadSit1Lane3HwSet')
trafLoadSit1RestHwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit1RestHw_rg,setName='trafLoadSit1RestHwSet')
trafLoadSit2Lane1HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit2Lane1Hw_rg,setName='trafLoadSit2Lane1HwSet')
trafLoadSit2Lane2HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit2Lane2Hw_rg,setName='trafLoadSit2Lane2HwSet')
trafLoadSit2Lane3HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit2Lane3Hw_rg,setName='trafLoadSit2Lane3HwSet')
trafLoadSit2RestHwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit2RestHw_rg,setName='trafLoadSit2RestHwSet')
trafLoadSit12Lane1SrSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit12Lane1Sr_rg,setName='trafLoadSit12Lane1SrSet')

deadLoadAsphalt= loads.UniformLoadOnSurfaces(name= 'deadLoadAsphalt',xcSet=deadLoadAsphaltSet ,loadVector= xc.Vector([0,0,-grav*asphaltDens*asphaltTh]))
deadLoadSubbSr=loads.UniformLoadOnSurfaces(name= 'deadLoadSubbSr',xcSet=deadLoadSubbSrSet ,loadVector= xc.Vector([0,0,-gammaSubb*grav*subbThSr]))
deadLoadGuardrail=loads.UniformLoadOnSurfaces(name= 'deadLoadGuardrail',xcSet=deadLoadGuardrailSet ,loadVector= xc.Vector([0,0,-guardRailWght/(yList[2]-yList[1])]))
trafLoadSit1Lane1Hw=loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Lane1Hw',xcSet=trafLoadSit1Lane1HwSet ,loadVector= xc.Vector([0,0,-alphq1hw*qk1]))
trafLoadSit1Lane2Hw=loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Lane2Hw',xcSet=trafLoadSit1Lane2HwSet ,loadVector= xc.Vector([0,0,-alphq2hw*qk2]))
trafLoadSit1Lane3Hw=loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Lane3Hw',xcSet=trafLoadSit1Lane3HwSet ,loadVector= xc.Vector([0,0,-alphq3hw*qk3]))
trafLoadSit1RestHw=loads.UniformLoadOnSurfaces(name= 'trafLoadSit1RestHw',xcSet=trafLoadSit1RestHwSet ,loadVector= xc.Vector([0,0,-alphqrhw*qkr]))
trafLoadSit2Lane1Hw=loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Lane1Hw',xcSet=trafLoadSit2Lane1HwSet ,loadVector= xc.Vector([0,0,-alphq1hw*qk1]))
trafLoadSit2Lane2Hw=loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Lane2Hw',xcSet=trafLoadSit2Lane2HwSet ,loadVector= xc.Vector([0,0,-alphq2hw*qk2]))
trafLoadSit2Lane3Hw=loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Lane3Hw',xcSet=trafLoadSit2Lane3HwSet ,loadVector= xc.Vector([0,0,-alphq3hw*qk3]))
trafLoadSit2RestHw=loads.UniformLoadOnSurfaces(name= 'trafLoadSit2RestHw',xcSet=trafLoadSit2RestHwSet ,loadVector= xc.Vector([0,0,-alphqrhw*qkr]))
trafLoadSit12Lane1Sr=loads.UniformLoadOnSurfaces(name= 'trafLoadSit12Lane1Sr',xcSet=trafLoadSit12Lane1SrSet ,loadVector= xc.Vector([0,0,-alphq1sr*qk1]))

# Load acting on one or several nodes
#     name:       name identifying the load
#     lstNod:     list of nodes  on which the load is applied
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).

#auxilary fuction

def RotatePoint(fleetAngle,lstCoordPto):
  x0=lstCoordPto[0]
  y0=lstCoordPto[1]
  z=lstCoordPto[2]
  x=x0-x0*math.sin(fleetAngle)
  y=y0+x0*math.cos(fleetAngle)
  return [x,y,z]

def CoordTrainLoads(fleetAngle,x,y,z):
#  print '[x0,y0]=',[x,y]
  rpto=RotatePoint(fleetAngle,[x,y,z])
  x1=rpto[0]
  y1=rpto[1]
  x2=x1-2*math.cos(fleetAngle)
  y2=y1+2*math.sin(fleetAngle)
  x3=x1+1.2*math.sin(fleetAngle)
  y3=y1+1.2*math.cos(fleetAngle)
  x4=x2+1.2*math.sin(fleetAngle)
  y4=y2+1.2*math.cos(fleetAngle)
#  print '[x1,y1]=',[x1,y1]
#  print '[x2,y2]=',[x2,y2]
#  print math.sqrt((x2-x1)**2+(y2-y1)**2)
#  print '[x3,y3]=',[x3,y3]
#  print math.sqrt((x3-x1)**2+(y3-y1)**2)
#  print '[x4,y4]=',[x4,y4]
#  print math.sqrt((x4-x3)**2+(y4-y3)**2)
  points=[geom.Pos3d(x1,y1,z),geom.Pos3d(x2,y2,z),geom.Pos3d(x3,y3,z),geom.Pos3d(x4,y4,z)]
  return sets.get_lstNod_from_lst3DPos(prep,points)

deltaX=3
deltaY=3
deltaY2=4

trafQLoadLane1HwSit1a=loads.NodalLoad(name='trafQLoadLane1HwSit1a',lstNod=CoordTrainLoads(fleetAngle,0.2+deltaX,yList[YposLane1HwSit1[0]]+deltaY,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit1a=loads.NodalLoad(name='trafQLoadLane2HwSit1a',lstNod=CoordTrainLoads(fleetAngle,0.2+deltaX,yList[YposLane2HwSit1[0]]+deltaY,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1HwSit1b=loads.NodalLoad(name='trafQLoadLane1HwSit1b',lstNod=CoordTrainLoads(fleetAngle,xList[lastXpos]/2.0+deltaX,yList[YposLane1HwSit1[0]]+deltaY2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit1b=loads.NodalLoad(name='trafQLoadLane2HwSit1b',lstNod=CoordTrainLoads(fleetAngle,xList[lastXpos]/2.0+deltaX,yList[YposLane2HwSit1[0]]+deltaY2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1HwSit2b=loads.NodalLoad(name='trafQLoadLane1HwSit2b',lstNod=CoordTrainLoads(fleetAngle,xList[lastXpos]/2.0+deltaX,yList[YposLane1HwSit2[0]]+deltaY2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit2a=loads.NodalLoad(name='trafQLoadLane2HwSit2a',lstNod=CoordTrainLoads(fleetAngle,0.2+deltaX,yList[YposLane2HwSit2[0]]+deltaY,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1SrSit12a=loads.NodalLoad(name='trafQLoadLane1SrSit12a',lstNod=CoordTrainLoads(fleetAngle,0.2+deltaX,yList[YposLane1Sr[0]]+deltaY,zList[zPosDownDeck]),loadVector=xc.Vector([0,0,-alphQ1sr*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit2b=loads.NodalLoad(name='trafQLoadLane2HwSit2b',lstNod=CoordTrainLoads(fleetAngle,xList[lastXpos]/2.0+deltaX,yList[YposLane2HwSit2[0]]+deltaY2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1HwSit2a=loads.NodalLoad(name='trafQLoadLane1HwSit2a',lstNod=CoordTrainLoads(fleetAngle,0.5+deltaX,yList[YposLane1HwSit2[0]]+deltaY,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane1SrSit12b=loads.NodalLoad(name='trafQLoadLane1SrSit12b',lstNod=CoordTrainLoads(fleetAngle,xList[lastXpos]/2.0+deltaX,yList[YposLane1Sr[0]]+deltaY2,zList[zPosDownDeck]),loadVector=xc.Vector([0,0,-alphQ1sr*Qk1wheel,0,0,0]))

points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1HwSit1[0]]+yList[YposLane1HwSit1[1]])/2.0+xList[lastXpos]/2.0/math.tan(fleetAngle),zList[lastZpos])]
trafBrakingHwSit1=loads.NodalLoad(name='trafBrakingHwSit1',lstNod=sets.get_lstNod_from_lst3DPos(prep,points),loadVector=xc.Vector([-brakingQhw*math.sin(fleetAngle),-brakingQhw*math.cos(fleetAngle),0,0,0,0]))

points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1HwSit2[0]]+yList[YposLane1HwSit2[1]])/2.0+xList[lastXpos]/2.0/math.tan(fleetAngle),zList[lastZpos])]
trafBrakingHwSit2=loads.NodalLoad(name='trafBrakingHwSit2',lstNod=sets.get_lstNod_from_lst3DPos(prep,points),loadVector=xc.Vector([-brakingQhw*math.sin(fleetAngle),-brakingQhw*math.cos(fleetAngle),0,0,0,0]))
points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1Sr[0]]+yList[YposLane1Sr[1]])/2.0+xList[zPosDownDeck]/2.0/math.tan(fleetAngle),zList[zPosDownDeck])]
trafBrakingSrSit12=loads.NodalLoad(name='trafBrakingSrSit12',lstNod=sets.get_lstNod_from_lst3DPos(prep,points),loadVector=xc.Vector([-brakingQsr*math.sin(fleetAngle)-brakingQsr*math.cos(fleetAngle),0,0,0,0]))

# #Exceptional transport
deltX=distLnWheels*math.sin(fleetAngle)
deltY=distLnWheels*math.cos(fleetAngle)
xDistWhells=distTrWheels*math.cos(fleetAngle)
yDistWhells=distTrWheels*math.sin(fleetAngle)

xWheel2=xminTruck
yWheel2=yList[YposAxe]+xminTruck/math.tan(fleetAngle)+(distTrWheels/2.0+excentr)/math.sin(fleetAngle)

xWheel1=xWheel2+xDistWhells
yWheel1=yWheel2-yDistWhells


cWheelsET=[]
for i in range (0,6):
  cWheelsET.append(geom.Pos3d(xWheel1+i*deltX,yWheel1+i*deltY,zList[lastZpos]))
  cWheelsET.append(geom.Pos3d(xWheel2+i*deltX,yWheel2+i*deltY,zList[lastZpos]))
#   print xWheel1+i*deltX,yWheel1+i*deltY
#   print xWheel2+i*deltX,yWheel2+i*deltY

# print 'Wheel1',xWheel1,yWheel1
# print 'Wheel2',xWheel2,yWheel2

# print 'deltX',deltX
# print 'deltY',deltY

points=cWheelsET
trafExceptTransp=loads.NodalLoad(name='trafExceptTransp',lstNod=sets.get_lstNod_from_lst3DPos(prep,points),loadVector=xc.Vector([0,0,-alphQExcTr*QwheelExcTr,0,0,0]))

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

soil01=ep.EarthPressureModel(zGround=zList[lastZpos]+asphaltTh,zBottomSoils=[-10],KSoils=[KearthPress], gammaSoils=[densSoil*grav], zWater=-10.0, gammaWater=densWater*grav)
leftWall=leftDownWall+leftUpWall
rightWall=rightDownWall+rightUpWall
earthPressLoadleftWall= loads.EarthPressLoad(name= 'earthPressLoadleftWall',xcSet=leftWall, soilData=soil01 ,vDir=xc.Vector([1,0,0]))
earthPressLoadrightWall= loads.EarthPressLoad(name= 'earthPressLoadrightWall', xcSet=rightWall, soilData=soil01, vDir=xc.Vector([-1,0,0]))
earthPressLoadmidWall= loads.EarthPressLoad(name= 'earthPressLoadmidWall', xcSet=midWall, soilData=soil01, vDir=xc.Vector([math.cos(fleetAngle),-math.sin(fleetAngle),0]))

#    ***LOAD CASES***
GselfWeight= lcases.LoadCase(preprocessor=prep,name='GselfWeight',loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])
GdeadLoad= lcases.LoadCase(preprocessor=prep,name='GdeadLoad',loadPType="default",timeSType="constant_ts")
GdeadLoad.create()
GdeadLoad.addLstLoads([deadLoadAsphalt,deadLoadSubbSr,deadLoadGuardrail])
GearthPress=lcases.LoadCase(preprocessor=prep,name='GearthPress',loadPType="default",timeSType="constant_ts")
GearthPress.create()
GearthPress.addLstLoads([earthPressLoadleftWall,earthPressLoadrightWall,earthPressLoadmidWall])
QtrafSit1a= lcases.LoadCase(preprocessor=prep,name='QtrafSit1a',loadPType="default",timeSType="constant_ts")
QtrafSit1a.create()
QtrafSit1a.addLstLoads([trafLoadSit1Lane1Hw,trafLoadSit1Lane2Hw,trafLoadSit1Lane3Hw,trafLoadSit1RestHw,trafLoadSit12Lane1Sr,trafQLoadLane1HwSit1a,trafQLoadLane2HwSit1a,trafBrakingHwSit1,trafQLoadLane1SrSit12a,trafBrakingSrSit12])
QtrafSit1b= lcases.LoadCase(preprocessor=prep,name='QtrafSit1b',loadPType="default",timeSType="constant_ts")
QtrafSit1b.create()
QtrafSit1b.addLstLoads([trafLoadSit1Lane1Hw,trafLoadSit1Lane2Hw,trafLoadSit1Lane3Hw,trafLoadSit1RestHw,trafLoadSit12Lane1Sr,trafQLoadLane1HwSit1b,trafQLoadLane2HwSit1b,trafBrakingHwSit1,trafQLoadLane1SrSit12b,trafBrakingSrSit12])
QtrafSit2a= lcases.LoadCase(preprocessor=prep,name='QtrafSit2a',loadPType="default",timeSType="constant_ts")
QtrafSit2a.create()
QtrafSit2a.addLstLoads([trafLoadSit2Lane1Hw,trafLoadSit2Lane2Hw,trafLoadSit2Lane3Hw,trafLoadSit2RestHw,trafLoadSit12Lane1Sr,trafQLoadLane1HwSit2a,trafQLoadLane2HwSit2a,trafBrakingHwSit2,trafQLoadLane1SrSit12a,trafBrakingSrSit12])
QtrafSit2b= lcases.LoadCase(preprocessor=prep,name='QtrafSit2b',loadPType="default",timeSType="constant_ts")
QtrafSit2b.create()
QtrafSit2b.addLstLoads([trafLoadSit2Lane1Hw,trafLoadSit2Lane2Hw,trafLoadSit2Lane3Hw,trafLoadSit2RestHw,trafLoadSit12Lane1Sr,trafQLoadLane1HwSit2b,trafQLoadLane2HwSit2b,trafBrakingHwSit2,trafQLoadLane1SrSit12b,trafBrakingSrSit12]) 

QtrafExcept= lcases.LoadCase(preprocessor=prep,name='QtrafExcept',loadPType="default",timeSType="constant_ts")
QtrafExcept.create()
QtrafExcept.addLstLoads([trafExceptTransp])

QtrafSit1aPoint= lcases.LoadCase(preprocessor=prep,name='QtrafSit1aPoint',loadPType="default",timeSType="constant_ts")
QtrafSit1aPoint.create()
QtrafSit1aPoint.addLstLoads([trafQLoadLane1HwSit1a])
QtrafSit1bPoint= lcases.LoadCase(preprocessor=prep,name='QtrafSit1bPoint',loadPType="default",timeSType="constant_ts")
QtrafSit1bPoint.create()
QtrafSit1bPoint.addLstLoads([trafQLoadLane1HwSit1b])
QtrafSit2aPoint= lcases.LoadCase(preprocessor=prep,name='QtrafSit2aPoint',loadPType="default",timeSType="constant_ts")
QtrafSit2aPoint.create()
QtrafSit2aPoint.addLstLoads([trafQLoadLane1HwSit2a])
QtrafSit2bPoint= lcases.LoadCase(preprocessor=prep,name='QtrafSit2bPoint',loadPType="default",timeSType="constant_ts")
QtrafSit2bPoint.create()
QtrafSit2bPoint.addLstLoads([trafQLoadLane1HwSit2b]) 

QtrafSit1unif= lcases.LoadCase(preprocessor=prep,name='QtrafSit1unif',loadPType="default",timeSType="constant_ts")
QtrafSit1unif.create()
QtrafSit1unif.addLstLoads([trafLoadSit1Lane1Hw,trafLoadSit1Lane2Hw,trafLoadSit1Lane3Hw,trafLoadSit1RestHw,trafLoadSit12Lane1Sr]) #defined only for the purpose of displaying
QtrafSit2unif= lcases.LoadCase(preprocessor=prep,name='QtrafSit2unif',loadPType="default",timeSType="constant_ts")
QtrafSit2unif.create()
QtrafSit2unif.addLstLoads([trafLoadSit2Lane1Hw,trafLoadSit2Lane2Hw,trafLoadSit2Lane3Hw,trafLoadSit2RestHw,trafLoadSit12Lane1Sr]) #defined only for the purpose of displaying



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
combContainer.SLS.rare.add('ELSR05', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafExcept')
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
combContainer.ULS.perm.add('ELU01', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafSit1a')
combContainer.ULS.perm.add('ELU02', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafSit1a')
combContainer.ULS.perm.add('ELU03', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafSit1b')
combContainer.ULS.perm.add('ELU04', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafSit1b')
combContainer.ULS.perm.add('ELU05', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafSit2a')
combContainer.ULS.perm.add('ELU06', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafSit2a')
combContainer.ULS.perm.add('ELU07', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafSit2b')
combContainer.ULS.perm.add('ELU08', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafSit2b')
combContainer.ULS.perm.add('ELU09', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafExcept')
combContainer.ULS.perm.add('ELU10', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafExcept')

#Fatigue.
combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress + 1.00*QtrafSit1aPoint')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress + 1.00*QtrafSit1bPoint')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress + 1.00*QtrafSit2aPoint')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress + 1.00*QtrafSit2bPoint')


#Sets of elements for graphical displays and reports
foundation=foundExtSlab+foundIntSlab
foundation.name='foundation'
foundation.description='fondation'
walls=leftDownWall+leftUpWall+rightDownWall+rightUpWall+midWall
walls.name='walls'
walls.description='murs'
upDeck=upDeckExtSlab+upDeckIntSlab
upDeck.name='upDeck'
upDeck.description='dalle supérieure'
downDeck=downDeckExtSlab+downDeckIntSlab
downDeck.name='downDeck'
downDeck.description='dalle inférieure'
deck=upDeck+downDeck
deck.name='deck'
deck.description='dalles'
foundDeck=foundExtSlab+foundIntSlab+upDeckExtSlab+upDeckIntSlab+downDeckExtSlab+downDeckIntSlab
foundDeck.name='foundDeck'
foundDeck.description='dalles et fondation'
shellElements=foundExtSlab+foundIntSlab+leftDownWall+leftUpWall+rightDownWall+rightUpWall+midWall+upDeckExtSlab+upDeckIntSlab+downDeckExtSlab+downDeckIntSlab+upDeckExtSlab+upDeckIntSlab+downDeckExtSlab+downDeckIntSlab
overallSet=prep.getSets.getSet('total')








