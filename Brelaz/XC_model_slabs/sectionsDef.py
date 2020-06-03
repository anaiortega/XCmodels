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
deckTh=0.25
curbTh=0.50



concrete= SIA262_materials.c50_60
reinfSteel= SIA262_materials.B500A

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

execfile('../generic_layers_aux.py')

#instances of def_simple_RC_section.RCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

deckRCSects= def_simple_RC_section.RCSlabBeamSection(name='deckRCSects',sectionDescr='slab of shell elements',concrType=concrete, reinfSteelType=reinfSteel,depth=deckTh)  
deckRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])  #transv. sup.
deckRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])  #transv. inf.
deckRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])  #long. sup.
deckRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])  #long. inf.

deckRCSects.creaTwoSections() 
sections.append(deckRCSects)   

curbRCSects= def_simple_RC_section.RCSlabBeamSection(name='curbRCSects',sectionDescr='curbs',concrType=concrete, reinfSteelType=reinfSteel,depth=curbTh)
curbRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])  #hor.
curbRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
curbRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])  #vert.
curbRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])

curbRCSects.creaTwoSections() 
sections.append(curbRCSects)   


