# -*- coding: utf-8 -*-

import math
import os
import geom
import xc
# Macros
from materials.sections.fiber_section import def_simple_RC_section
from postprocess import RC_material_distribution



from materials.sia262 import SIA262_materials
from materials.sia262 import normalStressesSIA262 as ns
from materials.sia262 import shearSIA262
from materials.sia262 import crackControlSIA262 as cc

from postprocess import limit_state_data as lsd
from postprocess import element_section_map

#Thickness of the elements
deckTh=0.20
foundTh=0.70
wallTh=0.25
hbeamX=0.25
hbeamY=0.5
hbeamZ=0.25
wbeamX=0.5
wbeamY=0.5
wbeamZ=0.25



concrete= SIA262_materials.c30_37
reinfSteel= SIA262_materials.B500A

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

exec(open('../generic_layers_aux.py').read())

#instances of element_section_map.RCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

deckRCSects= element_section_map.RCSlabBeamSection(name='deckRCSects',sectionDescr='slab of shell elements',concrType=concrete, reinfSteelType=reinfSteel,depth=deckTh)  
deckRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
deckRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])
deckRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
deckRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(deckRCSects)   

foundRCSects= element_section_map.RCSlabBeamSection(name='foundRCSects',sectionDescr='foundation',concrType=concrete, reinfSteelType=reinfSteel,depth=foundTh)
#D1: transversal rebars
#D2: longitudinal rebars
foundRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
foundRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])
foundRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
foundRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(foundRCSects)   

wallRCSects= element_section_map.RCSlabBeamSection(name='wallRCSects',sectionDescr='wall of shell elements',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)  
wallRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
wallRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
wallRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
wallRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(wallRCSects)   

beamXRCsect=element_section_map.RCSlabBeamSection(name='beamXRCsect',sectionDescr='beam elements in X direction',concrType=concrete, reinfSteelType=reinfSteel,width=wbeamX,depth=hbeamX)
beamXRCsect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
beamXRCsect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])
beamXRCsect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
beamXRCsect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])

sections.append(beamXRCsect)

beamYRCsect=element_section_map.RCSlabBeamSection(name='beamYRCsect',sectionDescr='beam elements in Y direction',concrType=concrete, reinfSteelType=reinfSteel,width=wbeamY,depth=hbeamY)
beamYRCsect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
beamYRCsect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])
beamYRCsect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
beamYRCsect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])

sections.append(beamYRCsect)

columnZRCsect=element_section_map.RCSlabBeamSection(name='columnZRCsect',sectionDescr='columnZ',concrType=concrete, reinfSteelType=reinfSteel,width=wbeamZ,depth=hbeamZ)
columnZRCsect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
columnZRCsect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])
columnZRCsect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
columnZRCsect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])

sections.append(columnZRCsect)


