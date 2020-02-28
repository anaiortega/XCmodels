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

#instances of def_simple_RC_section.RecordRCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

deckRCSects= def_simple_RC_section.RecordRCSlabBeamSection(name='deckRCSects',sectionDescr='slab of shell elements',concrType=concrete, reinfSteelType=reinfSteel,depth=deckTh)  
deckRCSects.dir1PositvRebarRows=[fi20s150r35]  #transv. sup.
deckRCSects.dir1NegatvRebarRows=[fi20s150r35]  #transv. inf.
deckRCSects.dir2PositvRebarRows=[fi18s150r35]  #long. sup.
deckRCSects.dir2NegatvRebarRows=[fi22s150r35]  #long. inf.

deckRCSects.creaTwoSections() 
sections.append(deckRCSects)   

curbRCSects= def_simple_RC_section.RecordRCSlabBeamSection(name='curbRCSects',sectionDescr='curbs',concrType=concrete, reinfSteelType=reinfSteel,depth=curbTh)
curbRCSects.dir1PositvRebarRows=[fi16s150r35]  #hor.
curbRCSects.dir1NegatvRebarRows=[fi16s150r35]
curbRCSects.dir2PositvRebarRows=[fi12s150r35]  #vert.
curbRCSects.dir2NegatvRebarRows=[fi12s150r35]

curbRCSects.creaTwoSections() 
sections.append(curbRCSects)   


