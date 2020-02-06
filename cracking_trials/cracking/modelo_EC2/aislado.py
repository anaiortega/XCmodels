# -*- coding: utf-8 -*-

__author__= "Ana Ortega (AO_O) "
__copyright__= "Copyright 2016, AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "ana.ortega@ciccp.es "

''' Evaluation of crack amplitude according to EC2 in rectangular RC 
sections. 
It imports the geometric, material and load data from a file
'''

import xc_base
import geom
import xc
import math
from solution import predefined_solutions
from model import predefined_spaces
from materials.ec2 import EC2_materials
from materials import concrete_base
from materials import typical_materials
from materials.sections.fiber_section import fiber_sets
from materials.sections.fiber_section import sectionReport 
import matplotlib.pyplot as plt
import numpy as np
from materials.ec2 import EC2_limit_state_checking

#execfile('data_sect03.py')
#execfile('data_sect04.py')
execfile('data_sect05.py')
#execfile('data_sect06.py')






# Model definition
problem=xc.FEProblem()              #necesary to create this instance of
                                     #the class xc.FEProblem()
preprocessor=problem.getPreprocessor
nodes= preprocessor.getNodeHandler     #nodes container
modelSpace= predefined_spaces.StructuralMechanics3D(nodes)  #Defines the dimension of nodes  three coordinates (x,y,z) and six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)


nodes.defaultTag= 1 #First node number.
nod= nodes.newNodeXYZ(1.0,0,0)     #node 1 defined by its (x,y,z) global coordinates
nod= nodes.newNodeXYZ(1.0+l,0,0)   #node 2 defined by its (x,y,z) global coordinates

# Materials definition
concrete=EC2_materials.EC2Concrete("C33",-33e6,1.5) #concrete according to EC2 fck=33 MPa

#Reinforcing steel.
rfSteel=EC2_materials.S450C #reinforcing steel according to EC2 fyk=450 MPa
steelDiagram= rfSteel.defDiagK(preprocessor) #Definition of steel stress-strain diagram in XC. 

'''
ro_s_eff=0.0643875431034      #effective ratio of reinforcement
paramTS=concrete_base.paramTensStiffness(concrMat=concrete,reinfMat=rfSteel,reinfRatio=ro_s_eff,diagType='K')
concrete.tensionStiffparam=paramTS           #parameters for tension stiffening are assigned to concrete
#concrDiagram=concrete.defDiagK(preprocessor) #Definition of concrete stress-strain diagram in XC.
concrete.tensionStiffparam=paramTS           #parameters for tension stiffening
ftdiag=concrete.tensionStiffparam.pointOnsetCracking()['ft']      #stress at the adopted point for concrete onset cracking
Etsdiag=abs(concrete.tensionStiffparam.regresLine()['slope'])
'''
ftdiag=concrete.fctk()/10.
epsct0=ftdiag/concrete.E0()
#Ets0=ft0/(19*epsct0)     #Schnobrich: epscu=20*epsct0
Etsdiag=ftdiag/(5*epsct0)

concrete.materialDiagramK=typical_materials.defConcrete02(preprocessor=preprocessor,name=concrete.nmbDiagK,epsc0=concrete.epsilon0(),fpc=concrete.fmaxK(),fpcu=0.85*concrete.fmaxK(),epscu=concrete.epsilonU(),ratioSlope=0.1,ft=ftdiag,Ets=Etsdiag)
concrete.matTagK=concrete.materialDiagramK.tag


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
reinfBottLayer.numReinfBars= nmbBarsBott
reinfBottLayer.barArea= math.pi*fiBott**2/4.0
yBotL=(width-2*cover-fiBott)/2.0
zBotL=-depth/2.0+cover+fiBott/2.0
reinfBottLayer.p1= geom.Pos2d(-yBotL,zBotL) # center point position of the starting rebar
reinfBottLayer.p2= geom.Pos2d(yBotL,zBotL) # center point position of the starting rebar

#top layer (negative bending)
if nmbBarsTop > 0:
    reinfTopLayer= reinforcement.newStraightReinfLayer(rfSteel.nmbDiagK) #Steel stress-strain diagram to use.
    reinfTopLayer.numReinfBars= nmbBarsTop
    reinfTopLayer.barArea= math.pi*fiTop**2/4.0
    yTopL=(width-2*cover-fiTop)/2.0
    zTopL=depth/2.0-cover-fiTop/2.0
    reinfTopLayer.p1= geom.Pos2d(-yTopL,zTopL) # center point position of the starting rebar
    reinfTopLayer.p2= geom.Pos2d(yTopL,zTopL) # center point position of the starting rebar

#Section material 
#it is a generic section created to be assigned to the elements specified
#its stress and strain state is neutral (if we ask this section for stress or strain
#values the result is always 0)
materialHandler= preprocessor.getMaterialHandler
sctFibers= materialHandler.newMaterial("fiber_section_3d","sctFibers")

fiberSectionRepr= sctFibers.getFiberSectionRepr()
fiberSectionRepr.setGeomNamed("geomSectFibers")
sctFibers.setupFibers()


# #report of the section material
# sectParam=sectionReport.SectionInfo(preprocessor=preprocessor,sectName='example_7.3_EC2W',sectDescr='Test example 7.3 EC2 Worked examples. Section definition',concrete=concrete,rfSteel=rfSteel,concrDiag=concrDiagram,rfStDiag=steelDiagram,geomSection=geomSectFibers,width=width,depth=depth) #Obtains section parameters for report



# Elements definition
elements= preprocessor.getElementHandler
elements.defaultMaterial='sctFibers'
elements.dimElem= 1 # Dimension of element space
elements.defaultTag= 1
elem= elements.newElement("ZeroLengthSection",xc.ID([1,2]))

# Constraints
constraints= preprocessor.getBoundaryCondHandler      #constraints container
modelSpace.fixNode000_000(1)
modelSpace.fixNodeF00_0FF(2)
# Loads definition
cargas= preprocessor.getLoadHandler   #loads container

casos= cargas.getLoadPatterns

#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"
#Load case definition
lp0= casos.newLoadPattern("default","0")
pointLoad=xc.Vector([N_x,0,0,0,M_y,M_z])  

lp0.newNodalLoad(2,pointLoad)    #applies the point load on node 2 

#We add the load case to domain.
casos.addToDomain("0")           #reads load pattern "0" and adds it to the domain

# Solve
analisis= predefined_solutions.simple_static_modified_newton(problem)
analOk= analisis.analyze(1)

#printing results
nodes= preprocessor.getNodeHandler
nodes.calculateNodalReactions(True,1e-6)


elements= preprocessor.getElementHandler
ele1= elements.getElement(1)
#section of element 1: it's the copy of the material section 'sctFibers' 
#assigned to element 1 and specific of this element. It has the tensional
#state of the element
sccEl1= ele1.getSection()          #fiber section     
fibersSccEl1= sccEl1.getFibers()   #fiber container

#Creation of two separate sets of fibers: concrete and reinforcement steel 
setsRCEl1= fiber_sets.fiberSectionSetupRCSets(scc=sccEl1,concrMatTag=concrete.matTagK,concrSetName="concrSetFbEl1",reinfMatTag=rfSteel.matTagK,reinfSetName="reinfSetFbEl1")
# we can access to the created sets by calling:
#  setsRCEl1.concrFibers   or setsRCEl1.reinfFibers
#We create another set with the fibers in tension:
setsRCEl1.reselTensionFibers(scc=sccEl1,tensionFibersSetName='tensSetFbEl1')
# Now we can access this set by calling:
#   setsRCEl1.tensionFibers

concrSetFbEl1=sccEl1.getFiberSets()["concrSetFbEl1"]
reinfSetFbEl1=sccEl1.getFiberSets()["reinfSetFbEl1"]
concrFibers=[f for f in concrSetFbEl1]

x= sccEl1.getNeutralAxisDepth()
d=sccEl1.getEffectiveDepth()
h=sccEl1.getLeverArm()

print 'x= ', x, '   d= ', d, '   h= ', h

As=setsRCEl1.tensionFibers.getArea(1.0)

#maximum depth of the effective area:
hceff=EC2_limit_state_checking.h_c_eff(depth_tot=h,depht_eff=abs(d),depth_neutral_axis=abs(x))

print 'depth of the effective area: ',hceff,' m'
#Aceff_EHE_gross=sccEl1.getGrossEffectiveConcreteArea(hceff)
Aceff=sccEl1.getNetEffectiveConcreteArea(hceff,'reinfSetFbEl1',15.0)
print 'effective concrete tension area: ',Aceff,' m2'
print 'As=', As
ro_s_eff=As/Aceff      #effective ratio of reinforcement
print 'effective ratio of reinforcement=', ro_s_eff
#maximum crack spacing
srmax=EC2_limit_state_checking.s_r_max(k1=0.8,k2=0.5,k3=3.4,k4=0.425,cover=cover,fiReinf=fiBott,ro_eff=ro_s_eff)
print 'maximum crack spacing: ',srmax,' m'
#mean strain in the concrete between cracks
eps_cm=concrete.fctm()/concrete.E0()/2.0
#mean strain in the reinforcemen taking into account the effects of tension stiffening
fReinfMax= setsRCEl1.reinfFibers.getFiberWithMaxStrain()
epsSMax= fReinfMax.getMaterial().getStrain() # maximum strain among steel fibers
eps_sm=epsSMax
#crack withs
w_k=srmax*(eps_sm-eps_cm)
print 'crack widths: ',w_k*1e3, ' mm'

dom=preprocessor.getDomain


#step 2: only revert to start and new run
print 'step 2'
execfile('calc_fis.py')
quit()
sccEl1.revertToStart()
dom=preprocessor.getDomain
dom.revertToStart()

analisis= predefined_solutions.simple_static_modified_newton(problem)
analOk= analisis.analyze(1)
x= sccEl1.getNeutralAxisDepth()
d=sccEl1.getEffectiveDepth()
h=sccEl1.getLeverArm()

print 'x= ', x, '   d= ', d, '   h= ', h

As=setsRCEl1.tensionFibers.getArea(1.0)

#maximum depth of the effective area:
hceff=EC2_limit_state_checking.h_c_eff(depth_tot=h,depht_eff=abs(d),depth_neutral_axis=abs(x))

print 'depth of the effective area: ',hceff,' m'
#Aceff_EHE_gross=sccEl1.getGrossEffectiveConcreteArea(hceff)
Aceff=sccEl1.getNetEffectiveConcreteArea(hceff,'reinfSetFbEl1',15.0)
print 'effective concrete tension area: ',Aceff,' m2'
print 'As=', As
ro_s_eff=As/Aceff      #effective ratio of reinforcement
print 'effective ratio of reinforcement=', ro_s_eff
#maximum crack spacing
srmax=EC2_limit_state_checking.s_r_max(k1=0.8,k2=0.5,k3=3.4,k4=0.425,cover=cover,fiReinf=fiBott,ro_eff=ro_s_eff)
print 'maximum crack spacing: ',srmax,' m'
#mean strain in the concrete between cracks
eps_cm=concrete.fctm()/concrete.E0()/2.0
#mean strain in the reinforcemen taking into account the effects of tension stiffening
fReinfMax= setsRCEl1.reinfFibers.getFiberWithMaxStrain()
epsSMax= fReinfMax.getMaterial().getStrain() # maximum strain among steel fibers
eps_sm=epsSMax
#crack withs
w_k=srmax*(eps_sm-eps_cm)
print 'crack widths: ',w_k*1e3, ' mm'
ro_s_eff=0.0643875431034      #effective ratio of reinforcement



quit()
#step 2
print 'step 2'
execfile('calc_fis.py')

#step 3
print 'step 3'
execfile('calc_fis.py')

#step 4
print 'step 4'
execfile('calc_fis.py')

#step 5
print 'step 5'
execfile('calc_fis.py')




