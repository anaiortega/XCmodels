# -*- coding: utf-8 -*-
import math

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

#Auxiliary data
 #   ***Geometry
slope=-0.18 #Deck Y-direction slope (%)
alpha=math.atan(slope)
proj_fc=math.cos(alpha)   #projection factor
delta_Y=3.9*proj_fc
L_long_side_Y=29.3*proj_fc
L_short_side_Y=21.6*proj_fc
delta_crossect_1=0.21

deckTh=0.25 #Deck thickness [m]
curbTh=0.50 #Curbs thickness [m]

hCables=0.0 # Position (Z) of cables above the deck median plane 
deltaZ_lastcable=-0.02


#  ***Materials
fcmConcr=50e6
EcConcr=8500*(fcmConcr/1e6)**(1/3.0)*1e6
cpoisConcr=0.2                #Poisson's coefficient of concrete
densConcr= 2500               #specific mass of concrete (kg/m3)

wModulus_fill=5e7             #[N/m3]
wModulus_walls=10*wModulus_fill             #[N/m3]

#cables Y186057 tendons made up of 3 strands with nominal diameter 15.7 mm
Ecabl= 2.1e11         # Young modulus of the steel [Pa]
area_cable=3*150e-6   #cross-section area [m2]
Fm_cable=3*279e3      #F max. cable [N]
sigmaPret=0.7*Fm_cable/area_cable      #prestressing stress [Pa]

eSize_deck= 0.5     #length of concrete elements
eSize_cabl= 1.0     #length of cable elements

# ***Actions
unifPavRoad=2.35e3  # dead uniform load on the roadway [N/m2]
unifPavSide=1.57e3  # dead uniform load on the sideways [N/m2]
linKerb=2.35e3      # [N/m]
linBarrier=1.57e3   # [N/m]

coef_tr_load=0.9
qunif1_Trafmod1=coef_tr_load*9e3    #[N/m2] Load model 1, lane 1
Qpoint1_Trafmod1=coef_tr_load*300e3/2.0 #[N]  Load model  1, lane 1
qunif2_Trafmod1=coef_tr_load*2.5e3  #[N/m2] Load model 1, rest
Qpoint2_Trafmod1=coef_tr_load*200e3/2.0 #[N]  Load model  1, lane 1



#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)

#           **** Grid model for the generation of the DECK ****

# coordinates in global X,Y,Z axes for the grid generation
xList_deck=[0,0.45,6.45,8.15]
yList_deck=[0,delta_Y+3,L_long_side_Y-delta_Y-3,L_long_side_Y]
zList_deck=[0,0.4]
#auxiliary data
lastXpos=len(xList_deck)-1
lastYpos=len(yList_deck)-1
lastZpos=len(zList_deck)-1

# grid model definition
gridDeck= gm.GridModel(prep,xList_deck,yList_deck,zList_deck)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridDeck.generatePoints()

#Displacements of the grid points in a range
# deltZ_max=L_long_side_Y*math.tan(alpha)
r= gm.IJKRange((0,0,0),(1,0,lastZpos))
gridDeck.movePointsRange(r,xc.Vector([0.0,delta_Y,delta_Y*math.tan(alpha)]))
r= gm.IJKRange((0,lastYpos,0),(1,lastYpos,lastZpos))
gridDeck.movePointsRange(r,xc.Vector([0.0,-delta_Y,(L_long_side_Y-delta_Y)*math.tan(alpha)]))

r= gm.IJKRange((0,1,0),(lastXpos,1,lastZpos))
gridDeck.movePointsRange(r,xc.Vector([0.0,0,yList_deck[1]*math.tan(alpha)]))
r= gm.IJKRange((0,2,0),(lastXpos,2,lastZpos))
gridDeck.movePointsRange(r,xc.Vector([0.0,0,yList_deck[2]*math.tan(alpha)]))

r= gm.IJKRange((2,lastYpos,0),(lastXpos,lastYpos,lastZpos))
gridDeck.movePointsRange(r,xc.Vector([0.0,0,yList_deck[lastYpos]*math.tan(alpha)]))
r= gm.IJKRange((lastXpos,0,0),(lastXpos,lastYpos,lastZpos))
gridDeck.movePointsRange(r,xc.Vector([0.0,0,delta_crossect_1]))
r= gm.IJKRange((0,0,lastZpos),(0,lastYpos,lastZpos))
gridDeck.movePointsRange(r,xc.Vector([0.0,0,0.2]))

#Ranges for surfaces
deck_rg=[gm.IJKRange((0,0,0),(lastXpos,lastYpos,0))]
curb_rg=[gm.IJKRange((0,0,0),(0,lastYpos,lastZpos)),gm.IJKRange((lastXpos,0,0),(lastXpos,lastYpos,lastZpos))]

#Surfaces generation
deck=gridDeck.genSurfMultiRegion(lstIJKRange=deck_rg,nameSet='deck')
deck.description='Deck'
curb=gridDeck.genSurfMultiRegion(lstIJKRange=curb_rg,nameSet='curb')
curb.description='Curbs'


#           **** Grid model for the generation of the PRESTRESSING CABLES ****

# coordinates in global X,Y,Z axes for the grid generation
xList_cabl=[0.1457-0.1,1.5469,3.1680,4.7891,6.4112,7.9025+0.1]
yList_cabl=[0,L_long_side_Y]
zList_cabl=[hCables]
#auxiliary data
lastXpos_cabl=len(xList_cabl)-1
lastYpos_cabl=len(yList_cabl)-1
lastZpos_cabl=len(zList_cabl)-1

# grid model definition
gridCables= gm.GridModel(prep,xList_cabl,yList_cabl,zList_cabl)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridCables.generatePoints()

#Displacements of the grid points in a range
deltZ_max=L_long_side_Y*math.tan(alpha)
for i in range(0,1):
    deltY=delta_Y
    deltZ=deltY*math.tan(alpha)
    r= gm.IJKRange((i,0,0),(i,0,lastZpos_cabl))
    gridCables.movePointsRange(r,xc.Vector([0.0,deltY,deltZ]))
    r= gm.IJKRange((i,lastYpos_cabl,0),(i,lastYpos_cabl,lastZpos_cabl))
    gridCables.movePointsRange(r,xc.Vector([0.0,-deltY,deltZ_max-deltZ]))

slope_aux=delta_Y/(xList_deck[2]-xList_deck[1])
for i in range(1,lastXpos_cabl):
    deltY=delta_Y-slope_aux*(xList_cabl[i]-xList_deck[1])
    deltZ=deltY*math.tan(alpha)
    r= gm.IJKRange((i,0,0),(i,0,lastZpos_cabl))
    gridCables.movePointsRange(r,xc.Vector([0.0,deltY,deltZ]))
    r= gm.IJKRange((i,lastYpos_cabl,0),(i,lastYpos_cabl,lastZpos_cabl))
    gridCables.movePointsRange(r,xc.Vector([0.0,-deltY,deltZ_max-deltZ]))

i=lastXpos_cabl
deltZ_global=delta_crossect_1/(xList_deck[3]-xList_deck[2])*(xList_cabl[i]-xList_deck[2])
r= gm.IJKRange((i,0,0),(i,lastYpos_cabl,lastZpos_cabl))
gridCables.movePointsRange(r,xc.Vector([0.0,0.0,deltZ_global+deltaZ_lastcable]))
r= gm.IJKRange((i,lastYpos_cabl,0),(i,lastYpos_cabl,lastZpos_cabl))
gridCables.movePointsRange(r,xc.Vector([0.0,0.0,deltZ_max+deltaZ_lastcable]))


#Lines generation
cabl_rg=gm.IJKRange((0,0,0),(lastXpos_cabl,lastYpos_cabl,0)).extractIncludedJranges()
cables=gridCables.genLinMultiRegion(lstIJKRange=cabl_rg,nameSet='cables')
cables.description='Prestressing cables'


#                         *** MATERIALS *** 
concrete=tm.MaterialData(name='concrete',E=EcConcr,nu=cpoisConcr,rho=densConcr)

# Isotropic elastic section-material appropiate for plate and shell analysis
deck_mat=tm.DeckMaterialData(name='deck_mat',thickness= deckTh,material=concrete)
deck_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
curb_mat=tm.DeckMaterialData(name='curb_mat',thickness= curbTh,material=concrete)
curb_mat.setupElasticSection(preprocessor=prep)   #creates de section-material

#Geometric sections
#rectangular sections
# from materials.sections import section_properties as sectpr
# geomSectCabl=sectpr.RectangularSection(name='geomSectCabl',b=0.01,h=0.01)

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
from materials import typical_materials

cabl_mat=typical_materials.defCableMaterial(prep, name="cabl_mat",E=Ecabl,prestress=sigmaPret,rho=0.0)


#                         ***FE model - MESH***

cabl_mesh=fem.LinSetToMesh(linSet=cables,matSect=cabl_mat,elemSize=eSize_cabl,vDirLAxZ=xc.Vector([0,0,1]),elemType='corot_truss',dimElemSpace=3)
cabl_mesh.generateMesh(prep)    # mesh this set of lines

for e in cables.elements:
    e.area=area_cable

deck_mesh=fem.SurfSetToMesh(surfSet=deck,matSect=deck_mat,elemSize=eSize_deck,elemType='ShellMITC4')
deck_mesh.generateMesh(prep)     #mesh the set of surfaces

curb_mesh=fem.SurfSetToMesh(surfSet=curb,matSect=curb_mat,elemSize=eSize_deck,elemType='ShellMITC4')
curb_mesh.generateMesh(prep)     #mesh the set of surfaces

#fem.multi_mesh(preprocessor=prep,lstMeshSets=[beamY_mesh,columnZ_mesh,found_mesh,wall_mesh])     #mesh these sets


shells=deck+curb
shells.description="deck"

roadway_rg=gm.IJKRange((1,0,0),(2,lastYpos,0))
roadway=gridDeck.getSetSurfOneRegion(ijkRange=roadway_rg,nameSet='roadway')
sideway_rg=[gm.IJKRange((0,0,0),(1,lastYpos,0)),gm.IJKRange((2,0,0),(lastXpos,lastYpos,0))]
sideway=gridDeck.getSetSurfMultiRegion(lstIJKRange=sideway_rg, nameSet='sideway')
kerb1_rg=gm.IJKRange((1,0,0),(1,lastYpos,0))
kerb1_kps=gridDeck.getSetPntRange(ijkRange=kerb1_rg,setName='kerb1_kps')
kerb1_ln=sets.get_lines_on_points(setPoints=kerb1_kps,setLinName='kerb1_ln',onlyIncluded=True)
kerb2_rg=gm.IJKRange((2,0,0),(2,lastYpos,0))
kerb2_kps=gridDeck.getSetPntRange(ijkRange=kerb2_rg,setName='kerb2_kps')
kerb2_ln=sets.get_lines_on_points(setPoints=kerb2_kps,setLinName='kerb2_ln',onlyIncluded=True)
kerbs=kerb1_ln+kerb2_ln
kerbs.name='kerbs'

barr1_rg=gm.IJKRange((0,0,lastZpos),(0,lastYpos,lastZpos))
barr1_kps=gridDeck.getSetPntRange(ijkRange=barr1_rg,setName='barr1_kps')
barr1_ln=sets.get_lines_on_points(setPoints=barr1_kps,setLinName='barr1_ln',onlyIncluded=True)
barr2_rg=gm.IJKRange((lastXpos,0,lastZpos),(lastXpos,lastYpos,lastZpos))
barr2_kps=gridDeck.getSetPntRange(ijkRange=barr2_rg,setName='barr2_kps')
barr2_ln=sets.get_lines_on_points(setPoints=barr2_kps,setLinName='barr2_ln',onlyIncluded=True)
barrs=barr1_ln+barr2_ln
barrs.name='barrs'


# Connection between cables and deck
gluedDOFs= [0,1,2,3,4,5]
deckElem=shells.elements
cablNod=cables.nodes
for n in cablNod:
    nearElem=deckElem.getNearestElement(n.getCurrentPos3d(0.0))
    modelSpace.constraints.newGlueNodeToElement(n,nearElem,xc.ID(gluedDOFs))


#                       ***BOUNDARY CONDITIONS***
#execfile('/home/ana/projects/XCmodels/Brelaz/XC_model/sets_springs.py')
execfile('/home/luis/Documents/XCmodels/Brelaz/XC_model/sets_springs.py')
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
found_wink_walls=sprbc.ElasticFoundation(wModulus=wModulus_walls,cRoz=0.002)
found_wink_walls.generateSprings(xcSet=setShortWall)
found_wink_walls.generateSprings(xcSet=setLongWall)

found_wink_fill=sprbc.ElasticFoundation(wModulus=wModulus_fill,cRoz=0.002)
found_wink_fill.generateSprings(xcSet=setInsideArea)



#                       ***ACTIONS***

#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[deck_mesh,curb_mesh], vAccel=xc.Vector( [0.0,0.0,-grav,0,0,0]))

# Uniform loads applied on shell elements
#    name:       name identifying the load
#    xcSet:     set that contains the surfaces
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)

deadLoadRoadway= loads.UniformLoadOnSurfaces(name= 'deadLoadRoadway',xcSet=roadway,loadVector=xc.Vector([0,0,-unifPavRoad,0,0,0]),refSystem='Global')
deadLoadSideway= loads.UniformLoadOnSurfaces(name= 'deadLoadSideway',xcSet=sideway,loadVector=xc.Vector([0,0,-unifPavSide,0,0,0]),refSystem='Global')

# Uniform load applied to all the lines (not necessarily defined as lines
# for latter generation of beam elements, they can be lines belonging to 
# surfaces for example) found in the xcSet
# The uniform load is introduced as point loads in the nodes
#     name:   name identifying the load
#     xcSet:  set that contains the lines
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).

deadLoadKerb=loads.UniformLoadOnLines(name='deadLoadKerb',xcSet=kerbs,loadVector=xc.Vector([0,0,-linKerb,0,0,0]))
deadLoadBarr=loads.UniformLoadOnLines(name='deadLoadKerb',xcSet=barrs,loadVector=xc.Vector([0,0,-linBarrier,0,0,0]))

# *Traffic loads
# Sets definition
poly_lane_Bern=geom.Polygon2d()
poly_lane_Bern.appendVertex(geom.Pos2d(xList_deck[1],0))
poly_lane_Bern.appendVertex(geom.Pos2d(xList_deck[1],yList_deck[lastYpos]))
poly_lane_Bern.appendVertex(geom.Pos2d(xList_deck[1]+3,yList_deck[lastYpos]))
poly_lane_Bern.appendVertex(geom.Pos2d(xList_deck[1]+3,0))
lane_Bern=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=deck,prismBase=poly_lane_Bern,prismAxis='Z',setName='lane_Bern')

poly_lane_Lausanne=geom.Polygon2d()
poly_lane_Lausanne.appendVertex(geom.Pos2d(xList_deck[1]+3,0))
poly_lane_Lausanne.appendVertex(geom.Pos2d(xList_deck[1]+3,yList_deck[lastYpos]))
poly_lane_Lausanne.appendVertex(geom.Pos2d(xList_deck[2],yList_deck[lastYpos]))
poly_lane_Lausanne.appendVertex(geom.Pos2d(xList_deck[2],0))
lane_Lausanne=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=deck,prismBase=poly_lane_Lausanne,prismAxis='Z',setName='lane_Lausanne')

rest_A=lane_Bern+sideway
rest_A.name='rest_A'
rest_B=lane_Lausanne+sideway
rest_B.name='rest_B'

poly_lane1_Acc=geom.Polygon2d()
poly_lane1_Acc.appendVertex(geom.Pos2d(xList_deck[lastXpos]-3,0))
poly_lane1_Acc.appendVertex(geom.Pos2d(xList_deck[lastXpos]-3,yList_deck[lastYpos]))
poly_lane1_Acc.appendVertex(geom.Pos2d(xList_deck[lastXpos],yList_deck[lastYpos]))
poly_lane1_Acc.appendVertex(geom.Pos2d(xList_deck[lastXpos],0))
lane1_Acc=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=deck,prismBase=poly_lane1_Acc,prismAxis='Z',setName='lane1_Acc')

poly_rest_Acc=geom.Polygon2d()
poly_rest_Acc.appendVertex(geom.Pos2d(xList_deck[1],0))
poly_rest_Acc.appendVertex(geom.Pos2d(xList_deck[1],yList_deck[lastYpos]))
poly_rest_Acc.appendVertex(geom.Pos2d(xList_deck[lastXpos]-3,yList_deck[lastYpos]))
poly_rest_Acc.appendVertex(geom.Pos2d(xList_deck[lastXpos]-3,0))
rest_Acc=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=deck,prismBase=poly_rest_Acc,prismAxis='Z',setName='rest_Acc')

q1_liveLoadA=loads.UniformLoadOnSurfaces(name= 'q1_liveLoadA',xcSet=lane_Lausanne,loadVector=xc.Vector([0,0,-qunif1_Trafmod1,0,0,0]),refSystem='Global')
q2_liveLoadA=loads.UniformLoadOnSurfaces(name= 'q2_liveLoadA',xcSet=rest_A,loadVector=xc.Vector([0,0,-qunif2_Trafmod1,0,0,0]),refSystem='Global')
q1_liveLoadB=loads.UniformLoadOnSurfaces(name= 'q1_liveLoadB',xcSet=lane_Bern,loadVector=xc.Vector([0,0,-qunif1_Trafmod1,0,0,0]),refSystem='Global')
q2_liveLoadB=loads.UniformLoadOnSurfaces(name= 'q2_liveLoadB',xcSet=rest_B,loadVector=xc.Vector([0,0,-qunif2_Trafmod1,0,0,0]),refSystem='Global')
q1_fatigueLoad=loads.UniformLoadOnSurfaces(name= 'q1_fatigueLoad',xcSet=lane_Lausanne,loadVector=xc.Vector([0,0,-qunif1_Trafmod1,0,0,0]),refSystem='Global')
q2_fatigueLoad=loads.UniformLoadOnSurfaces(name= 'q2_fatigueLoad',xcSet=rest_A,loadVector=xc.Vector([0,0,-qunif2_Trafmod1,0,0,0]),refSystem='Global')
q1_accidental=loads.UniformLoadOnSurfaces(name= 'q1_accidental',xcSet=lane1_Acc,loadVector=xc.Vector([0,0,-qunif1_Trafmod1,0,0,0]),refSystem='Global')
q2_accidental=loads.UniformLoadOnSurfaces(name= 'q2_accidental',xcSet=rest_Acc,loadVector=xc.Vector([0,0,-qunif2_Trafmod1,0,0,0]),refSystem='Global')

# Load acting on one or several nodes
#     name:       name identifying the load
#     lstNod:     list of nodes  on which the load is applied
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
def trafficPointLoads(centerTruck):
    xc=centerTruck.x
    yc=centerTruck.y
    p1=geom.Pos3d(xc-1,yc-0.6,(yc-0.6)*math.tan(alpha))
    p2=geom.Pos3d(xc+1,yc-0.6,(yc-0.6)*math.tan(alpha))
    p3=geom.Pos3d(xc-1,yc+0.6,(yc+0.6)*math.tan(alpha))
    p4=geom.Pos3d(xc+1,yc+0.6,(yc+0.6)*math.tan(alpha))
    nodLst=sets.get_lstNod_from_lst3DPos(preprocessor=prep,lst3DPos=[p1,p2,p3,p4])
    return nodLst

centTr=geom.Pos2d(xList_deck[2]-1.25,yList_deck[lastYpos]/2.0)
Q1p_liveLoadA=loads.NodalLoad(name='Q1p_liveLoadA',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-Qpoint1_Trafmod1,0,0,0]))
centTr=geom.Pos2d(xList_deck[2]-4.25,yList_deck[lastYpos]/2.0)
Q2p_liveLoadA=loads.NodalLoad(name='Q2p_liveLoadA',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-Qpoint2_Trafmod1,0,0,0]))

centTr=geom.Pos2d(xList_deck[1]+1.25,yList_deck[lastYpos]/2.0)
Q1p_liveLoadB=loads.NodalLoad(name='Q1p_liveLoadB',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-Qpoint1_Trafmod1,0,0,0]))
centTr=geom.Pos2d(xList_deck[1]+4.25,yList_deck[lastYpos]/2.0)
Q2p_liveLoadB=loads.NodalLoad(name='Q2p_liveLoadB',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-Qpoint2_Trafmod1,0,0,0]))

centTr=geom.Pos2d(xList_deck[1]+3.25,yList_deck[lastYpos]/2.0)
Q1p_fatigueLoad=loads.NodalLoad(name='Q1p_fatigueLoad',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-Qpoint1_Trafmod1,0,0,0]))
centTr=geom.Pos2d(xList_deck[1]+3-1.25,yList_deck[lastYpos]/2.0)
Q2p_fatigueLoad=loads.NodalLoad(name='Q2p_fatigueLoad',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-Qpoint2_Trafmod1,0,0,0]))

centTr=geom.Pos2d(xList_deck[3]-1.25,yList_deck[lastYpos]/2.0)
Q1p_accidental=loads.NodalLoad(name='Q1p_accidental',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-Qpoint1_Trafmod1,0,0,0]))


#    ***LOAD CASES***
GselfWeight=lcases.LoadCase(preprocessor=prep,name="GselfWeight",loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])

GdeadLoad=lcases.LoadCase(preprocessor=prep,name="GdeadLoad",loadPType="default",timeSType="constant_ts")
GdeadLoad.create()
GdeadLoad.addLstLoads([deadLoadRoadway,deadLoadSideway,deadLoadKerb,deadLoadBarr])

QliveLoadA=lcases.LoadCase(preprocessor=prep,name="QliveLoadA",loadPType="default",timeSType="constant_ts")
QliveLoadA.create()
QliveLoadA.addLstLoads([q1_liveLoadA,q2_liveLoadA,Q1p_liveLoadA,Q2p_liveLoadA])

QliveLoadB=lcases.LoadCase(preprocessor=prep,name="QliveLoadB",loadPType="default",timeSType="constant_ts")
QliveLoadB.create()
QliveLoadB.addLstLoads([q1_liveLoadB,q2_liveLoadB,Q1p_liveLoadB,Q2p_liveLoadB])

QfatigueLoad=lcases.LoadCase(preprocessor=prep,name="QfatigueLoad",loadPType="default",timeSType="constant_ts")
QfatigueLoad.create()
QfatigueLoad.addLstLoads([q1_fatigueLoad,q2_fatigueLoad,Q1p_fatigueLoad,Q2p_fatigueLoad])

Qaccidental=lcases.LoadCase(preprocessor=prep,name="Qaccidental",loadPType="default",timeSType="constant_ts")
Qaccidental.create()
Qaccidental.addLstLoads([q1_accidental,Q1p_accidental])

overallSet=prep.getSets.getSet('total')
shellsPcable=deck+curb+cables

#Load cases defined only for purposes of loads displaying
QliveLoadA_unif=lcases.LoadCase(preprocessor=prep,name="QliveLoadA_unif",loadPType="default",timeSType="constant_ts")
QliveLoadA_unif.create()
QliveLoadA_unif.addLstLoads([q1_liveLoadA,q2_liveLoadA])

QliveLoadB_unif=lcases.LoadCase(preprocessor=prep,name="QliveLoadB_unif",loadPType="default",timeSType="constant_ts")
QliveLoadB_unif.create()
QliveLoadB_unif.addLstLoads([q1_liveLoadB,q2_liveLoadB])

QfatigueLoad_unif=lcases.LoadCase(preprocessor=prep,name="QfatigueLoad_unif",loadPType="default",timeSType="constant_ts")
QfatigueLoad_unif.create()
QfatigueLoad_unif.addLstLoads([q1_fatigueLoad,q2_fatigueLoad])

Qaccidental_unif=lcases.LoadCase(preprocessor=prep,name="Qaccidental_unif",loadPType="default",timeSType="constant_ts")
Qaccidental_unif.create()
Qaccidental_unif.addLstLoads([q1_accidental])

QliveLoadA_point=lcases.LoadCase(preprocessor=prep,name="QliveLoadA_point",loadPType="default",timeSType="constant_ts")
QliveLoadA_point.create()
QliveLoadA_point.addLstLoads([Q1p_liveLoadA,Q2p_liveLoadA])

QliveLoadB_point=lcases.LoadCase(preprocessor=prep,name="QliveLoadB_point",loadPType="default",timeSType="constant_ts")
QliveLoadB_point.create()
QliveLoadB_point.addLstLoads([Q1p_liveLoadB,Q2p_liveLoadB])

QfatigueLoad_point=lcases.LoadCase(preprocessor=prep,name="QfatigueLoad_point",loadPType="default",timeSType="constant_ts")
QfatigueLoad_point.create()
QfatigueLoad_point.addLstLoads([Q1p_fatigueLoad,Q2p_fatigueLoad])

Qaccidental_point=lcases.LoadCase(preprocessor=prep,name="Qaccidental_point",loadPType="default",timeSType="constant_ts")
Qaccidental_point.create()
Qaccidental_point.addLstLoads([Q1p_accidental])

#LOAD COMBINATIONS
combContainer= cc.CombContainer()  #Container of load combinations
# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
combContainer.ULS.perm.add('ELUA', '1.35*GselfWeight+1.35*GdeadLoad+1.5*QliveLoadA')
combContainer.ULS.perm.add('ELUB', '1.35*GselfWeight+1.35*GdeadLoad+1.5*QliveLoadB')
combContainer.ULS.perm.add('A', '1.00*GselfWeight+1.00*GdeadLoad+1.00*Qaccidental')

#Fatigue.
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad')
combContainer.ULS.fatigue.add('ELUF2','1.00*GselfWeight+1.0*GdeadLoad+1.0*QfatigueLoad')

# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
#Frequent combinations.
combContainer.SLS.freq.add('ELS', '1.0*GselfWeight+1.0*GdeadLoad+0.75*QliveLoadA')

