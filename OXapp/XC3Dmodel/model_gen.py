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
home= '/home/ana/projects/XCmodels/OXapp/'

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

#Displacements of the grid points in a range
#syntax: movePointsRange(ijkRange,vDisp)
#        ijkRange: range for the search
#        vDisp: xc vector displacement
# for i in range(1,len(xList)):
#     r= gm.IJKRange((i,0,lastZpos),(i,lastYpos,lastZpos))
#     gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,-trSlope*xList[i]]))


#Slope (in X direction, Y direction or both) the grid points in a range
#syntax: slopePointsRange(ijkRange,slopeX,xZeroSlope,slopeY,yZeroSlope)
#     ijkRange: range for the search.
#     slopeX: slope in X direction, expressed as deltaZ/deltaX 
#                       (defaults to 0 = no slope applied)
#     xZeroSlope: coordinate X of the "rotation axis".
#     slopeY: slope in Y direction, expressed as deltaZ/deltaY)
#                       (defaults to 0 = no slope applied)
#     yZeroSlope: coordinate Y of the "rotation axis".

#Scale in X with origin xOrig (fixed axis: X=xOrig) to the points in a range
#Only X coordinate of points is modified in the following way:
#       x_scaled=xOrig+scale*(x_inic-xOrig)
#syntax: scaleCoorXPointsRange(ijkRange,xOrig,scale)
#     ijkRange: range for the search.
#     xOrig: origin X to apply scale (point in axis X=xOrig)
#            are not affected by the transformation 
#     scale: scale to apply to X coordinate

#Scale in Y with origin yOrig (fixed axis: Y=yOrig) to the points in a range
#Only Y coordinate of points is modified in the following way:
#       y_scaled=yOrig+scale*(y_inic-yOrig)
#syntax: scaleCoorYPointsRange(ijkRange,yOrig,scale)
#     ijkRange: range for the search.
#     yOrig: origin Y to apply scale (point in axis Y=yOrig)
#            are not affected by the transformation 
#     scale: scale to apply to Y coordinate

#Scale in Z with origin zOrig (fixed axis: Z=zOrig) to the points in a range
#Only Z coordinate of points is modified in the following way:
#       z_scaled=zOrig+scale*(z_inic-zOrig)
#syntax: scaleCoorZPointsRange(ijkRange,zOrig,scale)
#     ijkRange: range for the search.
#     zOrig: origin Z to apply scale (point in axis Z=zOrig)
#            are not affected by the transformation 
#     scale: scale to apply to Z coordinate

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
j1=yList.index(yCols[4]-gap/2.)
j2=yList.index(yFac[-1])
k=zList.index(zHlwHigh)
slab45_rg.append(gm.IJKRange((0,j1,k),(xList.index(xCols[1]-gap/2.),j2,k)))

slabBC_rg=[]
i1=xList.index(xStair2Elev[0])
i2=xList.index(xCols[2]-gap/2.)
k=zList.index(zHlwHigh)
slabBC_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yCols[0]),k)))
i1=xList.index(xCols[1]+gap/2.)
i2=xList.index(xCols[2]-gap/2.)
k=zList.index(zHlwHigh)
slabBC_rg.append(gm.IJKRange((i1,yList.index(yCols[0]),k),(i2,yList.index(yFac[2]),k)))

slabCD_H_rg=[]
i1=xList.index(xCols[2]+gap/2.0)
i2=xList.index(xCols[3]-gap/2.)
k=zList.index(zHlwHigh)
slabCD_H_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yCols[-1]),k)))
slabCD_L_rg=[]
k=zList.index(zHlwLow)
slabCD_L_rg.append(gm.IJKRange((i1,yList.index(yCols[-1]),k),(i2,lastYpos,k)))

slabDG_rg=[]
i1=xList.index(xCols[3]+gap/2.)
i2=xList.index(xCols[4]-gap/2.)
k=zList.index(zHlwHigh)
slabDG_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yFac[2]),k)))

slabGF_rg=[]
i1=xList.index(xCols[4]+gap/2.)
i2=xList.index(xCols[-1]-gap/2.)
k=zList.index(zHlwHigh)
slabGF_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yFac[2]),k)))

slabFW_rg=[]
i1=xList.index(xCols[-1]+gap/2.)
i2=xList.index(xFac[3])
k=zList.index(zHlwHigh)
slabFW_rg.append(gm.IJKRange((i1,0,k),(i2,yList.index(yFac[2]),k)))

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
beams=beamA+beamB+beamC+beamD+beamG+beamF+beam1+beam2H+beam2L+beam3H+beam3L+beam4H+beam4L+beam5H+beam5L
beams.fillDownwards()
beams.description='Beams'
slabs_H=slabW1+slab12+slab23+slab34+slab45+slab5W+slabBC+slabCD_H+slabDG+slabGF+slabFW
slabs_H.fillDownwards()
slabs_H.description='Precast planks, top level'
slabs_L=slabCD_L+slabsF_L+slabs5_L
slabs_L.fillDownwards()
slabs_L.description='Precast planks, down level'
slabs=slabs_H+slabs_L




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
beams_sets=[beamA,beamB,beamC+beamD+beamG+beamF+beam1,beam2,beam3,beam4,beam5]
for st in beams_sets:
    st.fillDownwards()
slabs_sets=[slabW1,slab12,slab23,slab34,slab45,slab5W,slabBC,slabCD_H,slabDG,slabGF,slabFW,slabCD_L,slabsF_L,slabs5_L]

'''
#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
foot_wink=sprbc.ElasticFoundation(wModulus=20e7,cRoz=0.2)
foot_wink.generateSprings(xcSet=foot)
'''

# Springs (defined by Kx,Ky,Kz) to apply on nodes, points, 3Dpos, ...
# Default values for Kx, Ky, Kz are 0, which means that no spring is
# created in the corresponding direction
# spring_col=sprbc.SpringBC(name='spring_col',modelSpace=modelSpace,Kx=10e3,Ky=50e3,Kz=30e3)
# a=spring_col.applyOnNodesIn3Dpos(lst3DPos=[geom.Pos3d(0,LbeamY,0)])

#fixed DOF (ux:'0FF_FFF', uy:'F0F_FFF', uz:'FF0_FFF',
#           rx:'FFF_0FF', ry:'FFF_F0F', rz:'FFF_FF0')
# Base columns
for x in xCols:
    for y in yCols:
        n=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(x,y,0))
        modelSpace.fixNode('000_000',n.tag)
# Simple support beams on walls
z=zBeamHigh

x=xCols[0]
y=0
n=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(x,y,z))
modelSpace.fixNode('000_FFF',n.tag)

x=xList[-1]
for y in yCols:
    n=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(x,y,z))
    modelSpace.fixNode('000_FFF',n.tag)

y=yList[-1]
for x in xCols:
    n=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(x,y,z))
    modelSpace.fixNode('000_FFF',n.tag)

#Links between beams and columns
y=yCols[0]
z=zCol
for x in xCols[2:6]:
    for y in yCols[0:5]:
        nCol=columns.getNodes.getNearestNode(geom.Pos3d(x,y,z))
        nBeam1=beams.getNodes.getNearestNode(geom.Pos3d(x-gap/2.0,y,z))
        nBeam2=beams.getNodes.getNearestNode(geom.Pos3d(x+gap/2.0,y,z))
        modelSpace.setFulcrumBetweenNodes(nCol.tag,nBeam1.tag)
        modelSpace.setFulcrumBetweenNodes(nCol.tag,nBeam2.tag)
        
for x in xCols[2:6]:
    for y in yCols[4:5]:
        nCol=columns.getNodes.getNearestNode(geom.Pos3d(x,y,z))
        nBeam1=beams.getNodes.getNearestNode(geom.Pos3d(x,y+gap/2.0,z))
        modelSpace.setFulcrumBetweenNodes(nCol.tag,nBeam1.tag)

for x in xCols[1:2]:
    for y in yCols[0:5]:
        nCol=columns.getNodes.getNearestNode(geom.Pos3d(x,y,z))
        nBeam1=beams.getNodes.getNearestNode(geom.Pos3d(x-gap/2.0,y,z))
        modelSpace.setFulcrumBetweenNodes(nCol.tag,nBeam1.tag)

for x in xCols[1:2]:
    for y in yCols[1:2]:
        nCol=columns.getNodes.getNearestNode(geom.Pos3d(x,y,z))
        nBeam1=beams.getNodes.getNearestNode(geom.Pos3d(x,y+gap/2.0,z))
        modelSpace.setFulcrumBetweenNodes(nCol.tag,nBeam1.tag)
        
for x in xCols[1:2]:
    for y in yCols[2:5]:
        nCol=columns.getNodes.getNearestNode(geom.Pos3d(x,y,z))
        nBeam1=beams.getNodes.getNearestNode(geom.Pos3d(x,y-gap/2.0,z))
        nBeam2=beams.getNodes.getNearestNode(geom.Pos3d(x,y+gap/2.0,z))
        modelSpace.setFulcrumBetweenNodes(nCol.tag,nBeam1.tag)
        modelSpace.setFulcrumBetweenNodes(nCol.tag,nBeam2.tag)
        
for x in xCols[0:1]:
    for y in yCols[0:5]:
        nCol=columns.getNodes.getNearestNode(geom.Pos3d(x,y,z))
        nBeam1=beams.getNodes.getNearestNode(geom.Pos3d(x,y-gap/2.0,z))
        nBeam2=beams.getNodes.getNearestNode(geom.Pos3d(x,y+gap/2.0,z))
        modelSpace.setFulcrumBetweenNodes(nCol.tag,nBeam1.tag)
        modelSpace.setFulcrumBetweenNodes(nCol.tag,nBeam2.tag)

# Simple support precast planks on walls
#wallWest=sets.get_nodes_wire(setBusq=beams, lstPtsWire, tol=0.01)
# Links beam1 to precast planks


'''



#                       ***ACTIONS***

#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
#selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[beamXconcr_mesh,beamY_mesh,columnZconcr_mesh,deck_mesh,wall_mesh,foot_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[beamXconcr_mesh,beamY_mesh,columnZconcr_mesh,decklv1_mesh,decklv2_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

# Point load acting on one or several nodes
#     name:       name identifying the load
#     lstNod:     list of nodes  on which the load is applied
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).

nodPLoad=sets.get_lstNod_from_lst3DPos(preprocessor=prep,lst3DPos=[geom.Pos3d(0,yList[lastYpos]/2.0,zList[lastZpos]),geom.Pos3d(xList[lastXpos],yList[lastYpos]/2.0,zList[lastZpos])])
QpuntBeams=loads.NodalLoad(name='QpuntBeams',lstNod=nodPLoad,loadVector=xc.Vector([0,0,-Qbeam,0,0,0]))

# Uniform loads applied on shell elements
#    name:       name identifying the load
#    xcSet:     set that contains the surfaces
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)

unifLoadDeck1= loads.UniformLoadOnSurfaces(name= 'unifLoadDeck1',xcSet=decklv1,loadVector=xc.Vector([0,0,-qdeck1,0,0,0]),refSystem='Global')
unifLoadDeck2= loads.UniformLoadOnSurfaces(name= 'unifLoadDeck2',xcSet=decklv2,loadVector=xc.Vector([0,0,-qdeck2,0,0,0]),refSystem='Global')

# Earth pressure applied to shell or beam elements
#     Attributes:
#     name:       name identifying the load
#     xcSet:      set that contains the elements to be loaded
#     soilData: instance of the class EarthPressureModel, with 
#               the following attributes:
#                 zGround: global Z coordinate of ground level
#                 zBottomSoils: list of global Z coordinates of the bottom level
#                   for each soil (from top to bottom)
#                 KSoils: list of pressure coefficients for each soil (from top 
#                   to bottom)
#                 gammaSoils: list of weight density for each soil (from top to
#                   bottom)
#                 zWater: global Z coordinate of groundwater level 
#                   (if zGroundwater<minimum z of model => there is no groundwater)
#                 gammaWater: weight density of water
#                 qUnif: uniform load over the backfill surface (defaults to 0)
#     vDir: unit xc vector defining pressures direction

soil01=ep.EarthPressureModel( zGround=zList[lastZpos]-3, zBottomSoils=[-10],KSoils=[KearthPress],gammaSoils=[densSoil*grav], zWater=0, gammaWater=densWater*grav)
earthPressLoadWall= loads.EarthPressLoad(name= 'earthPressLoadWall', xcSet=wall,soilData=soil01, vDir=xc.Vector([0,1,0]))

earthPressLoadColumn= loads.EarthPressLoad(name= 'earthPressLoadColumn', xcSet=columnZconcr,soilData=soil01, vDir=xc.Vector([0,1,0]))

soil02=ep.EarthPressureModel(zGround=zList[lastZpos],zBottomSoils=[-10],KSoils=[0.001],  gammaSoils=[densSoil*grav], zWater=0.05, gammaWater=densWater*grav)
stripL01=ep.StripLoadOnBackfill(qLoad=2e5, zLoad=zList[lastZpos],distWall=1.5, stripWidth=1.2)
earthPColumnStrL= loads.EarthPressLoad(name= 'earthPColumnStrL', xcSet=columnZconcr,soilData=None, vDir=xc.Vector([0,1,0]))
earthPColumnStrL.stripLoads=[stripL01]

lineL01=ep.LineVerticalLoadOnBackfill(qLoad=1e5, zLoad=zList[lastZpos],distWall=1.0)
earthPColumnLinL= loads.EarthPressLoad(name= 'earthPColumnLinL', xcSet=columnZconcr,soilData=None, vDir=xc.Vector([0,1,0]))
earthPColumnLinL.lineLoads=[lineL01]

hrzL01=ep.HorizontalLoadOnBackfill(soilIntFi=30, qLoad=2e5, zLoad=zList[lastZpos],distWall=1,widthLoadArea=0.5,lengthLoadArea=1.5,horDistrAngle=45)
earthPColumnHrzL=loads.EarthPressLoad(name= 'earthPColumnHrzL', xcSet=columnZconcr,soilData=None, vDir=xc.Vector([0,1,0]))
earthPColumnHrzL.horzLoads=[hrzL01]

#Uniform load on beams
# syntax: UniformLoadOnBeams(name, xcSet, loadVector,refSystem)
#    name:       name identifying the load
#    xcSet:      set that contains the lines
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)
unifLoadBeamsY=loads.UniformLoadOnBeams(name='unifLoadBeamsY', xcSet=beamY, loadVector=xc.Vector([0,0,-qunifBeam,0,0,0]),refSystem='Global')

# Strain gradient on shell elements
#     name:  name identifying the load
#     xcSet: set that contains the surfaces
#     nabla: strain gradient in the thickness of the elements:
#            nabla=espilon/thickness    

#strGrad=loads.StrainLoadOnShells(name='strGrad', xcSet=deck,epsilon=0.001)

# Uniform load applied to all the lines (not necessarily defined as lines
# for latter generation of beam elements, they can be lines belonging to 
# surfaces for example) found in the xcSet
# The uniform load is introduced as point loads in the nodes
#     name:   name identifying the load
#     xcSet:  set that contains the lines
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).

unifLoadLinDeck2=loads.UniformLoadOnLines(name='unifLoadLinDeck2',xcSet=decklv2,loadVector=xc.Vector([0,qLinDeck2,0,0,0,0]))

# Point load distributed over the shell elements in xcSet whose 
# centroids are inside the prism defined by the 2D polygon prismBase
# and one global axis.
# syntax: PointLoadOverShellElems(name, xcSet, loadVector,prismBase,prismAxis,refSystem):
#    name: name identifying the load
#    xcSet: set that contains the shell elements
#    loadVector: xc vector with the six components of the point load:
#                   xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    prismBase: 2D polygon that defines the n-sided base of the prism.
#                   The vertices of the polygon are defined in global 
#                   coordinates in the following way:
#                      - for X-axis-prism: (y,z)
#                      - for Y-axis-prism: (x,z)
#                      - for Z-axis-prism: (x,y)
#    prismAxis: axis of the prism (can be equal to 'X', 'Y', 'Z')
#                   (defaults to 'Z')
#    refSystem:  reference system in which loadVector is defined:
#                   'Local': element local coordinate system
#                   'Global': global coordinate system (defaults to 'Global')

prBase=gut.rect2DPolygon(xCent=LbeamX/2.,yCent=LbeamY/2.,Lx=0.5,Ly=1.0)
wheelDeck1=loads.PointLoadOverShellElems(name='wheelDeck1', xcSet=decklv1, loadVector=xc.Vector([0,0,-Qwheel]),prismBase=prBase,prismAxis='Z',refSystem='Global')

# ---------------------------------------------------------------

# Point loads defined in the object lModel, distributed over the shell 
# elements under the wheels affected by them.

# syntax: VehicleDistrLoad(name,xcSet,loadModel, xCentr,yCentr,hDistr,slopeDistr)
#      name: name identifying the load
#      xcSet: set that contains the shell elements
#      lModel: instance of the class LoadModel with the definition of
#               vehicle of the load model.
#      xCent: global coord. X where to place the centroid of the vehicle
#      yCent: global coord. Y where  to place the centroid of the vehicle
#      hDistr: height considered to distribute each point load with
#               slope slopeDistr 
#      slopeDistr: slope (H/V) through hDistr to distribute the load of 
#               a wheel

from actions.roadway_trafic import standard_load_models as slm
from actions.roadway_trafic import load_model_base as lmb
vehicleDeck1=lmb.VehicleDistrLoad(name='vehicleDeck1',xcSet=decklv1,loadModel=slm.IAP_carril_virt3_fren, xCentr=LbeamX/2,yCentr=LbeamY/2.,hDistr=0.25,slopeDistr=1.0)


#    ***LOAD CASES***

GselfWeight=lcases.LoadCase(preprocessor=prep,name="GselfWeight",loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])

Qdecks=lcases.LoadCase(preprocessor=prep,name="Qdecks")
Qdecks.create()
Qdecks.addLstLoads([unifLoadDeck1,unifLoadDeck2])

QearthPressWall=lcases.LoadCase(preprocessor=prep,name="QearthPressWall",loadPType="default",timeSType="constant_ts")
QearthPressWall.create()
QearthPressWall.addLstLoads([earthPressLoadWall])

QearthPressCols=lcases.LoadCase(preprocessor=prep,name="QearthPressCols",loadPType="default",timeSType="constant_ts")
QearthPressCols.create()
QearthPressCols.addLstLoads([earthPressLoadColumn])
#eval('1.0*earthPressLoadColumn')  #add this weighted load to the curret load case

QearthPColsStrL=lcases.LoadCase(preprocessor=prep,name="QearthPColsStrL",loadPType="default",timeSType="constant_ts")
QearthPColsStrL.create()
QearthPColsStrL.addLstLoads([earthPColumnStrL])

QearthPColsLinL=lcases.LoadCase(preprocessor=prep,name="QearthPColsLinL",loadPType="default",timeSType="constant_ts")
QearthPColsLinL.create()    
QearthPColsLinL.addLstLoads([earthPColumnLinL])

QearthPColsHrzL=lcases.LoadCase(preprocessor=prep,name="QearthPColsHrzL",loadPType="default",timeSType="constant_ts")
QearthPColsHrzL.create()
QearthPColsHrzL.addLstLoads([earthPColumnHrzL])

qunifBeams=lcases.LoadCase(preprocessor=prep,name="qunifBeams",loadPType="default",timeSType="constant_ts")
qunifBeams.create()
qunifBeams.addLstLoads([unifLoadBeamsY])

QpntBeams=lcases.LoadCase(preprocessor=prep,name="QpntBeams",loadPType="default",timeSType="constant_ts")
QpntBeams.create()
QpntBeams.addLstLoads([QpuntBeams])

qlinDeck=lcases.LoadCase(preprocessor=prep,name="qlinDeck",loadPType="default",timeSType="constant_ts")
qlinDeck.create()
qlinDeck.addLstLoads([unifLoadLinDeck2])

QwheelDeck1=lcases.LoadCase(preprocessor=prep,name="QwheelDeck1",loadPType="default",timeSType="constant_ts")
QwheelDeck1.create()
QwheelDeck1.addLstLoads([wheelDeck1])

QvehicleDeck1=lcases.LoadCase(preprocessor=prep,name="QvehicleDeck1",loadPType="default",timeSType="constant_ts")
QvehicleDeck1.create()
QvehicleDeck1.addLstLoads([vehicleDeck1])

LS1=lcases.LoadCase(preprocessor=prep,name="LS1",loadPType="default",timeSType="constant_ts")
LS1.create()
LS1.addLstLoads([selfWeight,unifLoadDeck1,unifLoadDeck2,earthPressLoadWall,earthPressLoadColumn,earthPColumnStrL,earthPColumnLinL])

LS2=lcases.LoadCase(preprocessor=prep,name="LS2",loadPType="default",timeSType="constant_ts")
LS2.create()
LS2.addLstLoads([selfWeight,earthPColumnHrzL,unifLoadBeamsY,QpuntBeams,unifLoadLinDeck2,wheelDeck1])
    
#    ***LIMIT STATE COMBINATIONS***
combContainer= cc.CombContainer()  #Container of load combinations

# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
    # name:        name to identify the combination
    # rare:        combination for a rare design situation
    # freq:        combination for a frequent design situation
    # qp:          combination for a quasi-permanent design situation
    # earthquake:  combination for a seismic design situation
#Characteristic combinations.
combContainer.SLS.rare.add('ELSR01', '1.0*LS2')
#Frequent combinations.
combContainer.SLS.freq.add('ELSF01', '1.0*LS1')
#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP01', '1.0*LS2')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELU01', '1.2*LS1')
combContainer.ULS.perm.add('ELU02', '1.0*LS2')

#Fatigue.
# Combinations' names must be:
#        - ELUF0: unloaded structure (permanent loads)
#        - ELUF1: fatigue load in position 1.
combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*Qdecks')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*QearthPressWall')

decks=prep.getSets.defSet('decks')  #only this way we can recover this
                         #set by calling it by its name with:
                         #prep.getSets.getSet('decks') 
decks=decklv1+decklv2
#decks.name='decks'
decks.description='Decks'
decks.color=cfg.colors['purple01']
allShells=decklv1+decklv2+foot+wall
allShells.description='Shell elements'
allBeams=beamXconcr+beamXsteel+beamY+columnZconcr+columnZsteel
allBeams.description='Beams+columns'
overallSet=beamXconcr+beamXsteel+beamY+columnZconcr+columnZsteel+wall+foot+decklv1+decklv2
overallSet.description='overall set'
overallSet.color=cfg.colors['purple01']
beamX=beamXconcr+beamXsteel
beamX.description='beams X'
columnZ=columnZconcr+columnZsteel
columnZ.description='columns'

#sets for displaying some results
pBase=gut.rect2DPolygon(xCent=LbeamX/2.,yCent=0,Lx=LbeamX,Ly=LbeamY-1.0)

allShellsRes=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=allShells,prismBase=pBase,prismAxis='Z',setName='allShellsRes')
''' 
overallSet=colA+colB+colC+colD+colG+colF+beamA+beamB+beam1+beam2H+beam2L+beam3H+beam3L+beam4H+beam4L+beam5H+beam5L+slabW1+slab12+slab23+slab34+slab45+slab5W+slabBC+slabCD_H+slabCD_L+slabDG+slabGF+slabFW+slabsF_L+slabs5_L




