# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
from materials.sections.fiber_section import defSimpleRCSection
#from materials.sections import section_properties
from postprocess import RC_material_distribution


from materials.sia262 import SIA262_materials
from materials.sia262 import SIA262_limit_state_checking

from postprocess import limit_state_data as lsd
#from postprocess import element_section_map
from model import predefined_spaces
from materials import typical_materials
from actions import combinations as combs
from materials.sia262 import SIA262_limit_state_checking

from solution import predefined_solutions

hbeam=0.25
wbeam=0.5

areaFi8= SIA262_materials.section_barres_courantes[8e-3]
areaFi10= SIA262_materials.section_barres_courantes[10e-3]
areaFi16= SIA262_materials.section_barres_courantes[16e-3]
areaFi20= SIA262_materials.section_barres_courantes[20e-3]

concrete= SIA262_materials.c30_37
reinfSteel= SIA262_materials.SpecialII1956SIA161
#Define available sections for the elements (spatial distribution of RC sections).
#It refers to the reinforced concrete sections associated with the element
#(i.e. for shell elements we typically define two RC sections, one for each
#main direction; in the case of beam elements the most common way is to define
#RC sections in the front and back ends of the elements)

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition #creates an RC sections container

#Generic layers (rows of rebars). Other instance variables that we can define
#for MainReinfLayers are coverLat and nRebars.If we define nRebars that
#value overrides the rebarsSpacing
fi10s200r44=defSimpleRCSection.MainReinfLayer(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi16s200r44=defSimpleRCSection.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi20s200r44=defSimpleRCSection.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi8s200r44=defSimpleRCSection.MainReinfLayer(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)

#instances of defSimpleRCSection.RecordRCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element
beamRCsect=defSimpleRCSection.RecordRCSlabBeamSection(name='beamRCsect',sectionDescr='beam section',concrType=concrete, reinfSteelType=reinfSteel,width=wbeam,depth=hbeam)
beamRCsect.lstRCSects[0].positvRebarRows=[fi10s200r44]
beamRCsect.lstRCSects[0].negatvRebarRows=[fi16s200r44]
beamRCsect.lstRCSects[1].positvRebarRows=[fi10s200r44]
beamRCsect.lstRCSects[1].negatvRebarRows=[fi16s200r44]
sections.append(beamRCsect)

test= xc.FEProblem()
preprocessor=  test.getPreprocessor   
nodes= preprocessor.getNodeHandler
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and six
                  #DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)


nodes.defaultTag= 0 #First node number.
nod= nodes.newNodeXYZ(0,0,0.0)
nod= nodes.newNodeXYZ(1.0,0.0,0.0)
nod= nodes.newNodeXYZ(2.0,0.0,0.0)


# Geometric transformations
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf3d("lin")
lin.xzVector= xc.Vector([0,-1,0])  #The local Z axis of the elements matches
                            #the direction of the local Z axis of the
                            #reinforced concrete sections (parallel to the
                            #width), that is why we define:
IzElem=beamRCsect.lstRCSects[0].getIz_RClocalZax()
IyElem=beamRCsect.lstRCSects[0].getIy_RClocalYax()
JElem= beamRCsect.lstRCSects[0].getJTorsion()   

# Materials definition
# A:            cross-sectional area of the section
# E:            Young’s modulus of material
# G:            Shear modulus of the material          
# Iz:           second moment of area about the local z-axis
# Iy:           second moment of area about the local y-axis 
# J:            torsional moment of inertia of the section

scc= typical_materials.defElasticSection3d(preprocessor=preprocessor, name="scc",A=beamRCsect.lstRCSects[0].getAc(),E=beamRCsect.lstRCSects[0].concrType.Ecm(),G=beamRCsect.lstRCSects[0].concrType.Gcm(),Iz=IzElem,Iy=IyElem,J=JElem)


# Elements definition
elementos= preprocessor.getElementHandler
elementos.defaultTransformation= "lin"
elementos.defaultMaterial= "scc"
elementos.defaultTag= 1 #Tag for next element.

beam3dA= elementos.newElement("ElasticBeam3d",xc.ID([0,1]))
beam3dB= elementos.newElement("ElasticBeam3d",xc.ID([1,2]))
    
# Constraints
coacciones= preprocessor.getBoundaryCondHandler
#
spc= coacciones.newSPConstraint(0,0,0.0) # Node 0
spc= coacciones.newSPConstraint(0,1,0.0)
spc= coacciones.newSPConstraint(0,2,0.0)
spc= coacciones.newSPConstraint(0,3,0.0)
spc= coacciones.newSPConstraint(0,4,0.0)
spc= coacciones.newSPConstraint(0,5,0.0)


# Loads definition
cargas= preprocessor.getLoadHandler
casos= cargas.getLoadPatterns
#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"
#Load case definition
#Nodal Loads defined as [Fx,Fy,Fz,Mx,My,Mz] in the global coordinate system
lpA= casos.newLoadPattern("default","A")
lpA.newNodalLoad(2,xc.Vector([10e3,0,0,0,0,0])) #Axial force at front end
lpB= casos.newLoadPattern("default","B")
lpB.newNodalLoad(2,xc.Vector([0,0,0,0,-1e3,0])) #Bending moment generating
                                      #turning section about the RClocalZaxis
                                      #(parallel to width dimension)
#lpC= casos.newLoadPattern("default","C")
#lpC.newNodalLoad(1,xc.Vector([0,0,1e3,0,0,0])) #Vertical force in the middle
                                      #point of the beam generating shear
                                      #internal forces in the RCLocalYAx
                                      #direction
lpC= casos.newLoadPattern("default","C")
lpC.newNodalLoad(2,xc.Vector([0,0,1e3,0,0,0])) #Vertical force in the end
lpD= casos.newLoadPattern("default","D")
lpD.newNodalLoad(1,xc.Vector([0,1e3,0,0,0,0])) #Horizontal force in the middle
                                      #point of the beam generating shear
                                      #internal forces in the RCLocalZAx
                                      #direction


#20161202 added to check

#We add the load case to domain.
casos.addToDomain("C")

# Solution
analisis= predefined_solutions.simple_static_linear(test)
result= analisis.analyze(1)

elem1= elementos.getElement(1)
elem1.getResistingForce()
(N1,Vy1,Vz1,Mx1,My1,Mz1)=(elem1.getN1,elem1.getVy1,elem1.getVz1,elem1.getT1,elem1.getMy1,elem1.getMz1)
(N2,Vy2,Vz2,Mx2,My2,Mz2)=(elem1.getN2,elem1.getVy2,elem1.getVz2,elem1.getT2,elem1.getMy2,elem1.getMz2)
(N1,Vy1,Vz1,Mx1,My1,Mz1)
(N2,Vy2,Vz2,Mx2,My2,Mz2)

elem2= elementos.getElement(1)
elem2.getResistingForce()
(N1,Vy1,Vz1,Mx1,My1,Mz1)=(elem2.getN1,elem2.getVy1,elem2.getVz1,elem2.getT1,elem2.getMy1,elem2.getMz1)
(N2,Vy2,Vz2,Mx2,My2,Mz2)=(elem2.getN2,elem2.getVy2,elem2.getVz2,elem2.getT2,elem2.getMy2,elem2.getMz2)
print (N1,Vy1,Vz1,Mx1,My1,Mz1)
print (N2,Vy2,Vz2,Mx2,My2,Mz2)

#end added
quit()
                                      
#Load combinations
combContainer= combs.CombContainer()
#Permanent and transitory situations.
#combContainer.ULS.perm.add('combN', '1.0*A')
#combContainer.ULS.perm.add('combM', '1.0*B')
combContainer.ULS.perm.add('combV', '1.0*C')
#combContainer.ULS.perm.add('combV', '1.0*D')

totalSet= preprocessor.getSets.getSet('total')
lsd.LimitStateData.internal_forces_results_directory= '/tmp/'
lsd.normalStressesResistance.saveAll(test,combContainer,totalSet)
lsd.shearResistance.saveAll(test,combContainer,totalSet)

reinfConcreteSectionDistribution.assign(elemSet=totalSet.getElements,setRCSects=beamRCsect)

# #Checking normal stresses.
# limitStateLabel= lsd.normalStressesResistance.label
# lsd.normalStressesResistance.controller= SIA262_limit_state_checking.BiaxialBendingNormalStressController(limitStateLabel)
# meanFCs= lsd.normalStressesResistance.check(reinfConcreteSectionDistribution)

#Shear checking.
limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
meanFCs= lsd.shearResistance.check(reinfConcreteSectionDistribution)
