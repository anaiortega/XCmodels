# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
#from materials.ehe import auxEHE
from materials.sections.fiber_section import defSimpleRCSection
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

concrete= SIA262_materials.c30_37 #Rapport ERTEC 2013 page 10/28.
reinfSteel= SIA262_materials.B500B
#Generic layers (rows of rebars)
fi8s150r40=defSimpleRCSection.MainReinfLayer(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi8s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

fi10s150r40=defSimpleRCSection.MainReinfLayer(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing= 0.150,width=1.0,nominalCover=0.040)
fi10s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

fi12s150r40=defSimpleRCSection.MainReinfLayer(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi12s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

fi14s150r40=defSimpleRCSection.MainReinfLayer(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi14s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

fi16s150r40=defSimpleRCSection.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi16s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

fi18s150r40=defSimpleRCSection.MainReinfLayer(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi18s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

fi20s150r40=defSimpleRCSection.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi20s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

fi26s150r40=defSimpleRCSection.MainReinfLayer(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.040)
fi26s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

#Define available sections for the elements (spatial distribution of RC sections).
reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

slab30RCSect= defSimpleRCSection.RecordRCSlabBeamSection(name='slab30RCSect',sectionDescr="foundation slab thickness 30 cm.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.3)
slab30RCSect.dir1PositvRebarRows=[fi14s150r40] #Longitudinal
slab30RCSect.dir1NegatvRebarRows=[fi14s150r40] #
slab30RCSect.dir2PositvRebarRows=[fi14s150r50] #Transverse
slab30RCSect.dir2NegatvRebarRows=[fi14s150r50] #

slab30RCSect.creaTwoSections() 
sections.append(slab30RCSect)

slab40RCSect= defSimpleRCSection.RecordRCSlabBeamSection(name='slab40RCSect',sectionDescr="foundation slab thickness 40 cm.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.4)
slab40RCSect.dir1PositvRebarRows=[fi16s150r40] #Longitudinal
slab40RCSect.dir1NegatvRebarRows=[fi16s150r40] #
slab40RCSect.dir2PositvRebarRows=[fi14s150r50] #Transverse
slab40RCSect.dir2NegatvRebarRows=[fi14s150r50] #

slab40RCSect.creaTwoSections() 
sections.append(slab40RCSect)

wall30RCSect= defSimpleRCSection.RecordRCSlabBeamSection(name='wall30RCSect',sectionDescr="walls thickness 30 cm.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.3)
wall30RCSect.dir1PositvRebarRows=[fi14s150r40] #Vertical
wall30RCSect.dir1NegatvRebarRows=[fi14s150r40] #
wall30RCSect.dir2PositvRebarRows=[fi14s150r50] #Horizontal
wall30RCSect.dir2NegatvRebarRows=[fi14s150r50] #

wall30RCSect.creaTwoSections() 
sections.append(wall30RCSect)

wall40RCSect= defSimpleRCSection.RecordRCSlabBeamSection(name='wall40RCSect',sectionDescr="walls thickness 40 cm.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.4)
wall40RCSect.dir1PositvRebarRows=[fi16s150r40] #Vertical
wall40RCSect.dir1NegatvRebarRows=[fi16s150r40] #
wall40RCSect.dir2PositvRebarRows=[fi14s150r50] #Horizontal
wall40RCSect.dir2NegatvRebarRows=[fi14s150r50] #

wall40RCSect.creaTwoSections() 
sections.append(wall40RCSect)

deckRCSect= defSimpleRCSection.RecordRCSlabBeamSection(name='deckRCSect',sectionDescr="roof deck.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.4)
deckRCSect.dir1PositvRebarRows=[fi16s150r40] #Longitudinal
deckRCSect.dir1NegatvRebarRows=[fi16s150r40] #
deckRCSect.dir2PositvRebarRows=[fi16s150r50] #Transverse
deckRCSect.dir2NegatvRebarRows=[fi16s150r50] #

deckRCSect.creaTwoSections() 
sections.append(deckRCSect)
