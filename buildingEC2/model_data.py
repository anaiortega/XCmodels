# -*- coding: utf-8 -*-

# worked example from the technical report: «Eurocode 2: background and applications. Design of concrete buildings»
#It corresponds to the case study in chapter 8 of the guidebook 2 'Design of bridges',
#by Pietro Croce et al.
#concrete:C50/60 
#reinforcing steel B450C

import os
import xc_base
import geom
import xc
from model.grid_based_oldStyle_deprecated import ijkGrid
from model.grid_based_oldStyle_deprecated import GridModel as gm
from actions import combinations as cc
from postprocess import limit_state_data as lsd
from materials import typical_materials 

from materials.sections import structural_steel
from actions.utils import staggered_patterns as stg_pat


from materials.ec3 import EC3_materials

import EarthPressure as ep

import math

#      ****Auxiliary data [Données auxiliaires] ******
#Geometry auxiliary data
HeightStoreys=[3,3,4,3,3,3,3,3]     
SpanX=[6,6,6,6,6]
SpanY=[7.125,7.125,7.125]
thickWallsBasement=0.60
thickShearWallStaircase=0.30
dimXShearWallStaircase=3.6
dimYShearWallStaircase=1.8
thickFacadeColumns=0.25
lengthFacadeColumns=0.70
thickFacadeShearWalls=0.30
lengthFacadeShearWalls=4.00
lengthSquareColumns=0.5
thickSlabs=0.21
dimXHole=3.6
dimYHole=3.75
distBetweenHoles=1.8
#Materials auxiliary data
fck=35                    #valeur caractéristique de la résistance (N/mm2)
fcm=fck+8                 #valeur moyenne de la résistance du béton dans de bonnes conditions de fabrication a l'âge de 28 jours
Econcr=8500*fcm**(1/3)*1e3 #module d'élasticité du béton (kN/m2). Art. 39.6
cpoisC=0.2                #Coefficient de Poisson du béton
densC=2.5                 #densité du béton armé (t/m3)
cdtC=1e-5                 #Coefficient de dilatation thermique du béton
grav=9.81                 #Gravity acceleration (m/s2) [Accélération de la pesanteur (m/s2)]

#Elements' mean size [Grandeur moyen des éléments]
eSize=0.5

#Charges auxiliary data
deadLoadInterior=3.0                  #(kN/m2)
deadLoadFacade=8.0                    #(kN/m)
snow=1.70                             #(kN/m2)
wind10m=0.77                          #(kN/m2) wind below 10 m
wind19m=1.04                          #(kN/m2) wind at 19 m (linear rising between 10 and 19 m)
serviceLoad1Dwelling=2.0              #(kN/m2) level 1-6
serviceLoad1Office=4.0                #(kN/m2) level 0 stairs office
serviceLoad2parking=2.5               #(kN/m2) level -1 -2, parking and external area

# *** GEOMETRY  [GÉOMÉTRIE]***
EC2building= xc.FEProblem()
model= gm.GridModel(EC2building)
prep=model.getPreprocessor()

# coordinates in global X,Y,Z axes for the grid generation
# X coordinates
xList=[0]
xAxis=0
for i in range (0,2):
    xAxis=xAxis+SpanX[i]
    xList.append(xAxis-lengthFacadeColumns/2)
    xList.append(xAxis)
    xList.append(xAxis+lengthFacadeColumns/2)

dimAux=(SpanX[2]-dimXHole)/2
xList.append(xAxis+dimAux)
xList.append(xAxis+dimAux+dimXHole)

for i in range (2,4):
    xAxis=xAxis+SpanX[i]
    xList.append(xAxis-lengthFacadeColumns/2)
    xList.append(xAxis)
    xList.append(xAxis+lengthFacadeColumns/2)

xList.append(xAxis+SpanX[4])
#Coord. Y
yAxis=0
yList=[yAxis]
yAxis+=SpanY[0]
yList.append(yAxis)
yList.append(yAxis+lengthFacadeColumns)
yAxis+=SpanY[1]
yList.append(yAxis-distBetweenHoles-dimYShearWallStaircase)
yList.append(yAxis-lengthFacadeShearWalls/2)
yList.append(yAxis-distBetweenHoles)
yList.append(yAxis)
yList.append(yAxis+lengthFacadeShearWalls/2)
yList.append(yAxis+dimYHole)
yAxis+=SpanY[2]
yList.append(yAxis-lengthFacadeColumns)
yList.append(yAxis)
#Elevations
elev=0
zList=[elev]
for i in range(0,len(HeightStoreys)):
    elev+=HeightStoreys[i]
    zList.append(elev)

#auxiliary data
lastXind=len(xList)-1
lastYind=len(yList)-1
lastZind=len(zList)-1

# grid of X,Y,Z axes coordinates
rejXYZ= model.setGrid(xList,yList,zList)

#Displacements of the grid points in a range
#syntax: moveRange(ijkGrid.IJKRange([minIindex,minJindex,minKindex],[maxIindex,maxJindex,maxKindex],[dispX,dispY,dispZ])
# for i in range(1,len(xList)):
#   r= ijkGrid.IJKRange([i,0,lastZind],[i,lastYpos,lastZind])
#   mr= ijkGrid.moveRange(r,[0.0,0.0,trSlope*xList[i]])
#   rejXYZ.rangesToMove.append(mr)



# *** MATERIALS *** 

concrForAll=typical_materials.MaterialData(name='concrForAll',E=Econcr,nu=cpoisC,rho=densC)
# S275JR= EC3_materials.S275JR
# S275JRbeam=typical_materials.MaterialData(name='S275JRbeam',E=S275JR.E,nu=S275JR.nu,rho=7850)

#geometric sections
  # Isotropic elastic section-material appropiate for plate and shell analysis
  # Attributes:
  #   name:         name identifying the section
  #   E:            Young’s modulus of the material
  #   nu:           Poisson’s ratio
  #   rho:          mass density
  #   thickness:    overall depth of the section

wallsBasement_mat= gm.DeckMaterialData(name= 'wallsBasement', thickness= thickWallsBasement, material=concrForAll)
facadeShearWall_mat= gm.DeckMaterialData(name= 'facadeShearWall', thickness= thickFacadeShearWalls, material=concrForAll)
shearWallStaircase_mat= gm.DeckMaterialData(name= 'shearWallStaircase', thickness= thickShearWallStaircase, material=concrForAll)
slabs_mat= gm.DeckMaterialData(name= 'slabs', thickness= thickSlabs, material=concrForAll)


  # Elastic section appropiate for 3D beam analysis, including shear deformations. 
#Rectangular sections:
  # Attributes:
  #   name:         name identifying the section
  #   b:            cross-section width (parallel to local z axis)
  #   h:            cross-section height (parallel to local y axis)
  #   E:            Young’s modulus of the material
  #   nu:           Poisson’s ratio
from materials.sections import section_properties as sp
sqrColumns_sect=sp.RectangularSection(name='sqrColumns_sect',b=lengthSquareColumns,h=lengthSquareColumns)  #section definition
sqrColumns_mat=gm.BeamMaterialData(name='sqrColumns',section=sqrColumns_sect,material=concrForAll) #material definition (rho: mass density)

#Circular sections:
  # Attributes:
  #  name:      name identifying the section
  #  r:         radius
  #  E:         Young’s modulus of the material
  #  nu:        Poisson’s ratio
# from materials.sections import section_properties
# sect_beamR0_5=section_properties.CircularSection(name='sect_beamR0_5',r=0.5)  #section definition
# beamR0_5=gm.BeamMaterialData(name='beamR0_5',section=sect_beamR0_5,material=concrDeckBeam) #material definition (rho: mass density)

#I sections:
  #  name:         name identifying the section
  #  wdTopFlange:  width of the top flange (parallel to local z-axis)
  #  thTopFlange:  thickness of the top flange (parallel to local y-axis)
  #  thWeb:        thickness of the web (parallel to local z-axis)
  #  hgWeb:        height of the web (parallel to local y-axis)
  #  wdBotFlange:  width of the bottom flange (parallel to local z-axis)
  #  thBotFlange:  thickness of the bottom flange (parallel to local y-axis)
  #  E:            Young’s modulus of the material
  #  nu:           Poisson’s ratio

# from materials.sections import section_properties
# sect_Ibeam=section_properties.ISection(name='sect_Ibeam',wdTopFlange=0.9,thTopFlange=0.3,thWeb=0.25,hgWeb=1.80,wdBotFlange=0.95,thBotFlange=0.5)  #section definition
# Ibeam=gm.BeamMaterialData(name='Ibeam',section=sect_Ibeam,material=concrDeckBeam)     #material definition (rho: mass density)

#Generic sections
  # name:         name identifying the section
  # area:         cross-sectional area
  # Iy:           second moment of area about the local y-axis
  # Iz:           second moment of area about the local z-axis
  # Jtors:        torsional moment of inertia of the section
  # Wy:           section modulus with respect to local y-axis
  # Wz:           section modulus with respect to local z-axis
# from materials.sections import section_properties
# sect_generic=section_properties.GenericSection(name='sect_generic',area=areaBeam,I_y=IhorizBeam,I_z=IvertBeam,Jtors=Jbeam,W_y=WhorizBeam,W_z=WvertBeam,alphY=alphYBeam,alphZ=alphZBeam)  #section definition
# prestBeam=gm.BeamMaterialData(name='prestBeam',section=sect_generic,material=concrDeckBeam)     #material definition (rho: mass density)


#steel shape
  # steel:    steel object (e.g. S275JR)
  # table:    module containing a dictionary with mechanical characteristics
  #                of a series of shapes 
  #                (e.g. materials.sections.structural_shapes.arcelor_metric_shapes)
  # name:     name identifying the section in the table

# from materials.sections.structural_shapes import arcelor_metric_shapes
# from materials.ec3 import EC3_materials
# S275JR= EC3_materials.S275JR
# sect_HE400B= stP.SteelShape(S275JR,"HE_400_B",arcelor_metric_shapes.HE)
# HE400B=gm.BeamMaterialData(name='HE_400_B',section=sect_HE400B,material=S275JRbeam)


#  Dictionary of materials
matElMembPlat= model.setMaterials([wallsBasement_mat,facadeShearWall_mat,shearWallStaircase_mat,slabs_mat,sqrColumns_mat])

#Mesh parameters and sets
    # Types of surfaces to be discretized from the defined 
    # material, type of element and size of the elements.
    # Parameters:
    #   name:     name to identify the type of surface
    #   material: name of the material that makes up the surface
    #   elemType: element type to be used in the discretization
    #   elemSize: mean size of the elements
    #   ranges:   lists of grid ranges to delimit the surfaces of 
    #             the type in question
wallBasYmin= model.newMaterialSurface('wallBasYmin', material=wallsBasement_mat, elemType='ShellMITC4',elemSize= eSize)
wallBasYmin.ranges= [ ijkGrid.IJKRange([0,0,0],[lastXind,0,2])]

wallBasYmax= model.newMaterialSurface('wallBasYmax', material=wallsBasement_mat, elemType='ShellMITC4',elemSize= eSize)
wallBasYmax.ranges= [ ijkGrid.IJKRange([0,lastYind,0],[lastXind,lastYind,2])]

wallBasXmin= model.newMaterialSurface('wallBasXmin', material=wallsBasement_mat, elemType='ShellMITC4',elemSize= eSize)
wallBasXmin.ranges= [ ijkGrid.IJKRange([0,0,0],[0,lastYind,2])]

wallBasXmax= model.newMaterialSurface('wallBasXmax', material=wallsBasement_mat, elemType='ShellMITC4',elemSize= eSize)
wallBasXmax.ranges= [ ijkGrid.IJKRange([lastXind,0,0],[lastXind,lastYind,2])]

columnFacYmin= model.newMaterialSurface('columnFacYmin', material=facadeShearWall_mat, elemType='ShellMITC4',elemSize= eSize)
columnFacYmin.ranges= [ ijkGrid.IJKRange([1,1,0],[3,1,lastZind]),ijkGrid.IJKRange([4,1,0],[6,1,lastZind]),ijkGrid.IJKRange([9,1,0],[11,1,lastZind]),ijkGrid.IJKRange([12,1,0],[14,1,lastZind])]

columnFacYmax= model.newMaterialSurface('columnFacYmax', material=facadeShearWall_mat, elemType='ShellMITC4',elemSize= eSize)
columnFacYmax.ranges= [ ijkGrid.IJKRange([1,lastYind,0],[3,lastYind,lastZind]),ijkGrid.IJKRange([4,lastYind,0],[6,lastYind,lastZind]),ijkGrid.IJKRange([9,lastYind,0],[11,lastYind,lastZind]),ijkGrid.IJKRange([12,lastYind,0],[14,lastYind,lastZind])]

columnFacXmin= model.newMaterialSurface('columnFacXmin', material=facadeShearWall_mat, elemType='ShellMITC4',elemSize= eSize)
columnFacXmin.ranges= [ ijkGrid.IJKRange([0,1,2],[0,2,lastZind]),ijkGrid.IJKRange([0,5,2],[0,7,lastZind]),ijkGrid.IJKRange([0,9,2],[0,10,lastZind])]

columnFacXmax= model.newMaterialSurface('columnFacXmax', material=facadeShearWall_mat, elemType='ShellMITC4',elemSize= eSize)
columnFacXmax.ranges= [ ijkGrid.IJKRange([lastXind,1,2],[lastXind,2,lastZind]),ijkGrid.IJKRange([lastXind,5,2],[lastXind,7,lastZind]),ijkGrid.IJKRange([lastXind,9,2],[lastXind,10,lastZind])]

ShearWallStaircaseXmin= model.newMaterialSurface('ShearWallStaircaseXmin', material=shearWallStaircase_mat, elemType='ShellMITC4',elemSize= eSize)
ShearWallStaircaseXmin.ranges= [ ijkGrid.IJKRange([7,3,0],[7,4,lastZind])]

ShearWallStaircaseXmax= model.newMaterialSurface('ShearWallStaircaseXmax', material=shearWallStaircase_mat, elemType='ShellMITC4',elemSize= eSize)
ShearWallStaircaseXmax.ranges= [ ijkGrid.IJKRange([8,3,0],[8,4,lastZind])]

ShearWallStaircaseZ= model.newMaterialSurface('ShearWallStaircaseZ', material=shearWallStaircase_mat, elemType='ShellMITC4',elemSize= eSize)
ShearWallStaircaseZ.ranges= [ ijkGrid.IJKRange([7,3,0],[8,3,lastZind])]

SlabLevelBas1= model.newMaterialSurface('SlabLevelBas1', material=slabs_mat, elemType='ShellMITC4',elemSize= eSize)
SlabLevelBas1.ranges= [ ijkGrid.IJKRange([0,0,1],[7,lastYind,1]),ijkGrid.IJKRange([7,0,1],[8,3,1]),ijkGrid.IJKRange([7,4,1],[8,6,1]),ijkGrid.IJKRange([7,8,1],[8,lastYind,1]),ijkGrid.IJKRange([8,0,1],[lastXind,lastYind,1])]

SlabLevel0= model.newMaterialSurface('SlabLevel0', material=slabs_mat, elemType='ShellMITC4',elemSize= eSize)
SlabLevel0.ranges= [ ijkGrid.IJKRange([0,0,2],[7,lastYind,2]),ijkGrid.IJKRange([7,0,2],[8,3,2]),ijkGrid.IJKRange([7,4,2],[8,6,2]),ijkGrid.IJKRange([7,8,2],[8,lastYind,2]),ijkGrid.IJKRange([8,0,2],[lastXind,lastYind,2])]

SlabLevel1= model.newMaterialSurface('SlabLevel1', material=slabs_mat, elemType='ShellMITC4',elemSize= eSize)
SlabLevel1.ranges= [ ijkGrid.IJKRange([0,1,3],[7,lastYind,3]),ijkGrid.IJKRange([7,1,3],[8,3,3]),ijkGrid.IJKRange([7,4,3],[8,6,3]),ijkGrid.IJKRange([7,8,3],[8,lastYind,3]),ijkGrid.IJKRange([8,1,3],[lastXind,lastYind,3])]

SlabLevel2= model.newMaterialSurface('SlabLevel2', material=slabs_mat, elemType='ShellMITC4',elemSize= eSize)
SlabLevel2.ranges= [ ijkGrid.IJKRange([0,1,4],[7,lastYind,4]),ijkGrid.IJKRange([7,1,4],[8,3,4]),ijkGrid.IJKRange([7,4,4],[8,6,4]),ijkGrid.IJKRange([7,8,4],[8,lastYind,4]),ijkGrid.IJKRange([8,1,4],[lastXind,lastYind,4])]

SlabLevel3= model.newMaterialSurface('SlabLevel3', material=slabs_mat, elemType='ShellMITC4',elemSize= eSize)
SlabLevel3.ranges= [ ijkGrid.IJKRange([0,1,5],[7,lastYind,5]),ijkGrid.IJKRange([7,1,5],[8,3,5]),ijkGrid.IJKRange([7,4,5],[8,6,5]),ijkGrid.IJKRange([7,8,5],[8,lastYind,5]),ijkGrid.IJKRange([8,1,5],[lastXind,lastYind,5])]

SlabLevel4= model.newMaterialSurface('SlabLevel4', material=slabs_mat, elemType='ShellMITC4',elemSize= eSize)
SlabLevel4.ranges= [ ijkGrid.IJKRange([0,1,6],[7,lastYind,6]),ijkGrid.IJKRange([7,1,6],[8,3,6]),ijkGrid.IJKRange([7,4,6],[8,6,6]),ijkGrid.IJKRange([7,8,6],[8,lastYind,6]),ijkGrid.IJKRange([8,1,6],[lastXind,lastYind,6])]

SlabLevel5= model.newMaterialSurface('SlabLevel5', material=slabs_mat, elemType='ShellMITC4',elemSize= eSize)
SlabLevel5.ranges= [ ijkGrid.IJKRange([0,1,7],[7,lastYind,7]),ijkGrid.IJKRange([7,1,7],[8,3,7]),ijkGrid.IJKRange([7,4,7],[8,6,7]),ijkGrid.IJKRange([7,8,7],[8,lastYind,7]),ijkGrid.IJKRange([8,1,7],[lastXind,lastYind,7])]

SlabLevel6= model.newMaterialSurface('SlabLevel6', material=slabs_mat, elemType='ShellMITC4',elemSize= eSize)
SlabLevel6.ranges= [ ijkGrid.IJKRange([0,1,8],[7,lastYind,8]),ijkGrid.IJKRange([7,1,8],[8,3,8]),ijkGrid.IJKRange([7,4,8],[8,6,8]),ijkGrid.IJKRange([7,8,8],[8,lastYind,8]),ijkGrid.IJKRange([8,1,8],[lastXind,lastYind,8])]

objWallBas=[wallBasYmin,wallBasYmax,wallBasXmin,wallBasXmax]
objColumnFac=[columnFacYmin,columnFacYmax,columnFacXmin,columnFacXmax]
objShearWallStaircase=[ShearWallStaircaseXmin,ShearWallStaircaseXmax,ShearWallStaircaseZ]
objSlabs=[SlabLevelBas1,SlabLevel0,SlabLevel1,SlabLevel2,SlabLevel3,SlabLevel4,SlabLevel5,SlabLevel6]
objSupTotal=objWallBas+objColumnFac+objShearWallStaircase+objSlabs

#Dictionary of material-surfaces
conjSup= model.setMaterialSurfacesMap(objSupTotal)


    # Types of lines to be discretized from the defined 
    # material, type of element and size of the elements.
    # Parameters:
    #   name:     name to identify the material-line
    #   material: name of the material that makes up the line
    #   elemType: element type to be used in the discretization
    #   elemSize: mean size of the elements
    #   vDirLAxZ: direction vector for the element local axis Z 
    #             defined as xc.Vector([x,y,z]). This is the direction in which
    #             the Z local axis of the reinforced concrete sections will be
    #             oriented (i.e. in the case of rectangular sections this Z 
    #             local axis of the RC section is parallel to the dimension
    #             defined as width of the rectangle)
    #   ranges:   lists of grid ranges to delimit the lines of 
    #             the type in question
columnB2= model.newMaterialLine('columnB2', material= sqrColumns_mat, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([1,0,0]))
columnB2.ranges= [ ijkGrid.IJKRange([2,6,0],[2,6,lastZind])]

columnB3= model.newMaterialLine('columnB3', material= sqrColumns_mat, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([1,0,0]))
columnB3.ranges= [ ijkGrid.IJKRange([5,6,0],[5,6,lastZind])]

columnB4= model.newMaterialLine('columnB4', material= sqrColumns_mat, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([1,0,0]))
columnB4.ranges= [ ijkGrid.IJKRange([10,6,0],[10,6,lastZind])]

columnB5= model.newMaterialLine('columnB5', material= sqrColumns_mat, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([1,0,0]))
columnB5.ranges= [ ijkGrid.IJKRange([13,6,0],[13,6,lastZind])]

#Dictionary of material-lines
objColumns=[columnB2,columnB3,columnB4,columnB5]
conjLines= model.setMaterialLinesMap(objColumns)


    # Regions resting on springs (Winkler elastic foundation)
    #   name:     name to identify the region
    #   wModulus: Winkler modulus of the foundation (springs in Z direction)
    #   cRoz:     fraction of the Winkler modulus to apply for friction in
    #             the contact plane (springs in X, Y directions)
    #   ranges:   lists of grid ranges to delimit the regions of 
    #             the type of foundation in question
# foundationElasticSupports= model.newElasticFoundationRanges('apElT1', wModulus= winkMod,cRoz=coefHorVerSprings)
# foundationElasticSupports.ranges.extend(foundExtSlab.ranges)
# foundationElasticSupports.ranges.extend(foundIntSlab.ranges)

#Dictionary with the list of Winkler elastic foundations given as a parameter
# elasticSupports= model.setElasticFoundationRangesMap([foundationElasticSupports])

#Boundary conditions
    #Constrains in the nodes belonging to the lines of a range-region 
    #    name:        name to identify the boundary condition
    #    constraints: constraint conditions, expressed as [uX, uY, uZ,rotX, rotY, rotZ], where:
    #                 - uX, uY, uZ: translations in the X, Y and Z directions; 
    #                 - rotX, rotY, rotZ: rotations about the X, Y and Z axis
    #                 - 'free': means no constraint

# foundFix=model.newConstrainedRanges(name='foundFix',constraints=[0,0,0,0,0,0])
# foundFix.ranges.extend([ijkGrid.IJKRange([0,0,0],[lastXind,lastYind,0])])
# foundFix=model.newConstrainedRanges(name='foundFix',constraints=[0,0,0,0,0,0])
# foundFix.ranges.extend([ijkGrid.IJKRange([1,1,0],[lastXind-1,lastYind-1,0])])


# #Dictionary with the list of constraints given as a parameter
# boundConstr=model.setConstrainedRangesMap([foundFix])
 

model.generateMesh()

#Boundary conditions
#Constrains in the nodes belonging to a region defined by coordinates
#constrCond:   list of constraint conditions, expressed as 
             #   [uX, uY, uZ,rotX, rotY, rotZ], where:
             # - uX, uY, uZ: translations in the X, Y and Z directions; 
             # - rotX, rotY, rotZ: rotations about the X, Y and Z axis
             # - 'free': means no constraint values 
from model import model_inquiry
lstNodes=model_inquiry.getNodesInCoordinateRegion(xmin=xList[0],xmax=xList[lastXind],ymin=yList[0],ymax=yList[lastYind],zmin=zList[0],zmax=zList[0],xcSet=prep.getSets.getSet('total'))  #list of nodes in the region

from model import predefined_spaces
modelSpace= predefined_spaces.getStructuralMechanics3DSpace(prep)
modelSpace.LstNodes6DOFConstr(lstNodes=lstNodes,constrCond=[0,0,0,0,0,0])

# const=prep.getBoundaryCondHandler
# print const.getNumSPs

# ***** ACTIONS *****

  # Inertial loads applied to the shell elements belonging to a list of 
  # surfaces 
  # Attributes:
  #   name:     name identifying the load
  #   surfaces: list of names of material-surfaces sets, e.g. [deck, wall, ..]
  #   accel:    list with the three components of the acceleration vector [ax,ay,az]
#Self weight.
selfWeight= gm.InertialLoadOnMaterialSurfaces(name= 'selfWeight',surfaces=objSupTotal,accel= [0.0,0.0,-grav])


    # Uniform loads applied to shell elements
    # name:       name identifying the load
    # lstGridRg:   lists of grid ranges to delimit the surfaces to
    #             be loaded
    # loadVector: list with the three components of the load vector


deadLoadInt=gm.PressureLoadOnSurfaces(name= 'deadLoadInt',lstGridRg=gm.getIJKRangeListFromSurfaces(objSlabs),loadVector=[0,0,-deadLoadInterior])
snowRoof=gm.PressureLoadOnSurfaces(name= 'snowRoof',lstGridRg=gm.getIJKRangeListFromSurfaces([SlabLevel6]),loadVector=[0,0,-snow])
snowAx1_2=gm.PressureLoadOnSurfaces(name= 'snowAx1_2',lstGridRg=model.getSurfacesFromListOfRanges([[[0,0,2],[2,1,2]]]),loadVector=[0,0,-snow])
snowAx2_3=gm.PressureLoadOnSurfaces(name= 'snowAx2_3',lstGridRg=model.getSurfacesFromListOfRanges([[[2,0,2],[5,1,2]]]),loadVector=[0,0,-snow])
snowAx3_4=gm.PressureLoadOnSurfaces(name= 'snowAx3_4',lstGridRg=model.getSurfacesFromListOfRanges([[[5,0,2],[10,1,2]]]),loadVector=[0,0,-snow])
snowAx4_5=gm.PressureLoadOnSurfaces(name= 'snowAx4_5',lstGridRg=model.getSurfacesFromListOfRanges([[[10,0,2],[13,1,2]]]),loadVector=[0,0,-snow])
snowAx5_6=gm.PressureLoadOnSurfaces(name= 'snowAx5_6',lstGridRg=model.getSurfacesFromListOfRanges([[[13,0,2],[15,1,2]]]),loadVector=[0,0,-snow])
#auxiliary data Axis indexes
xindAx1=0
xindAx2=2
xindAx3=5
xindAx4=10
xindAx5=13
xindAx6=15
yindAxD=0
yindAxC=1
yindAxB=6 
yindAxA=10
#Wind
#repartXextr=
windX10extr=wind10m*(yindAxA-yindAxB)/(yindAxA-(yindAxA-1))

windX10=gm.PressureLoadOnSurfaces(name= 'windX10',lstGridRg=model.getSurfacesFromListOfRanges([[[0,1,2],[0,2,5]],[[0,5,2],[0,7,5]],[[0,9,2],[0,10,5]]]),loadVector=[wind10m,0,0])
windX19=gm.PressureLoadOnSurfaces(name= 'windX19',lstGridRg=model.getSurfacesFromListOfRanges([[[0,1,5],[0,2,lastZind]],[[0,5,5],[0,7,lastZind]],[[0,9,5],[0,10,lastZind]]]),loadVector=[wind19m,0,0])
windY10=gm.PressureLoadOnSurfaces(name= 'windY10',lstGridRg=model.getSurfacesFromListOfRanges([[[1,1,2],[3,1,5]],[[4,1,2],[6,1,5]],[[9,1,2],[11,1,5]],[[12,1,2],[14,1,5]]]),loadVector=[0,wind10m,0])
windY19=gm.PressureLoadOnSurfaces(name= 'windY19',lstGridRg=model.getSurfacesFromListOfRanges([[[1,1,5],[3,1,lastZind]],[[4,1,5],[6,1,lastZind]],[[9,1,5],[11,1,lastZind]],[[12,1,5],[14,1,lastZind]]]),loadVector=[0,wind19m,0])

#Service load 1 on the roof 
indAux=stg_pat.staggeredPatternType1([xindAx1,xindAx3,xindAx4,xindAx5],[yindAxC,yindAxA],8)
#arrLoadType1(8)
serviceLC1326=gm.PressureLoadOnSurfaces(name= 'serviceLC1326',lstGridRg=gm.IJKRangeList('sc1236',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Dwelling])
serviceLC1336=gm.PressureLoadOnSurfaces(name= 'serviceLC1336',lstGridRg=gm.getIJKRangeListFromSurfaces([SlabLevel6]),loadVector=[0,0,-serviceLoad1Dwelling])
indAux=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxB,yindAxA],8)
#arrLoadType2(8)
serviceLC1356=gm.PressureLoadOnSurfaces(name= 'serviceLC1356',lstGridRg=gm.IJKRangeList('serviceLC1356',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Dwelling])
indAux=stg_pat.staggeredPatternType1([xindAx2,xindAx3,xindAx4,xindAx5],[yindAxC,yindAxA],8)
#arrLoadType3(8)
serviceLC1366=gm.PressureLoadOnSurfaces(name= 'serviceLC1366',lstGridRg=gm.IJKRangeList('serviceLC1366',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Dwelling])
#Service load 1 on levels 1 to 5
indAux=[]
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxB,yindAxA],4)
#indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxB,yindAxA],4)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxB,yindAxA],6)
indAux+=stg_pat.staggeredPatternType2([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxB,yindAxA],3)
indAux+=stg_pat.staggeredPatternType2([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxB,yindAxA],5)
indAux+=stg_pat.staggeredPatternType2([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxB,yindAxA],7)
serviceLC10001dw=gm.PressureLoadOnSurfaces(name= 'serviceLC10001dw',lstGridRg=gm.IJKRangeList('serviceLC10001dw',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Dwelling])
indAux=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxB,yindAxA],2)
serviceLC10001off=gm.PressureLoadOnSurfaces(name= 'serviceLC10001off',lstGridRg=gm.IJKRangeList('serviceLC10001off',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Office])
indAux=[]
indAux+=stg_pat.staggeredPatternType2([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxA],4)
indAux+=stg_pat.staggeredPatternType2([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxA],6)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxA],3)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxA],5)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxA],7)
serviceLC10011dw=gm.PressureLoadOnSurfaces(name= 'serviceLC10011dw',lstGridRg=gm.IJKRangeList('serviceLC10011dw',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Dwelling])
indAux=[]
indAux+=stg_pat.staggeredPatternType2([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxC,yindAxA],2)
serviceLC10011off=gm.PressureLoadOnSurfaces(name= 'serviceLC10011off',lstGridRg=gm.IJKRangeList('serviceLC10011off',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Office])
indAux=[]
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx3,xindAx4,xindAx5],[yindAxC,yindAxA],3)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx3,xindAx4,xindAx5],[yindAxC,yindAxA],4)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx3,xindAx4,xindAx5],[yindAxC,yindAxA],5)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx3,xindAx4,xindAx5],[yindAxC,yindAxA],6)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx3,xindAx4,xindAx5],[yindAxC,yindAxA],7)
serviceLC10021dw=gm.PressureLoadOnSurfaces(name= 'serviceLC10021dw',lstGridRg=gm.IJKRangeList('serviceLC10021dw',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Dwelling])
indAux=[]
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx3,xindAx4,xindAx5],[yindAxC,yindAxA],2)
serviceLC10021off=gm.PressureLoadOnSurfaces(name= 'serviceLC10021off',lstGridRg=gm.IJKRangeList('serviceLC10021off',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Office])
indAux=[]
for indLev in range(3,8):
    indAux.append([[0,1,indLev],[lastXind,lastYind,indLev]])

serviceLC10031dw=gm.PressureLoadOnSurfaces(name= 'serviceLC10031dw',lstGridRg=model.getSurfacesFromListOfRanges(indAux),loadVector=[0,0,-serviceLoad1Dwelling])
indAux=[]
indLev=2
indAux.append([[0,1,indLev],[lastXind,lastYind,indLev]])
#serviceLC10031off=gm.PressureLoadOnSurfaces(name= 'serviceLC10031off',lstGridRg=gm.IJKRangeList('',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad1Office])
serviceLC10031off=gm.PressureLoadOnSurfaces(name= 'serviceLC10031off',lstGridRg=model.getSurfacesFromListOfRanges(indAux),loadVector=[0,0,-serviceLoad1Office])
#Service loads in parking and external areas loads
indAux=[]
indAux+=stg_pat.staggeredPatternType1([xindAx2,xindAx3,xindAx4,xindAx5],[yindAxD,yindAxC],2)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxD,yindAxC,yindAxB,yindAxA],1)
serviceLC10101pk=gm.PressureLoadOnSurfaces(name= 'serviceLC10101pk',lstGridRg=gm.IJKRangeList('serviceLC10101pk',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad2parking])
indAux=[]
indAux+=stg_pat.staggeredPatternType1([xindAx2,xindAx3,xindAx4,xindAx5],[yindAxD,yindAxC],2)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx2,xindAx3,xindAx4,xindAx5,xindAx6],[yindAxD,yindAxA],1)
serviceLC10111pk=gm.PressureLoadOnSurfaces(name= 'serviceLC10111pk',lstGridRg=gm.IJKRangeList('serviceLC10111pk',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad2parking])
indAux=[]
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx3,xindAx4,xindAx5],[yindAxD,yindAxC],2)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx3,xindAx4,xindAx5],[yindAxD,yindAxA],1)
serviceLC10121pk=gm.PressureLoadOnSurfaces(name= 'serviceLC10121pk',lstGridRg=gm.IJKRangeList('serviceLC10121pk',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad2parking])
indAux=[]
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx6],[yindAxD,yindAxC],2)
indAux+=stg_pat.staggeredPatternType1([xindAx1,xindAx6],[yindAxD,yindAxA],1)
serviceLC10131pk=gm.PressureLoadOnSurfaces(name= 'serviceLC10131pk',lstGridRg=gm.IJKRangeList('sc10131',model.grid,ranges=indAux),loadVector=[0,0,-serviceLoad2parking])

  # Uniform load applied to all the lines found in the list of grid ranges
  # passed as parameter.'lnEndsCoo':
    
  # :ivar name:       name identifying the load
  # :ivar grid:       name of the grid-based model
  # :ivar lstGridRg:  lists of grid ranges to delimit the lines to be loaded
  # :ivar loadVector: xc.Vector with the six components of the load: xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).

prejAux=[]
for i in range(2,8):
    prejAux.append([ijkGrid.IJKRange([0,1,i],[lastXind,1,i]),ijkGrid.IJKRange([0,lastYind,i],[lastXind,lastYind,i]),ijkGrid.IJKRange([0,1,i],[0,5,i]),ijkGrid.IJKRange([0,7,i],[0,lastYind,i]),ijkGrid.IJKRange([lastXind,1,i],[lastXind,5,i]),ijkGrid.IJKRange([lastXind,7,i],[lastXind,lastYind,i])])

qFacSlab0=gm.UniformLoadOnLinesInRange(name= 'qFacSlab0',grid=model.grid,lstGridRg=prejAux[0],loadVector=xc.Vector([0,0,-4*deadLoadFacade,0,0,0]))
qFacSlab1=gm.UniformLoadOnLinesInRange(name= 'qFacSlab1',grid=model.grid,lstGridRg=prejAux[1],loadVector=xc.Vector([0,0,-3*deadLoadFacade,0,0,0]))
qFacSlab2=gm.UniformLoadOnLinesInRange(name= 'qFacSlab2',grid=model.grid,lstGridRg=prejAux[2],loadVector=xc.Vector([0,0,-3*deadLoadFacade,0,0,0]))
qFacSlab3=gm.UniformLoadOnLinesInRange(name= 'qFacSlab3',grid=model.grid,lstGridRg=prejAux[3],loadVector=xc.Vector([0,0,-3*deadLoadFacade,0,0,0]))
qFacSlab4=gm.UniformLoadOnLinesInRange(name= 'qFacSlab4',grid=model.grid,lstGridRg=prejAux[4],loadVector=xc.Vector([0,0,-3*deadLoadFacade,0,0,0]))
qFacSlab5=gm.UniformLoadOnLinesInRange(name= 'qFacSlab5',grid=model.grid,lstGridRg=prejAux[5],loadVector=xc.Vector([0,0,-3*deadLoadFacade,0,0,0]))

    # Load acting on one or several points
    # name:       name identifying the load
    # points:     list of points (list of geom.Pos3d(x,y,z)) where 
    #             the load must be applied.
    # loadVector: xc.Vector with the six components of the load: 
    #             xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#trafBrakingHwSit1=gm.LoadOnPoints(name='trafBrakingHwSit1',points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1HwSit1[0]]+yList[YposLane1HwSit1[1]])/2.0,zList[lastZind])],loadVector=xc.Vector([brakingQhw,0,0,0,0,0]))


    # Earth pressure applied to shell elements
    # Attributes:
    # name:        name identifying the load
    # lstGridRg:   lists of grid ranges to delimit the surfaces to
    #              be loaded
    # earthPressure: instance of the class EarthPressure, with 
    #               the following attributes:
    #               K:Coefficient of pressure
    #               zTerrain:global Z coordinate of ground level
    #               gammaSoil: weight density of soil 
    #               zWater: global Z coordinate of groundwater level 
    #                       (if zGroundwater<minimum z of model => there is no groundwater)
    #               gammaWater: weight density of water
    #               vDir: unit vector defining pressures direction

indAux=[ijkGrid.IJKRange([0,1,5],[0,2,lastZind]),ijkGrid.IJKRange([0,5,5],[0,7,lastZind]),ijkGrid.IJKRange([0,9,5],[0,10,lastZind]) ]
windX=gm.EarthPressureOnSurfaces(name= 'windX', lstGridRg= gm.IJKRangeList('windX',model.grid,ranges=indAux),earthPressure= ep.EarthPressure(K=1,zGround=zList[lastZind],gammaSoil=(wind19m-wind10m)/9,zWater=0,gammaWater=grav,vDir=[-1,0,0]))
indAux=[ ijkGrid.IJKRange([1,1,5],[3,1,lastZind]),ijkGrid.IJKRange([4,1,5],[6,1,lastZind]),ijkGrid.IJKRange([9,1,5],[11,1,lastZind]),ijkGrid.IJKRange([12,1,5],[14,1,lastZind]) ]
windY=gm.EarthPressureOnSurfaces(name= 'windY', lstGridRg=gm.IJKRangeList('windY',model.grid,ranges=indAux),earthPressure= ep.EarthPressure(K=1,zGround=zList[lastZind],gammaSoil=(wind19m-wind10m)/9,zWater=0,gammaWater=grav,vDir=[0,-1,0]))


#ACTIONS
  # Definition of the actions to be combined in design situations for 
  # performing a limit state analysis
  #   inercLoad:     list of inertial loads
  #   unifPressLoad: list of pressures on surfaces
  #   unifVectLoad:  list of uniform loads on shell elements
  #   unifLoadLinRng: list of uniform loads on the lines in a list of grid ranges
  #   pointLoad:     list of point loads
  #   earthPressLoad:list of earth pressure loads
  #   hydrThrustLoad:list of hydrostatic thrust on the walls that delimit a volume
  #   tempGrad:      list of temperature gradient loads
LC1_deadLoadBearingStructure = gm.LoadState('LC1_deadLoadBearingStructure',inercLoad=[selfWeight])

LC2_deadLoadInterior = gm.LoadState('LC2_deadLoadInterior',unifPressLoad= [deadLoadInt])

LC3_deadLoadFacade = gm.LoadState('LC3_deadLoadFacade',unifLoadLinRng=[qFacSlab0,qFacSlab1,qFacSlab2,qFacSlab3,qFacSlab4,qFacSlab5] )
LC51_windX = gm.LoadState('LC51_windX',unifPressLoad= [windX10,windX19],unifLoadLinRng=[],earthPressLoad=[windX])
LC101_windY = gm.LoadState('LC101_windY',unifPressLoad= [windY10,windY19],unifLoadLinRng=[],earthPressLoad=[windY])
LC201_snowRoof = gm.LoadState('LC201_snowRoof',unifPressLoad= [snowRoof])

LC202_snowAx1_2 = gm.LoadState('LC202_snowAx1_2',unifPressLoad= [snowAx1_2])

LC203_snowAx2_3 = gm.LoadState('LC203_snowAx2_3',unifPressLoad= [snowAx2_3])
LC204_snowAx3_4 = gm.LoadState('LC204_snowAx3_4',unifPressLoad= [snowAx3_4])
LC205_snowAx4_5 = gm.LoadState('LC205_snowAx4_5',unifPressLoad= [snowAx4_5])
LC206_snowAx5_6 = gm.LoadState('LC206_snowAx5_6',unifPressLoad= [snowAx5_6])
#Service load 1 on the roof 
LC1326_servRoof = gm.LoadState('LC1326_servRoof',unifPressLoad= [serviceLC1326])
LC1336_servRoof = gm.LoadState('LC1336_servRoof',unifPressLoad= [serviceLC1336])
LC1356_servRoof = gm.LoadState('LC1356_servRoof',unifPressLoad= [serviceLC1356])
LC1366_servRoof = gm.LoadState('LC1366_servRoof',unifPressLoad= [serviceLC1366])
#Service load 1 on levels 1 to 5
LC10001_serv1 = gm.LoadState('LC10001_serv1',unifPressLoad= [serviceLC10001dw,serviceLC10001off])
LC10011_serv1 = gm.LoadState('LC10011_serv1',unifPressLoad= [serviceLC10011dw,serviceLC10011off])
LC10021_serv1 = gm.LoadState('LC10021_serv1',unifPressLoad= [serviceLC10021dw,serviceLC10021off])
LC10031_serv1 = gm.LoadState('LC10031_serv1',unifPressLoad= [serviceLC10031dw,serviceLC10031off])
#Service loads in parking and external areas loads
LC10101_servParking = gm.LoadState('LC10101_servParking',unifPressLoad= [serviceLC10101pk])
LC10111_servParking = gm.LoadState('LC10111_servParking',unifPressLoad= [serviceLC10111pk])
LC10121_servParking = gm.LoadState('LC10121_servParking',unifPressLoad= [serviceLC10121pk])
LC10131_servParking = gm.LoadState('LC10131_servParking',unifPressLoad= [serviceLC10131pk])

#Dictionary of actions
loadStates= gm.LoadStateMap([LC1_deadLoadBearingStructure,LC2_deadLoadInterior,LC3_deadLoadFacade,LC51_windX,LC101_windY,LC201_snowRoof,LC202_snowAx1_2,LC203_snowAx2_3,LC204_snowAx3_4,LC205_snowAx4_5,LC206_snowAx5_6,LC1326_servRoof,LC1336_servRoof,LC1356_servRoof,LC1366_servRoof,LC10001_serv1,LC10011_serv1,LC10021_serv1,LC10031_serv1,LC10101_servParking,LC10111_servParking,LC10121_servParking,LC10131_servParking])

model.setLoadStates(loadStates)
model.generateLoads()


#LOAD COMBINATIONS
combContainer= cc.CombContainer()  #Container of load combinations
# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELUmaxMy', '1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterio+1.35*LC3_deadLoadFacader+1.5*LC101_windY+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5+0.75*LC206_snowAx5_6+1.05*LC1356_servRoof+1.05*LC10111_servParking')
combContainer.ULS.perm.add('ELUmaxMz', '1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10111_servParking+0.9*LC51_windX+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5+0.75*LC206_snowAx5_6+1.05*LC10011_serv1')
combContainer.ULS.perm.add('ELUmaxVy', '1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10111_servParking+0.9*LC51_windX+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5+0.75*LC206_snowAx5_6+1.05*LC10011_serv1')
combContainer.ULS.perm.add('ELUmaxVz', '1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC51_windX+1.05*LC10031_serv1+1.05*LC10101_servParking')
combContainer.ULS.perm.add('ELUmaxN','1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC51_windX+0.75*LC202_snowAx1_2+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5')
combContainer.ULS.perm.add('ELUminMy','1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC51_windX+0.75*LC201_snowRoof+1.05*LC1326_servRoof+1.05*LC10031_serv1+1.05*LC10101_servParking')
combContainer.ULS.perm.add('ELUminMz','1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10121_servParking+0.9*LC101_windY+0.75*LC201_snowRoof+0.75*LC202_snowAx1_2+1.05*LC1326_servRoof+1.5*LC10021_serv1')
combContainer.ULS.perm.add('ELUminVy','1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10121_servParking+0.75*LC201_snowRoof+0.75*LC202_snowAx1_2+1.05*LC1356_servRoof+1.05*LC10021_serv1')
combContainer.ULS.perm.add('ELUminVz','1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC101_windY+0.75*LC202_snowAx1_2+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5+0.75*LC206_snowAx5_6+1.05*LC10111_servParking')
combContainer.ULS.perm.add('ELUminN','1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10031_serv1+1.5*LC1366_servRoof+0.75*LC201_snowRoof+1.05*LC10121_servParking')


#Here we define sets of elements that we are to use in the displays and reports
#Instances of the object postprocess.utils_display.setToDisplay are created, which attributes are:
#   elSet:     the set of elements,
#   genDescr:  a general description for the set and
#   sectDescr: a list with the descriptions that apply to each of the sections that configures the element
#For a grid model it's also possible to use the function getSetForDisplay that also generates the the set from a list of parts

conjWallBas=['wallBasYmin','wallBasYmax','wallBasXmin','wallBasXmax']
wallBasSet=model.getSetForDisplay(setName='wallBasSet',parts=conjWallBas,setGenDescr='basement walls',setSectDescr=['rebars dir. 1','rebars dir. 2'])
conjColumnFac=['columnFacYmin','columnFacYmax','columnFacXmin','columnFacXmax']
columnFacSet=model.getSetForDisplay(setName='columnFacSet',parts=conjColumnFac,setGenDescr='facade columns',setSectDescr=['rebars dir. 1','rebars dir. 2'])
conjShearWallStaircase=['ShearWallStaircaseXmin','ShearWallStaircaseXmax','ShearWallStaircaseZ']
shearWallStaircaseSet=model.getSetForDisplay(setName='shearWallStaircaseSet',parts=conjShearWallStaircase,setGenDescr='shear walls staircase',setSectDescr=['rebars dir. 1','rebars dir. 2'])
conjSlabs=['SlabLevelBas1','SlabLevel0','SlabLevel1','SlabLevel2','SlabLevel3','SlabLevel4','SlabLevel5','SlabLevel6']
slabsSet=model.getSetForDisplay(setName='slabsSet',parts=conjSlabs,setGenDescr='slabs levels 0 to 6',setSectDescr=['rebars dir. 1','rebars dir. 2'])
conjColumns=['columnB2','columnB3','columnB4','columnB5']
columnsSet=model.getSetForDisplay(setName='columnsSet',parts=conjColumns,setGenDescr='inner columns',setSectDescr=['rebars dir. 1','rebars dir. 2'])
columnB2Set=model.getSetForDisplay(setName='columnB2Set',parts=['columnB2'],setGenDescr='column B2',setSectDescr=['rebars dir. 1','rebars dir. 2'])
conjNoWalls=conjColumnFac+conjShearWallStaircase+conjSlabs+conjColumns
noWallsSet=model.getSetForDisplay(setName='noWallsSet',parts=conjNoWalls,setGenDescr=' ',setSectDescr=['rebars dir. 1','rebars dir. 2'])
conjAll=conjWallBas+conjColumnFac+conjShearWallStaircase+conjSlabs+conjColumns
xcTotalSet=model.getSetForDisplay(setName='xcTotalSet',parts=conjAll,setGenDescr='overall set',setSectDescr=['rebars dir. 1','rebars dir. 2'])
conjShell=conjShearWallStaircase+conjSlabs
shellSet=model.getSetForDisplay(setName='shellSet',parts=conjShell,setGenDescr='shell elements',setSectDescr=['rebars dir. 1','rebars dir. 2'])

