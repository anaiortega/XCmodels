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

# ***Auxiliar data***
#Geometry - columns axes
HinfColumn=1.00+1.63
HSupColumn=2.06
RGlass=4
AnglGlass=70
AnglIncr=5
excentInf=0.124
excentSup=0.55/2.0-0.50/2.0

#Bottom column
BCwidthSupFlange=0.65
BCthickSupFlange=0.29
BCthickWeb=0.20
BCheightWeb=0.25
BCwidthInfFlange=0.65
BCthickInfFlange=0.51
BCxCOG=-0.1317

ArBC=BCwidthSupFlange*BCthickSupFlange+BCthickWeb*BCheightWeb+BCwidthInfFlange*BCthickInfFlange
IxBC=1/12*BCwidthSupFlange*BCthickSupFlange**3

#Top column
TCwidthSupFlange=0.45
TCthickSupFlange=0.14
TCthickWeb=0.20
TCheightWeb=0.24
TCwidthInfFlange=0.45
TCthickInfFlange=0.19


#Material concrete
EcConcr=17e9     #concrete modulus or elasticity (Pa)
cpoisConcr=0.2   #concrete coefficient of Poisson
densConcr=2500   #specific mass of concrete (kg/m3)

# Fictitious material to represent rigid motion
Efict=1e14     # modulus or elasticity (Pa)
cpoisFict=0.2  #coefficient of Poisson
densFict=0.0   #specific mass (kg/m3)
# GFict=1e12     #shear modulus

#Actions 
colSpacing=6.50   #spacing between columns [m] 
windPress=1.35e3    #wind pressure [N/m2]
vehicCrashF=750e3   #component of vehicle crash perpendicular to the wall [N]
zvehicCrashF=3.05 #Z coordinate of the point where the force acts [m]

ULwindTC=colSpacing*windPress   # uniform load on the top column due to wind [N/m]
ULwindCC=colSpacing/3.0*windPress  # uniform load on the curve column due to wind [N/m]
PLwind2C=2*colSpacing/3.0*4.12*windPress  #horizontal point load transfered to the head of the
                                          #top column due to wind supported by the 2
                                          #central metallic curved columns

eSize= 0.2     #length of elements

# *** GEOMETRY ***
FEcase= xc.FEProblem()
model= gm.GridModel(FEcase)
preprocessor= model.getPreprocessor()   


# coordinates in global X,Y,Z axes for the grid generation
xList=[0,excentInf,excentInf+excentSup]
yList=[0]
zList=[0,HinfColumn,HinfColumn+HSupColumn]

#we add  Z coordinates (after moving these points in X they would
#shape the curve column that sustains the glass)
incrAngRad=math.radians(AnglIncr)
zBottomGlass=HinfColumn+HSupColumn
for i in range(1,int(AnglGlass/AnglIncr)+1):
    zList.append(zBottomGlass+RGlass*math.sin(i*incrAngRad))


#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid of X,Y,Z axes coordinates
rejXYZ= model.setGrid(xList,yList,zList)

#Displacements of the grid points in a range
#syntax: moveRange(ijkGrid.IJKRange([minIindex,minJindex,minKindex],[maxIindex,maxJindex,maxKindex],[dispX,dispY,dispZ])
for k in range(3,lastZpos+1):
  r= ijkGrid.IJKRange([lastXpos,0,k],[lastXpos,lastYpos,k])
  deltaXPto=-RGlass*(1-math.cos((k-2)*incrAngRad))
  mr= ijkGrid.moveRange(r,[deltaXPto,0.0,0.0])
  rejXYZ.rangesToMove.append(mr)


# *** MATERIALS *** 
concrete=typical_materials.MaterialData(name='concrete',E=EcConcr,nu=cpoisConcr,rho=densConcr)
#Fictitious material to represent rigid motion
fictMat=typical_materials.MaterialData(name='fictMat',E=Efict,nu=cpoisFict,rho=densFict)
#fictMat.G=GFict


  # Isotropic elastic section-material appropiate for plate and shell analysis
  # Attributes:
  #   name:         name identifying the section
  #   E:            Young’s modulus of the material
  #   nu:           Poisson’s ratio
  #   rho:          mass density
  #   thickness:    overall depth of the section

#matDeck= gm.DeckMaterialData(name= 'matDeck',thickness= deckTh,material=concrete)


  #Geometric sections
  #I sections
from materials.sections import section_properties
geomBotCol=section_properties.ISection(name='geomBotCol',wdTopFlange=BCwidthSupFlange,thTopFlange=BCthickSupFlange,thWeb=BCthickWeb,hgWeb=BCheightWeb,wdBotFlange=BCwidthInfFlange,thBotFlange=BCthickInfFlange)
geomTopCol=section_properties.ISection(name='geomTopCol',wdTopFlange=TCwidthSupFlange,thTopFlange=TCthickSupFlange,thWeb=TCthickWeb,hgWeb=TCheightWeb,wdBotFlange=TCwidthInfFlange,thBotFlange=TCthickInfFlange)
  #rectangular sections
from materials.sections import section_properties as rectSect
geomCurvCol=rectSect.RectangularSection(name='geomCurvCol',b=0.2,h=0.5)
#Fictitious geometric section to represent rigid motion
geomFictBeam=rectSect.RectangularSection(name='geomFictBeam',b=5,h=5)

# Elastic material-section appropiate for 3D beam analysis, including shear deformations.
  # Attributes:
  #   name:         name identifying the section
  #   section:      instance of a class that defines the geometric and mechanical characteristiscs
  #                 of a section (e.g: RectangularSection, CircularSection, ISection, ...)
  #   material:     instance of a class that defines the elastic modulus, shear modulus
  #                 and mass density of the material

matBotCol= gm.BeamMaterialData(name= 'matBotCol', section=geomBotCol, material=concrete)
matTopCol= gm.BeamMaterialData(name= 'matTopCol', section=geomTopCol, material=concrete)
matCurvCol= gm.BeamMaterialData(name= 'matCurvCol', section=geomCurvCol, material=concrete)
#Fictitious material section to represent rigid motion
matFictBeam= gm.BeamMaterialData(name= 'matFictBeam', section=geomFictBeam, material=fictMat)

#  Dictionary of materials
matElMembPlat= model.setMaterials([matCurvCol,matBotCol,matTopCol,matFictBeam])


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

botCol= model.newMaterialLine(name='botCol', material= matBotCol, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([0,-1,0]))
botCol.ranges= [ ijkGrid.IJKRange([0,0,0],[0,0,1])]

topCol= model.newMaterialLine(name='topCol', material= matTopCol, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([0,-1,0]))
topCol.ranges= [ ijkGrid.IJKRange([1,0,1],[1,0,2])]
curvCol= model.newMaterialLine(name='curvCol', material= matCurvCol, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([0,-1,0]))
curvCol.ranges= [ ijkGrid.IJKRange([2,0,2],[2,0,lastZpos])]
fictBeam=model.newMaterialLine(name='fictBeam', material= matFictBeam, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([0,1,0]))
fictBeam.ranges= [ ijkGrid.IJKRange([0,0,1],[1,0,1]),ijkGrid.IJKRange([1,0,2],[2,0,2])]


#Dictionary of material-lines
allLinList=[botCol,topCol,curvCol,fictBeam]
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
# boundConstr=model.setConstrainedRangesMap([foundFix])

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
lstNodes=model_inquiry.getNodesInCoordinateRegion(xmin=xList[0],xmax=xList[lastXpos],ymin=yList[0],ymax=yList[lastYpos],zmin=zList[0],zmax=zList[0],xcSet=preprocessor.getSets.getSet('total'))  #list of nodes in the region
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
grav=9.81 #Gravity acceleration (m/s2)
selfWeight= gm.InertialLoadOnMaterialLines(name= 'selfWeight',matLines=[botCol,topCol,curvCol],accel= [0.0,0.0,-grav])


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

windUnifTC= gm.UniformLoadOnBeamsInRangeLines(name= 'windUnifTC',lstGridRg=model.getSurfacesFromListOfRanges([[[1,0,1],[1,0,2]]]),loadVector= xc.Vector([0,-ULwindTC,0]),refSystem='Local')
windUnifCC= gm.UniformLoadOnBeamsInRangeLines(name= 'windUnifCC',lstGridRg=model.getSurfacesFromListOfRanges([[[2,0,2],[2,0,lastZpos]]]),loadVector= xc.Vector([0,-ULwindCC,0]),refSystem='Local')


# Load acting on one or several points
    # name:       name identifying the load
    # points:     list of points (list of geom.Pos3d(x,y,z)) where 
    #             the load must be applied.
    # loadVector: xc.Vector with the six components of the load: 
    #             xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#auxilary fuction

windPoint=gm.LoadOnPoints(name='windPoint',points=[geom.Pos3d(excentInf,0,HinfColumn+HSupColumn)],loadVector=xc.Vector([PLwind2C,0,0,0,0,0]))
vehicCrash=gm.LoadOnPoints(name='vehiclCrash',points=[geom.Pos3d(0,0,zvehicCrashF)],loadVector=xc.Vector([vehicCrashF,0,0,0,0,0]))




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

GselfWeight= gm.LoadState('GselfWeight',inercLoad= [selfWeight])
Qwind=gm.LoadState('Qwind',unifVectLoadBeam=[windUnifTC,windUnifCC],pointLoad=[windPoint])
AvehicCrash=gm.LoadState('AvehicCrash',pointLoad=[vehicCrash])
# Qdeck= gm.LoadState('Qdeck',unifPressLoad= [unifLoadDeck])
#Qbeams=gm.LoadState('Qbeams',pointLoad=[QpuntBeams])

#Dictionary of actions
loadStates= gm.LoadStateMap([GselfWeight,Qwind,AvehicCrash])

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
combContainer.SLS.rare.add('ELSR01', '1.0*GselfWeight')
#Frequent combinations.
combContainer.SLS.freq.add('ELSF01', '1.0*GselfWeight+1.0*Qwind')
#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP01', '1.0*GselfWeight+1.0*Qwind')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELU01', '1.35*GselfWeight+1.5*Qwind')
combContainer.ULS.perm.add('ELU02', '0.8*GselfWeight')

#Fatigue.
combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*Qwind')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight')

#Accidental
combContainer.ULS.acc.add('ELUA0','1.00*GselfWeight+1.0*AvehicCrash')

#Here we define sets of elements that we are to use in the displays and reports
#Instances of the object postprocess.utils_display.setToDisplay are created, which attributes are:
#   elSet:     the set of elements,
#   genDescr:  a general description for the set and
#   sectDescr: a list with the descriptions that apply to each of the sections that configures the element
#For a grid model it's also possible to use the function getSetForDisplay that also generates the the set from a list of parts
botColSet=model.getSetForDisplay(setName='botColSet',parts=['botCol'],setGenDescr='fut fondation prefabriquée',setSectDescr=['noeud i','noeud j'])
topColSet=model.getSetForDisplay(setName='topColSet',parts=['topCol'],setGenDescr='pilier prefabriqué',setSectDescr=['noeud i','noeud j'])
curvColSet=model.getSetForDisplay(setName='curvColSet',parts=['curvCol'],setGenDescr='pilier incurvé',setSectDescr=['noeud i','noeud j'])

colsSet=model.getSetForDisplay(setName='colsSet',parts=['botCol','topCol','curvCol'],setGenDescr='piliers ',setSectDescr=['noeud i','noeud j'])

xcTotalSet=utils_display.setToDisplay(elSet=model.getPreprocessor().getSets.getSet('total'),genDescr='',sectDescr=[])




