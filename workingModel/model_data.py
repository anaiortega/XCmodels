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
from postprocess.config import colors
from postprocess.config import sp_captions as cpt

#Auxiliary data
 #Geometry
LbeamX=5
LbeamY=6
LcolumnZ=4
hbeamX=0.25
hbeamY=0.5
hcolumnZ=0.25
wbeamX=0.5
wbeamY=0.5
wcolumnZ=0.25
deckTh=0.20
wallTh=0.25
foundTh=0.7

 #Actions
qdeck=10e3  #N/m2
Qbeam=30e3  #N/m
firad=math.radians(31)  #internal friction angle (radians)                   
KearthPress=(1-math.sin(firad))/(1+math.sin(firad))     #Active coefficient of p
densSoil=2200       #mass density of the soil (kg/m3)
densWater=1000      #mass density of the water (kg/m3)


#Materials
fcmConcr=30e6
EcConcr=8500*(fcmConcr/1e6)**(1/3.0)*1e6
cpoisConcr=0.2                #Poisson's coefficient of concrete
densConcr= 2500               #specific mass of concrete (kg/m3)

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
xList=[0,LbeamX/2.0,LbeamX]
yList=[0,LbeamY/2.0,LbeamY]
zList=[0,LcolumnZ/2.0,LcolumnZ]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

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
beamX_rg=gm.IJKRange((0,0,lastZpos),(lastXpos,lastYpos,lastZpos)).extractIncludedIranges()
beamY_rg=gm.IJKRange((0,0,lastZpos),(lastXpos,lastYpos,lastZpos)).extractIncludedJranges()
columnZ_rg=gm.IJKRange((0,0,1),(lastXpos,lastYpos,lastZpos)).extractIncludedKranges()+gm.IJKRange((0,lastYpos,0),(lastXpos,lastYpos,1)).extractIncludedKranges()
deck_rg=gm.IJKRange((0,0,1),(lastXpos,lastYpos,1)).extractIncludedIJranges()
wall_rg=gm.IJKRange((0,0,0),(lastXpos,0,1))
found_rg=[gm.IJKRange((0,0,0),(lastXpos,lastYpos,0))]
#Lines generation
beamX=gridGeom.genLinMultiRegion(lstIJKRange=beamX_rg,nameSet='beamX')
beamY=gridGeom.genLinMultiRegion(lstIJKRange=beamY_rg,nameSet='beamY')
columnZ=gridGeom.genLinMultiRegion(lstIJKRange=columnZ_rg,nameSet='columnZ')
#Surfaces generation
deck=gridGeom.genSurfMultiRegion(lstIJKRange=deck_rg,nameSet='deck')
wall=gridGeom.genSurfOneRegion(ijkRange=wall_rg,nameSet='wall')
found=gridGeom.genSurfMultiRegion(lstIJKRange=found_rg,nameSet='found')
deck.description='Deck'
found.description='Foundation'
wall.description='Wall'
beamX.description='Beams in X direction'
beamY.description='Beams in Y direction'
columnZ.description='Columns'


#                         *** MATERIALS *** 
concrete=tm.MaterialData(name='concrete',E=EcConcr,nu=cpoisConcr,rho=densConcr)

# Isotropic elastic section-material appropiate for plate and shell analysis
deck_mat=tm.DeckMaterialData(name='deck_mat',thickness= deckTh,material=concrete)
deck_mat.setupElasticSection(preprocessor=prep)   #creates the section-material
wall_mat=tm.DeckMaterialData(name='wall_mat',thickness= wallTh,material=concrete)
wall_mat.setupElasticSection(preprocessor=prep)   #creates the section-material
found_mat=tm.DeckMaterialData(name='found_mat',thickness= foundTh,material=concrete)
found_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectBeamX=sectpr.RectangularSection(name='geomSectBeamX',b=wbeamX,h=hbeamX)
geomSectBeamY=sectpr.RectangularSection(name='geomSectBeamY',b=wbeamY,h=hbeamY)
geomSectColumnZ=sectpr.RectangularSection(name='geomSectColumnZ',b=wcolumnZ,h=hcolumnZ)

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

beamX_mat= tm.BeamMaterialData(name= 'beamX_mat', section=geomSectBeamX, material=concrete)
beamX_mat.setupElasticShear3DSection(preprocessor=prep)
beamY_mat= tm.BeamMaterialData(name= 'beamY_mat', section=geomSectBeamY, material=concrete)
beamY_mat.setupElasticShear3DSection(preprocessor=prep)
columnZ_mat= tm.BeamMaterialData(name= 'columnZ_mat', section=geomSectColumnZ, material=concrete)
columnZ_mat.setupElasticShear3DSection(preprocessor=prep)

#                         ***FE model - MESH***

beamX_mesh=fem.LinSetToMesh(linSet=beamX,matSect=beamX_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
beamX_mesh.generateMesh(prep)    # mesh this set of lines

beamY_mesh=fem.LinSetToMesh(linSet=beamY,matSect=beamY_mat,elemSize=eSize,vDirLAxZ=xc.Vector([1,0,0]),elemType='ElasticBeam3d',coordTransfType='linear')
columnZ_mesh=fem.LinSetToMesh(linSet=columnZ,matSect=columnZ_mat,elemSize=eSize,vDirLAxZ=xc.Vector([1,0,0]),elemType='ElasticBeam3d',coordTransfType='linear')
deck_mesh=fem.SurfSetToMesh(surfSet=deck,matSect=deck_mat,elemSize=eSize,elemType='ShellMITC4')
deck_mesh.generateMesh(prep)     #mesh the set of surfaces
wall_mesh=fem.SurfSetToMesh(surfSet=wall,matSect=wall_mat,elemSize=eSize,elemType='ShellMITC4')
found_mesh=fem.SurfSetToMesh(surfSet=found,matSect=found_mat,elemSize=eSize,elemType='ShellMITC4')

fem.multi_mesh(preprocessor=prep,lstMeshSets=[beamY_mesh,columnZ_mesh,found_mesh,wall_mesh])     #mesh these sets

overallSet=beamX+beamY+columnZ+wall+found+deck
overallSet.description='all'


#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
found_wink=sprbc.ElasticFoundation(wModulus=20e7,cRoz=0.2)
found_wink.generateSprings(xcSet=found)

# Springs (defined by Kx,Ky,Kz) to apply on nodes, points, 3Dpos, ...
# Default values for Kx, Ky, Kz are 0, which means that no spring is
# created in the corresponding direction
spring_roof=sprbc.SpringBC(name='spring_roof',modelSpace=modelSpace,Kx=1000,Ky=0,Kz=3000)
a=spring_roof.applyOnNodesIn3Dpos(lst3DPos=[geom.Pos3d(LbeamX/2.0,LbeamY/2.0,LcolumnZ/2.0)])

#fixed DOF
n_ux=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX,LbeamY,LcolumnZ))
modelSpace.fixNode('0FF_FFF',n_ux.tag)
n_uy=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX/2.,LbeamY,LcolumnZ))
modelSpace.fixNode('F0F_FFF',n_uy.tag)
n_uz=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX/2.,LbeamY/2.0,LcolumnZ))
modelSpace.fixNode('FF0_FFF',n_uz.tag)
n_rx=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX,LbeamY,LcolumnZ/2.0))
modelSpace.fixNode('FFF_0FF',n_rx.tag)
n_ry=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX/2.,LbeamY,LcolumnZ/2.0))
modelSpace.fixNode('FFF_F0F',n_ry.tag)
n_rz=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX/2.,LbeamY/2.0,LcolumnZ/2.0))
modelSpace.fixNode('FFF_FF0',n_rz.tag)

n_uxyz=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX,LbeamY,LcolumnZ/3))
modelSpace.fixNode('000_FFF',n_uxyz.tag)
n_rxyz=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX,LbeamY,LcolumnZ/3))
modelSpace.fixNode('FFF_000',n_rxyz.tag)

#                       ***ACTIONS***
#overallSet=prep.getSets.getSet('total')
#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
#selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[beamX_mesh,beamY_mesh,columnZ_mesh,deck_mesh,wall_mesh,found_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[beamX_mesh,beamY_mesh,columnZ_mesh,deck_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

# Load acting on one or several nodes
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

unifLoadDeck= loads.UniformLoadOnSurfaces(name= 'unifLoadDeck',xcSet=deck,loadVector=xc.Vector([0,0,-qdeck,0,0,0]),refSystem='Global')

# Earth pressure applied to shell or beam elements
#     Attributes:
#     name:       name identifying the load
#     xcSet:      set that contains the elements to be loaded
#     EarthPressureModel: instance of the class EarthPressureModel, with 
#                 the following attributes:
#                   K:Coefficient of pressure
#                   zGround:global Z coordinate of ground level
#                   gammaSoil: weight density of soil 
#                   zWater: global Z coordinate of groundwater level 
#                   (if zGroundwater<minimum z of model => there is no groundwater)
#                   gammaWater: weight density of water
#     if EarthPressureModel==None no earth thrust is considered
#     vDir: unit xc vector defining pressures direction

soil01=ep.EarthPressureModel(K=KearthPress, zGround=zList[lastZpos], gammaSoil=densSoil*grav, zWater=0.75, gammaWater=densWater*grav)
earthPressLoadWall= loads.EarthPressLoad(name= 'earthPressLoadWall', xcSet=wall,soilData=soil01, vDir=xc.Vector([0,1,0]))

earthPressLoadColumn= loads.EarthPressLoad(name= 'earthPressLoadColumn', xcSet=columnZ,soilData=soil01, vDir=xc.Vector([0,1,0]))

soil02=ep.EarthPressureModel(K=0.001, zGround=zList[lastZpos], gammaSoil=densSoil*grav, zWater=0.75, gammaWater=densWater*grav)
stripL01=ep.StripLoadOnBackfill(qLoad=2e5, zLoad=zList[lastZpos],distWall=1.5, stripWidth=1.2)
earthPColumnStrL= loads.EarthPressLoad(name= 'earthPColumnStrL', xcSet=columnZ,soilData=None, vDir=xc.Vector([0,1,0]))
earthPColumnStrL.stripLoads=[stripL01]

lineL01=ep.LineVerticalLoadOnBackfill(qLoad=1e5, zLoad=zList[lastZpos],distWall=1.0)
earthPColumnLinL= loads.EarthPressLoad(name= 'earthPColumnLinL', xcSet=columnZ,soilData=None, vDir=xc.Vector([0,1,0]))
earthPColumnLinL.lineLoads=[lineL01]

hrzL01=ep.HorizontalLoadOnBackfill(soilIntFi=30, qLoad=2e5, zLoad=zList[lastZpos],distWall=1,widthLoadArea=0.5,lengthLoadArea=1.5,horDistrAngle=45)
earthPColumnHrzL=loads.EarthPressLoad(name= 'earthPColumnHrzL', xcSet=columnZ,soilData=None, vDir=xc.Vector([0,1,0]))
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
unifLoadBeamsY=loads.UniformLoadOnBeams(name='unifLoadBeamsY', xcSet=beamY, loadVector=xc.Vector([0,-5,0,0,0,0]),refSystem='Global')

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

unifLoadLinFound=loads.UniformLoadOnLines(name='unifLoadLinFound',xcSet=found,loadVector=xc.Vector([0,0,-5,0,0,0]))

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



#    ***LOAD CASES***




GselfWeight=lcases.LoadCase(preprocessor=prep,name="GselfWeight",loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight,QpuntBeams])

Qdeck=lcases.LoadCase(preprocessor=prep,name="Qdeck")
Qdeck.create()
Qdeck.addLstLoads([unifLoadDeck,unifLoadBeamsY])
eval('1.25*unifLoadLinFound')   #add this weighted load to the curret load case

QearthPressWall=lcases.LoadCase(preprocessor=prep,name="QearthPressWall",loadPType="default",timeSType="constant_ts")
QearthPressWall.create()
eval('1.1*earthPressLoadWall')  #add this weighted load to the curret load case
'''
QearthPressCols=lcases.LoadCase(preprocessor=prep,name="QearthPressCols",loadPType="default",timeSType="constant_ts")
QearthPressCols.create()
eval('1.0*earthPressLoadColumn')  #add this weighted load to the curret load case

QearthPColsStrL=lcases.LoadCase(preprocessor=prep,name="QearthPColsStrL",loadPType="default",timeSType="constant_ts")
QearthPColsStrL.create()
eval('1.0*earthPColumnStrL')

QearthPColsLinL=lcases.LoadCase(preprocessor=prep,name="QearthPColsLinL",loadPType="default",timeSType="constant_ts")
QearthPColsLinL.create()
eval('1.0*earthPColumnLinL')
#QearthPColsLinL.addLstLoads([earthPColumnLinL])

QearthPColsHrzL=lcases.LoadCase(preprocessor=prep,name="QearthPColsHrzL",loadPType="default",timeSType="constant_ts")
QearthPColsHrzL.create()
eval('1.0*earthPColumnHrzL')
#QearthPColsHrzL.addLstLoads([earthPColumnHrzL])
'''

#    ***LIMIT STATE COMBINATIONS***
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
combContainer.SLS.freq.add('ELSF01', '1.0*GselfWeight+1.0*Qdeck+1.0*QearthPressWall')
#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP01', '1.0*GselfWeight+1.0*Qdeck')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELU01', '10*GselfWeight+1*Qdeck')
combContainer.ULS.perm.add('ELU02', '0.8*GselfWeight+1.0*QearthPressWall')

#Fatigue.
# Combinations' names must be:
#        - ELUF0: unloaded structure (permanent loads)
#        - ELUF1: fatigue load in position 1.
combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*Qdeck')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*QearthPressWall')


allShells=deck+found+wall
allShells.description='Shell elements'
allBeams=beamX+beamY+columnZ
allBeams.description='Beams+columns'
overallSet=deck+found+wall+beamX+beamY+columnZ

 




