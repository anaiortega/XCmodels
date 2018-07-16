# -*- coding: utf-8 -*-

# Example taken from the publication: «Eurocode 2: worked examples», by
# the European Concrete Platform. Example 6.15
#
# It deals with a railway bridge deck made up bu a continuous slab of three
# spans with two orders of prestressing tendons (longitudinal and transversal
# prestressing).

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
xSpacGrid=3*[0.55]+2*[0.765]+[14]+[0.75]+2*[0.5]+[0.75]+[12]+[1.25]+[12]+[0.75]+2*[0.5]+[0.75]+[14]+2*[0.765]+3*[0.55]
ySpacGrid=4*[0.8875]+2*[0.75]+7*[0.5]+2*[0.75]+4*[0.8875]
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
nu=0.2           #Poisson ratio

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
slab_unif=gridGeom.genSurfOneRegion(ijkRange=slab_unif_rg,nameSet='slab_unif')
slab_step1=gridGeom.genSurfMultiRegion(lstIJKRange=slab_step1_rg,nameSet='slab_step1')
slab_step2=gridGeom.genSurfMultiRegion(lstIJKRange=slab_step2_rg,nameSet='slab_step2')
slab_step3=gridGeom.genSurfMultiRegion(lstIJKRange=slab_step3_rg,nameSet='slab_step3')
slab_step4=gridGeom.genSurfMultiRegion(lstIJKRange=slab_step4_rg,nameSet='slab_step4')

slab_unif.description='Inner slab (const. thickness)'
slab_step1.description='Extr. slab (var. thickness, step 1)'
slab_step2.description='Extr. slab (var. thickness, step 2)'
slab_step3.description='Extr. slab (var. thickness, step 3)'
slab_step4.description='Extr. slab (var. thickness, step 4)'


overallSet=prep.getSets.getSet('total')
