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
from materials.sections.fiber_section import section_report 
import matplotlib.pyplot as plt
import numpy as np
from materials.ec2 import EC2_limit_state_checking

#execfile('data_sect03.py')
execfile('data_test_sect04.py')
#execfile('data_sect05.py')
#execfile('data_sect06.py')


# Model definition
problem=xc.FEProblem()              #necesary to create this instance of
                                     #the class xc.FEProblem()
preprocessor=problem.getPreprocessor
nodes= preprocessor.getNodeHandler     #nodes container
modelSpace= predefined_spaces.StructuralMechanics3D(nodes)  #Defines the dimension of nodes:  three coordinates (x,y,z) and six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)


nodes.defaultTag= 1 #First node number.
n1= nodes.newNodeXYZ(0,0,0)     #node 1 defined by its (x,y,z) global coordinates
n2= nodes.newNodeXYZ(Lbeam/5.,0,0)   #node 2 defined by its (x,y,z) global coordinates
n3= nodes.newNodeXYZ(2*Lbeam/5.,0,0)
n4= nodes.newNodeXYZ(3*Lbeam/5.,0,0)
n5= nodes.newNodeXYZ(4*Lbeam/5.,0,0)
n6= nodes.newNodeXYZ(Lbeam,0,0)

# Materials definition
concrete=EC2_materials.EC2Concrete("C33",-33e6,1.5) #concrete according to EC2 fck=33 MPa
#concrete.initTensStiff='Y'  #initialize a concrete02 diagram in which the
                            #tension branch has a value near to 0 (analogous to
                            #concrete01)
concrDiagram=concrete.defDiagK(preprocessor)
#We add some properties to concrete in order to define the beam material data
concrete.E=concrete.Ecm()
concrete.nu=0.2    #Poisson's coefficient of concrete
concrete.rho=2500  #specific mass of concrete (kg/m3)
concrete.G=concrete.Gcm()

#Reinforcing steel.
rfSteel=EC2_materials.S450C #reinforcing steel according to EC2 fyk=450 MPa
steelDiagram= rfSteel.defDiagK(preprocessor) #Definition of steel stress-strain diagram in XC. 

# Section geometry (rectangular)
from materials.sections import section_properties as sectpr
geomSectBeam=sectpr.RectangularSection(name='geomSectBeamX',b=width,h=depth)

# Elastic material-section appropiate for 3D beam analysis, including shear
beam_mat= typical_materials.defElasticShearSection3d(preprocessor=preprocessor,name='beam_mat',A=geomSectBeam.A(),E=concrete.Ecm(),G=concrete.Gcm(),Iz=geomSectBeam.Iz(),Iy=geomSectBeam.Iy(),J=geomSectBeam.J(),alpha=geomSectBeam.alphaY())



lin= modelSpace.newLinearCrdTransf("lin",xc.Vector([0,0,1]))

# Elements definition
elements= preprocessor.getElementHandler
elements.defaultMaterial='beam_mat'
elements.defaultTransformation= "lin"
elements.dimElem= 3 # Dimension of element space
elements.defaultTag= 1
e1= elements.newElement("ElasticBeam3d",xc.ID([1,2]))
e2= elements.newElement("ElasticBeam3d",xc.ID([2,3]))
e3= elements.newElement("ElasticBeam3d",xc.ID([3,4]))
e4= elements.newElement("ElasticBeam3d",xc.ID([4,5]))
e5= elements.newElement("ElasticBeam3d",xc.ID([5,6]))

# Constraints
constraints= preprocessor.getBoundaryCondHandler      #constraints container
modelSpace.fixNode000_F00(1)
modelSpace.fixNodeF00_F00(6)

# Loads definition
cargas= preprocessor.getLoadHandler   #loads container

casos= cargas.getLoadPatterns

#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"



#Load case definition
lpA= casos.newLoadPattern("default","A")
lpB= casos.newLoadPattern("default","B")
casos.currentLoadPattern= "A"
elements= preprocessor.getSets.getSet("total").elements
for e in elements:
  e.vector3dUniformLoadGlobal(fUnif)
casos.currentLoadPattern= "B"
for e in elements:
  e.vector3dUniformLoadGlobal(0.5*fUnif)
# Combinaciones
combs= cargas.getLoadCombinations
combs.newLoadCombination("CombA","1.00*A")
combs.newLoadCombination("CombB","1.00*B")

#Reinforced concrete sections
from materials.sections.fiber_section import def_simple_RC_section
concrete=EC2_materials.C30
mainBottReinf=def_simple_RC_section.MainReinfLayer(rebarsDiam=fiBott,areaRebar=math.pi*fiBott**2/4.,width=width,nominalCover=cover)
mainBottReinf.nRebars=nmbBarsBott
beamRCSect=def_simple_RC_section.RecordRCSlabBeamSection(name='beamRCSect',sectionDescr='beam',concrType=concrete, reinfSteelType=rfSteel,width=width,depth=depth,elemSetName='total') 
beamRCSect.dir1NegatvRebarRows=mainBottReinf
beamRCSect.dir2NegatvRebarRows=mainBottReinf

#list of RC sections (from those whose attributes (materials, geometry, refinforcement, set of elements to which apply, ... are defined in the file 'sectionsDef.py') that we want to process in order to run different limit-state checkings.
lstOfSectRecords=[beamRCSect]
from postprocess import RC_material_distribution
reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()

sections= reinfConcreteSectionDistribution.sectionDefinition #sections container
for secRec in lstOfSectRecords:
    secRec.concrType.initTensStiff='Y' #tension stiffening initialized in
                                       #concrete material diagram
    secRec.creaTwoSections()    
    sections.append(secRec)
for secRec in lstOfSectRecords:
    elset=preprocessor.getSets.getSet(secRec.elemSetName)
    reinfConcreteSectionDistribution.assign(elemSet=elset.elements,setRCSects=secRec)
reinfConcreteSectionDistribution.mapSectionsFileName='./mapSectionsReinforcementTenStiff.pkl'
reinfConcreteSectionDistribution.dump()




quit()

cargas.addToDomain("CombA","CombB")





lp0.newNodalLoad(2,pointLoad)    #applies the point load on node 2 

#We add the load case to domain.
casos.addToDomain("0")           #reads load pattern "0" and adds it to the domain

# Solve
analisis= predefined_solutions.simple_static_modified_newton(problem)
analOk= analisis.analyze(1)

#printing results
nodes= preprocessor.getNodeHandler
nodes.calculateNodalReactions(True)
nodes= preprocessor.getNodeHandler


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
concrFibers= setsRCEl1.concrFibers.fSet
reinfFibers= setsRCEl1.reinfFibers.fSet

concrSetFbEl1=sccEl1.getFiberSets()["concrSetFbEl1"]
reinfSetFbEl1=sccEl1.getFiberSets()["reinfSetFbEl1"]
concrFibers=[f for f in concrSetFbEl1]

x= sccEl1.getNeutralAxisDepth()
d=sccEl1.getEffectiveDepth()
h=sccEl1.getLeverArm()

As=setsRCEl1.tensionFibers.getArea(1.0)

print 'As= ',As
#maximum depth of the effective area:
hceff=EC2_limit_state_checking.h_c_eff(depth_tot=h,depht_eff=abs(d),depth_neutral_axis=abs(x))

print 'depth of the effective area: ',hceff,' m'
#Aceff_EHE_gross=sccEl1.getGrossEffectiveConcreteArea(hceff)
Aceff=sccEl1.getNetEffectiveConcreteArea(hceff,'reinfSetFbEl1',15.0)
print 'effective concrete tension area: ',Aceff,' m2'
ro_s_eff=As/Aceff      #effective ratio of reinforcement
print 'effective ratio of reinforcement=', ro_s_eff
#maximum crack spacing
srmax=EC2_limit_state_checking.s_r_max(k1=0.8,k2=0.5,k3=3.4,k4=0.425,cover=cover,fiReinf=0.024,ro_eff=ro_s_eff)
# print 'maximum crack spacing: ',srmax,' m'
#mean strain in the concrete between cracks
eps_cm=concrete.fctm()/concrete.E0()/2.0
#mean strain in the reinforcemen takin into account the effects of tension stiffening
fReinfMax= setsRCEl1.reinfFibers.getFiberWithMaxStrain()
epsSMax= fReinfMax.getMaterial().getStrain() # maximum strain among steel fibers
eps_sm=epsSMax
#crack withs
w_k=srmax*(eps_sm-eps_cm)
print 'crack widths: ',w_k*1e3, ' mm'
ro_s_eff=0.0643875431034

dom=preprocessor.getDomain

#step 2
print 'step 2'
execfile('calc_fis.py')
quit()
#step 3
print 'step 3'
execfile('calc_fis.py')

#step 4
print 'step 4'
execfile('calc_fis.py')

#step 5
print 'step 5'
execfile('calc_fis.py')




