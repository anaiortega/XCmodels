# -*- coding: utf-8 -*-
import os
import geom
import xc
import math
from materials.ehe import EHE_materials
#from materials.sia262 import SIA262_materials
from materials.ec3 import EC3_materials
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
from postprocess.config import default_config

# Default configuration of environment variables.
from postprocess import output_styles as outSty
from postprocess import output_handler as outHndl


workingDirectory= default_config.findWorkingDirectory()+'/' #search env_config.py
exec(open(workingDirectory+'env_config.py').read())
sty=outSty.OutputStyle() 

#Data
exec(open(workingDirectory+'data.py').read())

#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)
out=outHndl.OutputHandler(modelSpace,sty)

# coordinates in global X,Y,Z axes for the grid generation
xList=[0,LbeamX/2.0,LbeamX]
yList=[-Wfoot/2.,0,Wfoot/2.,LbeamY]
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
beamXconcr_rg=gm.IJKRange((0,1,lastZpos),(lastXpos,lastYpos,lastZpos)).extractIncludedIranges(stepJ=2,stepK=1)
beamY_rg=gm.IJKRange((0,1,lastZpos),(lastXpos,lastYpos,lastZpos)).extractIncludedJranges(stepI=2,stepK=1)
columnZconcr_rg=gm.IJKRange((0,1,0),(lastXpos,1,lastZpos)).extractIncludedKranges(stepI=2)
columnZsteel_rg=gm.IJKRange((0,lastYpos,0),(lastXpos,lastYpos,lastZpos)).extractIncludedJKranges(step=2)+[gm.IJKRange((1,lastYpos,0),(1,lastYpos,1))]
decklv1_rg=gm.IJKRange((0,1,1),(lastXpos,lastYpos,lastZpos)).extractIncludedIJranges(step=2)
foot_rg=[gut.def_rg_cooLim(XYZLists=(xList,yList,zList),Xcoo=(0,LbeamX),Ycoo=(-Wfoot/2.,Wfoot/2.),Zcoo=(0,0))]
beamXsteel_rg=gm.IJKRange((0,2,lastZpos),(lastXpos,2,lastZpos))
#Lines generation
beamXconcr=gridGeom.genLinMultiRegion(lstIJKRange=beamXconcr_rg,setName='beamXconcr')
beamXsteel=gridGeom.genLinOneRegion(ijkRange=beamXsteel_rg,setName='beamXsteel')
beamY=gridGeom.genLinMultiRegion(lstIJKRange=beamY_rg,setName='beamY')
columnZconcr=gridGeom.genLinMultiRegion(lstIJKRange=columnZconcr_rg,setName='columnZconcr')
columnZsteel=gridGeom.genLinMultiRegion(lstIJKRange=columnZsteel_rg,setName='columnZsteel')

#out.displayBlocks()

#Surfaces generation
decklv1=gridGeom.genSurfMultiRegion(lstIJKRange=decklv1_rg,setName='decklv1')
decklv2=gridGeom.genSurfOneXYZRegion(xyzRange=((0,Wfoot/2.,LcolumnZ),(LbeamX/2.0,LbeamY,LcolumnZ)),setName='decklv2')
wall=gridGeom.genSurfOneXYZRegion(xyzRange=((0,0,0),(LbeamX,0,LcolumnZ)),setName='wall')
foot=gridGeom.genSurfMultiRegion(lstIJKRange=foot_rg,setName='foot')
decklv1.description='Deck level 1'
decklv1.color=cfg.colors['purple01']
decklv2.description='Deck level 2'
decklv2.color=cfg.colors['blue01']
foot.description='Foundation'
foot.color=cfg.colors['orange01']
wall.description='Wall'
wall.color=cfg.colors['green01']
beamXconcr.description='Beams in X direction'
beamXconcr.color=cfg.colors['blue03']
beamY.description='Beams in Y direction'
beamY.color=cfg.colors['green03']
columnZconcr.description='Concrete columns'
columnZconcr.color=cfg.colors['red03']
columnZsteel.description='Steel columns'
columnZsteel.color=cfg.colors['blue02']

beams=modelSpace.setSum('beams',[beamXconcr,beamY])
beams.description='Beams'
beams.fillDownwards()
#out.displayBlocks()

#                         *** MATERIALS *** 
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())
S235JR= EC3_materials.S235JR
S235JR.gammaM= 1.00

# Isotropic elastic section-material appropiate for plate and shell analysis
deck_mat=tm.DeckMaterialData(name='deck_mat',thickness= deckTh,material=concrProp)
deck_mat.setupElasticSection(preprocessor=prep)   #creates the section-material
wall_mat=tm.DeckMaterialData(name='wall_mat',thickness= wallTh,material=concrProp)
wall_mat.setupElasticSection(preprocessor=prep)   #creates the section-material
foot_mat=tm.DeckMaterialData(name='foot_mat',thickness= footTh,material=concrProp)
foot_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

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

beamXconcr_mat= tm.BeamMaterialData(name= 'beamXconcr_mat', section=geomSectBeamX, material=concrProp)
beamXconcr_mat.setupElasticShear3DSection(preprocessor=prep)
beamY_mat= tm.BeamMaterialData(name= 'beamY_mat', section=geomSectBeamY, material=concrProp)
beamY_mat.setupElasticShear3DSection(preprocessor=prep)
columnZconcr_mat= tm.BeamMaterialData(name= 'columnZconcr_mat', section=geomSectColumnZ, material=concrProp)
columnZconcr_mat.setupElasticShear3DSection(preprocessor=prep)

# Steel material-section appropiate for 3D beam analysis, including shear
  # deformations.
  # Attributes:
  #   steel:         steel material (
  #   name: name of the standard steel profile. Types: IPEShape, HEShape,
  #         UPNShape, AUShape, CHSShape
  #      (defined in materials.sections.structural_shapes.arcelor_metric_shapes)
columnZsteel_mat= EC3_materials.HEShape(steel=S235JR,name='HE_200_A')
columnZsteel_mat.defElasticShearSection3d(prep)
beamXsteel_mat= EC3_materials.IPEShape(steel=S235JR,name='IPE_A_300')
beamXsteel_mat.defElasticShearSection3d(prep)

#                         ***FE model - MESH***
# IMPORTANT: it's convenient to generate the mesh of surfaces before meshing
# the lines, otherwise, sets of shells can take also beam elements touched by
# them

beamXconcr_mesh=fem.LinSetToMesh(linSet=beamXconcr,matSect=beamXconcr_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
beamY_mesh=fem.LinSetToMesh(linSet=beamY,matSect=beamY_mat,elemSize=eSize,vDirLAxZ=xc.Vector([1,0,0]),elemType='ElasticBeam3d',coordTransfType='linear')
columnZconcr_mesh=fem.LinSetToMesh(linSet=columnZconcr,matSect=columnZconcr_mat,elemSize=eSize,vDirLAxZ=xc.Vector([1,0,0]),elemType='ElasticBeam3d',coordTransfType='linear')
decklv1_mesh=fem.SurfSetToMesh(surfSet=decklv1,matSect=deck_mat,elemSize=eSize,elemType='ShellMITC4')
decklv1_mesh.generateMesh(prep)     #mesh the set of surfaces
decklv2_mesh=fem.SurfSetToMesh(surfSet=decklv2,matSect=deck_mat,elemSize=eSize,elemType='ShellMITC4')
decklv2_mesh.generateMesh(prep)     #mesh the set of surfaces
wall_mesh=fem.SurfSetToMesh(surfSet=wall,matSect=wall_mat,elemSize=eSize,elemType='ShellMITC4')
wall_mesh.generateMesh(prep) 
foot_mesh=fem.SurfSetToMesh(surfSet=foot,matSect=foot_mat,elemSize=eSize,elemType='ShellMITC4')
foot_mesh.generateMesh(prep)

#Steel elements: local Z-axis corresponds to weak axis of the steel shape
beamXsteel_mesh=fem.LinSetToMesh(linSet=beamXsteel,matSect=beamXsteel_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,-1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
columnZsteel_mesh=fem.LinSetToMesh(linSet=columnZsteel,matSect=columnZsteel_mat,elemSize=eSize,vDirLAxZ=xc.Vector([-1,0,0]),elemType='ElasticBeam3d',coordTransfType='linear')

fem.multi_mesh(preprocessor=prep,lstMeshSets=[beamXconcr_mesh,beamXsteel_mesh,beamY_mesh,columnZconcr_mesh,columnZsteel_mesh])     #mesh these sets

#out.displayFEMesh([beamXconcr,beamY,columnZconcr,decklv1,decklv2,wall,foot])
#out.displayFEMesh([beamXconcr,beamXsteel])
#out.displayFEMesh([columnZconcr,columnZsteel])
#out.displayLocalAxes()
#out.displayStrongWeakAxis(beams)

#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
foot_wink=sprbc.ElasticFoundation(wModulus=20e7,cRoz=0.2)
foot_wink.generateSprings(xcSet=foot)
#out.displayFEMesh()

# Springs (defined by Kx,Ky,Kz) to apply on nodes, points, 3Dpos, ...
# Default values for Kx, Ky, Kz are 0, which means that no spring is
# created in the corresponding direction
# spring_col=sprbc.SpringBC(name='spring_col',modelSpace=modelSpace,Kx=10e3,Ky=50e3,Kz=30e3)
# a=spring_col.applyOnNodesIn3Dpos(lst3DPos=[geom.Pos3d(0,LbeamY,0)])

#fixed DOF (ux:'0FF_FFF', uy:'F0F_FFF', uz:'FF0_FFF',
#           rx:'FFF_0FF', ry:'FFF_F0F', rz:'FFF_FF0')
n_col1=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(0,LbeamY,0))
modelSpace.fixNode('000_FFF',n_col1.tag)
n_col2=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX,LbeamY,0))
modelSpace.fixNode('000_FFF',n_col2.tag)
n_col3=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(LbeamX/2.,LbeamY,0))
modelSpace.fixNode('FF0_000',n_col3.tag)
#out.displayFEMesh()

#                       ***ACTIONS***

#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
#selfWeight=loads.InertialLoad(name='selfWeight', lstSets=[beamXconcr,beamY,columnZconcr,deck,wall,foot], vAccel=xc.Vector( [0.0,0.0,-grav]))
selfWeight=loads.InertialLoad(name='selfWeight', lstSets=[beamXconcr,beamY,columnZconcr,decklv1,decklv2], vAccel=xc.Vector( [0.0,0.0,-grav]))

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
unifLoadDeck2= loads.UniformLoadOnSurfaces(name= 'unifLoadDeck2',xcSet=decklv1,loadVector=xc.Vector([0,0,-qdeck2,0,0,0]),refSystem='Global')

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

hrzL01=ep.HorizontalLoadOnBackfill(phi= math.radians(30), qLoad=2e5, zLoad=zList[lastZpos],distWall=1, loadedAreaWidth= 0.5, loadedAreaLength= 1.5, horDistrAngle= math.radians(45))
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
unifLoadBeamsY=loads.UniformLoadOnBeams(name='unifLoadBeamsY', xcSet=beamY, loadVector=xc.Vector([1e3,2e3,-qunifBeam,0,0,0]),refSystem='Global')
unifLoadBeamsY2=loads.UniformLoadOnBeams(name='unifLoadBeamsY2', xcSet=beamY, loadVector=xc.Vector([2e3,4e3,-2*qunifBeam,0,0,0]),refSystem='Global')

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

from actions.roadway_traffic import IAP_load_models as slm
from actions.roadway_traffic import load_model_base as lmb
vehicleDeck1=lmb.VehicleDistrLoad(name='vehicleDeck1',xcSet=decklv1,loadModel=slm.IAP_notional_lane3_brake, xCentr=LbeamX/2,yCentr=LbeamY/2.,hDistr=0.25,slopeDistr=1.0)


#    ***LOAD CASES***

GselfWeight=lcases.LoadCase(preprocessor=prep,name="GselfWeight",loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])
'''
modelSpace.addLoadCaseToDomain("GselfWeight")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("GselfWeight")
'''

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
'''
modelSpace.addLoadCaseToDomain("qunifBeams")
out.displayLoads(beams)
modelSpace.removeLoadCaseFromDomain("qunifBeams")
'''

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
LS1.addLstLoads([unifLoadDeck1])

LS2=lcases.LoadCase(preprocessor=prep,name="LS2",loadPType="default",timeSType="constant_ts")
LS2.create()
LS2.addLstLoads([unifLoadDeck2])

LS3=lcases.LoadCase(preprocessor=prep,name="LS3",loadPType="default",timeSType="constant_ts")
LS3.create()
LS3.addLstLoads([unifLoadBeamsY,unifLoadBeamsY2])

LS4=lcases.LoadCase(preprocessor=prep,name="LS4",loadPType="default",timeSType="constant_ts")
LS4.create()
LS4.addLstLoads([unifLoadBeamsY])


modelSpace.addLoadCaseToDomain("LS3")
#activeLoadPatterns= prep.getDomain.getConstraints.getLoadPatterns
#lps=[lp.data() for lp in activeLoadPatterns]
out.displayLoads(elLoadComp='xyzComponents')
modelSpace.addLoadCaseToDomain("LS4")
out.displayLoads(elLoadComp='xyzComponents')
quit()
modelSpace.removeLoadCaseFromDomain("LS1")

