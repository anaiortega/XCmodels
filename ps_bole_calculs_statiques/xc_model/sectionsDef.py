# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
#from materials.ehe import auxEHE
from materials.sections.fiber_section import def_simple_RC_section
from materials.sections import section_properties
from postprocess import RC_material_distribution


from materials.sia262 import SIA262_materials
from materials.sia262 import SIA262_limit_state_checking

from postprocess import limit_state_data as lsd
from postprocess import element_section_map


areaFi6= SIA262_materials.section_barres_courantes[6e-3]
areaFi8= SIA262_materials.section_barres_courantes[8e-3]
areaFi10= SIA262_materials.section_barres_courantes[10e-3]
areaFi12= SIA262_materials.section_barres_courantes[12e-3]
areaFi14= SIA262_materials.section_barres_courantes[14e-3]
areaFi16= SIA262_materials.section_barres_courantes[16e-3]
areaFi18= SIA262_materials.section_barres_courantes[18e-3]
areaFi20= SIA262_materials.section_barres_courantes[20e-3]
areaFi22= SIA262_materials.section_barres_courantes[22e-3]
areaFi26= SIA262_materials.section_barres_courantes[26e-3]
areaFi30= SIA262_materials.section_barres_courantes[30e-3]
areaFi34= SIA262_materials.section_barres_courantes[34e-3]
areaFi40= SIA262_materials.section_barres_courantes[40e-3]

concrete= SIA262_materials.c25_30
reinfSteel= SIA262_materials.B500B
#Define available sections for the elements (spatial distribution of RC sections).
reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

#Generic layers (rows of rebars)
fi8s150r40=def_simple_RC_section.MainReinfLayer(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi8s150r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

fi10s150r40=def_simple_RC_section.MainReinfLayer(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing= 0.150,width=1.0,nominalCover=0.040)
fi10s150r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

fi12s150r40=def_simple_RC_section.MainReinfLayer(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi12s150r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

fi14s150r40=def_simple_RC_section.MainReinfLayer(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi14s150r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

fi16s150r40=def_simple_RC_section.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi16s150r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

fi18s150r40=def_simple_RC_section.MainReinfLayer(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi18s150r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

fi20s150r40=def_simple_RC_section.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi20s150r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

fi26s150r40=def_simple_RC_section.MainReinfLayer(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi26s150r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)


deckSlabRCSect= def_simple_RC_section.RCSlabBeamSection(name='deckSlabRCSect',sectionDescr="estacade.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.20)
#[0]: rebars on back end section.
#[1]: rebars on front end section


deckSlabRCSect.dir1PositvRebarRows=[fi12s150r40] #Ok
deckSlabRCSect.dir1NegatvRebarRows=[fi12s150r40] #Ok
deckSlabRCSect.dir2PositvRebarRows=[fi12s150r40] #Ok
deckSlabRCSect.dir2NegatvRebarRows=[fi12s150r40] #Ok

deckSlabRCSect.creaTwoSections() 
sections.append(deckSlabRCSect)

parapetRCSect= def_simple_RC_section.RCSlabBeamSection(name='parapetRCSect',sectionDescr="estacade.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.20)
#[0]: rebars on back end section.
#[1]: rebars on front end section
parapetRCSect.dir1PositvRebarRows=[fi10s150r40] #Ok
parapetRCSect.dir1NegatvRebarRows=[fi12s150r40] #Ok
parapetRCSect.dir2PositvRebarRows=[fi10s150r40] #Ok
parapetRCSect.dir2NegatvRebarRows=[fi12s150r40] #Ok

parapetRCSect.creaTwoSections() 
sections.append(parapetRCSect)
