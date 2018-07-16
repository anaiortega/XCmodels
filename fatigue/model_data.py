# -*- coding: utf-8 -*-

import os
import xc_base
import geom
import xc
import math
from model.grid_based_oldStyle_deprecated import ijkGrid
from model.grid_based_oldStyle_deprecated import GridModel as gm
from actions import combinations as cc
from postprocess import limit_state_data as lsd
from materials import typical_materials
from postprocess import utils_display

# Cantlv elements. Working example
#Auxiliary data
 #Geometry
Lcantlv=10
hcantlv=0.5
wcantlv=1


 #Actions
Qcantlv=10e3  #N/m2

#Materials
fcmConcr=30e6
EcConcr=8500*(fcmConcr/1e6)**(1/3.0)*1e6
cpoisConcr=0.2                #Poisson's coefficient of concrete
densConcr= 2500               #specific mass of concrete (kg/m3)

eSize= 1     #length of elements

# *** GEOMETRY ***
FEcase= xc.FEProblem()
model= gm.GridModel(FEcase)
preprocessor=model.getPreprocessor()

# coordinates in global X,Y,Z axes for the grid generation
xList=[0,wcantlv]
yList=[0.1*i for i in range(int(Lcantlv/0.1)+1)]
zList=[0]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid of X,Y,Z axes coordinates
rejXYZ= model.setGrid(xList,yList,zList)

#Displacements of the grid points in a range
#syntax: moveRange(ijkGrid.IJKRange([minIindex,minJindex,minKindex],[maxIindex,maxJindex,maxKindex],[dispX,dispY,dispZ])
# mr= ijkGrid.moveRange( ijkGrid.IJKRange([1,0,1],[1,lastYpos,1]),[0.5,0.0,0.0])
# rejXYZ.rangesToMove.append(mr)


# *** MATERIALS *** 
#*Auxiliary data
#fck=30e6  #characteristic strength of concrete (Pa)
#fcm=fck+8e6 #mean strength of concrete (Pa)
#Ec=8500*fcm/1e6**(1/3.0)*1e6 #modulus of elasticity of concrete

concrCantlv=typical_materials.MaterialData(name='concrCantlv',E=EcConcr,nu=cpoisConcr,rho=densConcr)



  # Isotropic elastic section-material appropiate for plate and shell analysis
  # Attributes:
  #   name:         name identifying the section
  #   E:            Young’s modulus of the material
  #   nu:           Poisson’s ratio
  #   rho:          mass density
  #   thickness:    overall depth of the section

matCantlv= gm.DeckMaterialData(name= 'matCantlv',thickness= hcantlv,material=concrCantlv)


  #Geometric sections
  #rectangular sections
# from materials.sections import section_properties as rectSect
# geomSectBeamX=rectSect.RectangularSection(name='geomSectBeamX',b=wbeamX,h=hbeamX)
# geomSectBeamY=rectSect.RectangularSection(name='geomSectBeamY',b=wbeamY,h=hbeamY)
# geomSectColumnZ=rectSect.RectangularSection(name='geomSectColumnZ',b=wcolumnZ,h=hcolumnZ)

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

# matBeamX= gm.BeamMaterialData(name= 'matBeamX', section=geomSectBeamX, material=concrBeams)
# matBeamY= gm.BeamMaterialData(name= 'matBeamY', section=geomSectBeamY, material=concrBeams)
# matColumnZ= gm.BeamMaterialData(name= 'matColumnZ', section=geomSectColumnZ, material=concrBeams)

#  Dictionary of materials
matElMembPlat= model.setMaterials([matCantlv])


    # Types of surfaces to be discretized from the defined 
    # material, type of element and size of the elements.
    # Parameters:
    #   name:     name to identify the type of surface
    #   material: name of the material that makes up the surface
    #   elemType: element type to be used in the discretization
    #   elemSize: mean size of the elements
    #   ranges:   lists of grid ranges to delimit the surfaces of 
    #             the type in question
cantlv= model.newMaterialSurface('cantlv', material=matCantlv, elemType='ShellMITC4',elemSize= eSize)
cantlv.ranges= [ ijkGrid.IJKRange([0,0,0],[lastXpos,lastYpos,lastZpos])]

allSurfList=[cantlv]

# #Dictionary of material-surfaces
conjSup= model.setMaterialSurfacesMap(allSurfList)

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
# beamX= model.newMaterialLine(name='beamX', material= matBeamX, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([0,1,0]))
# beamX.ranges= [ ijkGrid.IJKRange([0,0,lastZpos],[lastXpos,0,lastZpos]),ijkGrid.IJKRange([0,lastYpos,lastZpos],[lastXpos,lastYpos,lastZpos])]

#Dictionary of material-lines
# allLinList=[beamX,beamY,columnZ]
# conjLines= model.setMaterialLinesMap(allLinList)

#Boundary conditions

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
# foundationElasticSupports.ranges.extend(found.ranges) #WARNING DO NOT ASSIGN ranges OTHERWISE FURTHER MODIFICATIONS ARE MADE IN BOTH RANGES


#Dictionary with the list of Winkler elastic foundations given as a parameter
# elasticSupports= model.setElasticFoundationRangesMap([foundationElasticSupports])

    #Constrains in the nodes belonging to the lines of a range-region
    #    name:        name to identify the boundary condition
    #    constraints: constraint conditions, expressed as [uX, uY, uZ,rotX, rotY, rotZ], where:
    #                 - uX, uY, uZ: translations in the X, Y and Z directions; 
    #                 - rotX, rotY, rotZ: rotations about the X, Y and Z axis
    #                 - 'free': means no constraint

# foundFix=model.newConstrainedRanges(name='foundFix',constraints=[0,0,0,0,0,0])
# foundFix.ranges.extend([ijkGrid.IJKRange([0,0,0],[lastXpos,lastYpos,0])])


#Dictionary with the list of constraints given as a parameter
# boundConstr=model.setConstrainedRangesMap([foundFix])


dicGeomEnt= model.generateMesh() 

#Boundary conditions
#Constrains in the nodes belonging to a region defined by coordinates
#constrCond:   list of constraint conditions, expressed as 
             #   [uX, uY, uZ,rotX, rotY, rotZ], where:
             # - uX, uY, uZ: translations in the X, Y and Z directions; 
             # - rotX, rotY, rotZ: rotations about the X, Y and Z axis
             # - 'free': means no constraint values 
from model import model_inquiry
lstNodes=model_inquiry.getNodesInCoordinateRegion(xmin=xList[0],xmax=xList[lastXpos],ymin=yList[0],ymax=yList[0],zmin=zList[0],zmax=zList[0],xcSet=preprocessor.getSets.getSet('total'))  #list of nodes in the region
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
#Self weight.
# grav=9.81 #Gravity acceleration (m/s2)
# selfWeight= gm.InertialLoadOnMaterialSurfaces(name= 'selfWeight',surfaces=allSurfList,accel= [0.0,0.0,-grav])


  # Uniform loads applied to shell elements
  # name:       name identifying the load
  # lstGridRg:   lists of grid ranges to delimit the surfaces to
  #             be loaded
  # loadVector: list with the three components of the load vector

unifLoadCantlv= gm.PressureLoadOnSurfaces(name= 'unifLoadCantlv',lstGridRg=model.getSurfacesFromListOfRanges([[[0,0,0],[lastXpos,lastYpos,lastZpos]]]),loadVector= [0,0,-Qcantlv])

    # Load acting on one or several points
    # name:       name identifying the load
    # points:     list of points (list of geom.Pos3d(x,y,z)) where 
    #             the load must be applied.
    # loadVector: xc.Vector with the six components of the load: 
    #             xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#auxilary fuction

# QpuntBeams=gm.LoadOnPoints(name='QpuntBeams',points=[geom.Pos3d(0,yList[lastYpos]/2.0,zList[lastZpos]),geom.Pos3d(xList[lastXpos],yList[lastYpos]/2.0,zList[lastZpos])],loadVector=xc.Vector([0,0,-Qbeam,0,0,0]))




#ACTIONS
  # Definition of the actions to be combined in design situations for 
  # performing a limit state analysis
  #   inercLoad:     list of inertial loads
  #   unifPressLoad: list of pressures on surfaces
  #   unifVectLoad:  list of uniform loads on shell elements
  #   pointLoad:     list of point loads
  #   earthPressLoad:list of earth pressure loads
  #   hydrThrustLoad:list of hydrostatic thrust on the walls that delimit a volume
  #   tempGrad:      list of temperature gradient loads

#GselfWeight= gm.LoadState('GselfWeight',inercLoad= [selfWeight])
Qcantlv= gm.LoadState('Qcantlv',unifPressLoad= [unifLoadCantlv])
#Qbeams=gm.LoadState('Qbeams',pointLoad=[QpuntBeams])

#Dictionary of actions
loadStates= gm.LoadStateMap([Qcantlv])

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
combContainer.SLS.rare.add('ELSR01', '1.0*Qcantlv')
#Frequent combinations.
combContainer.SLS.freq.add('ELSF01', '1.0*Qcantlv')
#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP01', '1.0*Qcantlv')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELU01', '1.0*Qcantlv')

#Fatigue.
#        - ELUF0: unloaded structure (permanent loads)
#        - ELUF1: fatigue load in position 1.

combContainer.ULS.fatigue.add('ELUF0','1.0*Qcantlv')


#Here we define sets of elements that we are to use in the displays and reports
#Instances of the object postprocess.utils_display.setToDisplay are created, which attributes are:
#   elSet:     the set of elements,
#   genDescr:  a general description for the set and
#   sectDescr: a list with the descriptions that apply to each of the sections that configures the element
#For a grid model it's also possible to use the function getSetForDisplay that also generates the the set from a list of parts
cantlvSet=model.getSetForDisplay(setName='cantlvSet',parts=['cantlv'],setGenDescr='cantlv elements',setSectDescr=['rebars dir. X','rebars dir. Y'])

xcTotalSet=utils_display.setToDisplay(elSet=preprocessor.getSets.getSet('total'),genDescr='',sectDescr=[])



 

