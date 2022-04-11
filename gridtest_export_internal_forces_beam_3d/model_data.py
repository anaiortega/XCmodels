# -*- coding: utf-8 -*-

import os
import geom
import xc
import math
from model.grid_based_oldStyle_deprecated import ijkGrid
from model.grid_based_oldStyle_deprecated import GridModel as gm
from actions import combinations as cc
from postprocess import limit_state_data as lsd
from materials import typical_materials
from postprocess import utils_display

from materials.sia262 import SIA262_limit_state_checking

# ***Auxiliar data***
#Geometry 
hbeam=0.25
wbeam=0.5




#Materials
from materials.sia262 import SIA262_materials
concrete= SIA262_materials.c30_37
reinfSteel= SIA262_materials.SpecialII1956SIA161


#Actions 
FxLoc=10e3
MyLoc=1e3
FyLoc=1e3


eSize= 1.0     #length of elements

# *** GEOMETRY ***
FEcase= xc.FEProblem()
model= gm.GridModel(FEcase)
preprocessor= model.getPreprocessor()   


# coordinates in global X,Y,Z axes for the grid generation
xList=[0,1,2]
yList=[0]
zList=[0]



#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid of X,Y,Z axes coordinates
rejXYZ= model.setGrid(xList,yList,zList)

#Displacements of the grid points in a range
#syntax: moveRange(ijkGrid.IJKRange([minIindex,minJindex,minKindex],[maxIindex,maxJindex,maxKindex],[dispX,dispY,dispZ])
# for k in range(3,lastZpos+1):
#   r= ijkGrid.IJKRange([lastXpos,0,k],[lastXpos,lastYpos,k])
#   deltaXPto=-RGlass*(1-math.cos((k-2)*incrAngRad))
#   mr= ijkGrid.moveRange(r,[deltaXPto,0.0,0.0])
#   rejXYZ.rangesToMove.append(mr)


# *** MATERIALS *** 
concrete=typical_materials.MaterialData(name='concrete',E=concrete.Ecm(),nu=concrete.nuc,rho=2500)


  # Isotropic elastic section-material appropiate for plate and shell analysis
  # Attributes:
  #   name:         name identifying the section
  #   E:            Young’s modulus of the material
  #   nu:           Poisson’s ratio
  #   rho:          mass density
  #   thickness:    overall depth of the section

#matDeck= gm.DeckMaterialData(name= 'matDeck',thickness= deckTh,material=concrete)


  #Geometric sections
  #rectangular sections
from materials.sections import section_properties as rectSect

geomBeam=rectSect.RectangularSection(name='geomBeam',b=wbeam,h=hbeam)

# Elastic material-section appropiate for 3D beam analysis, including shear deformations.
  # Attributes:
  #   name:         name identifying the section
  #   section:      instance of a class that defines the geometric and mechanical characteristiscs
  #                 of a section (e.g: RectangularSection, CircularSection, ISection, ...)
  #   material:     instance of a class that defines the elastic modulus, shear modulus
  #                 and mass density of the material

matBeam= gm.BeamMaterialData(name= 'matBeam', section=geomBeam, material=concrete)

#  Dictionary of materials
matElMembPlat= model.setMaterials([matBeam])


    # Types of surfaces to be discretized from the defined 
    # material, type of element and size of the elements.
    # Parameters:
    #   name:     name to identify the type of surface
    #   material: name of the material that makes up the surface
    #   elemType: element type to be used in the discretization
    #   elemSize: mean size of the elements
    #   ranges:   lists of grid ranges to delimit the surfaces of 
    #             the type in question
# deck= model.newMaterialSurface('deck', material=matDeck, elemType='ShellMITC4',elemSize= eSize)
# deck.ranges= [ ijkGrid.IJKRange([0,0,1],[lastXpos,lastYpos,1]) ]

# allSurfList=[deck]

# #Dictionary of material-surfaces
# conjSup= model.setMaterialSurfacesMap(allSurfList)

    # Types of lines to be discretized from the defined 
    # material, type of element and size of the elements.
    # Parameters:
    #   name:     name to identify the type of line
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

beam= model.newMaterialLine(name='beam', material= matBeam, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([0,-1,0]))
beam.ranges= [ ijkGrid.IJKRange([0,0,0],[2,0,0])]

#Dictionary of material-lines
allLinList=[beam]
conjLines= model.setMaterialLinesMap(allLinList)


    # Regions resting on springs (Winkler elastic foundation)
    #   name:     name to identify the region
    #   wModulus: Winkler modulus of the foundation (springs in Z direction)
    #   cRoz:     fraction of the Winkler modulus to apply for friction in
    #             the contact plane (springs in X, Y directions)
    #   ranges:   lists of grid ranges to delimit the regions of 
    #             the type of foundation in question
# winkMod=20e7
# coefHorVerSprings=0.2
# foundationElasticSupports= model.newElasticFoundationRanges('apElT1', wModulus= winkMod,cRoz=coefHorVerSprings)
# foundationElasticSupports.ranges.extend(found.ranges)


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
# foundFix.ranges.extend([ijkGrid.IJKRange([0,0,0],[lastXpos,lastYpos,0])])


#Dictionary with the list of constraints given as a parameter
# fundConstr=model.setConstrainedRangesMap([foundFix])

#dicGeomEnt= model.generateMesh() 
model.generateMesh() 

#Boundary conditions
#Constrains in the nodes belonging to a region defined by coordinates
#constrCond:   list of constraint conditions, expressed as 
             #   [uX, uY, uZ,rotX, rotY, rotZ], where:
             # - uX, uY, uZ: translations in the X, Y and Z directions; 
             # - rotX, rotY, rotZ: rotations about the X, Y and Z axis
             # - 'free': means no constraint values 
from model import model_inquiry
lstNodes=model_inquiry.getNodesInCoordinateRegion(xmin=xList[0],xmax=xList[0],ymin=yList[0],ymax=yList[0],zmin=zList[0],zmax=zList[0],xcSet=preprocessor.getSets.getSet('total'))  #list of nodes in the region
from model import predefined_spaces
modelSpace= predefined_spaces.getStructuralMechanics3DSpace(preprocessor)
modelSpace.LstNodes6DOFConstr(lstNodes=lstNodes,constrCond=[0,0,0,0,0,0])


# ***** ACTIONS *****

  # Inertial loads applied to the shell elements belonging to a list of 
  # surfaces 
  # Attributes:
  #   name:     name identifying the load
  #   surfaces: list of names of material-surfaces sets, e.g. [deck, wall, ..]
  #   accel:    list with the three components of the acceleration vector [ax,ay,az]
#Self weight surfaces.
# grav=9.81 #Gravity acceleration (m/s2)
# selfWeight= gm.InertialLoadOnMaterialSurfaces(name= 'selfWeight',surfaces=allSurfList,accel= [0.0,0.0,-grav])

#Self weight line materials.
# grav=9.81 #Gravity acceleration (m/s2)
# selfWeight= gm.InertialLoadOnMaterialLines(name= 'selfWeight',matLines=allLinList,accel= [0.0,0.0,-grav])


# Uniform loads applied to shell elements
  # name:       name identifying the load
  # lstGridRg:   lists of grid ranges to delimit the surfaces to
  #             be loaded
  # loadVector: list with the three components of the load vector

# unifLoadDeck= gm.PressureLoadOnSurfaces(name= 'unifLoadDeck',lstGridRg=model.getSurfacesFromListOfRanges([[[0,0,1],[lastXpos,lastYpos,1]]]),loadVector= [0,0,-qdeck])

# Uniform loads applied to beam elements
  # name:       name identifying the load
  # lstGridRg:  lists of grid ranges to delimit the lines to
  #             be loaded
  # loadVector: load vector
  # refSystem:  reference system in which loadVector is defined:
  #             'Local': element local coordinate system
  #             'Global' (or any other value): global coordinate system 

# windUnifTC= gm.UniformLoadOnBeamsInRangeLines(name= 'windUnifTC',lstGridRg=model.getSurfacesFromListOfRanges([[[0,0,1],[0,0,2]]]),loadVector= xc.Vector([0,-ULwindTC,0]),refSystem='Local')
# windUnifGC= gm.UniformLoadOnBeamsInRangeLines(name= 'windUnifGC',lstGridRg=model.getSurfacesFromListOfRanges([[[0,0,2],[0,0,lastZpos]]]),loadVector= xc.Vector([0,-ULwindGC,0]),refSystem='Local')


# Load acting on one or several points
    # name:       name identifying the load
    # points:     list of points (list of geom.Pos3d(x,y,z)) where 
    #             the load must be applied.
    # loadVector: xc.Vector with the six components of the load: 
    #             xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#auxilary fuction

lpA=gm.LoadOnPoints(name='lpA',points=[geom.Pos3d(xList[lastXpos],0,0)],loadVector=xc.Vector([FxLoc,0,0,0,0,0]))
lpB=gm.LoadOnPoints(name='lpB',points=[geom.Pos3d(xList[lastXpos],0,0)],loadVector=xc.Vector([0,0,0,0,-MyLoc,0]))
lpC=gm.LoadOnPoints(name='lpC',points=[geom.Pos3d(xList[1],0,0)],loadVector=xc.Vector([0,0,FyLoc,0,0,0]))





#ACTIONS
  # Definition of the actions to be combined in design situations for 
  # performing a limit state analysis
  #   inercLoad:     list of inertial loads
  #   unifPressLoad: list of pressures on surfaces
  #   unifVectLoad:  list of uniform loads on shell elements
  #   unifVectLoadBeam:  list of uniform loads on beam elements
  #   pointLoad:     list of point loads
  #   earthPressLoad:list of earth pressure loads
  #   hydrThrustLoad:list of hydrostatic thrust on the walls that delimit a volume
  #   tempGrad:      list of temperature gradient loads

A= gm.LoadState('A',pointLoad= [lpA])
B= gm.LoadState('B',pointLoad= [lpB])
C= gm.LoadState('C',pointLoad= [lpC])


#Dictionary of actions
loadStates= gm.LoadStateMap([A,B,C])

model.setLoadStates(loadStates)

    # generateLoads(): Apply the loads for each load state and returns the dictionary 
    # [model.dicGeomEnt] with identifiers and the geometric entities (lines and surfaces) 
    # generated
model.generateLoads()


#LOAD COMBINATIONS
combContainer= cc.CombContainer()  #Container of load combinations

# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
    # name:        name to identify the combination
    # rare:        combination for a rare design situation
    # freq:        combination for a frequent design situation
    # qp:          combination for a quasi-permanent design situation
    # earthquake:  combination for a seismic design situation
#Characteristic combinations.
#combContainer.SLS.rare.add('ELSR01', '1.0*GselfWeight')
#Frequent combinations.
#combContainer.SLS.freq.add('ELSF01', '1.0*GselfWeight+1.0*Qwind')
#Quasi permanent combinations.
#combContainer.SLS.qp.add('ELSQP01', '1.0*GselfWeight+1.0*Qwind')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELU01', '1*C')
#combContainer.ULS.perm.add('ELU02', '0.8*GselfWeight')

#Fatigue.
# combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*Qwind')
# combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight')

#Accidental
#combContainer.ULS.acc.add('ELUA0','1.00*GselfWeight+1.0*AvehicCrash')

#Here we define sets of elements that we are to use in the displays and reports
#Instances of the object postprocess.utils_display.setToDisplay are created, which attributes are:
#   elSet:     the set of elements,
#   genDescr:  a general description for the set and
#   sectDescr: a list with the descriptions that apply to each of the sections that configures the element
#For a grid model it's also possible to use the function getSetForDisplay that also generates the the set from a list of parts
beamSet=model.getSetForDisplay(setName='beamSet',parts=['beam'],setGenDescr='beam',setSectDescr=['noeud i','noeud j'])

xcTotalSet=utils_display.setToDisplay(elSet=model.getPreprocessor().getSets.getSet('total'),genDescr='',sectDescr=[])




