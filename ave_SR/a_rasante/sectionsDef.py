# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
from materials.sections.fiber_section import def_simple_RC_section
from postprocess import RC_material_distribution


from materials.ehe import EHE_materials
concrete=EHE_materials.HA30
reinfSteel= EHE_materials.B500S

# from postprocess import limit_state_data as lsd
# from postprocess import element_section_map


reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

execfile('../generic_layers_aux.py')

#instances of def_simple_RC_section.RecordRCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

dintExtRCSects= def_simple_RC_section.RecordRCSlabBeamSection(name='dintExtRCSects',sectionDescr='dintel, zona extremos',concrType=concrete, reinfSteelType=reinfSteel,depth=deckTh)  
dintExtRCSects.dir1PositvRebarRows=[fi12s150r80]  #long. sup.
dintExtRCSects.dir1NegatvRebarRows=[fi16s150r85]  #long. inf.
dintExtRCSects.dir2PositvRebarRows=[fi20s200r60]  #transv.sup
dintExtRCSects.dir2NegatvRebarRows=[fi25s200r60]  #transv.inf
sh1=def_simple_RC_section.RecordShearReinforcement(familyName= "sh1",nShReinfBranches= 4.0,areaShReinfBranch= areaFi8,shReinfSpacing= 0.25,angAlphaShReinf= math.radians(90),angThetaConcrStruts= math.radians(30))
dintExtRCSects.dir2ShReinfY=sh1

dintExtRCSects.creaTwoSections() 
sections.append(dintExtRCSects)   

dintCentRCSects= def_simple_RC_section.RecordRCSlabBeamSection(name='dintCentRCSects',sectionDescr='dintel, zona central',concrType=concrete,reinfSteelType=reinfSteel,depth=deckTh)  
dintCentRCSects.dir1PositvRebarRows=[fi12s150r76]  #long. sup.
dintCentRCSects.dir1NegatvRebarRows=[fi16s150r85]  #long. inf.
dintCentRCSects.dir2PositvRebarRows=[fi16s200r60]  #transv.sup
dintCentRCSects.dir2NegatvRebarRows=[fi25s200r60]  #transv.inf

dintCentRCSects.creaTwoSections() 
sections.append(dintCentRCSects)   

losCimExtRCSects= def_simple_RC_section.RecordRCSlabBeamSection(name='losCimExtRCSects',sectionDescr='losa de cimentación, zona exterior',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
losCimExtRCSects.dir1PositvRebarRows=[fi12s150r80]  #long. sup.
losCimExtRCSects.dir1NegatvRebarRows=[fi12s150r80]  #long. inf.
losCimExtRCSects.dir2PositvRebarRows=[fi20s200r60]  #transv.sup
losCimExtRCSects.dir2NegatvRebarRows=[fi20s200r60]  #transv.inf

losCimExtRCSects.creaTwoSections() 
sections.append(losCimExtRCSects)   

losCimCentRCSects= def_simple_RC_section.RecordRCSlabBeamSection(name='losCimCentRCSects',sectionDescr='losa de cimentación, zona central',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
losCimCentRCSects.dir1PositvRebarRows=[fi12s150r80]  #long. sup.
losCimCentRCSects.dir1NegatvRebarRows=[fi12s150r60]  #long. inf.
losCimCentRCSects.dir2PositvRebarRows=[fi20s200r76]  #transv.sup
losCimCentRCSects.dir2NegatvRebarRows=[fi16s200r60]  #transv.inf

losCimCentRCSects.creaTwoSections() 
sections.append(losCimCentRCSects)   

hastIzqRCSects= def_simple_RC_section.RecordRCSlabBeamSection(name='hastIzqRCSects',sectionDescr='hastial izquierdo',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
#0:Vert
#1:Hor
#+:Cent
hastIzqRCSects.dir1PositvRebarRows=[fi16s200r60]   #vert. int.
hastIzqRCSects.dir1NegatvRebarRows=[fi20s200r60]   #vert. ext.
hastIzqRCSects.dir2PositvRebarRows=[fi12s150r76]   #hor. int.
hastIzqRCSects.dir2NegatvRebarRows=[fi12s150r80]   #hor. ext.

hastIzqRCSects.creaTwoSections() 
sections.append(hastIzqRCSects)   

hastDerRCSects= def_simple_RC_section.RecordRCSlabBeamSection(name='hastDerRCSects',sectionDescr='hastial izquierdo',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
#0:Vert
#1:Hor
#+:Int
hastDerRCSects.dir1PositvRebarRows=[fi20s200r60]   #vert. ext.
hastDerRCSects.dir1NegatvRebarRows=[fi16s200r60]   #vert. int.
hastDerRCSects.dir2PositvRebarRows=[fi12s150r80]   #hor. ext.
hastDerRCSects.dir2NegatvRebarRows=[fi12s150r76]   #hor. int.

hastDerRCSects.creaTwoSections() 
sections.append(hastDerRCSects)   

# muretesRCsect=def_simple_RC_section.RecordRCSlabBeamSection(name='muretesRCsect',sectionDescr='muretes',concrType=concrete, reinfSteelType=reinfSteel,width=emuret,depth=hmuret)
# muretesRCsect.dir1PositvRebarRows=[fi20s150r35]
# muretesRCsect.dir1NegatvRebarRows=[fi20s150r35]
# muretesRCsect.dir2PositvRebarRows=[fi20s150r35]
# muretesRCsect.dir2NegatvRebarRows=[fi20s150r35]
# 
muretesRCsect.creaTwoSections() 
sections.append(muretesRCsect)

