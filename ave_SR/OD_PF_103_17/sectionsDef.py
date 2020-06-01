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
from materials.sia262 import SIA262_limit_state_checking
from postprocess import limit_state_data as lsd
from postprocess import element_section_map

#Thickness of the elements


concrete=EHE_materials.HA30
reinfSteel= EHE_materials.B500S


reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

execfile('../generic_layers_aux.py')

#instances of def_simple_RC_section.RCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

M1dintExtRCSects= def_simple_RC_section.RCSlabBeamSection(name='M1dintExtRCSects',sectionDescr='Módulo 1- dintel, zona extremos',concrType=concrete, reinfSteelType=reinfSteel,depth=deckTh)  
M1dintExtRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #long. sup
M1dintExtRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #long. inf.
M1dintExtRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60]) #transv. sup.
M1dintExtRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi25s200r60]) #transv. inf.

M1dintExtRCSects.creaTwoSections() 
sections.append(M1dintExtRCSects)   

M1dintCentRCSects= def_simple_RC_section.RCSlabBeamSection(name='M1dintCentRCSects',sectionDescr='Módulo 1- dintel, zona central',concrType=concrete,reinfSteelType=reinfSteel,depth=deckTh)  
M1dintCentRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #long. sup
M1dintCentRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #long. inf.
M1dintCentRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #transv. sup.
M1dintCentRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi25s200r60]) #transv. inf.

M1dintCentRCSects.creaTwoSections() 
sections.append(M1dintCentRCSects)   

M1losCimExtRCSects= def_simple_RC_section.RCSlabBeamSection(name='M1losCimExtRCSects',sectionDescr='Módulo 1- losa de cimentación, zona exterior',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
M1losCimExtRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #long. sup
M1losCimExtRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #long. inf.
M1losCimExtRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60]) #transv. sup.
M1losCimExtRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60]) #transv. inf.

M1losCimExtRCSects.creaTwoSections() 
sections.append(M1losCimExtRCSects)   

M1losCimCentRCSects= def_simple_RC_section.RCSlabBeamSection(name='M1losCimCentRCSects',sectionDescr='Módulo 1- losa de cimentación, zona central',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
M1losCimCentRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #long. sup
M1losCimCentRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #long. inf.
M1losCimCentRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60]) #transv. sup.
M1losCimCentRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #transv. inf.

M1losCimCentRCSects.creaTwoSections() 
sections.append(M1losCimCentRCSects)   

M1hastIzqRCSects= def_simple_RC_section.RCSlabBeamSection(name='M1hastIzqRCSects',sectionDescr='Módulo 1- hastial izquierdo',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
M1hastIzqRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #vert. int.
M1hastIzqRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60])  #vert. ext.
M1hastIzqRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #hor. int.
M1hastIzqRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #hor. ext.

M1hastIzqRCSects.creaTwoSections() 
sections.append(M1hastIzqRCSects)   

M1hastDerRCSects= def_simple_RC_section.RCSlabBeamSection(name='M1hastDerRCSects',sectionDescr='Módulo 1- hastial derecho',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
M1hastDerRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s200r60])  #vert. ext.
M1hastDerRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #vert. int.
M1hastDerRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #hor. ext.
M1hastDerRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #hor. int.

M1hastDerRCSects.creaTwoSections() 
sections.append(M1hastDerRCSects)   

# muretesRCsect=def_simple_RC_section.RCSlabBeamSection(name='muretesRCsect',sectionDescr='muretes',concrType=concrete, reinfSteelType=reinfSteel,width=emuret,depth=hmuret)
# muretesRCsect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
# muretesRCsect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
# muretesRCsect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
# muretesRCsect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
# 
muretesRCsect.creaTwoSections() 
sections.append(muretesRCsect)

M2dintExtRCSects= def_simple_RC_section.RCSlabBeamSection(name='M2dintExtRCSects',sectionDescr='Módulo 2- dintel, zona extremos',concrType=concrete, reinfSteelType=reinfSteel,depth=deckTh)  
M2dintExtRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60]) #long. sup
M2dintExtRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60]) #long. inf.
M2dintExtRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s100r60]) #transv. sup.
M2dintExtRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s100r60]) #transv. inf.

M2dintExtRCSects.creaTwoSections() 
sections.append(M2dintExtRCSects)   

M2dintCentRCSects= def_simple_RC_section.RCSlabBeamSection(name='M2dintCentRCSects',sectionDescr='Módulo 2- dintel, zona central',concrType=concrete,reinfSteelType=reinfSteel,depth=deckTh)  
M2dintCentRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60]) #long. sup
M2dintCentRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60]) #long. inf.
M2dintCentRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #transv. sup.
M2dintCentRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s100r60]) #transv. inf.

M2dintCentRCSects.creaTwoSections() 
sections.append(M2dintCentRCSects)   

M2losCimExtRCSects= def_simple_RC_section.RCSlabBeamSection(name='M2losCimExtRCSects',sectionDescr='Módulo 2- losa de cimentación, zona exterior',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
M2losCimExtRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60]) #long. sup
M2losCimExtRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60]) #long. inf.
M2losCimExtRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s100r60]) #transv. sup.
M2losCimExtRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s100r60]) #transv. inf.

M2losCimExtRCSects.creaTwoSections() 
sections.append(M2losCimExtRCSects)   

M2losCimCentRCSects= def_simple_RC_section.RCSlabBeamSection(name='M2losCimCentRCSects',sectionDescr='Módulo 2- losa de cimentación, zona central',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
M2losCimCentRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60]) #long. sup
M2losCimCentRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60]) #long. inf.
M2losCimCentRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s100r60]) #transv. sup.
M2losCimCentRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60]) #transv. inf.

M2losCimCentRCSects.creaTwoSections() 
sections.append(M2losCimCentRCSects)   

M2hastIzqRCSects= def_simple_RC_section.RCSlabBeamSection(name='M2hastIzqRCSects',sectionDescr='Módulo 2- hastial izquierdo',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
M2hastIzqRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s100r60])  #vert. int.
M2hastIzqRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s100r60])  #vert. ext.
M2hastIzqRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60])  #hor. int.
M2hastIzqRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #hor. ext.

M2hastIzqRCSects.creaTwoSections() 
sections.append(M2hastIzqRCSects)   

M2hastDerRCSects= def_simple_RC_section.RCSlabBeamSection(name='M2hastDerRCSects',sectionDescr='Módulo 2- hastial derecho',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
M2hastDerRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s100r60])  #vert. ext.
M2hastDerRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s100r60])  #vert. int.
M2hastDerRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s200r60])  #hor. ext.
M2hastDerRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r60])  #hor. int.

M2hastDerRCSects.creaTwoSections() 
sections.append(M2hastDerRCSects)   

