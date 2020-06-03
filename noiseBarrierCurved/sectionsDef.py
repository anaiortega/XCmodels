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

#Béton project: béton 35/25 

#Dimensions of the pieces (rectangular approximation)
#Bottom column
BCwidthSupFlange=0.65
BCthickSupFlange=0.29
BCthickWeb=0.20
BCheightWeb=0.25
BCwidthInfFlange=0.65
BCthickInfFlange=0.51
ArBC=BCwidthSupFlange*BCthickSupFlange+BCthickWeb*BCheightWeb+BCwidthInfFlange*BCthickInfFlange

BCheight=BCthickSupFlange+BCheightWeb+BCthickInfFlange
BCwidth=ArBC/BCheight

#Top column
TCwidthSupFlange=0.45
TCthickSupFlange=0.14
TCthickWeb=0.20
TCheightWeb=0.24
TCwidthInfFlange=0.45
TCthickInfFlange=0.19

ArTC=TCwidthSupFlange*TCthickSupFlange+TCthickWeb*TCheightWeb+TCwidthInfFlange*TCthickInfFlange

TCheight=TCthickSupFlange+TCheightWeb+TCthickInfFlange
TCwidth=ArTC/TCheight

#Curve column
CCheight=0.5
CCwidth=0.2

concrete= SIA262_materials.c25_30
reinfSteel= SIA262_materials.B500A
coverForAll=0.025

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

#execfile('../generic_layers_aux.py')
execfile('../generic_fis.py')


botColRCSects= def_simple_RC_section.RCSlabBeamSection(name='botColRCSects',sectionDescr='fut fondation prefabriqué',concrType=concrete, reinfSteelType=reinfSteel,width=BCheight,depth=BCwidth)
#auxiliar data
layer1=def_simple_RC_section.ReinfRow(rebarsDiam=22e-3,areaRebar= areaFi22,rebarsSpacing=coverForAll+22e-3,width=BCheight,nominalCover=coverForAll)
layer1.nRebars=2
layer2=def_simple_RC_section.ReinfRow(rebarsDiam=22e-3,areaRebar= areaFi22,rebarsSpacing=coverForAll+22e-3,width=BCheight,nominalCover=coverForAll+0.1)
layer2.nRebars=2
layer3=def_simple_RC_section.ReinfRow(rebarsDiam=22e-3,areaRebar= areaFi22,rebarsSpacing=coverForAll+22e-3,width=BCheight,nominalCover=coverForAll+0.2)
layer3.nRebars=2
layer4=def_simple_RC_section.ReinfRow(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.20,width=BCheight,nominalCover=coverForAll)
layer4.nRebars=5
layer5=def_simple_RC_section.ReinfRow(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.20,width=BCheight,nominalCover=coverForAll+0.15)
layer5.nRebars=6

shear1=def_simple_RC_section.ShearReinforcement(familyName= "sh1",nShReinfBranches= 2.0,areaShReinfBranch= areaFi8,shReinfSpacing= 0.15,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)


#end auxiliar data
botColRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2,layer3,layer4,layer5])
botColRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2,layer4,layer5])
botColRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2,layer3,layer4,layer5])
botColRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2,layer4,layer5])
botColRCSects.dir1ShReinfY=shear1
botColRCSects.dir1ShReinfZ=shear1
botColRCSects.dir2ShReinfY=shear1
botColRCSects.dir2ShReinfZ=shear1

botColRCSects.creaTwoSections() 
sections.append(botColRCSects)

topColRCSects= def_simple_RC_section.RCSlabBeamSection(name='topColRCSects',sectionDescr='pilier prefabriqué',concrType=concrete, reinfSteelType=reinfSteel,width=TCheight,depth=TCwidth)  
#auxiliar data
layer1=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=coverForAll+16e-3,width=TCheight,nominalCover=coverForAll)
layer1.nRebars=2
layer2=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=coverForAll+16e-3,width=TCheight,nominalCover=coverForAll+0.10)
layer2.nRebars=2
layer3=def_simple_RC_section.ReinfRow(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.15,width=TCheight,nominalCover=coverForAll)
layer3.nRebars=2
layer4=def_simple_RC_section.ReinfRow(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.15,width=TCheight,nominalCover=coverForAll+0.10)
layer4.nRebars=3
#end auxiliar data
topColRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2,layer3,layer4])
topColRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2,layer3,layer4])
topColRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2,layer3,layer4])
topColRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2,layer3,layer4])
topColRCSects.dir1ShReinfY=shear1
topColRCSects.dir1ShReinfZ=shear1
topColRCSects.dir2ShReinfY=shear1
topColRCSects.dir2ShReinfZ=shear1

topColRCSects.creaTwoSections() 
sections.append(topColRCSects)

curvColRCSects= def_simple_RC_section.RCSlabBeamSection(name='curvColRCSects',sectionDescr='pilier incurvé',concrType=concrete, reinfSteelType=reinfSteel,width=CCheight,depth=CCwidth)  
#auxiliar data
layer1=def_simple_RC_section.ReinfRow(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=coverForAll+12e-3,width=CCheight,nominalCover=coverForAll)
layer1.nRebars=2
layer2=def_simple_RC_section.ReinfRow(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.20,width=CCheight,nominalCover=coverForAll)
layer2.nRebars=2
#end auxiliar data
curvColRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2])
curvColRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2])
curvColRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2])
curvColRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([layer1,layer2])
curvColRCSects.dir1ShReinfY=shear1
curvColRCSects.dir1ShReinfZ=shear1
curvColRCSects.dir2ShReinfY=shear1
curvColRCSects.dir2ShReinfZ=shear1

curvColRCSects.creaTwoSections() 
sections.append(curvColRCSects)
