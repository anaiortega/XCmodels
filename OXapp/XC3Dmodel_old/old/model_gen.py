# -*- coding: utf-8 -*-

import os
import xc_base
import geom
import xc
import math
from model import predefined_spaces as psp
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
#home= '/home/luis/projects/XCmodels/OXapp/'
home= '/home/luis/Documents/XCmodels/OXapp/'

fullProjPath= home + 'XC3Dmodel/'
execfile(fullProjPath+'env_config.py')
execfile(fullProjPath+'data.py')

#Auxiliary data
#Materials
concrete=EHE_materials.HA30
reinfSteel=EHE_materials.B500S
# concrete=SIA262_materials.c30_37
# reinfSteel=SIA262_materials.B500B

eSize= 0.35     #length of elements

#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= psp.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)


# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()


#Ranges for lines and surfaces
# extractIncludedIJranges(step): subranges index K=constant (default step=1)
# extractIncludedIKranges((step): subranges index J=constant (default step=1)
# extractIncludedJKranges((step): subranges index I=constant (default step=1)
# extractIncludedIranges(stepJ,stepK): subranges indexes J,K=constant (default
#                                      stpes= 1)
# idem for J and K ranges

#  Columns
k1=zList.index(0)
k2=zList.index(zCol)

colA_rg=[]
i=xList.index(xCols[0])
for y in yCols:
    j=yList.index(y)
    colA_rg.append(gm.IJKRange((i,j,k1),(i,j,k2)))
colB_rg=[]
i=xList.index(xCols[1])
for y in yCols:
    j=yList.index(y)
    colB_rg.append(gm.IJKRange((i,j,k1),(i,j,k2)))
colC_rg=[]
i=xList.index(xCols[2])
for y in yCols:
    j=yList.index(y)
    colC_rg.append(gm.IJKRange((i,j,k1),(i,j,k2)))
colD_rg=[]
i=xList.index(xCols[3])
for y in yCols:
    j=yList.index(y)
    colD_rg.append(gm.IJKRange((i,j,k1),(i,j,k2)))
colG_rg=[]
i=xList.index(xCols[4])
for y in yCols:
    j=yList.index(y)
    colG_rg.append(gm.IJKRange((i,j,k1),(i,j,k2)))
colF_rg=[]
i=xList.index(xCols[5])
for y in yCols:
    j=yList.index(y)
    colF_rg.append(gm.IJKRange((i,j,k1),(i,j,k2)))

#Beams
beamA_rg=[]
i=xList.index(xCols[0])
k=zList.index(zBeamHigh)
beamA_rg.append(gm.IJKRange((i,0,k),(i,yList.index(yCols[0]-gap/2.0),k)))
for j in range(len(yCols)-1):
    beamA_rg.append(gm.IJKRange((i,yList.index(yCols[j]+gap/2.),k),(i,yList.index(yCols[j+1]-gap/2.0),k)))
beamA_rg.append(gm.IJKRange((i,yList.index(yCols[-1]+gap/2.),k),(i,lastYpos,k)))

beamB_rg=[]
i=xList.index(xCols[1])
k=zList.index(zBeamHigh)
for j in range(1,len(yCols)-1):
    beamB_rg.append(gm.IJKRange((i,yList.index(yCols[j]+gap/2.),k),(i,yList.index(yCols[j+1]-gap/2.0),k)))
beamB_rg.append(gm.IJKRange((i,yList.index(yCols[-1]+gap/2.),k),(i,lastYpos,k)))

beamC_rg=[]
i=xList.index(xCols[2])
k=zList.index(zBeamHigh)
beamC_rg.append(gm.IJKRange((i,yList.index(yCols[-1]+gap/2.),k),(i,lastYpos,k)))

beamD_rg=[]
i=xList.index(xCols[3])
k=zList.index(zBeamHigh)
beamD_rg.append(gm.IJKRange((i,yList.index(yCols[-1]+gap/2.),k),(i,lastYpos,k)))

beamG_rg=[]
i=xList.index(xCols[4])
k=zList.index(zBeamHigh)
beamG_rg.append(gm.IJKRange((i,yList.index(yCols[-1]+gap/2.),k),(i,lastYpos,k)))

beamF_rg=[]
i=xList.index(xCols[5])
k=zList.index(zBeamHigh)
beamF_rg.append(gm.IJKRange((i,yList.index(yCols[-1]+gap/2.),k),(i,lastYpos,k)))

beam1_rg=[]
j=yList.index(yCols[0])
k=zList.index(zBeamHigh)
for i in range(1,len(xCols)-1):
    beam1_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))
beam1_rg.append(gm.IJKRange((xList.index(xCols[-1]+gap/2.),j,k),(lastXpos,j,k)))

beam2H_rg=[]
j=yList.index(yCols[1])
k=zList.index(zBeamHigh)
i=1
beam2H_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))
for i in range(3,len(xCols)-1):
    beam2H_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))
beam2H_rg.append(gm.IJKRange((xList.index(xCols[-1]+gap/2.),j,k),(lastXpos,j,k)))

beam2L_rg=[]
j=yList.index(yCols[1])
k=zList.index(zBeamHigh)
i=2
beam2L_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))

beam3H_rg=[]
j=yList.index(yCols[2])
k=zList.index(zBeamHigh)
i=1
beam3H_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))
for i in range(3,len(xCols)-1):
    beam3H_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))
beam3H_rg.append(gm.IJKRange((xList.index(xCols[-1]+gap/2.),j,k),(lastXpos,j,k)))

beam3L_rg=[]
j=yList.index(yCols[2])
k=zList.index(zBeamHigh)
i=2
beam3L_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))

beam4H_rg=[]
j=yList.index(yCols[3])
k=zList.index(zBeamHigh)
i=1
beam4H_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))
for i in range(3,len(xCols)-1):
    beam4H_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))
beam4H_rg.append(gm.IJKRange((xList.index(xCols[-1]+gap/2.),j,k),(lastXpos,j,k)))

beam4L_rg=[]
j=yList.index(yCols[3])
k=zList.index(zBeamHigh)
i=2
beam4L_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))

beam5H_rg=[]
j=yList.index(yCols[4])
k=zList.index(zBeamHigh)
i=1
beam5H_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))
for i in range(3,len(xCols)-1):
    beam5H_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))
beam5H_rg.append(gm.IJKRange((xList.index(xCols[-1]+gap/2.),j,k),(lastXpos,j,k)))

beam5L_rg=[]
j=yList.index(yCols[4])
k=zList.index(zBeamHigh)
i=2
beam5L_rg.append(gm.IJKRange((xList.index(xCols[i]+gap/2.),j,k),(xList.index(xCols[i+1]-gap/2.0),j,k)))


# Precast slabs

slabW1_rg=[]
j1=0
j2=yList.index(yCols[0]-gap/2.)
k=zList.index(zHlwHigh)
slabW1_rg.append(gm.IJKRange((0,j1,k),(xList.index(xRamp[0]),j2,k)))

slab12_rg=[]
j1=yList.index(yCols[0]+gap/2.)
j2=yList.index(yCols[1]-gap/2.)
k=zList.index(zHlwHigh)
slab12_rg.append(gm.IJKRange((0,j1,k),(xList.index(xRamp[0]),j2,k)))
slab12_rg.append(gm.IJKRange((xList.index(xRamp[0]),j1,k),(xList.index(xCols[0]-gap/2.),j2,k)))

slab23_rg=[]
j1=yList.index(yCols[1]+gap/2.)
j2=yList.index(yCols[2]-gap/2.)
k=zList.index(zHlwHigh)
slab23_rg.append(gm.IJKRange((0,j1,k),(xList.index(xCols[1]-gap/2.),j2,k)))

slab34_rg=[]
j1=yList.index(yCols[2]+gap/2.)
j2=yList.index(yStair1[0])
k=zList.index(zHlwHigh)
slab34_rg.append(gm.IJKRange((0,j1,k),(xList.index(xCols[1]-gap/2.),j2,k)))
j1=yList.index(yStair1[0])
j2=yList.index(yCols[3]-gap/2.)
slab34_rg.append(gm.IJKRange((xList.index(xCols[0]),j1,k),(xList.index(xCols[1]-gap/2.),j2,k)))

slab45_rg=[]
j1=yList.index(yCols[3]+gap/2.)
j2=yList.index(yCols[4]-gap/2.)
k=zList.index(zHlwHigh)
slab45_rg.append(gm.IJKRange((0,j1,k),(xList.index(xCols[1]-gap/2.),j2,k)))

slab5W_rg=[]
j1=yList.index(yCols[4]+gap/2.)
j2=yList.index(yFac[-1])
k=zList.index(zHlwHigh)
slab5W_rg.append(gm.IJKRange((0,j1,k),(xList.index(xCols[2]-gap/2.),j2,k)))
slab5W_rg.append(gm.IJKRange((xList.index(xCols[3]+gap/2.),j1,k),(xList.index(xFac[-1]),j2,k)))

slabBC_rg=[]
i1=xList.index(xStair2Elev[0])
i2=xList.index(xCols[2]-gap/2.)
k=zList.index(zHlwHigh)
slabBC_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yCols[0]),k)))
i1=xList.index(xCols[1]+gap/2.)
i2=xList.index(xCols[2]-gap/2.)
k=zList.index(zHlwHigh)
slabBC_rg.append(gm.IJKRange((i1,yList.index(yCols[0]),k),(i2,yList.index(yCols[-1]-gap/2.),k)))

slabCD_H_rg=[]
i1=xList.index(xCols[2]+gap/2.0)
i2=xList.index(xCols[3]-gap/2.)
k=zList.index(zHlwHigh)
slabCD_H_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yFac[1]),k)))
slabCD_L_rg=[]
k=zList.index(zHlwLow)
slabCD_L_rg.append(gm.IJKRange((i1,yList.index(yCols[0]),k),(i2,lastYpos,k)))

slabDG_rg=[]
i1=xList.index(xCols[3]+gap/2.)
i2=xList.index(xCols[4]-gap/2.)
k=zList.index(zHlwHigh)
slabDG_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yCols[-1]-gap/2.),k)))

slabGF_rg=[]
i1=xList.index(xCols[4]+gap/2.)
i2=xList.index(xCols[-1]-gap/2.)
k=zList.index(zHlwHigh)
slabGF_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yCols[-1]-gap/2.),k)))

slabFW_rg=[]
i1=xList.index(xCols[-1]+gap/2.)
i2=xList.index(xFac[3])
k=zList.index(zHlwHigh)
slabFW_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yCols[-1]-gap/2.),k)))

slabsF_L_rg=[]
i1=xList.index(xFac[3])
i2=lastXpos
k=zList.index(zHlwLow)
slabsF_L_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yFac[2]),k)))


slabs5_L_rg=[]
j1=yList.index(yFac[2])
j2=lastYpos
k=zList.index(zHlwLow)
slabs5_L_rg.append(gm.IJKRange((0,j1,k),(xList.index(xCols[2]),j2,k)))
slabs5_L_rg.append(gm.IJKRange((xList.index(xCols[3]),j1,k),(lastXpos,j2,k)))


#Lines generation
colA=gridGeom.genLinMultiRegion(lstIJKRange=colA_rg,nameSet='colA')
colB=gridGeom.genLinMultiRegion(lstIJKRange=colB_rg,nameSet='colB')
colC=gridGeom.genLinMultiRegion(lstIJKRange=colC_rg,nameSet='colC')
colD=gridGeom.genLinMultiRegion(lstIJKRange=colD_rg,nameSet='colD')
colG=gridGeom.genLinMultiRegion(lstIJKRange=colG_rg,nameSet='colG')
colF=gridGeom.genLinMultiRegion(lstIJKRange=colF_rg,nameSet='colF')
beamA=gridGeom.genLinMultiRegion(lstIJKRange=beamA_rg,nameSet='beamA')
beamB=gridGeom.genLinMultiRegion(lstIJKRange=beamB_rg,nameSet='beamB')
beamC=gridGeom.genLinMultiRegion(lstIJKRange=beamC_rg,nameSet='beamC')
beamD=gridGeom.genLinMultiRegion(lstIJKRange=beamD_rg,nameSet='beamD')
beamG=gridGeom.genLinMultiRegion(lstIJKRange=beamG_rg,nameSet='beamG')
beamF=gridGeom.genLinMultiRegion(lstIJKRange=beamF_rg,nameSet='beamF')
beam1=gridGeom.genLinMultiRegion(lstIJKRange=beam1_rg,nameSet='beam1')
beam2H=gridGeom.genLinMultiRegion(lstIJKRange=beam2H_rg,nameSet='beam2H')
beam2L=gridGeom.genLinMultiRegion(lstIJKRange=beam2L_rg,nameSet='beam2L')
beam3H=gridGeom.genLinMultiRegion(lstIJKRange=beam3H_rg,nameSet='beam3H')
beam3L=gridGeom.genLinMultiRegion(lstIJKRange=beam3L_rg,nameSet='beam3L')
beam4H=gridGeom.genLinMultiRegion(lstIJKRange=beam4H_rg,nameSet='beam4H')
beam4L=gridGeom.genLinMultiRegion(lstIJKRange=beam4L_rg,nameSet='beam4L')
beam5H=gridGeom.genLinMultiRegion(lstIJKRange=beam5H_rg,nameSet='beam5H')
beam5L=gridGeom.genLinMultiRegion(lstIJKRange=beam5L_rg,nameSet='beam5L')


#Surfaces generation
slabW1=gridGeom.genSurfMultiRegion(lstIJKRange=slabW1_rg,nameSet='slabW1')
slab12=gridGeom.genSurfMultiRegion(lstIJKRange=slab12_rg,nameSet='slab12')
slab23=gridGeom.genSurfMultiRegion(lstIJKRange=slab23_rg,nameSet='slab23')
slab34=gridGeom.genSurfMultiRegion(lstIJKRange=slab34_rg,nameSet='slab34')
slab45=gridGeom.genSurfMultiRegion(lstIJKRange=slab45_rg,nameSet='slab45')
slab5W=gridGeom.genSurfMultiRegion(lstIJKRange=slab5W_rg,nameSet='slab5W')
slabBC=gridGeom.genSurfMultiRegion(lstIJKRange=slabBC_rg,nameSet='slabBC')
slabCD_H=gridGeom.genSurfMultiRegion(lstIJKRange=slabCD_H_rg,nameSet='slabCD_H')
slabCD_L=gridGeom.genSurfMultiRegion(lstIJKRange=slabCD_L_rg,nameSet='slabCD_L')
slabDG=gridGeom.genSurfMultiRegion(lstIJKRange=slabDG_rg,nameSet='slabDG')
slabGF=gridGeom.genSurfMultiRegion(lstIJKRange=slabGF_rg,nameSet='slabGF')
slabFW=gridGeom.genSurfMultiRegion(lstIJKRange=slabFW_rg,nameSet='slabFW')

slabsF_L=gridGeom.genSurfMultiRegion(lstIJKRange=slabsF_L_rg,nameSet='slabsF_L')
slabs5_L=gridGeom.genSurfMultiRegion(lstIJKRange=slabs5_L_rg,nameSet='slabs5_L')

columns=colA+colB+colC+colD+colG+colF
columns.fillDownwards()
columns.description='Columns'
columns.color=cfg.colors['green01']
beams= beamA+beamB+beamC+beamD+beamG+beamF+beam1+beam2H+beam2L+beam3H+beam3L+beam4H+beam4L+beam5H+beam5L
beams.fillDownwards()
beams.description='Beams'
slabs_H=slabW1+slab12+slab23+slab34+slab45+slab5W+slabBC+slabCD_H+slabDG+slabGF+slabFW
slabs_H.fillDownwards()
slabs_H.description='Precast planks, top level'
slabs_L=slabCD_L+slabsF_L+slabs5_L
slabs_L.fillDownwards()
slabs_L.description='Precast planks, down level'
slabs=slabs_H+slabs_L
slabs.fillDownwards()
slabs.description='Precast planks'


#                         *** MATERIALS *** 
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())

# Isotropic elastic section-material appropiate for plate and shell analysis
slabs_mat=tm.DeckMaterialData(name='slabs_mat',thickness= slabTh,material=concrProp)
slabs_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectBeams=sectpr.RectangularSection(name='geomSectBeams',b=beamWidth,h=beamHeight)
geomSectColumns=sectpr.RectangularSection(name='geomSectBeamY',b=colYdim,h=colXdim)

# Elastic material-section appropiate for 3D beam analysis, including shear
  # deformations.
  # Attributes:
  #   name:         name identifying the section
  #   section:      instance of a class that defines the geometric and
  #                 mechanical characteristiscs
  #                 of a section (e.g: RectangularSection, CircularSection,
  #                 ISection, ...)
  #   material:     instance of a class that defines the elastic modulus,
  #                 shear modulus and mass density of the material

beams_mat= tm.BeamMaterialData(name= 'beams_mat', section=geomSectBeams, material=concrProp)
beams_mat.setupElasticShear3DSection(preprocessor=prep)
columns_mat= tm.BeamMaterialData(name= 'columns_mat', section=geomSectColumns, material=concrProp)
columns_mat.setupElasticShear3DSection(preprocessor=prep)


#                         ***FE model - MESH***
# IMPORTANT: it's convenient to generate the mesh of surfaces before meshing
# the lines, otherwise, sets of shells can take also beam elements touched by
# them


beams_mesh=fem.LinSetToMesh(linSet=beams,matSect=beams_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,0,1]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
columns_mesh=fem.LinSetToMesh(linSet=columns,matSect=columns_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',coordTransfType='linear')
slabs_mesh=fem.SurfSetToMesh(surfSet=slabs,matSect=slabs_mat,elemSize=eSize,elemType='ShellMITC4')
slabs_mesh.generateMesh(prep)     #mesh the set of surfaces

fem.multi_mesh(preprocessor=prep,lstMeshSets=[beams_mesh,columns_mesh])

column_sets=[colA,colB,colC,colD,colG,colF]
for st in column_sets:
    st.fillDownwards()

beam2=beam2H+beam2L
beam3=beam3H+beam3L
beam4=beam4H+beam4L
beam5=beam5H+beam5L
beams_sets=[beamA,beamB,beamC,beamD,beamG,beamF,beam1,beam2,beam3,beam4,beam5]
for st in beams_sets:
    st.fillDownwards()
slabs_sets=[slabW1,slab12,slab23,slab34,slab45,slab5W,slabBC,slabCD_H,slabCD_L,slabDG,slabGF,slabFW,slabCD_L,slabsF_L,slabs5_L]
for st in slabs_sets:
    st.fillDownwards()
slabs_H.fillDownwards()
slabs_L.fillDownwards()


#                       ***BOUNDARY CONDITIONS***

# Springs (defined by Kx,Ky,Kz) to apply on nodes, points, 3Dpos, ...
# Default values for Kx, Ky, Kz are 0, which means that no spring is
# created in the corresponding direction
# spring_col=sprbc.SpringBC(name='spring_col',modelSpace=modelSpace,Kx=10e3,Ky=50e3,Kz=30e3)
# a=spring_col.applyOnNodesIn3Dpos(lst3DPos=[geom.Pos3d(0,LbeamY,0)])

#fixed DOF (ux:'0FF_FFF', uy:'F0F_FFF', uz:'FF0_FFF',
#           rx:'FFF_0FF', ry:'FFF_F0F', rz:'FFF_FF0')
# Column bases
for c in columns.getLines:
    tangVector= c.getTang(0.0)
    gluedDOFs= list()
    for i in range(0,len(tangVector)):
        s= tangVector[i]
        if(s!=0.0):
            gluedDOFs.append(3+i)
    columnFirstNode= c.firstNode
    columnFirstNodePos= columnFirstNode.getInitialPos3d
    if(abs(columnFirstNodePos.z)<0.01):
        modelSpace.fixNode('000_000',columnFirstNode.tag)
    columnLastNode= c.lastNode
    columnLastNodePos= columnLastNode.getInitialPos3d
    if(abs(columnLastNodePos.z)<0.01):
        modelSpace.fixNode('000_000',columnLastNode.tag)
    
# Simple support beams on walls
xMin= xList[0]; yMin= yList[0]
xMax= xList[-1]; yMax= yList[-1]

def nodeOnEdge(node):
    retval= False
    nodePos= node.getInitialPos3d
    if(abs(nodePos.x-xMin)<.01):
        retval= True
    elif(abs(nodePos.x-xMax)<.01):
        retval= True
    elif(abs(nodePos.y-yMin)<.01):
        retval= True
    elif(abs(nodePos.y-yMax)<.01):
        retval= True
    return retval

for l in beams.getLines:
    tangVector= l.getTang(0.0)
    gluedDOFs= [0,1,2]
    for i in range(0,len(tangVector)):
        s= tangVector[i]
        if(s!=0.0):
            gluedDOFs.append(3+i)
    for node in [l.firstNode, l.lastNode]:
        if nodeOnEdge(node):
            for nc in gluedDOFs:
                modelSpace.constraints.newSPConstraint(node.tag,nc,0.0)

#Links between beams and columns
for l in beams.getLines:
    tangVector= l.getTang(0.0)
    gluedDOFs= list()
    for i in range(0,len(tangVector)):
        s= tangVector[i]
        if(s!=0.0):
            gluedDOFs.append(3+i)
    beamFirstNode= l.firstNode
    beamFirstNodePos= beamFirstNode.getInitialPos3d
    nCol= columns.nodes.getNearestNode(beamFirstNodePos)
    nColPos= nCol.getInitialPos3d
    dist= nColPos.distPos3d(beamFirstNodePos)
    if(dist<2.0*gap):
        fulcrumNode= modelSpace.setFulcrumBetweenNodes(nCol.tag,beamFirstNode.tag)
        modelSpace.constraints.newEqualDOF(fulcrumNode.tag,beamFirstNode.tag,xc.ID(gluedDOFs)) #torsion
    beamLastNode= l.firstNode
    beamLastNodePos= beamLastNode.getInitialPos3d
    nCol= columns.nodes.getNearestNode(beamLastNodePos)
    nColPos= nCol.getInitialPos3d
    dist= nColPos.distPos3d(beamLastNodePos)
    if(dist<2.0*gap):
        fulcrumNode= modelSpace.setFulcrumBetweenNodes(nCol.tag,beamLastNode.tag)
        modelSpace.constraints.newEqualDOF(fulcrumNode.tag,beamLastNode.tag,xc.ID(gluedDOFs)) #torsion
    
# Simple support precast planks on walls
# for node in slabs.nodes:
#     if nodeOnEdge(node):
#         print 'here node: ', node.tag
#         modelSpace.fixNode('000_FFF',node.tag)

# AAAAAAAAAAAAAAA        
#East
stBusq=slabW1+slab12+slab23+slab34+slab45+slab5W
z=zHlwHigh
nod=sets.get_nodes_wire(setBusq=stBusq,lstPtsWire=[geom.Pos3d(0,0,z),geom.Pos3d(0,yFac[-1],z)])
for n in nod:
    modelSpace.fixNode('000_FFF',n.tag)
stBusq=slabs5_L
z=zHlwLow
nod=sets.get_nodes_wire(setBusq=stBusq,lstPtsWire=[geom.Pos3d(0,yFac[-1],z),geom.Pos3d(0,yList[-1],z)])
for n in nod:
    modelSpace.fixNode('000_FFF',n.tag)
#North
stBusq=slabBC+slabCD_H+slabDG+slabGF+slabFW
y=0
z=zHlwHigh
nod=sets.get_nodes_wire(setBusq=stBusq,lstPtsWire=[geom.Pos3d(0,y,z),geom.Pos3d(xFac[-1],y,z)])
for n in nod:
    modelSpace.fixNode('000_FFF',n.tag)
stBusq=slabsF_L
z=zHlwLow
nod=sets.get_nodes_wire(setBusq=stBusq,lstPtsWire=[geom.Pos3d(xFac[-1],y,z),geom.Pos3d(xList[-1],y,z)])
for n in nod:
    modelSpace.fixNode('000_FFF',n.tag)
#West
stBusq=slabsF_L+slabs5_L
x=xList[-1]
z=zHlwLow
nod=sets.get_nodes_wire(setBusq=stBusq,lstPtsWire=[geom.Pos3d(x,yCols[-1],z),geom.Pos3d(x,yList[-1],z)])
for n in nod:
    modelSpace.fixNode('000_FFF',n.tag)
#South
stBusq=slabCD_L
y=yList[-1]
z=zHlwLow
nod=sets.get_nodes_wire(setBusq=stBusq,lstPtsWire=[geom.Pos3d(xCols[2],y,z),geom.Pos3d(xCols[3],y,z)])
for n in nod:
    modelSpace.fixNode('000_FFF',n.tag)
#Ramp
stBusq=slabW1+slab12
x=xRamp[0]
z=zHlwHigh
nod=sets.get_nodes_wire(setBusq=stBusq,lstPtsWire=[geom.Pos3d(x,yList[0],z),geom.Pos3d(x,yCols[1],z)])
for n in nod:
    modelSpace.fixNode('000_FFF',n.tag)
#Cantilever
stBusq=slab5W
x=xFac[-1]
z=zHlwHigh
nod=sets.get_nodes_wire(setBusq=stBusq,lstPtsWire=[geom.Pos3d(x,yCols[4],z),geom.Pos3d(x,yFac[-1],z)])
for n in nod:
    modelSpace.fixNode('000_FFF',n.tag)
# AAAAAAAAAAAAAAA        


# Links beams to precast planks
gluedDOFs= [0,1,2]
distances=[zHlwHigh-zBeamHigh,zBeamHigh-zHlwLow]
stbeams=beam1+beam2+beam3+beam4+beam5
stslabs=slabBC+slabCD_L+slabCD_H+slabDG+slabGF+slabFW+slabsF_L
stbeams.fillDownwards()
stslabs.fillDownwards()
nod_stbeams=stbeams.nodes
nod_stslabs=stslabs.nodes
for n in nod_stbeams:
    n1=nod_stslabs.getNearestNode(n.getInitialPos3d)
    nPos= n.getInitialPos3d
    n1Pos= n1.getInitialPos3d
    dist2XY= (nPos.x-n1Pos.x)**2+(nPos.y-n1Pos.y)**2
    #print 'dist2XY: ', dist2XY
    if (dist2XY<0.1):
        modelSpace.constraints.newEqualDOF(n.tag,n1.tag,xc.ID(gluedDOFs))
#    modelSpace.fixNode('FF0_FFF',n1.tag)
    
stbeams=beamA+beamB
stslabs=slabW1+slab12+slab23+slab34+slab45+slab5W+slabs5_L
stbeams.fillDownwards()
stslabs.fillDownwards()
nod_stbeams=stbeams.nodes
nod_stslabs=stslabs.nodes
for n in nod_stbeams:
    n1=nod_stslabs.getNearestNode(n.getInitialPos3d)
    dist=n.getInitialPos3d.distPos3d(n1.getInitialPos3d)
    if dist in distances:
        modelSpace.constraints.newEqualDOF(n.tag,n1.tag,xc.ID(gluedDOFs))
#    modelSpace.fixNode('FF0_FFF',n1.tag)
    
stbeams=beamC
stslabs=slab5W+slabs5_L
stbeams.fillDownwards()
stslabs.fillDownwards()
nod_stbeams=stbeams.nodes
nod_stslabs=stslabs.nodes
for n in nod_stbeams:
    n1=nod_stslabs.getNearestNode(n.getInitialPos3d)
    dist=n.getInitialPos3d.distPos3d(n1.getInitialPos3d)
    if dist in distances:
        modelSpace.constraints.newEqualDOF(n.tag,n1.tag,xc.ID(gluedDOFs))
#    modelSpace.fixNode('FF0_FFF',n1.tag)

    
stbeams=beamD+beamG+beamF
stslabs=slab5W+slabs5_L
stbeams.fillDownwards()
stslabs.fillDownwards()
nod_stbeams=stbeams.nodes
nod_stslabs=stslabs.nodes
for n in nod_stbeams:
    n1=nod_stslabs.getNearestNode(n.getInitialPos3d)
    dist=n.getInitialPos3d.distPos3d(n1.getInitialPos3d)
    if dist in distances:
        modelSpace.constraints.newEqualDOF(n.tag,n1.tag,xc.ID(gluedDOFs))
#    modelSpace.fixNode('FF0_FFF',n1.tag)

# Support of slabCD_H on slabCD_L
i1=xList.index(xCols[1]+gap/2.)
i2=xList.index(xCols[2]-gap/2.)
j1=yList.index(yCols[0])
j2=yList.index(yFac[1])
k=zList.index(zHlwHigh)
st1=gridGeom.getSetSurfOneRegion(gm.IJKRange((i1,j1,k),(i2,j2,k)),'st1')
nod_st1=st1.nodes
nod_st2=slabCD_L.nodes
for n in nod_st1:
    n1=nod_st2.getNearestNode(n.getInitialPos3d)
    modelSpace.constraints.newEqualDOF(n.tag,n1.tag,xc.ID(gluedDOFs))

execfile(fullProjPath+'lines_loads.py')
#                       ***ACTIONS***

#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
#selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[beamXconcr_mesh,beamY_mesh,columnZconcr_mesh,deck_mesh,wall_mesh,foot_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))
selfWeightBeamCols=loads.InertialLoad(name='selfWeightBeamCols', lstMeshSets=[beams_mesh,columns_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

# Uniform loads applied on shell elements
#    name:       name identifying the load
#    xcSet:     set that contains the surfaces
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)

selfWeightSlabs= loads.UniformLoadOnSurfaces(name= 'selfWeightSlabs',xcSet=slabs,loadVector=xc.Vector([0,0,-Whollowdeck,0,0,0]),refSystem='Global')

LLunif_rooms_1floor=loads.UniformLoadOnSurfaces(name= 'LLunif_rooms_1floor',xcSet=slabs_H,loadVector=xc.Vector([0,0,-unifLLrooms,0,0,0]),refSystem='Global')
LLunif_terrace_1floor=loads.UniformLoadOnSurfaces(name= 'LLunif_rooms_1floor',xcSet=slabs_L,loadVector=xc.Vector([0,0,-unifLLterrace,0,0,0]),refSystem='Global')

SL_terrace_1floor=loads.UniformLoadOnSurfaces(name= 'SL_terrace_1floor',xcSet=slabs_L,loadVector=xc.Vector([0,0,-unifSL,0,0,0]),refSystem='Global')

#staggered patterns
from actions.utils import staggered_patterns as sptt
auxInd=list()
for x in xCols:
    auxInd.append(xList.index(x))
lIndX=[0]+auxInd+[xList.index(xFac[-1])]+[lastXpos]
auxInd=list()
for y in yCols:
    auxInd.append(yList.index(y))
lIndY=[0]+auxInd+[yList.index(yFac[-1])]+[lastYpos]
indZ=zList.index(zHlwHigh)
stag1_rg=sptt.staggeredPatternType1(lIndX,lIndY,indZ)
stag1Set=gridGeom.getSetSurfMultiRegion(stag1_rg,'stag1Set')
stag1Set.fillDownwards()
LLstag_rooms_1floor=loads.UniformLoadOnSurfaces(name= 'LLstag_rooms_1floor',xcSet=stag1Set,loadVector=xc.Vector([0,0,-unifLLrooms,0,0,0]),refSystem='Global')

indZ=zList.index(zHlwLow)
stag2_rg=sptt.staggeredPatternType1(lIndX,lIndY,indZ)
stag2Set=gridGeom.getSetSurfMultiRegion(stag2_rg,'stag2Set')
stag2Set.fillDownwards()
LLstag_terrace_1floor=loads.UniformLoadOnSurfaces(name= 'LLstag_terrace_1floor',xcSet=stag2Set,loadVector=xc.Vector([0,0,-unifLLterrace,0,0,0]),refSystem='Global')

# Uniform load applied to all the lines (not necessarily defined as lines
# for latter generation of beam elements, they can be lines belonging to 
# surfaces for example) found in the xcSet
# The uniform load is introduced as point loads in the nodes
#     name:   name identifying the load
#     xcSet:  set that contains the lines
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).

DL_lnL1=loads.UniformLoadOnLines(name='DL_lnL1',xcSet=lnL1,loadVector=xc.Vector([0,0,-1*D_lnL1,0,0,0]))
LL_lnL1=loads.UniformLoadOnLines(name='LL_lnL1',xcSet=lnL1,loadVector=xc.Vector([0,0,-1*L_lnL1,0,0,0]))
SL_lnL1=loads.UniformLoadOnLines(name='SL_lnL1',xcSet=lnL1,loadVector=xc.Vector([0,0,-1*S_lnL1,0,0,0]))

DL_lnL2=loads.UniformLoadOnLines(name='DL_lnL2',xcSet=lnL2,loadVector=xc.Vector([0,0,-1*D_lnL2,0,0,0]))
LL_lnL2=loads.UniformLoadOnLines(name='LL_lnL2',xcSet=lnL2,loadVector=xc.Vector([0,0,-1*L_lnL2,0,0,0]))
SL_lnL2=loads.UniformLoadOnLines(name='SL_lnL2',xcSet=lnL2,loadVector=xc.Vector([0,0,-1*S_lnL2,0,0,0]))

DL_lnL3=loads.UniformLoadOnLines(name='DL_lnL3',xcSet=lnL3,loadVector=xc.Vector([0,0,-1*D_lnL3,0,0,0]))
LL_lnL3=loads.UniformLoadOnLines(name='LL_lnL3',xcSet=lnL3,loadVector=xc.Vector([0,0,-1*L_lnL3,0,0,0]))
SL_lnL3=loads.UniformLoadOnLines(name='SL_lnL3',xcSet=lnL3,loadVector=xc.Vector([0,0,-1*S_lnL3,0,0,0]))

DL_lnL4=loads.UniformLoadOnLines(name='DL_lnL4',xcSet=lnL4,loadVector=xc.Vector([0,0,-1*D_lnL4,0,0,0]))
LL_lnL4=loads.UniformLoadOnLines(name='LL_lnL4',xcSet=lnL4,loadVector=xc.Vector([0,0,-1*L_lnL4,0,0,0]))
SL_lnL4=loads.UniformLoadOnLines(name='SL_lnL4',xcSet=lnL4,loadVector=xc.Vector([0,0,-1*S_lnL4,0,0,0]))

DL_lnL5=loads.UniformLoadOnLines(name='DL_lnL5',xcSet=lnL5,loadVector=xc.Vector([0,0,-1*D_lnL5,0,0,0]))
LL_lnL5=loads.UniformLoadOnLines(name='LL_lnL5',xcSet=lnL5,loadVector=xc.Vector([0,0,-1*L_lnL5,0,0,0]))
SL_lnL5=loads.UniformLoadOnLines(name='SL_lnL5',xcSet=lnL5,loadVector=xc.Vector([0,0,-1*S_lnL5,0,0,0]))

DL_lnL6=loads.UniformLoadOnLines(name='DL_lnL6',xcSet=lnL6,loadVector=xc.Vector([0,0,-1*D_lnL6,0,0,0]))
LL_lnL6=loads.UniformLoadOnLines(name='LL_lnL6',xcSet=lnL6,loadVector=xc.Vector([0,0,-1*L_lnL6,0,0,0]))
SL_lnL6=loads.UniformLoadOnLines(name='SL_lnL6',xcSet=lnL6,loadVector=xc.Vector([0,0,-1*S_lnL6,0,0,0]))

DL_lnL7=loads.UniformLoadOnLines(name='DL_lnL7',xcSet=lnL7,loadVector=xc.Vector([0,0,-1*D_lnL7,0,0,0]))
LL_lnL7=loads.UniformLoadOnLines(name='LL_lnL7',xcSet=lnL7,loadVector=xc.Vector([0,0,-1*L_lnL7,0,0,0]))
SL_lnL7=loads.UniformLoadOnLines(name='SL_lnL7',xcSet=lnL7,loadVector=xc.Vector([0,0,-1*S_lnL7,0,0,0]))

DL_lnL8=loads.UniformLoadOnLines(name='DL_lnL8',xcSet=lnL8,loadVector=xc.Vector([0,0,-1*D_lnL8,0,0,0]))

DL_lnL9=loads.UniformLoadOnLines(name='DL_lnL9',xcSet=lnL9,loadVector=xc.Vector([0,0,-1*D_lnL9,0,0,0]))
LL_lnL9=loads.UniformLoadOnLines(name='LL_lnL9',xcSet=lnL9,loadVector=xc.Vector([0,0,-1*L_lnL9,0,0,0]))
SL_lnL9=loads.UniformLoadOnLines(name='SL_lnL9',xcSet=lnL9,loadVector=xc.Vector([0,0,-1*S_lnL9,0,0,0]))

DL_lnL10=loads.UniformLoadOnLines(name='DL_lnL10',xcSet=lnL10,loadVector=xc.Vector([0,0,-1*D_lnL10,0,0,0]))
LL_lnL10=loads.UniformLoadOnLines(name='LL_lnL10',xcSet=lnL10,loadVector=xc.Vector([0,0,-1*L_lnL10,0,0,0]))
SL_lnL10=loads.UniformLoadOnLines(name='SL_lnL10',xcSet=lnL10,loadVector=xc.Vector([0,0,-1*S_lnL10,0,0,0]))

DL_lnL11=loads.UniformLoadOnLines(name='DL_lnL11',xcSet=lnL11,loadVector=xc.Vector([0,0,-1*D_lnL11,0,0,0]))

DL_lnL12=loads.UniformLoadOnLines(name='DL_lnL12',xcSet=lnL12,loadVector=xc.Vector([0,0,-1*D_lnL12,0,0,0]))
LL_lnL12=loads.UniformLoadOnLines(name='LL_lnL12',xcSet=lnL12,loadVector=xc.Vector([0,0,-1*L_lnL12,0,0,0]))
SL_lnL12=loads.UniformLoadOnLines(name='SL_lnL12',xcSet=lnL12,loadVector=xc.Vector([0,0,-1*S_lnL12,0,0,0]))

DL_lnL13=loads.UniformLoadOnLines(name='DL_lnL13',xcSet=lnL13,loadVector=xc.Vector([0,0,-1*D_lnL13,0,0,0]))
LL_lnL13=loads.UniformLoadOnLines(name='LL_lnL13',xcSet=lnL13,loadVector=xc.Vector([0,0,-1*L_lnL13,0,0,0]))
SL_lnL13=loads.UniformLoadOnLines(name='SL_lnL13',xcSet=lnL13,loadVector=xc.Vector([0,0,-1*S_lnL13,0,0,0]))

#Wind W-E
WL_WE_lnL1W=loads.UniformLoadOnLines(name='WL_WE_lnL1W',xcSet=lnL1W,loadVector=xc.Vector([0,0,WWE_lnL1W,0,0,0]))
WL_WE_lnL2W=loads.UniformLoadOnLines(name='WL_WE_lnL2W',xcSet=lnL2W,loadVector=xc.Vector([0,0,WWE_lnL2W,0,0,0]))
WL_WE_lnL3W=loads.UniformLoadOnLines(name='WL_WE_lnL3W',xcSet=lnL3W,loadVector=xc.Vector([0,0,WWE_lnL3W,0,0,0]))
WL_WE_lnL4W=loads.UniformLoadOnLines(name='WL_WE_lnL4W',xcSet=lnL4W,loadVector=xc.Vector([0,0,WWE_lnL4W,0,0,0]))
WL_WE_lnL5W=loads.UniformLoadOnLines(name='WL_WE_lnL5W',xcSet=lnL5W,loadVector=xc.Vector([0,0,WWE_lnL5W,0,0,0]))

#Wind N-S
WL_NS_lnL1W=loads.UniformLoadOnLines(name='WL_NS_lnL1W',xcSet=lnL1W,loadVector=xc.Vector([0,0,WNS_lnL1W,0,0,0]))
WL_NS_lnL6W=loads.UniformLoadOnLines(name='WL_NS_lnL6W',xcSet=lnL6W,loadVector=xc.Vector([0,0,WNS_lnL6W,0,0,0]))
WL_NS_lnL7W=loads.UniformLoadOnLines(name='WL_NS_lnL7W',xcSet=lnL7W,loadVector=xc.Vector([0,0,WNS_lnL7W,0,0,0]))



#    ***LOAD CASES***

#Dead load
DeadL=lcases.LoadCase(preprocessor=prep,name="DeadL")
DeadL.create()
DeadL.addLstLoads([DL_lnL1,DL_lnL2,DL_lnL3,DL_lnL4,DL_lnL5,DL_lnL6,DL_lnL7,DL_lnL8,DL_lnL9,DL_lnL10,DL_lnL11,DL_lnL12,DL_lnL13,selfWeightSlabs,selfWeightBeamCols])
#DeadL.addLstLoads([selfWeightBeamCols])
#live load (uniform on rooms)
LiveL_ru=lcases.LoadCase(preprocessor=prep,name="LiveL_ru")
LiveL_ru.create()
LiveL_ru.addLstLoads([LL_lnL1,LL_lnL2,LL_lnL3,LL_lnL4,LL_lnL5,LL_lnL6,LL_lnL7,LL_lnL9,LL_lnL10,LL_lnL12,LL_lnL13,LLunif_rooms_1floor])

#live load (staggered pattern on rooms)
LiveL_rs=lcases.LoadCase(preprocessor=prep,name="LiveL_rs")
LiveL_rs.create()
LiveL_rs.addLstLoads([LL_lnL1,LL_lnL2,LL_lnL3,LL_lnL4,LL_lnL5,LL_lnL6,LL_lnL7,LL_lnL9,LL_lnL10,LL_lnL12,LL_lnL13,LLstag_rooms_1floor])

#live load (uniform on patios)
LiveL_pu=lcases.LoadCase(preprocessor=prep,name="LiveL_pu")
LiveL_pu.create()
LiveL_pu.addLstLoads([LLunif_terrace_1floor])

#live load (staggered pattern on patios)
LiveL_ps=lcases.LoadCase(preprocessor=prep,name="LiveL_ps")
LiveL_ps.create()
LiveL_ps.addLstLoads([LLstag_terrace_1floor])

SnowL=lcases.LoadCase(preprocessor=prep,name="SnowL")
SnowL.create()
SnowL.addLstLoads([SL_lnL1,SL_lnL2,SL_lnL3,SL_lnL4,SL_lnL5,SL_lnL6,SL_lnL7,SL_lnL9,SL_lnL10,SL_lnL12,SL_lnL13,SL_terrace_1floor])

Wind_WE=lcases.LoadCase(preprocessor=prep,name="Wind_WE")
Wind_WE.create()
Wind_WE.addLstLoads([WL_WE_lnL1W,WL_WE_lnL2W,WL_WE_lnL3W,WL_WE_lnL4W,WL_WE_lnL5W])

Wind_NS=lcases.LoadCase(preprocessor=prep,name="Wind_NS")
Wind_NS.create()
Wind_NS.addLstLoads([WL_NS_lnL1W,WL_NS_lnL6W,WL_NS_lnL7W])

overallSet=colA+colB+colC+colD+colG+colF+beamA+beamB+beam1+beam2H+beam2L+beam3H+beam3L+beam4H+beam4L+beam5H+beam5L+slabW1+slab12+slab23+slab34+slab45+slab5W+slabBC+slabCD_H+slabCD_L+slabDG+slabGF+slabFW+slabsF_L+slabs5_L

'''
preprocessor.getDomain.getMesh.getNumFreeNodes()
for n in slabs.nodes:
    print n.getInitialPos3d.z
'''
slabs.fillDownwards()
slabs.description='Precast planks'
columns.fillDownwards()
columns.description='Columns'
beams.fillDownwards()
beams.description='Beams'
slabs_H.fillDownwards()
slabs_L.fillDownwards()

column_sets=[colA,colB,colC,colD,colG,colF]
for st in column_sets:
    st.fillDownwards()

beams_sets=[beamA,beamB,beamC,beamD,beamG,beamF,beam1,beam2,beam3,beam4,beam5]
for st in beams_sets:
    st.fillDownwards()
slabs_sets=[slabW1,slab12,slab23,slab34,slab45,slab5W,slabBC,slabCD_H,slabCD_L,slabDG,slabGF,slabFW,slabCD_L,slabsF_L,slabs5_L]
for st in slabs_sets:
    st.fillDownwards()


#execfile(fullProjPath+'print_links_slabs_beams.py')
