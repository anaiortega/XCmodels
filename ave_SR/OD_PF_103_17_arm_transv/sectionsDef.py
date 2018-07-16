# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
from materials.sections.fiber_section import defSimpleRCSection
from postprocess import RC_material_distribution



from materials.ehe import EHE_materials
concrete=EHE_materials.HA30
reinfSteel= EHE_materials.B500S


reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

execfile('../generic_layers_aux.py')

#instances of defSimpleRCSection.RecordRCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

M1dintExtRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M1dintExtRCSects',sectionDescr='Módulo 1- dintel, zona extremos',concrType=concrete, reinfSteelType=reinfSteel,depth=deckTh)  
M1dintExtRCSects.dir1PositvRebarRows=[fi16s200r76] #long. sup
M1dintExtRCSects.dir1NegatvRebarRows=[fi16s200r85] #long. inf.
M1dintExtRCSects.dir2PositvRebarRows=[fi16s100r60] #transv. sup.
M1dintExtRCSects.dir2NegatvRebarRows=[fi25s200r60] #transv. inf.
sh1=defSimpleRCSection.RecordShearReinforcement(familyName= "sh1",nShReinfBranches= 4.0,areaShReinfBranch= areaFi8,shReinfSpacing= 0.25,angAlphaShReinf= math.radians(90),angThetaConcrStruts= math.radians(30))
M1dintExtRCSects.dir2ShReinfY=sh1

M1dintExtRCSects.creaTwoSections() 
sections.append(M1dintExtRCSects)   

M1dintCentRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M1dintCentRCSects',sectionDescr='Módulo 1- dintel, zona central',concrType=concrete,reinfSteelType=reinfSteel,depth=deckTh)  
M1dintCentRCSects.dir1PositvRebarRows=[fi16s200r76] #long. sup
M1dintCentRCSects.dir1NegatvRebarRows=[fi16s200r85] #long. inf.
M1dintCentRCSects.dir2PositvRebarRows=[fi16s200r60] #transv. sup.
M1dintCentRCSects.dir2NegatvRebarRows=[fi25s200r60] #transv. inf.

M1dintCentRCSects.creaTwoSections() 
sections.append(M1dintCentRCSects)   

M1losCimExtRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M1losCimExtRCSects',sectionDescr='Módulo 1- losa de cimentación, zona exterior',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
M1losCimExtRCSects.dir1PositvRebarRows=[fi16s200r76] #long. sup
M1losCimExtRCSects.dir1NegatvRebarRows=[fi16s200r76] #long. inf.
M1losCimExtRCSects.dir2PositvRebarRows=[fi16s200r60] #transv. sup.
M1losCimExtRCSects.dir2NegatvRebarRows=[fi16s200r60,fi20s200r60] #transv. inf.

M1losCimExtRCSects.creaTwoSections() 
sections.append(M1losCimExtRCSects)   

M1losCimCentRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M1losCimCentRCSects',sectionDescr='Módulo 1- losa de cimentación, zona central',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
M1losCimCentRCSects.dir1PositvRebarRows=[fi16s200r76] #long. sup
M1losCimCentRCSects.dir1NegatvRebarRows=[fi16s200r76] #long. inf.
M1losCimCentRCSects.dir2PositvRebarRows=[fi16s100r60] #transv. sup.
M1losCimCentRCSects.dir2NegatvRebarRows=[fi16s200r60] #transv. inf.

M1losCimCentRCSects.creaTwoSections() 
sections.append(M1losCimCentRCSects)   

M1hastIzqRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M1hastIzqRCSects',sectionDescr='Módulo 1- hastial izquierdo',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
M1hastIzqRCSects.dir1PositvRebarRows=[fi20s200r60]  #vert. int.
M1hastIzqRCSects.dir1NegatvRebarRows=[fi16s100r60]  #vert. ext.
M1hastIzqRCSects.dir2PositvRebarRows=[fi16s200r80]  #hor. int.
M1hastIzqRCSects.dir2NegatvRebarRows=[fi16s200r76]  #hor. ext.

M1hastIzqRCSects.creaTwoSections() 
sections.append(M1hastIzqRCSects)   

M1hastDerRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M1hastDerRCSects',sectionDescr='Módulo 1- hastial derecho',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
M1hastDerRCSects.dir1PositvRebarRows=[fi16s100r60]  #vert. ext.
M1hastDerRCSects.dir1NegatvRebarRows=[fi20s200r60]  #vert. int.
M1hastDerRCSects.dir2PositvRebarRows=[fi16s200r76]  #hor. ext.
M1hastDerRCSects.dir2NegatvRebarRows=[fi16s200r80]  #hor. int.

M1hastDerRCSects.creaTwoSections() 
sections.append(M1hastDerRCSects)   

# muretesRCsect=defSimpleRCSection.RecordRCSlabBeamSection(name='muretesRCsect',sectionDescr='muretes',concrType=concrete, reinfSteelType=reinfSteel,width=emuret,depth=hmuret)
# muretesRCsect.dir1PositvRebarRows=[fi20s150r35]
# muretesRCsect.dir1NegatvRebarRows=[fi20s150r35]
# muretesRCsect.dir2PositvRebarRows=[fi20s150r35]
# muretesRCsect.dir2NegatvRebarRows=[fi20s150r35]
# 
muretesRCsect.creaTwoSections() 
sections.append(muretesRCsect)

M2dintExtRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M2dintExtRCSects',sectionDescr='Módulo 2- dintel, zona extremos',concrType=concrete, reinfSteelType=reinfSteel,depth=deckTh)  
M2dintExtRCSects.dir1PositvRebarRows=[fi16s150r80] #long. sup
M2dintExtRCSects.dir1NegatvRebarRows=[fi20s150r85] #long. inf.
M2dintExtRCSects.dir2PositvRebarRows=[fi20s100r60] #transv. sup.
M2dintExtRCSects.dir2NegatvRebarRows=[fi25s200r60] #transv. inf.
sh2=defSimpleRCSection.RecordShearReinforcement(familyName= "sh2",nShReinfBranches= 5.0,areaShReinfBranch= areaFi10,shReinfSpacing= 0.20,angAlphaShReinf= math.radians(90),angThetaConcrStruts= math.radians(30))
M2dintExtRCSects.dir2ShReinfY=sh2

M2dintExtRCSects.creaTwoSections() 
sections.append(M2dintExtRCSects)   

M2dintCentRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M2dintCentRCSects',sectionDescr='Módulo 2- dintel, zona central',concrType=concrete,reinfSteelType=reinfSteel,depth=deckTh)  
M2dintCentRCSects.dir1PositvRebarRows=[fi16s150r76] #long. sup
M2dintCentRCSects.dir1NegatvRebarRows=[fi20s150r85] #long. inf.
M2dintCentRCSects.dir2PositvRebarRows=[fi16s200r60] #transv. sup.
M2dintCentRCSects.dir2NegatvRebarRows=[fi25s200r60,fi25s200r60] #transv. inf.

M2dintCentRCSects.creaTwoSections() 
sections.append(M2dintCentRCSects)   

M2losCimExtRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M2losCimExtRCSects',sectionDescr='Módulo 2- losa de cimentación, zona exterior',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
M2losCimExtRCSects.dir1PositvRebarRows=[fi20s200r80] #long. sup
M2losCimExtRCSects.dir1NegatvRebarRows=[fi12s200r80] #long. inf.
M2losCimExtRCSects.dir2PositvRebarRows=[fi20s200r60] #transv. sup.
M2losCimExtRCSects.dir2NegatvRebarRows=[fi20s100r60] #transv. inf.
sh3=defSimpleRCSection.RecordShearReinforcement(familyName= "sh3",nShReinfBranches= 5.0,areaShReinfBranch= areaFi8,shReinfSpacing= 0.20,angAlphaShReinf= math.radians(90),angThetaConcrStruts= math.radians(30))
M2losCimExtRCSects.dir2ShReinfY=sh3

M2losCimExtRCSects.creaTwoSections() 
sections.append(M2losCimExtRCSects)   

M2losCimCentRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M2losCimCentRCSects',sectionDescr='Módulo 2- losa de cimentación, zona central',concrType=concrete, reinfSteelType=reinfSteel,depth=baseSlabTh)
M2losCimCentRCSects.dir1PositvRebarRows=[fi16s100r85] #long. sup
M2losCimCentRCSects.dir1NegatvRebarRows=[fi12s200r76] #long. inf.
M2losCimCentRCSects.dir2PositvRebarRows=[fi20s200r60,fi25s200r60] #transv. sup.
M2losCimCentRCSects.dir2NegatvRebarRows=[fi16s200r60] #transv. inf.

M2losCimCentRCSects.creaTwoSections() 
sections.append(M2losCimCentRCSects)   

M2hastIzqRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M2hastIzqRCSects',sectionDescr='Módulo 2- hastial izquierdo',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
M2hastIzqRCSects.dir1PositvRebarRows=[fi16s100r60]  #vert. int.
M2hastIzqRCSects.dir1NegatvRebarRows=[fi20s100r60]  #vert. ext.
M2hastIzqRCSects.dir2PositvRebarRows=[fi16s200r76]  #hor. int.
M2hastIzqRCSects.dir2NegatvRebarRows=[fi16s200r80]  #hor. ext.

M2hastIzqRCSects.creaTwoSections() 
sections.append(M2hastIzqRCSects)   

M2hastDerRCSects= defSimpleRCSection.RecordRCSlabBeamSection(name='M2hastDerRCSects',sectionDescr='Módulo 2- hastial derecho',concrType=concrete, reinfSteelType=reinfSteel,depth=wallTh)
M2hastDerRCSects.dir1PositvRebarRows=[fi20s100r60]  #vert. ext.
M2hastDerRCSects.dir1NegatvRebarRows=[fi16s100r60]  #vert. int.
M2hastDerRCSects.dir2PositvRebarRows=[fi16s200r80]  #hor. ext.
M2hastDerRCSects.dir2NegatvRebarRows=[fi16s200r76]  #hor. int.

M2hastDerRCSects.creaTwoSections() 
sections.append(M2hastDerRCSects)   

