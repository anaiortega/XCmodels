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
from model.geometry import geom_utils as gut
from materials.ehe import EHE_materials
from materials.ec3 import EC3_materials

'''
# Default configuration of environment variables.
home= '/home/ana/projects/XCmodels/'

fullProjPath= home + 'cylind_model/'
execfile(fullProjPath+'env_config.py')
'''


#Materials
concrete=EHE_materials.HA30


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
xList=[0,2]
for i in range(20):
    xList.append(xList[-1]+0.2)
xList.append(8)
yList=[0,2]
for i in range(10):
    yList.append(yList[-1]+0.2)
yList.append(6)
zList=[0,5,7]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()

#Displacements of the grid points in a range to make them belong to 
#a vertical axis cylinder
#syntax: movePointsRangeToZcylinder(ijkRange,xCent,yCent,R)
#        ijkRange: range for the search
#        R: cylinder radius
#        xCent,yCent: coordinates of the cylinder axis
r= gm.IJKRange((1,0,0),(lastXpos-1,0,2))
gridGeom.movePointsRangeToZcylinder(ijkRange=r,xCent=4,yCent=4*math.cos(math.asin(2/4.)),R=4)

#Displacements of the grid points in a range to make them belong to 
#a cylinder with axis parallel to X 
#syntax: movePointsRangeToXcylinder(ijkRange,yCent,zCent,R)
#        ijkRange: range for the search
#        R: cylinder radius
#        yCent,zCent: coordinates of the cylinder axis
r= gm.IJKRange((0,1,lastZpos),(lastXpos,lastYpos-1,lastZpos))
gridGeom.movePointsRangeToXcylinder(ijkRange=r,yCent=3,zCent=zList[lastZpos]-1,R=1)

#Displacements of the grid points in a range to make them belong to 
#a cylinder with axis parallel to Y
#syntax: movePointsRangeToXcylinder(ijkRange,xCent,zCent,R)
#        ijkRange: range for the search
#        R: cylinder radius
#        xCent,zCent: coordinates of the cylinder axis
r= gm.IJKRange((1,1,1),(lastXpos-1,lastYpos,1))
gridGeom.movePointsRangeToYcylinder(ijkRange=r,xCent=4,zCent=zList[1]-4*math.cos(math.asin(2/4.)),R=4)


# ranges
flatwall_rg=[gm.IJKRange((0,0,0),(1,0,2)),gm.IJKRange((lastXpos-1,0,0),(lastXpos,0,2))]
cylwall_rg=[gm.IJKRange((1,0,0),(lastXpos-1,0,2))]
flatdeck_rg=[gm.IJKRange((0,0,lastZpos),(lastXpos,1,lastZpos))]
cyldeck_rg=[gm.IJKRange((0,1,lastZpos),(lastXpos,lastYpos-1,lastZpos))]
deck2_rg=[gm.IJKRange((1,1,1),(lastXpos-1,lastYpos,1))]

#Surfaces generation
flatwall=gridGeom.genSurfMultiRegion(lstIJKRange=flatwall_rg,nameSet='flatwall')
cylwall=gridGeom.genSurfMultiRegion(lstIJKRange=cylwall_rg,nameSet='cylwall')
flatdeck=gridGeom.genSurfMultiRegion(lstIJKRange=flatdeck_rg,nameSet='flatdeck')
cyldeck=gridGeom.genSurfMultiRegion(lstIJKRange=cyldeck_rg,nameSet='cyldeck')
deck2=gridGeom.genSurfMultiRegion(lstIJKRange=deck2_rg,nameSet='deck2')

'''
flatwall.description='Flat wall'
flatwall.color=cfg.colors['purple01']
cylwall.description='Cylindrical wall'
cylwall.color=cfg.colors['purple02']
flatdeck.description='Flat deck'
flatdeck.color=cfg.colors['blue01']
cyldeck.description='Cylindrical deck'
cyldeck.color=cfg.colors['blue02']
deck2.description='Cylindrical deck 2'
deck2.color=cfg.colors['green01']
'''

#                         *** MATERIALS *** 
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())
# Isotropic elastic section-material appropiate for plate and shell analysis
wall_mat=tm.DeckMaterialData(name='wall_mat',thickness= 0.2,material=concrProp)
wall_mat.setupElasticSection(preprocessor=prep)   #creates the section-material
deck_mat=tm.DeckMaterialData(name='deck_mat',thickness= 0.1,material=concrProp)
deck_mat.setupElasticSection(preprocessor=prep)   #creates the section-material


#                         ***FE model - MESH***
# Enforced lines' division
st=sets.get_subset_lin_parallel_to_axis(axis='Z',fromSet=flatwall+cylwall,toSetName='st')
fem.assign_ndiv_to_lines_in_set(lnSet=st,ndiv=5)
st.clear()
st=sets.get_subset_lin_parallel_to_axis(axis='X',fromSet=flatwall+flatdeck,toSetName='st')
fem.assign_ndiv_to_lines_in_set(lnSet=st,ndiv=3)
st.clear()
st=sets.get_subset_lin_parallel_to_axis(axis='Y',fromSet=flatdeck,toSetName='st',tol=0.01)
fem.assign_ndiv_to_lines_in_set(lnSet=st,ndiv=5)
st.clear()
st=sets.get_subset_lin_longer_than(Lmin=1.5,fromSet=deck2,toSetName='st')
fem.assign_ndiv_to_lines_in_set(lnSet=st,ndiv=3)
st.clear()
auxrg=[gm.IJKRange((0,1,lastZpos),(1,lastYpos-1,lastZpos)),gm.IJKRange((lastXpos-1,1,lastZpos),(lastXpos,lastYpos-1,lastZpos))]
auxSet=gridGeom.getSetSurfMultiRegion(lstIJKRange=auxrg, nameSet='auxSet')
st=sets.get_subset_lin_parallel_to_axis(axis='X',fromSet=auxSet,toSetName='st',tol=0.1)
fem.assign_ndiv_to_lines_in_set(lnSet=st,ndiv=3)
st.clear()
#Meshing
flatwall_mesh=fem.SurfSetToMesh(surfSet=flatwall,matSect=wall_mat,elemSize=None,elemType='ShellMITC4')
flatwall_mesh.generateMesh(prep) 
cylwall_mesh=fem.SurfSetToMesh(surfSet=cylwall,matSect=wall_mat,elemSize=None,elemType='ShellMITC4')
cylwall_mesh.generateMesh(prep) 
flatdeck_mesh=fem.SurfSetToMesh(surfSet=flatdeck,matSect=deck_mat,elemSize=None,elemType='ShellMITC4')
flatdeck_mesh.generateMesh(prep) 
cyldeck_mesh=fem.SurfSetToMesh(surfSet=cyldeck,matSect=deck_mat,elemSize=None,elemType='ShellMITC4')
cyldeck_mesh.generateMesh(prep) 
deck2_mesh=fem.SurfSetToMesh(surfSet=deck2,matSect=deck_mat,elemSize=None,elemType='ShellMITC4')
deck2_mesh.generateMesh(prep) 

overallSet=flatwall+cylwall+flatdeck+cyldeck+deck2
