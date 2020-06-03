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
cantlvTh=0.50

concrete= SIA262_materials.c30_37
reinfSteel= SIA262_materials.B500A

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

execfile('../generic_layers_aux.py')

#instances of def_simple_RC_section.RCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element
Twofi20r50=def_simple_RC_section.ReinfRow(rebarsDiam=20e-3,areaRebar= areaFi20,width=1.0,nominalCover=0.050)
Twofi20r50.nRebars=2
Twofi20r50.coverLat=0.05

Twofi10r50=def_simple_RC_section.ReinfRow(rebarsDiam=10e-3,areaRebar= areaFi10,width=1.0,nominalCover=0.050)
Twofi10r50.nRebars=2
Twofi10r50.coverLat=0.05

cantlvRCSects= def_simple_RC_section.RCSlabBeamSection(name='cantlvRCSects',sectionDescr='cantilever of shell elements',concrType=concrete, reinfSteelType=reinfSteel,depth=cantlvTh)  
cantlvRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([Twofi20r50])
cantlvRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([Twofi10r50])
cantlvRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([Twofi20r50])
cantlvRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([Twofi20r50])

cantlvRCSects.creaTwoSections() 
sections.append(cantlvRCSects)   

