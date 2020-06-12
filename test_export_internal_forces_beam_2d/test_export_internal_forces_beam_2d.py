# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
from materials.sections.fiber_section import def_simple_RC_section
#from materials.sections import section_properties
from postprocess import RC_material_distribution


from materials.sia262 import SIA262_materials
from materials.sia262 import SIA262_limit_state_checking

from postprocess import limit_state_data as lsd
from postprocess import element_section_map
from model import predefined_spaces
from materials import typical_materials
from actions import combinations as combs
from materials.sia262 import SIA262_limit_state_checking

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
#for ReinfRows are coverLat and nRebars.If we define nRebars that
#value overrides the rebarsSpacing
fi10s200r44=def_simple_RC_section.ReinfRow(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi16s200r44=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi20s200r44=def_simple_RC_section.ReinfRow(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi8s200r44=def_simple_RC_section.ReinfRow(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)

#instances of element_section_map.RCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element
beamRCsect=element_section_map.RCSlabBeamSection(name='beamRCsect',sectionDescr='beam section',concrType=concrete, reinfSteelType=reinfSteel,width=wbeam,depth=hbeam)
beamRCsect.lstRCSects[0].positvRebarRows= def_simple_RC_section.LongReinfLayers([fi10s200r44])
beamRCsect.lstRCSects[0].negatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r44])
beamRCsect.lstRCSects[1].positvRebarRows= def_simple_RC_section.LongReinfLayers([fi10s200r44])
beamRCsect.lstRCSects[1].negatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r44])
sections.append(beamRCsect)

test= xc.FEProblem()
preprocessor=  test.getPreprocessor   
nodes= preprocessor.getNodeHandler
# Problem type
modelSpace= predefined_spaces.StructuralMechanics2D(nodes) #Defines the dimension
           #of the space: nodes by two coordinates (x,y) and three DOF
           #for each node (Ux,Uy,theta)



nodes.defaultTag= 0 #First node number.
nod= nodes.newNodeXY(0,0)
nod= nodes.newNodeXY(1.0,0.0)
nod= nodes.newNodeXY(2.0,0.0)


# Geometric transformations
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")

# Materials definition
# A:            cross-sectional area of the section
# E:            Young’s modulus of material
# I:            second moment of area about the local z-axis

scc= typical_materials.defElasticSection2d(preprocessor=preprocessor, name="scc",A=beamRCsect.lstRCSects[0].getAc(),E=beamRCsect.lstRCSects[0].fiberSectionParameters.concrType.Ecm(),I=beamRCsect.lstRCSects[0].getI())


# Elements definition
elementos= preprocessor.getElementHandler
elementos.defaultTransformation= "lin"
elementos.defaultMaterial= "scc"
#  sintaxis: beam2d_02[<tag>] 
elementos.defaultTag= 1 #Tag for next element.
beam2dA= elementos.newElement("ElasticBeam2d",xc.ID([0,1]))
beam2dA.h= hbeam
beam2dB= elementos.newElement("ElasticBeam2d",xc.ID([1,2]))
beam2dB.h= hbeam
    

# Constraints
coacciones= preprocessor.getBoundaryCondHandler
#
spc= coacciones.newSPConstraint(0,0,0.0) # Node 0
spc= coacciones.newSPConstraint(0,1,0.0)
spc= coacciones.newSPConstraint(0,2,0.0)


# Loads definition
cargas= preprocessor.getLoadHandler
casos= cargas.getLoadPatterns
#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"
#Load case definition
lpA= casos.newLoadPattern("default","A")
lpA.newNodalLoad(2,xc.Vector([10e3,0,0]))
lpB= casos.newLoadPattern("default","B")
lpB.newNodalLoad(2,xc.Vector([0,0,1e3]))
lpC= casos.newLoadPattern("default","C")
lpC.newNodalLoad(1,xc.Vector([0,1e3,0]))


#Load combinations
combContainer= combs.CombContainer()
#Permanent and transitory situations.
#combContainer.ULS.perm.add('combN', '1.0*A')
#combContainer.ULS.perm.add('combM', '1.0*B')
combContainer.ULS.perm.add('combV', '1.0*C')

totalSet= preprocessor.getSets.getSet('total')
lsd.LimitStateData.internal_forces_results_directory= '/tmp/'
lsd.normalStressesResistance.saveAll(combContainer,totalSet)
lsd.shearResistance.saveAll(combContainer,totalSet)

reinfConcreteSectionDistribution.assign(elemSet=totalSet.elements,setRCSects=beamRCsect)

# #Checking normal stresses.
# limitStateLabel= lsd.normalStressesResistance.label
# lsd.normalStressesResistance.controller= SIA262_limit_state_checking.BiaxialBendingNormalStressController(limitStateLabel)
# meanFCs= lsd.normalStressesResistance.check(reinfConcreteSectionDistribution)

#Shear checking.
limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
meanFCs= lsd.shearResistance.check(reinfConcreteSectionDistribution)
