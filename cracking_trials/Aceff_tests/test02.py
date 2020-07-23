# -*- coding: utf-8 -*-


import xc_base
import geom
import xc
import math
from solution import predefined_solutions
from model import predefined_spaces
from materials.ehe import EHE_materials
from materials import concrete_base
from materials import typical_materials
from materials.sections.fiber_section import fiber_sets
from materials.sections.fiber_section import section_report 
import matplotlib.pyplot as plt
import numpy as np
from materials.ec2 import EC2_limit_state_checking
from misc import scc3d_testing_bench

#Data test 1
F=[ 7413.84526556 , 30248.8859239 , 43030.9860664 , 0.0 , 5782.47109466 , 9.09494701773e-13]
'''

#Cases that failed
#case 2 (Aceff returns 0 in the working model and a small value here)
F=[-10890.5704872 , -6230.1906486 , -3710.81869647 , 0.0 , 2410.0264365 , 5.68434188608e-13]
#case 3 (can't compute effective area )
#compressions occur in the bottom face and are very small
F=[-9166.22230203 , -6183.38966648 , -5477.37888812 , 0.0 , 1934.15531078 , 5.68434188608e-14]
#case 4 (idem as case 3)
F=[-6017.2868226 , -7191.71237352 , -6431.70178765 , 0.0 , 1423.15428553 , 3.90798504668e-13]
#case 5
F=[-3166.64616961 , -7305.18567331 , -4954.35102143 , 0.0 , 888.917037435 , -7.1054273576e-14 
'''

#Simple cases
#Pure compression: can't compute effective area concrete01=concrete02
F=[-25e6*0.2,0,0,0,0,0]

#Bending moment + (compression in bottom face): concrete01=concrete02
F=[0,0,0,0,300e6*6*math.pi*0.012**2/4.*0.12,0]
#Bending moment -(compression in top face): concrete01=concrete02
F=[0,0,0,0,-300e6*6*math.pi*0.012**2/4.*0.12,0]

#Pure tension: concrete01=concrete02
F=[25e6*0.2/10,0,0,0,0,0]


# Cases that give as a result Aceff=0 (in the working model, not in this test)
F=[-10890.5704872 , -6230.1906486 , -3710.81869647 , 0.0 , 2410.0264365 , 5.68434188608e-13]
F=[-12990.3997119 , -7048.04701811 , 526.81077107 , 0.0 , 2749.60838514 , -1.70530256582e-13]

# Cases that can't be computed
F=[-9166.22230203 , -6183.38966648 , -5477.37888812 , 0.0 , 1934.15531078 , 5.68434188608e-14]

F=[3166.64616961 , 7305.18567331 , 4954.35102143 , 0.0 , -888.917037435 , -7.1054273576e-14]

# Cases that result in a too high value
F=[-7981.06400767 , -5034.54365261 , -4536.52615259 , 0.0 , -2018.27448237 , 1.84741111298e-13]

#Data from the experiment
width=1.0     #width (cross-section coordinate Y)
depth=0.2     #depth (cross-section coordinate Z)
f_ck=30e6      #concrete characteristic strength [Pa] (concrete HA30 adopted)

fiBottom=16e-3
fiTop=12e-3

cover=0.035     #cover


#Other data
nDivIJ= 20  #number of cells (fibers) in the IJ direction (cross-section coordinate Y)
nDivJK= 20  #number of cells (fibers) in the JK direction (cross-section coordinate Z)



l= 1e-7     # Distance between nodes


# Model definition
problem=xc.FEProblem()              #necesary to create this instance of
                                     #the class xc.FEProblem()
preprocessor=problem.getPreprocessor
nodes= preprocessor.getNodeHandler     #nodes container

'''
nodes.defaultTag= 1 #First node number.
nod= nodes.newNodeXYZ(1.0,0,0)     #node 1 defined by its (x,y,z) global coordinates
nod= nodes.newNodeXYZ(1.0+l,0,0)   #node 2 defined by its (x,y,z) global coordinates
'''
# Materials definition
concrete=EHE_materials.HA30 #concrete according to EHE fck=30 MPa
concrete.initTensStiff='y'
concrDiagram=concrete.defDiagK(preprocessor) #Definition of concrete stress-strain diagram in XC.

#Reinforcing steel.
rfSteel=EHE_materials.B500S #reinforcing steel according to EHE fyk=500 MPa
steelDiagram= rfSteel.defDiagK(preprocessor) #Definition of steel stress-strain diagram in XC. 

# Section geometry (rectangular 0.3x0.5, 20x20 cells)
geomSectFibers= preprocessor.getMaterialHandler.newSectionGeometry("geomSectFibers")
y1= width/2.0
z1= depth/2.0
#concrete region
regiones= geomSectFibers.getRegions
concrSect= regiones.newQuadRegion(concrete.nmbDiagK)
concrSect.nDivIJ= nDivIJ
concrSect.nDivJK= nDivJK
concrSect.pMin= geom.Pos2d(-y1,-z1)
concrSect.pMax= geom.Pos2d(+y1,+z1)

#reinforcement layers
reinforcement= geomSectFibers.getReinfLayers
#bottom layer (positive bending)
reinfBottLayer= reinforcement.newStraightReinfLayer(rfSteel.nmbDiagK) #Steel stress-strain diagram to use.
reinfBottLayer.numReinfBars= 6
reinfBottLayer.barArea= math.pi*fiBottom**2/4.0
yBotL=(width-2*cover-fiBottom)/2.0
zBotL=-depth/2.0+cover+fiBottom/2.0
reinfBottLayer.p1= geom.Pos2d(-yBotL,zBotL) # center point position of the starting rebar
reinfBottLayer.p2= geom.Pos2d(yBotL,zBotL) # center point position of the starting rebar
#top layer (negative bending)
reinfTopLayer= reinforcement.newStraightReinfLayer(rfSteel.nmbDiagK) #Steel stress-strain diagram to use.
reinfTopLayer.numReinfBars= 6
reinfTopLayer.barArea= math.pi*fiTop**2/4.0
yTopL=(width-2*cover-fiTop)/2.0
zTopL=depth/2.0-cover-fiTop/2.0
reinfTopLayer.p1= geom.Pos2d(-yTopL,zTopL) # center point position of the starting rebar
reinfTopLayer.p2= geom.Pos2d(yTopL,zTopL) # center point position of the starting rebar

#Section material 
#it is a generic section created to be assigned to the elements specified
#its stress and strain state is neutral (if we ask this section for stress or strain
#values the result is always 0)
respT= typical_materials.defElasticMaterial(preprocessor, "respT",1e10) # Torsion response.
respVy= typical_materials.defElasticMaterial(preprocessor, "respVy",1e6) # Shear response in y direction.
respVz= typical_materials.defElasticMaterial(preprocessor, "respVz",1e3) # Shear response in y direction.

materialHandler= preprocessor.getMaterialHandler
sctFibers= materialHandler.newMaterial("fiberSectionShear3d","sctFibers")
fiberSectionRepr= sctFibers.getFiberSectionRepr()
fiberSectionRepr.setGeomNamed("geomSectFibers")
sctFibers.setupFibers()
sctFibers.setRespVyByName("respVy")
sctFibers.setRespVzByName("respVz")
sctFibers.setRespTByName("respT")
scc3d_testing_bench.sectionModel(preprocessor, "sctFibers")

# #report of the section material
# sectParam=section_report.SectionInfo(preprocessor=preprocessor,sectName='example_7.3_EC2W',sectDescr='Test example 7.3 EC2 Worked examples. Section definition',concrete=concrete,rfSteel=rfSteel,concrDiag=concrDiagram,rfStDiag=steelDiagram,geomSection=geomSectFibers,width=width,depth=depth) #Obtains section parameters for report



# Elements definition
'''
elements= preprocessor.getElementHandler
elements.defaultMaterial='sctFibers'
elements.dimElem= 3 # Dimension of element space
elements.defaultTag= 1
elem= elements.newElement("ZeroLengthSection",xc.ID([1,2]))
'''
# Constraints
modelSpace= predefined_spaces.getStructuralMechanics3DSpace(preprocessor) #Defines the dimension of nodes  three coordinates (x,y,z) and six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)
constraints= preprocessor.getBoundaryCondHandler      #constraints container
modelSpace.fixNode000_000(1)

# Loads definition
cargas= preprocessor.getLoadHandler   #loads container

casos= cargas.getLoadPatterns

#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"
#Load case definition
lp0= casos.newLoadPattern("default","0")
pointLoad=xc.Vector(F)  

lp0.newNodalLoad(2,pointLoad)    #applies the point load on node 2 

#We add the load case to domain.
casos.addToDomain("0")           #reads load pattern "0" and adds it to the domain

# Solve
#analysis= predefined_solutions.plain_static_modified_newton(problem)
analysis= predefined_solutions.plain_static_modified_newton(problem)
analOk= analysis.analyze(1)
#analysis= predefined_solutions.plain_newton_raphson(problem)  ##!!!DOESN'T WORK WITH concrete02
#analOk= analysis.analyze(10)


#printing results
nodes= preprocessor.getNodeHandler
nodes.calculateNodalReactions(True,1e-6)

elements= preprocessor.getElementHandler
ele1= elements.getElement(1)
#section of element 1: it's the copy of the material section 'sctFibers' assigned
#to element 1 and specific of this element. It has the tensional state of the element
R=ele1.getResistingForce()
print 'Resisting force: [', R[0] , ',', R[1] , ',', R[2] , ',', R[3] , ',', R[4] , ',', R[5], ',',R[6],']'
sccEl1= ele1.getSection()         
fibersSccEl1= sccEl1.getFibers()

#Creation of two separate sets of fibers: concrete and reinforcement steel 
setsRCEl1= fiber_sets.fiberSectionSetupRCSets(scc=sccEl1,concrMatTag=concrete.matTagK,concrSetName="concrSetFbEl1",reinfMatTag=rfSteel.matTagK,reinfSetName="reinfSetFbEl1")
setsRCEl1.reselTensionFibers(scc=sccEl1,tensionFibersSetName='tensSetFb')
x= sccEl1.getNeutralAxisDepth()
d=sccEl1.getEffectiveDepth()
h=sccEl1.getLeverArm()
print 'x= ', x, 'd= ',d, 'h= ', h

#EHE calculation
hceff_EHE=min(h+x,h/4.0)
print 'hceff_EHE= ',hceff_EHE
Aceff_EHE_gross=sccEl1.getGrossEffectiveConcreteArea(hceff_EHE)
print 'Aceff_EHE_gross= ', Aceff_EHE_gross
Aceff_EHE_net=sccEl1.getNetEffectiveConcreteArea(hceff_EHE,'tensSetFb',15.0)
print 'Aceff_EHE_net= ', Aceff_EHE_net

#EC2 calculation
hceff_EC2=min(2.5*(h-d),(h+x)/3.0,h/2.0)
print 'hceff_EC2= ',hceff_EC2
Aceff_EC2_gross=sccEl1.getGrossEffectiveConcreteArea(hceff_EC2)
print 'Aceff_EC2_gross= ', Aceff_EC2_gross
Aceff_EC2_net=sccEl1.getNetEffectiveConcreteArea(hceff_EC2,'tensSetFb',15.0)
print 'Aceff_EC2_net= ', Aceff_EC2_net


###  FIGURES & REPORTS
# #report concrete material
from postprocess.reports import graph_material
import matplotlib.pyplot as plt

'''
stressStrainDiag=graph_material.UniaxialMaterialDiagramGraphic(epsMin=concrete.epsilonU(),epsMax=-concrete.epsilonU(),title='concrete02')
# strain=stressStrainDiag.getStrains()
# stress=stressStrainDiag.getStresses(diag=concrDiagram)
stressStrainDiag.setupGraphic(plt=plt,materialDiagram=concrDiagram)
stressStrainDiag.show(plt)

for f in setsRCEl1.concrFibers.fSet:
    print 'y= ', f.getLocY(), 'z= ',f.getLocZ(), 'stress =', f.getForce()/f.getArea()*1e-6, 'strain= ',f.getStrain()
'''

# #plot cross-section strains and stresses 

from postprocess import utils_display
# '''
#   fiberSet: set of fibers to be represented
#   title:    general title for the graphic
#   fileName: name of the graphic file (defaults to None: no file generated)
#   nContours: number of contours to be generated (defaults to 100). If 
#         nContours=0 or nContours=None, then each fiber is represented with a
#         colored circle.
#   
# ''' 
#utils_display.plotStressStrainFibSet(fiberSet=fibersSccEl1,title='cross-section fibers',fileName=None,nContours=None)
utils_display.plotStressStrainFibSet(fiberSet=setsRCEl1.concrFibers.fSet,title='cross-section concrete fibers',fileName=None,nContours=None,pointSize=50)
utils_display.plotStressStrainFibSet(fiberSet=setsRCEl1.reinfFibers.fSet,title='cross-section reinforcement fibers',fileName=None,nContours=None,pointSize=100)

    
