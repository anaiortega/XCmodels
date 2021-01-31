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

exec(open('../generic_layers_aux.py').read()))

#instances of element_section_map.RCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

dintExtRCSects= element_section_map.RCSlabBeamSection(name='dintExtRCSects',sectionDescr='dintel, zona extremos',concrType=concrete, reinfSteelType=reinfSteel,depth=deckTh)  
dintExtRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r80])  #long. sup.
dintExtRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r85])  #long. inf.
dintExtRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60])  #transv.sup
dintExtRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi25s200r60])  #transv.inf
sh1=def_simple_RC_section.ShearReinforcement(familyName= "sh1",nShReinfBranches= 4.0,areaShReinfBranch= areaFi8,shReinfSpacing= 0.25,angAlphaShReinf= math.radians(90),angThetaConcrStruts= math.radians(30))
dintExtRCSects.dir2ShReinfY=sh1

sections.append(dintExtRCSects)   

dintCentRCSects= element_section_map.RCSlabBeamSection(name='dintCentRCSects',sectionDescr='dintel, zona central',concrType=concrete,reinfSteelType=reinfSteel,depth=deckTh)  
dintCentRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r76])  #long. sup.
dintCentRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r85])  #long. inf.
dintCentRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #transv.sup
dintCentRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi25s200r60])  #transv.inf

sections.append(dintCentRCSects)   

losCimExtRCSects= element_section_map.RCSlabBeamSection(name='losCimExtRCSects',sectionDescr='losa de cimentación, zona exterior',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
losCimExtRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r80])  #long. sup.
losCimExtRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r80])  #long. inf.
losCimExtRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60])  #transv.sup
losCimExtRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60])  #transv.inf

sections.append(losCimExtRCSects)   

losCimCentRCSects= element_section_map.RCSlabBeamSection(name='losCimCentRCSects',sectionDescr='losa de cimentación, zona central',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
losCimCentRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r80])  #long. sup.
losCimCentRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r60])  #long. inf.
losCimCentRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r76])  #transv.sup
losCimCentRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #transv.inf

sections.append(losCimCentRCSects)   

hastIzqRCSects= element_section_map.RCSlabBeamSection(name='hastIzqRCSects',sectionDescr='hastial izquierdo',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
#0:Vert
#1:Hor
#+:Cent
hastIzqRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])   #vert. int.
hastIzqRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60])   #vert. ext.
hastIzqRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r76])   #hor. int.
hastIzqRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r80])   #hor. ext.

sections.append(hastIzqRCSects)   

hastDerRCSects= element_section_map.RCSlabBeamSection(name='hastDerRCSects',sectionDescr='hastial izquierdo',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
#0:Vert
#1:Hor
#+:Int
hastDerRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60])   #vert. ext.
hastDerRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])   #vert. int.
hastDerRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r80])   #hor. ext.
hastDerRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r76])   #hor. int.

sections.append(hastDerRCSects)   

# muretesRCsect=element_section_map.RCSlabBeamSection(name='muretesRCsect',sectionDescr='muretes',concrType=concrete, reinfSteelType=reinfSteel,width=emuret,depth=hmuret)
# muretesRCsect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
# muretesRCsect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
# muretesRCsect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
# muretesRCsect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
# 
sections.append(muretesRCsect)

