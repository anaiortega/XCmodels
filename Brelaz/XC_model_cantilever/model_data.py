# -*- coding: utf-8 -*-

import math
import xc_base
import geom
import xc
import sys
import inspect
from materials import typical_materials as tm
from model import predefined_spaces
from model.sets import sets_mng
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc
import os

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

projectDirs= cfg.projectDirTree

cantileverWidth= 2.5
cantileverLength= 2.65
deckTh=0.25 #Deck thickness [m]

FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor
modelSpace= predefined_spaces.StructuralMechanics3D(prep.getNodeHandler)

points= prep.getMultiBlockTopology.getPoints
pt1= points.newPntFromPos3d(geom.Pos3d(0.0,0.0,0.0))
pt2a= points.newPntFromPos3d(geom.Pos3d(0.0,cantileverWidth,0.0))
pt2b= points.newPntFromPos3d(geom.Pos3d(0.0,cantileverWidth,0.0))
pt3a= points.newPntFromPos3d(geom.Pos3d(0.0,2*cantileverWidth,0.0))
pt3b= points.newPntFromPos3d(geom.Pos3d(0.0,2*cantileverWidth,0.0))
pt4= points.newPntFromPos3d(geom.Pos3d(0.0,3*cantileverWidth,0.0))
pt5= points.newPntFromPos3d(geom.Pos3d(cantileverLength,0.0,0.0))
pt6a= points.newPntFromPos3d(geom.Pos3d(cantileverLength,cantileverWidth,0.0))
pt6b= points.newPntFromPos3d(geom.Pos3d(cantileverLength,cantileverWidth,0.0))
pt7a= points.newPntFromPos3d(geom.Pos3d(cantileverLength,2*cantileverWidth,0.0))
pt7b= points.newPntFromPos3d(geom.Pos3d(cantileverLength,2*cantileverWidth,0.0))
pt8= points.newPntFromPos3d(geom.Pos3d(cantileverLength,3*cantileverWidth,0.0))

surfaces= prep.getMultiBlockTopology.getSurfaces
s1= surfaces.newQuadSurfacePts(pt1.tag,pt5.tag,pt6a.tag,pt2a.tag)
s2= surfaces.newQuadSurfacePts(pt2b.tag,pt6b.tag,pt7a.tag,pt3a.tag)
s3= surfaces.newQuadSurfacePts(pt3b.tag,pt7b.tag,pt8.tag,pt4.tag)

# **** Mesh parameters

# *** Materials *** 
fcmConcr=50e6
EcConcr=8500*(fcmConcr/1e6)**(1/3.0)*1e6
cpoisConcr=0.2                #Poisson's coefficient of concrete
densConcr= 2500               #specific mass of concrete (kg/m3)
concrete=tm.MaterialData(name='concrete',E=EcConcr,nu=cpoisConcr,rho=densConcr)

deckMat= tm.defElasticMembranePlateSection(prep, "deckMat",EcConcr,cpoisConcr,0.0,deckTh)

# *** Meshing ***
seedElemHandler= prep.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "deckMat"
elem= seedElemHandler.newElement("ShellMITC4",xc.ID([0,0,0,0]))

surfaces= [s1,s2,s3]

for s in surfaces:
    s.setElemSizeIJ(0.25,0.25)
    s.genMesh(xc.meshDir.I)

# *** Constraints ***
cl1= prep.getMultiBlockTopology.getLineWithEndPoints(pt1.tag,pt2a.tag)
cl2= prep.getMultiBlockTopology.getLineWithEndPoints(pt2b.tag,pt3a.tag)
cl3= prep.getMultiBlockTopology.getLineWithEndPoints(pt3b.tag,pt4.tag)
constrainedLines= [cl1,cl2,cl3]

for l in constrainedLines:
  for i in l.getNodeTags():
    modelSpace.fixNode000_F00(i)

wl1a= prep.getMultiBlockTopology.getLineWithEndPoints(pt2a.tag,pt6a.tag)    
wl1b= prep.getMultiBlockTopology.getLineWithEndPoints(pt2b.tag,pt6b.tag)    
wl2a= prep.getMultiBlockTopology.getLineWithEndPoints(pt3a.tag,pt7a.tag)    
wl2b= prep.getMultiBlockTopology.getLineWithEndPoints(pt3b.tag,pt7b.tag)    
lines2Glue= [(wl1a,wl1b),(wl2a,wl2b)]
gluedDOFs= xc.ID([2]) #Degrees of freedom to "glue".

for pair in lines2Glue:
  nodSet0= pair[0].nodes
  nodSet1= pair[1].nodes
  #print nodSet0, nodSet1
  for n0 in nodSet0:
    pos0= n0.getInitialPos3d #Position of first node.
    n1= pair[1].getNearestNode(pos0) #Second node.
    pos1= n1.getInitialPos3d
    d= pos1.dist(pos0) #Distance between nodes.
    if d<0.001:
      glue= prep.getBoundaryCondHandler.newEqualDOF(n0.tag,n1.tag,gluedDOFs)

# *** Sets **
overallSet= prep.getSets.getSet('total')
shells= overallSet

roadwayLimit= 0.95
roadway= prep.getSets.defSet('roadway')
sideway= prep.getSets.defSet('sideway')
for e in overallSet.elements:
    pos= e.getPosCentroid(True)
    if(pos.x<roadwayLimit):
      roadway.elements.append(e)
    else:
      sideway.elements.append(e)

#                       ***ACTIONS***
unifPavRoad=2.35e3  # dead uniform load on the roadway [N/m2]
unifPavSide=1.57e3  # dead uniform load on the sideways [N/m2]
linKerb=2.35e3      # linear uniform load on kerbs [N/m]
linBarrier=1.57e3   # linear uniform load due to barrier weight [N/m]

coef_tr_load=0.9
qunif1_Trafmod1=coef_tr_load*9e3    #[N/m2] Load model 1, lane 1
Qpoint1_Trafmod1=coef_tr_load*300e3/2.0 #[N]  Load model  1, lane 1
qunif2_Trafmod1=coef_tr_load*2.5e3  #[N/m2] Load model 1, rest
Qpoint2_Trafmod1=coef_tr_load*200e3/2.0 #[N]  Load model  1, lane 1

#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
overallSet.elemType= 'ShellMITC4'
selfWeight=loads.UniformLoadOnSurfaces(name='selfWeight', xcSet= overallSet, loadVector=xc.Vector( [0.0,0.0,-grav*0.25*2500,0,0,0]))

# Uniform loads applied on shell elements
#    name:       name identifying the load
#    xcSet:     set that contains the surfaces
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)
roadway.elemType= 'ShellMITC4'
deadLoadRoadway= loads.UniformLoadOnSurfaces(name= 'deadLoadRoadway',xcSet=roadway,loadVector=xc.Vector([0,0,-unifPavRoad,0,0,0]),refSystem='Global')
sideway.elemType= 'ShellMITC4'
deadLoadSideway= loads.UniformLoadOnSurfaces(name= 'deadLoadSideway',xcSet=sideway,loadVector=xc.Vector([0,0,-unifPavSide,0,0,0]),refSystem='Global')

q1_liveLoadA=loads.UniformLoadOnSurfaces(name= 'q1_liveLoadA',xcSet=roadway,loadVector=xc.Vector([0,0,-qunif1_Trafmod1,0,0,0]),refSystem='Global')
q2_liveLoadA=loads.UniformLoadOnSurfaces(name= 'q2_liveLoadA',xcSet=sideway,loadVector=xc.Vector([0,0,-qunif2_Trafmod1,0,0,0]),refSystem='Global')
q1_fatigueLoad=loads.UniformLoadOnSurfaces(name= 'q1_fatigueLoad',xcSet=roadway,loadVector=xc.Vector([0,0,-qunif1_Trafmod1,0,0,0]),refSystem='Global')
#q2_fatigueLoad=loads.UniformLoadOnSurfaces(name= 'q2_fatigueLoad',xcSet=sideway,loadVector=xc.Vector([0,0,-qunif2_Trafmod1,0,0,0]),refSystem='Global')
#q1_accidental=loads.UniformLoadOnSurfaces(name= 'q1_accidental',xcSet=lane1_Acc,loadVector=xc.Vector([0,0,-qunif1_Trafmod1,0,0,0]),refSystem='Global')
#q2_accidental=loads.UniformLoadOnSurfaces(name= 'q2_accidental',xcSet=rest_Acc,loadVector=xc.Vector([0,0,-qunif2_Trafmod1,0,0,0]),refSystem='Global')

# Load acting on one or several nodes
#     name:       name identifying the load
#     lstNod:     list of nodes  on which the load is applied
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
def trafficPointLoads(centerTruck):
    xc=centerTruck.x
    yc=centerTruck.y
    #p1=geom.Pos3d(xc-1,yc-0.6,0.0)
    p2=geom.Pos3d(xc+1,yc-0.6,0.0)
    #p3=geom.Pos3d(xc-1,yc+0.6,0.0)
    p4=geom.Pos3d(xc+1,yc+0.6,0.0)
    nodLst=sets_mng.get_lstNod_from_lst3DPos(preprocessor=prep,lst3DPos=[p2,p4])
    return nodLst

centTr= geom.Pos2d(0.5,1.5*cantileverWidth)
Q1p_liveLoadA=loads.NodalLoad(name='Q1p_liveLoadA',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-Qpoint1_Trafmod1,0,0,0]))

centTr=geom.Pos2d(2.4-0.2,1.5*cantileverWidth)
Q1p_accidental=loads.NodalLoad(name='Q1p_accidental',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-Qpoint1_Trafmod1,0,0,0]))

#    ***LOAD CASES***
GselfWeight=lcases.LoadCase(preprocessor=prep,name="GselfWeight",loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])

GdeadLoad=lcases.LoadCase(preprocessor=prep,name="GdeadLoad",loadPType="default",timeSType="constant_ts")
GdeadLoad.create()
GdeadLoad.addLstLoads([deadLoadRoadway,deadLoadSideway])

QliveLoadA=lcases.LoadCase(preprocessor=prep,name="QliveLoadA",loadPType="default",timeSType="constant_ts")
QliveLoadA.create()
QliveLoadA.addLstLoads([q1_liveLoadA,q2_liveLoadA,Q1p_liveLoadA])

# QfatigueLoad=lcases.LoadCase(preprocessor=prep,name="QfatigueLoad",loadPType="default",timeSType="constant_ts")
# QfatigueLoad.create()
# QfatigueLoad.addLstLoads([q1_fatigueLoad,Q1p_fatigueLoad])

Qaccidental=lcases.LoadCase(preprocessor=prep,name="Qaccidental",loadPType="default",timeSType="constant_ts")
Qaccidental.create()
Qaccidental.addLstLoads([Q1p_accidental])

#Load cases defined only for purposes of loads displaying
QliveLoadA_unif=lcases.LoadCase(preprocessor=prep,name="QliveLoadA_unif",loadPType="default",timeSType="constant_ts")
QliveLoadA_unif.create()
QliveLoadA_unif.addLstLoads([q1_liveLoadA,q2_liveLoadA])

QliveLoadA_point=lcases.LoadCase(preprocessor=prep,name="QliveLoadA_point",loadPType="default",timeSType="constant_ts")
QliveLoadA_point.create()
QliveLoadA_point.addLstLoads([Q1p_liveLoadA])

# QfatigueLoad_point=lcases.LoadCase(preprocessor=prep,name="QfatigueLoad_point",loadPType="default",timeSType="constant_ts")
# QfatigueLoad_point.create()
# QfatigueLoad_point.addLstLoads([Q1p_fatigueLoad,Q2p_fatigueLoad])

Qaccidental_point=lcases.LoadCase(preprocessor=prep,name="Qaccidental_point",loadPType="default",timeSType="constant_ts")
Qaccidental_point.create()
Qaccidental_point.addLstLoads([Q1p_accidental])

#LOAD COMBINATIONS
combContainer= cc.CombContainer()  #Container of load combinations
# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
#Characteristic combinations.
combContainer.SLS.rare.add('ELSR01', '1.0*GselfWeight+1.0*GdeadLoad+1.0*QliveLoadA')

#Frequent combinations.
combContainer.SLS.freq.add('ELSF01', '1.0*GselfWeight+1.0*GdeadLoad+0.75*QliveLoadA')
#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP01', '1.0*GselfWeight+1.0*GdeadLoad')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELUA01', '1.35*GselfWeight+1.35*GdeadLoad+1.5*QliveLoadA')
combContainer.ULS.perm.add('ELUA02', '0.80*GselfWeight+0.80*GdeadLoad+1.5*QliveLoadA')
#accidental
combContainer.ULS.perm.add('A', '1.00*GselfWeight+1.00*GdeadLoad+1.00*Qaccidental')

#Fatigue.
# Combinations' names must be:
#        - ELUF0: unloaded structure (permanent loads)
#        - ELUF1: fatigue load in position 1.
# combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*GdeadLoad')
# combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*QfatigueLoad')


