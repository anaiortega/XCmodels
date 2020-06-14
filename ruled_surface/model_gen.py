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
from model.geometry import geom_utils as gut
from materials.ehe import EHE_materials
#from materials.sia262 import SIA262_materials
from materials.ec3 import EC3_materials

# Default configuration of environment variables.
from postprocess.config import default_config

workingDirectory= default_config.findWorkingDirectory()+'/'
execfile(workingDirectory+'env_config.py')

#Data
Lx=8     
Ly=10
deltaH=4
hCol=2
roof_th=0.1

#Materials
concrete=EHE_materials.HA30

eSize= 0.2     #length of elements

#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)

# coordinates in global X,Y,Z axes for the grid generation
xList=list()
for i in range(int(math.floor(Lx/eSize))+1):
    xList.append(i*eSize)
yList=[0,Ly]
zList=[0,hCol]
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
r=gm.IJKRange((0,0,lastZpos),(lastXpos,0,lastZpos))
gridGeom.slopePointsRange(ijkRange=r,slopeX=deltaH/Lx,xZeroSlope=0)
r=gm.IJKRange((0,lastYpos,lastZpos),(lastXpos,lastYpos,lastZpos))
gridGeom.slopePointsRange(ijkRange=r,slopeX=-deltaH/Lx,xZeroSlope=Lx)

# ranges
roof_rg=[gm.IJKRange((0,0,lastZpos),(lastXpos,lastYpos,lastZpos))]

#Surfaces generation
roof=gridGeom.genSurfMultiRegion(lstIJKRange=roof_rg,setName='roof')

roof.description='Roof'
roof.color=cfg.colors['purple01']

#                         *** MATERIALS *** 
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())

# Isotropic elastic section-material appropiate for plate and shell analysis
roof_mat=tm.DeckMaterialData(name='roof_mat',thickness= roof_th,material=concrProp)
roof_mat.setupElasticSection(preprocessor=prep)   #creates the section-material


#                         ***FE model - MESH***

roof_mesh=fem.SurfSetToMesh(surfSet=roof,matSect=roof_mat,elemSize=eSize,elemType='ShellMITC4')
roof_mesh.generateMesh(prep) 

#                       ***BOUNDARY CONDITIONS***
#fixed DOF (ux:'0FF_FFF', uy:'F0F_FFF', uz:'FF0_FFF',
#           rx:'FFF_0FF', ry:'FFF_F0F', rz:'FFF_FF0')
p1=gridGeom.getPntGrid(indPnt=(0,0,lastZpos))
modelSpace.fixNode('000_FFF',p1.getNode().tag)
p2=gridGeom.getPntGrid(indPnt=(lastXpos,0,lastZpos))
modelSpace.fixNode('000_FFF',p2.getNode().tag)
p3=gridGeom.getPntGrid(indPnt=(0,lastYpos,lastZpos))
modelSpace.fixNode('000_FFF',p3.getNode().tag)
p4=gridGeom.getPntGrid(indPnt=(lastXpos,lastYpos,lastZpos))
modelSpace.fixNode('000_FFF',p4.getNode().tag)

#                       ***ACTIONS***

#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
#selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[beamXconcr_mesh,beamY_mesh,columnZconcr_mesh,deck_mesh,wall_mesh,foot_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[roof_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

#    ***LOAD CASES***

GselfWeight=lcases.LoadCase(preprocessor=prep,name="GselfWeight",loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])


overallSet=roof
