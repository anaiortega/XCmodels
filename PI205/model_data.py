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
deckTh=0.55  
wallTh=0.45
baseSlabTh=0.60
vertIntHeigXmin=6.04  #vertical internal height X=0
intSpan=10.75
totalHeightXmin=vertIntHeigXmin+deckTh/2.0+baseSlabTh/2.0
totalwidth=intSpan+wallTh
  #Actions
asphaltDens=2400    #mass density of asphalt (kg/m3)
asphaltTh=0.12      #thickness of asphalt on the deck (m)
guardRailWght=500   #weight of the guard rail (N/m)
firad=math.radians(31)  #internal friction angle (radians)                   
KearthPress=(1-math.sin(firad))/(1+math.sin(firad))     #Active coefficient of pressure considered 
densSoil=2200       #mass density of the soil (kg/m3)
densWater=1000      #mass density of the water (kg/ms)
   #traffic loads
     # coefficients (depending on the traffic composition: hw-highway sr-subsidiary road)
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
YposLane1HwSit1=[9,10]
YposLane2HwSit1=[8,9]
YposLane3HwSit1=[7,8]
YposRestHwSit1=[5,7]
YposLane1HwSit2=[7,8]
YposLane2HwSit2=[6,7]
YposLane3HwSit2=[5,6]
YposRestHwSit2=[8,10]
YposLane1Sr=[3,4]

#Exceptional transport (model 3)
YposAxe=9    
excentr=0.5
distTrWheels=3
distLnWheels=1.8
xminTruck=1
QwheelExcTr=100e3     #load/wheel [N]
alphQExcTr=1.00   

      #Braking load
brakingQhw=min(1.2*alphQ1hw*Qk1+0.1*alphq1hw*qk1*3*totalwidth,900e3)  #in highway
brakingQsr=min(1.2*alphQ1sr*Qk1+0.1*alphq1sr*qk1*3*totalwidth,900e3)  #in subsidiary road
    #Road sub-base thickness
subbThHw=1.8         #mean sub-base thickness under the highway
subbThSr=1.2         #mean sub-base thickness under the subsidiary road
densSubb=2.2e3        #mass density (kg/m3) of the sub-base material

#Winkler foundation model data
winkMod03=20e7         #Winkler modulus of subgrade reaction obtained from 0.3 m plate bearing test [N/m3] (2 kp/cm3)
fslabWidth=12        
fslabLength=20
# KsSquareSlab=winkMod03*((fslabWidth+0.3)/(2*fslabWidth))**2 # Terzaghi formula that gives the subgrade reaction modulus for square slab foundations on sandy soils
KsSquareSlab=winkMod03*(0.3)/(fslabWidth) # Terzaghi formula that gives the subgrade reaction modulus for square slab foundations on clay soils
winkMod=KsSquareSlab*(1+0.5*fslabWidth/fslabLength)/1.5 # Extrapolation of Terzagi formula for rectangular foundation slabs.
coefHorVerSprings=0.2  #ratio between horizontal and vertical stiffness of springs


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


trSlope=0.035     #transversal slope of the deck


# coordinates in global X,Y,Z axes for the grid generation
xList=[0,0.2*totalwidth,0.8*totalwidth,totalwidth]
yList=[0,0.3,0.6,2.6,6.6,8.1,11.1,14.1,17.1,20.1,23.1,26.2,26.5,26.8]
zList=[0,0.2*totalHeightXmin,0.8*totalHeightXmin,totalHeightXmin]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

#Displacements of the grid points in a range
# for i in range(1,len(xList)):
#   r= ijkGrid.IJKRange([i,0,lastZpos],[i,lastYpos,lastZpos])
#   mr= ijkGrid.moveRange(r,[0.0,0.0,trSlope*xList[i]])
#   rejXYZ.rangesToMove.append(mr)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()

#Displacements of the grid points in a range
for i in range(1,len(xList)):
    r= gm.IJKRange((i,0,lastZpos),(i,lastYpos,lastZpos))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,trSlope*xList[i]]))


#Ranges for lines and surfaces
foundExtSlab_rg= [ gm.IJKRange([0,0,0],[1,lastYpos,0]), gm.IJKRange([2,0,0],[lastXpos,lastYpos,0]) ]
foundIntSlab_rg= [ gm.IJKRange([1,0,0],[2,lastYpos,0])]
leftWall_rg= [ gm.IJKRange([0,0,0],[0,lastYpos,lastZpos])]
rightWall_rg= [gm.IJKRange([lastXpos,0,0],[lastXpos,lastYpos,lastZpos])]
deckExtSlab_rg= [ gm.IJKRange([0,0,lastZpos],[1,lastYpos,lastZpos]), gm.IJKRange([2,0,lastZpos],[lastXpos,lastYpos,lastZpos]) ]
deckIntSlab_rg= [ gm.IJKRange([1,0,lastZpos],[2,lastYpos,lastZpos])]
#Surfaces generation
foundExtSlab=gridGeom.genSurfMultiRegion(lstIJKRange=foundExtSlab_rg,nameSet='foundExtSlab')
foundIntSlab=gridGeom.genSurfMultiRegion(lstIJKRange=foundIntSlab_rg,nameSet='foundIntSlab')
leftWall=gridGeom.genSurfMultiRegion(lstIJKRange=leftWall_rg,nameSet='leftWall')
rightWall=gridGeom.genSurfMultiRegion(lstIJKRange=rightWall_rg,nameSet='rightWall')
deckExtSlab=gridGeom.genSurfMultiRegion(lstIJKRange=deckExtSlab_rg,nameSet='deckExtSlab')
deckIntSlab=gridGeom.genSurfMultiRegion(lstIJKRange=deckIntSlab_rg,nameSet='deckIntSlab')

#                         *** MATERIALS *** 

#*Auxiliary data

fcmDeck=30e6
EcDeck=8500*(fcmDeck/1e6)**(1/3.0)*1e6
fcmWalls=30e6
EcWalls=8500*(fcmWalls/1e6)**(1/3.0)*1e6
fcmFound=30e6
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



eSize= 0.5

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


#Dead load.

# 
deadLoadAsphalt_rg=[gm.IJKRange([0,3,lastZpos],[lastXpos,4,lastZpos]),gm.IJKRange([0,5,lastZpos],[lastXpos,10,lastZpos])]
deadLoadSubbT1_rg=gm.IJKRange([0,2,lastZpos],[lastXpos,3,lastZpos])
deadLoadSubbSr_rg=gm.IJKRange([0,3,lastZpos],[lastXpos,4,lastZpos])
deadLoadSubbHw_rg=gm.IJKRange([0,4,lastZpos],[lastXpos,10,lastZpos])
deadLoadSubbT2_rg=gm.IJKRange([0,10,lastZpos],[lastXpos,11,lastZpos])
deadLoadGuardrail_rg=[gm.IJKRange([0,1,lastZpos],[lastXpos,2,lastZpos]),gm.IJKRange([0,lastYpos-2,lastZpos],[lastXpos,lastYpos-1,lastZpos])]

trafLoadSit1Lane1Hw_rg=gm.IJKRange([0,YposLane1HwSit1[0],lastZpos],[lastXpos,YposLane1HwSit1[1],lastZpos])
trafLoadSit1Lane2Hw_rg=gm.IJKRange([0,YposLane2HwSit1[0],lastZpos],[lastXpos,YposLane2HwSit1[1],lastZpos])
trafLoadSit1Lane3Hw_rg=gm.IJKRange([0,YposLane3HwSit1[0],lastZpos],[lastXpos,YposLane3HwSit1[1],lastZpos])
trafLoadSit1RestHw_rg=gm.IJKRange([0,YposRestHwSit1[0],lastZpos],[lastXpos,YposRestHwSit1[1],lastZpos])
trafLoadSit2Lane1Hw_rg=gm.IJKRange([0,YposLane1HwSit2[0],lastZpos],[lastXpos,YposLane1HwSit2[1],lastZpos])
trafLoadSit2Lane2Hw_rg=gm.IJKRange([0,YposLane2HwSit2[0],lastZpos],[lastXpos,YposLane2HwSit2[1],lastZpos])
trafLoadSit2Lane3Hw_rg=gm.IJKRange([0,YposLane3HwSit2[0],lastZpos],[lastXpos,YposLane3HwSit2[1],lastZpos])
trafLoadSit2RestHw_rg=gm.IJKRange([0,YposRestHwSit2[0],lastZpos],[lastXpos,YposRestHwSit2[1],lastZpos])
trafLoadSit12Lane1Sr_rg=gm.IJKRange([0,YposLane1Sr[0],lastZpos],[lastXpos,YposLane1Sr[1],lastZpos])

deadLoadAsphaltSet=gridGeom.getSetSurfMultiRegion(lstIJKRange=deadLoadAsphalt_rg,nameSet='deadLoadAsphaltSet')
deadLoadSubbT1Set=gridGeom.getSetSurfOneRegion(ijkRange=deadLoadSubbT1_rg,nameSet='deadLoadSubbT1Set')
deadLoadSubbSrSet=gridGeom.getSetSurfOneRegion(ijkRange=deadLoadSubbSr_rg,nameSet='deadLoadSubbSrSet')
deadLoadSubbHwSet=gridGeom.getSetSurfOneRegion(ijkRange=deadLoadSubbHw_rg,nameSet='deadLoadSubbHwSet')
deadLoadSubbT2Set=gridGeom.getSetSurfOneRegion(ijkRange=deadLoadSubbT2_rg,nameSet='deadLoadSubbT2Set')
deadLoadGuardrailSet=gridGeom.getSetSurfMultiRegion(lstIJKRange=deadLoadGuardrail_rg,nameSet='deadLoadGuardrailSet')

trafLoadSit1Lane1HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit1Lane1Hw_rg,nameSet='trafLoadSit1Lane1HwSet')
trafLoadSit1Lane2HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit1Lane2Hw_rg,nameSet='trafLoadSit1Lane2HwSet')
trafLoadSit1Lane3HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit1Lane3Hw_rg,nameSet='trafLoadSit1Lane3HwSet')
trafLoadSit1RestHwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit1RestHw_rg,nameSet='trafLoadSit1RestHwSet')
trafLoadSit2Lane1HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit2Lane1Hw_rg,nameSet='trafLoadSit2Lane1HwSet')
trafLoadSit2Lane2HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit2Lane2Hw_rg,nameSet='trafLoadSit2Lane2HwSet')
trafLoadSit2Lane3HwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit2Lane3Hw_rg,nameSet='trafLoadSit2Lane3HwSet')
trafLoadSit2RestHwSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit2RestHw_rg,nameSet='trafLoadSit2RestHwSet')
trafLoadSit12Lane1SrSet=gridGeom.getSetSurfOneRegion(ijkRange=trafLoadSit12Lane1Sr_rg,nameSet='trafLoadSit12Lane1SrSet')


deadLoadAsphalt=  loads.UniformLoadOnSurfaces(name= 'deadLoadAsphalt',xcSet=deadLoadAsphaltSet ,loadVector= xc.Vector([0,0,-grav*asphaltDens*asphaltTh]))
deadLoadSubbT1= loads.UniformLoadOnSurfaces(name= 'deadLoadSubbT1',xcSet=deadLoadSubbT1Set ,loadVector= xc.Vector([0,0,-densSubb*grav*subbThSr/2.0]))
deadLoadSubbSr= loads.UniformLoadOnSurfaces(name= 'deadLoadSubbSr',xcSet=deadLoadSubbSrSet ,loadVector= xc.Vector([0,0,-densSubb*grav*subbThSr]))
deadLoadSubbHw= loads.UniformLoadOnSurfaces(name= 'deadLoadSubbHw',xcSet=deadLoadSubbHwSet ,loadVector= xc.Vector([0,0,-densSubb*grav*subbThHw]))
deadLoadSubbT2= loads.UniformLoadOnSurfaces(name= 'deadLoadSubbT2',xcSet=deadLoadSubbT2Set ,loadVector= xc.Vector([0,0,-densSubb*grav*subbThHw/2.0]))
deadLoadGuardrail= loads.UniformLoadOnSurfaces(name= 'deadLoadGuardrail',xcSet=deadLoadGuardrailSet ,loadVector= xc.Vector([0,0,-guardRailWght/(yList[2]-yList[1])]))

trafLoadSit1Lane1Hw= loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Lane1Hw',xcSet=trafLoadSit1Lane1HwSet ,loadVector= xc.Vector([0,0,-alphq1hw*qk1]))
trafLoadSit1Lane2Hw= loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Lane2Hw',xcSet=trafLoadSit1Lane2HwSet ,loadVector= xc.Vector([0,0,-alphq2hw*qk2]))
trafLoadSit1Lane3Hw= loads.UniformLoadOnSurfaces(name= 'trafLoadSit1Lane3Hw',xcSet=trafLoadSit1Lane3HwSet ,loadVector= xc.Vector([0,0,-alphq3hw*qk3]))
trafLoadSit1RestHw= loads.UniformLoadOnSurfaces(name= 'trafLoadSit1RestHw',xcSet=trafLoadSit1RestHwSet ,loadVector= xc.Vector([0,0,-alphqrhw*qkr]))
trafLoadSit2Lane1Hw= loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Lane1Hw',xcSet=trafLoadSit2Lane1HwSet ,loadVector= xc.Vector([0,0,-alphq1hw*qk1]))
trafLoadSit2Lane2Hw= loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Lane2Hw',xcSet=trafLoadSit2Lane2HwSet ,loadVector= xc.Vector([0,0,-alphq2hw*qk2]))
trafLoadSit2Lane3Hw= loads.UniformLoadOnSurfaces(name= 'trafLoadSit2Lane3Hw',xcSet=trafLoadSit2Lane3HwSet ,loadVector= xc.Vector([0,0,-alphq3hw*qk3]))
trafLoadSit2RestHw= loads.UniformLoadOnSurfaces(name= 'trafLoadSit2RestHw',xcSet=trafLoadSit2RestHwSet ,loadVector= xc.Vector([0,0,-alphqrhw*qkr]))
trafLoadSit12Lane1Sr= loads.UniformLoadOnSurfaces(name= 'trafLoadSit12Lane1Sr',xcSet=trafLoadSit12Lane1SrSet ,loadVector= xc.Vector([0,0,-alphq1sr*qk1]))



# Load acting on one or several nodes
#     name:       name identifying the load
#     lstNod:     list of nodes  on which the load is applied
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#auxilary fuction

#auxilary fuction
def CoordTrainLoads(xmin,ymin,z):
  xmax=xmin+1.20
  ymax=ymin+2.0
  points=[geom.Pos3d(xmin,ymin,z),geom.Pos3d(xmin,ymax,z),geom.Pos3d(xmax,ymin,z),geom.Pos3d(xmax,ymax,z)]
  return sets.get_lstNod_from_lst3DPos(prep,points)
#
trafQLoadLane1HwSit1a=loads.NodalLoad(name='trafQLoadLane1HwSit1a',lstNod=CoordTrainLoads(0.2,yList[YposLane1HwSit1[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit1a=loads.NodalLoad(name='trafQLoadLane2HwSit1a',lstNod=CoordTrainLoads(0.2,yList[YposLane2HwSit1[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1HwSit1b=loads.NodalLoad(name='trafQLoadLane1HwSit1b',lstNod=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane1HwSit1[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit1b=loads.NodalLoad(name='trafQLoadLane2HwSit1b',lstNod=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane2HwSit1[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1HwSit2b=loads.NodalLoad(name='trafQLoadLane1HwSit2b',lstNod=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane1HwSit2[0]]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit2a=loads.NodalLoad(name='trafQLoadLane2HwSit2a',lstNod=CoordTrainLoads(0.5,yList[YposLane2HwSit2[0]]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1SrSit12a=loads.NodalLoad(name='trafQLoadLane1SrSit12a',lstNod=CoordTrainLoads(0.2,yList[YposLane1Sr[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1sr*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit2b=loads.NodalLoad(name='trafQLoadLane2HwSit2b',lstNod=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane2HwSit2[0]]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1HwSit2a=loads.NodalLoad(name='trafQLoadLane1HwSit2a',lstNod=CoordTrainLoads(0.5,yList[YposLane1HwSit2[0]]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane1SrSit12b=loads.NodalLoad(name='trafQLoadLane1SrSit12b',lstNod=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane1Sr[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1sr*Qk1wheel,0,0,0]))
points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1HwSit1[0]]+yList[YposLane1HwSit1[1]])/2.0,zList[lastZpos])]
trafBrakingHwSit1=loads.NodalLoad(name='trafBrakingHwSit1',lstNod=sets.get_lstNod_from_lst3DPos(prep,points),loadVector=xc.Vector([brakingQhw,0,0,0,0,0]))
points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1HwSit2[0]]+yList[YposLane1HwSit2[1]])/2.0,zList[lastZpos])]
trafBrakingHwSit2=loads.NodalLoad(name='trafBrakingHwSit2',lstNod=sets.get_lstNod_from_lst3DPos(prep,points),loadVector=xc.Vector([brakingQhw,0,0,0,0,0]))
points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1Sr[0]]+yList[YposLane1Sr[1]])/2.0,zList[lastZpos])]
trafBrakingSrSit12=loads.NodalLoad(name='trafBrakingSrSit12',lstNod=sets.get_lstNod_from_lst3DPos(prep,points),loadVector=xc.Vector([brakingQsr,0,0,0,0,0]))
#Exceptional transport
yminTruck=yList[YposAxe]-distTrWheels/2.0+excentr
ymaxTruck=yminTruck+distTrWheels
cWheelsET=[]
for i in range (0,6):
  xw=xminTruck+i*distLnWheels
  cWheelsET.append(geom.Pos3d(xw,yminTruck,zList[lastZpos]))
  cWheelsET.append(geom.Pos3d(xw,ymaxTruck,zList[lastZpos]))

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

soil01=ep.EarthPressureModel(zGround=zList[lastZpos]+subbThHw+asphaltTh,zBottomSoils=[-10], KSoils=[KearthPress],gammaSoils=[densSoil*grav], zWater=-10.0, gammaWater=densWater*grav)

earthPressLoadleftWall= loads.EarthPressLoad(name= 'earthPressLoadleftWall', xcSet=leftWall, soilData=soil01,vDir=xc.Vector([1,0,0]))
earthPressLoadrightWall= loads.EarthPressLoad(name= 'earthPressLoadrightWall',xcSet=rightWall, soilData=soil01, vDir=xc.Vector([-1,0,0]))


#    ***LOAD CASES***


GselfWeight= lcases.LoadCase(preprocessor=prep,name='GselfWeight',loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])
GdeadLoad= lcases.LoadCase(preprocessor=prep,name='GdeadLoad',loadPType="default",timeSType="constant_ts")
GdeadLoad.create()
GdeadLoad.addLstLoads([deadLoadAsphalt,deadLoadSubbT1,deadLoadSubbSr,deadLoadSubbHw,deadLoadSubbT2,deadLoadGuardrail])
GearthPress=lcases.LoadCase(preprocessor=prep,name='GearthPress',loadPType="default",timeSType="constant_ts")
GearthPress.create()
GearthPress.addLstLoads([earthPressLoadleftWall,earthPressLoadrightWall])
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

