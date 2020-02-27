# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
from materials.sections.fiber_section import def_simple_RC_section
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking
from postprocess import limit_state_data as lsd
from postprocess import element_section_map

from materials.sia262 import SIA262_materials

#Béton project: béton 35/25 

#Dimensions of the pieces (rectangular approximation)
hbeam=0.25
wbeam=0.5
areaFi8= SIA262_materials.section_barres_courantes[8e-3]
areaFi10= SIA262_materials.section_barres_courantes[10e-3]
areaFi16= SIA262_materials.section_barres_courantes[16e-3]
areaFi20= SIA262_materials.section_barres_courantes[20e-3]
#Generic layers (rows of rebars). Other instance variables that we can define
#for MainReinfLayers are coverLat and nRebars.If we define nRebars that
#value overrides the rebarsSpacing
fi10s200r44=def_simple_RC_section.MainReinfLayer(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi16s200r44=def_simple_RC_section.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi20s200r44=def_simple_RC_section.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi8s200r44=def_simple_RC_section.MainReinfLayer(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)

concrete= SIA262_materials.c30_37
reinfSteel= SIA262_materials.SpecialII1956SIA161
#

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition


beamRCsects=def_simple_RC_section.RecordRCSlabBeamSection(name='beamRCsects',sectionDescr='beam section',concrType=concrete, reinfSteelType=reinfSteel,width=wbeam,depth=hbeam)
beamRCsects.dir1PositvRebarRows=[fi10s200r44]
beamRCsects.dir1NegatvRebarRows=[fi16s200r44]
beamRCsects.dir2PositvRebarRows=[fi10s200r44]
beamRCsects.dir2NegatvRebarRows=[fi16s200r44]

beamRCsects.creaTwoSections() 
sections.append(beamRCsects)
