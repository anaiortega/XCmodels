# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
from materials.sections.fiber_section import def_simple_RC_section
from postprocess import RC_material_distribution



from materials.sia262 import SIA262_materials
from materials.sia262 import SIA262_limit_state_checking

from postprocess import limit_state_data as lsd
from postprocess import element_section_map

#Thickness of the elements
deckThickness= 0.35
parapetBodyThickness= 0.38
parapetHeadThickness= 0.5



concrete= SIA262_materials.c30_37
reinfSteel= SIA262_materials.B500A

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

execfile('generic_layers_aux.py')

#instances of def_simple_RC_section.RCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

deckRCSects= def_simple_RC_section.RCSlabBeamSection(name='deckRCSects',sectionDescr='slab of shell elements',concrType=concrete, reinfSteelType=reinfSteel,depth=deckThickness)  
deckLong= def_simple_RC_section.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.150,width=1.0,nominalCover=0.040)
deckRCSects.dir1PositvRebarRows=[deckLong]  #long. sup.
deckRCSects.dir1NegatvRebarRows=[deckLong]  #long. inf.
deckTransv= def_simple_RC_section.MainReinfLayer(rebarsDiam=13e-3,areaRebar= (areaFi12+areaFi14)/2.0,rebarsSpacing=0.150,width=1.0,nominalCover=0.040)
deckRCSects.dir2PositvRebarRows=[deckTransv]  #transv. sup.
deckRCSects.dir2NegatvRebarRows=[deckTransv]  #transv. inf.
deckRCSects.creaTwoSections() 
sections.append(deckRCSects)

parapetBodyRCSects= def_simple_RC_section.RCSlabBeamSection(name='parapetBodyRCSects',sectionDescr='slab of shell elements',concrType=concrete, reinfSteelType=reinfSteel,depth=parapetBodyThickness)  
parapetBodyHoriz= def_simple_RC_section.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.150,width=1.0,nominalCover=0.040)
parapetBodyRCSects.dir1PositvRebarRows=[parapetBodyHoriz]  #horiz. sup.
parapetBodyRCSects.dir1NegatvRebarRows=[parapetBodyHoriz]  #horiz. inf.
parapetBodyVert= def_simple_RC_section.MainReinfLayer(rebarsDiam=13e-3,areaRebar= (areaFi12+areaFi14)/2.0,rebarsSpacing=0.150,width=1.0,nominalCover=0.040)
parapetBodyRCSects.dir2PositvRebarRows=[parapetBodyVert]  #vert. sup.
parapetBodyRCSects.dir2NegatvRebarRows=[parapetBodyVert]  #vert. inf.
parapetBodyRCSects.creaTwoSections() 
sections.append(parapetBodyRCSects)

parapetHeadRCSects= def_simple_RC_section.RCSlabBeamSection(name='parapetHeadRCSects',sectionDescr='slab of shell elements',concrType=concrete, reinfSteelType=reinfSteel,depth=parapetHeadThickness)  
parapetHeadHoriz= def_simple_RC_section.MainReinfLayer(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing=0.150,width=1.0,nominalCover=0.040)
parapetHeadRCSects.dir1PositvRebarRows=[parapetHeadHoriz]  #horiz. sup.
parapetHeadRCSects.dir1NegatvRebarRows=[parapetHeadHoriz]  #horiz. inf.
parapetHeadVert= def_simple_RC_section.MainReinfLayer(rebarsDiam=13e-3,areaRebar= (areaFi12+areaFi14)/2.0,rebarsSpacing=0.150,width=1.0,nominalCover=0.040)
parapetHeadRCSects.dir2PositvRebarRows=[parapetHeadVert]  #vert. sup.
parapetHeadRCSects.dir2NegatvRebarRows=[parapetHeadVert]  #vert. inf.
parapetHeadRCSects.creaTwoSections() 
sections.append(parapetHeadRCSects)




