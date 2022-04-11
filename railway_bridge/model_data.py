# -*- coding: utf-8 -*-

# Example taken from the publication: «Eurocode 2: worked examples», by
# the European Concrete Platform. Example 6.15
#
# It deals with a railway bridge deck made up bu a continuous slab of three
# spans with two orders of prestressing tendons (longitudinal and transversal
# prestressing).

import os
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
xSpacGrid=3*[0.55]+2*[0.765]+[14]+[0.75]+2*[0.5]+[0.75]+[12]+[1.25]+[12]+[0.75]+2*[0.5]+[0.75]+[14]+2*[0.765]+3*[0.55]
ySpacGrid=4*[0.8875]+2*[0.75]+7*[0.5]+2*[0.75]+4*[0.8875]

thick_unif=1.5    #slab thickness in its inner part, where the thickness
                  #is constant
thick_steps=[0.721,0.963,1.205,1.413]  #steps in slab thickness
#Actions


#Materials
# concrete grade 35
fck=35e6         #compressive characteristic strength (Pa)
fcd=23.3e6       #compressive design strength (Pa)
fcd1=17.1e6      #compressive resistance for uncracked zones (Pa)
fcd2=12e6        #compressive resistance for cracked zones (Pa)
fctm=3.23e6      #mean value of tensile strength (Pa)
Ec=29.7e9        #modulus of elasticity (Pa)
G=12.4e9         #shear modulus (Pa)
nuc=0.2          #Poisson ratio

densConcr= 2500               #specific mass of concrete (kg/m3)

# Prestressing steel, strands fi 0.6''
fptk=1800e6      #characteristic strength (Pa)
fp01k=1600e6     #0.1% proofstress (Pa)
epspu=0.035      #total elongation at maximum load
Ep=195e9         #modulus of elasticity (MPa)

#Reinforcing steel, grade 500
fyk=500e6        #characteristic strength (Pa)
fyd=434.8e6      #design strength (Pa)
Es=200e9         #modulus of elasticity (Pa)

#concrete cover
cnom=0.035       #concrete cover (m)

eSize= 1.0     #length of elements

#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)

# coordinates in global X,Y,Z axes for the grid generation
xList=[sum(xSpacGrid[:i+1]) for i in range(len(xSpacGrid))]
yList=[sum(ySpacGrid[:i+1]) for i in range(len(ySpacGrid))]
zList=[0]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()

#Slope (in X direction, Y direction or both) the grid points in a range
#syntax: slopePointsRange(ijkRange,slopeX,xZeroSlope,slopeY,yZeroSlope)
#     ijkRange: range for the search.
#     slopeX: slope in X direction, expressed as deltaZ/deltaX 
#                       (defaults to 0 = no slope applied)
#     xZeroSlope: coordinate X of the "rotation axis".
#     slopeY: slope in Y direction, expressed as deltaZ/deltaY)
#                       (defaults to 0 = no slope applied)
#     yZeroSlope: coordinate Y of the "rotation axis".

r= gm.IJKRange((0,0,0),(lastXpos,4,lastZpos))
deltZ=1.5/2.0-0.6/2.0
deltY=yList[0]-yList[4]
gridGeom.slopePointsRange(ijkRange=r,slopeY=deltZ/deltY,yZeroSlope=yList[4])

r= gm.IJKRange((0,15,0),(lastXpos,lastYpos,lastZpos))
deltZ=1.5/2.0-0.6/2.0
deltY=yList[lastYpos]-yList[15]
gridGeom.slopePointsRange(ijkRange=r,slopeY=deltZ/deltY,yZeroSlope=yList[15])

#Ranges for lines and surfaces
slab_unif_rg=gm.IJKRange((0,0,lastZpos),(lastXpos,lastYpos,lastZpos))
slab_step1_rg=[gm.IJKRange((0,0,lastZpos),(lastXpos,1,lastZpos)),gm.IJKRange((0,lastYpos-1,lastZpos),(lastXpos,lastYpos,lastZpos))]
slab_step2_rg=[gm.IJKRange((0,1,lastZpos),(lastXpos,2,lastZpos)),gm.IJKRange((0,lastYpos-2,lastZpos),(lastXpos,lastYpos-1,lastZpos))]
slab_step3_rg=[gm.IJKRange((0,2,lastZpos),(lastXpos,3,lastZpos)),gm.IJKRange((0,lastYpos-3,lastZpos),(lastXpos,lastYpos-2,lastZpos))]
slab_step4_rg=[gm.IJKRange((0,3,lastZpos),(lastXpos,4,lastZpos)),gm.IJKRange((0,lastYpos-4,lastZpos),(lastXpos,lastYpos-3,lastZpos))]

#Surfaces generation
slab_unif=gridGeom.genSurfOneRegion(ijkRange=slab_unif_rg,setName='slab_unif')
slab_step1=gridGeom.genSurfMultiRegion(lstIJKRange=slab_step1_rg,setName='slab_step1')
slab_step2=gridGeom.genSurfMultiRegion(lstIJKRange=slab_step2_rg,setName='slab_step2')
slab_step3=gridGeom.genSurfMultiRegion(lstIJKRange=slab_step3_rg,setName='slab_step3')
slab_step4=gridGeom.genSurfMultiRegion(lstIJKRange=slab_step4_rg,setName='slab_step4')

slab_unif.description='Inner slab (const. thickness)'
slab_step1.description='Extr. slab (var. thickness, step 1)'
slab_step2.description='Extr. slab (var. thickness, step 2)'
slab_step3.description='Extr. slab (var. thickness, step 3)'
slab_step4.description='Extr. slab (var. thickness, step 4)'


#                         *** MATERIALS *** 
concrete=tm.MaterialData(name='concrete',E=Ec,nu=nuc,rho=densConcr)

# Isotropic elastic section-material appropiate for plate and shell analysis
slab_unif_mat=tm.DeckMaterialData(name='slab_unif_mat',thickness= thick_unif,material=concrete)
slab_unif_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
slab_step1_mat=tm.DeckMaterialData(name='slab_step1_mat',thickness= thick_steps[0],material=concrete)
slab_step1_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
slab_step2_mat=tm.DeckMaterialData(name='slab_step2_mat',thickness= thick_steps[1],material=concrete)
slab_step2_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
slab_step3_mat=tm.DeckMaterialData(name='slab_step3_mat',thickness= thick_steps[2],material=concrete)
slab_step3_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
slab_step4_mat=tm.DeckMaterialData(name='slab_step4_mat',thickness= thick_steps[3],material=concrete)
slab_step4_mat.setupElasticSection(preprocessor=prep)   #creates de section-material

#                         ***FE model - MESH***

slab_unif_mesh=fem.SurfSetToMesh(surfSet=slab_unif,matSect=slab_unif_mat,elemSize=eSize,elemType='ShellMITC4')
slab_step1_mesh=fem.SurfSetToMesh(surfSet=slab_step1,matSect=slab_step1_mat,elemSize=eSize,elemType='ShellMITC4')
slab_step2_mesh=fem.SurfSetToMesh(surfSet=slab_step2,matSect=slab_step2_mat,elemSize=eSize,elemType='ShellMITC4')
slab_step3_mesh=fem.SurfSetToMesh(surfSet=slab_step3,matSect=slab_step3_mat,elemSize=eSize,elemType='ShellMITC4')
slab_step4_mesh=fem.SurfSetToMesh(surfSet=slab_step4,matSect=slab_step4_mat,elemSize=eSize,elemType='ShellMITC4')

fem.multi_mesh(preprocessor=prep,lstMeshSets=[slab_unif_mesh,slab_step1_mesh,slab_step2_mesh,slab_step3_mesh,slab_step4_mesh])     #mesh these sets


#                       ***BOUNDARY CONDITIONS***

# Springs (defined by Kx,Ky,Kz) to apply on nodes, points, 3Dpos, ...
# Default values for Kx, Ky, Kz are 0, which means that no spring is
# created in the corresponding direction

#abutment A- springs XY
abutmA_spr1=sprbc.SpringBC(name='abutmA_spr1',modelSpace=modelSpace,Kx=9.55/12.*1e6,Ky=178.8/12.*1e6)
r= gm.IJKRange((1,8,0),(3,11,0))
abutmA_spr1_setkp=gridGeom.getSetPntRange(ijkRange=r, setName='abutmA_spr1_setkp')
abutmA_spr1.applyOnPointsInSet(setEnt=abutmA_spr1_setkp)

#abutments A and B- springs Z
abutmAB_spr2=sprbc.SpringBC(name='abutmAB_spr2',modelSpace=modelSpace,Kx=0,Ky=0,Kz=10.02/2.*1e6)
lstpos=[geom.Pos3d(xList[2],yList[5],zList[0]),geom.Pos3d(xList[2],yList[14],zList[0]),geom.Pos3d(xList[19],yList[5],zList[0]),geom.Pos3d(xList[19],yList[14],zList[0])]
abutmAB_spr2.applyOnNodesIn3Dpos(lst3DPos=lstpos)

#abutment B- springs Y
abutmB_spr1=sprbc.SpringBC(name='abutmB_spr1',modelSpace=modelSpace,Kx=0,Ky=2.78/6.*1e6)
r= gm.IJKRange((18,9,0),(20,10,0))
abutmB_spr1_setkp=gridGeom.getSetPntRange(ijkRange=r, setName='abutmB_spr1_setkp')
abutmB_spr1.applyOnPointsInSet(setEnt=abutmB_spr1_setkp)

#piers 1 and 2 springs Z
piers1_2_spr1=sprbc.SpringBC(name='piers1_2_spr1',modelSpace=modelSpace,Kx=0,Ky=0,Kz=11.61/18.*1e6)
r1= gm.IJKRange((7,11,0),(9,13,0))
piers1_2_spr1_setkp1=gridGeom.getSetPntRange(ijkRange=r1, setName='piers1_2_spr1_setkp1')
r2= gm.IJKRange((12,11,0),(14,13,0))
piers1_2_spr1_setkp2=gridGeom.getSetPntRange(ijkRange=r2, setName='piers1_2_spr1_setkp2')
piers1_2_spr1_setkp=piers1_2_spr1_setkp1+piers1_2_spr1_setkp2
piers1_2_spr1.applyOnPointsInSet(setEnt=piers1_2_spr1_setkp)

#pier 1- springs YZ
pier1_spr1=sprbc.SpringBC(name='pier1_spr1',modelSpace=modelSpace,Kx=0,Ky=4.74/9.*1e6,Kz=11.61/18.*1e6)
r= gm.IJKRange((7,6,0),(9,8,0))
pier1_spr1_setkp=gridGeom.getSetPntRange(ijkRange=r, setName='pier1_spr1_setkp')
pier1_spr1.applyOnPointsInSet(setEnt=pier1_spr1_setkp)

#pier 2- springs YZ
pier2_spr1=sprbc.SpringBC(name='pier2_spr1',modelSpace=modelSpace,Kx=0,Ky=2.66/9.*1e6,Kz=11.61/18.*1e6)
r= gm.IJKRange((12,6,0),(14,8,0))
pier2_spr1_setkp=gridGeom.getSetPntRange(ijkRange=r, setName='pier2_spr1_setkp')
pier2_spr1.applyOnPointsInSet(setEnt=pier2_spr1_setkp)


overallSet=prep.getSets.getSet('total')
