# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
#from materials.ehe import auxEHE
from materials.sections.fiber_section import def_simple_RC_section
from postprocess import RC_material_distribution


from materials.sia262 import SIA262_materials as concrete
#from materials.ehe import EHE_reinforcing_steel
from materials.sia262 import SIA262_materials
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

concrete= concrete.c35_45 #Rapport ERTEC 2013 page 10/28.
reinfSteel= SIA262_materials.SpecialII1956SIA161
#Define available sections for the elements (spatial distribution of RC sections).
reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

#Generic layers (rows of rebars)
fi8s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi8s125r44=def_simple_RC_section.ReinfRow(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing=0.125,width=1.0,nominalCover=0.044)
fi10s200r44=def_simple_RC_section.ReinfRow(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi10s250r42=def_simple_RC_section.ReinfRow(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.250,width=1.0,nominalCover=0.042)
fi12s250r30=def_simple_RC_section.ReinfRow(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.250,width=1.0,nominalCover=0.030)
fi12s250r46=def_simple_RC_section.ReinfRow(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.250,width=1.0,nominalCover=0.046)
fi14s250r30=def_simple_RC_section.ReinfRow(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing=0.25,width=1.0,nominalCover=0.030)
fi14s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi16s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi16s250r50=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.250,width=1.0,nominalCover=0.050)
fi16s250r56=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.250,width=1.0,nominalCover=0.056)
fi18s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi18s125r44=def_simple_RC_section.ReinfRow(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing=0.125,width=1.0,nominalCover=0.044)
fi20s250r30=def_simple_RC_section.ReinfRow(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.250,width=1.0,nominalCover=0.030)
fi20s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi20s125r50=def_simple_RC_section.ReinfRow(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.125,width=1.0,nominalCover=0.050)
fi26s250r30=def_simple_RC_section.ReinfRow(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing=0.250,width=1.0,nominalCover=0.030)
fi26s250r50=def_simple_RC_section.ReinfRow(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing=0.250,width=1.0,nominalCover=0.050)

FoundExtSlabRCSect= def_simple_RC_section.RCSlabBeamSection(name='foundExtSlabRCSect',sectionDescr="underpass.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.60)
#[0]: transversal rebars
#[1]: longitudinal rebars
FoundExtSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi14s250r30])
FoundExtSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi14s125r30,fi18s125r44])
FoundExtSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi10s200r44])
FoundExtSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi10s200r44])

FoundExtSlabRCSect.creaTwoSections() 
sections.append(FoundExtSlabRCSect)


FoundIntSlabRCSect= def_simple_RC_section.RCSlabBeamSection('foundIntSlabRCSect',"underpass.",concrete, reinfSteel,0.60)
#[0]: transversal rebars
#[1]: longitudinal rebars
FoundIntSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi14s125r30,fi8s125r44])
FoundIntSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi14s250r30])
FoundIntSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi10s200r44])
FoundIntSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi10s200r44])

FoundIntSlabRCSect.creaTwoSections() 
sections.append(FoundIntSlabRCSect)

LeftWallRCSect= def_simple_RC_section.RCSlabBeamSection('leftWallRCSect',"underpass.",concrete, reinfSteel,0.45)
#[0]: horizontal rebars
#[1]: vertical rebars
LeftWallRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s250r46])
LeftWallRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s250r46])
LeftWallRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s125r30])
LeftWallRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s125r30])

LeftWallRCSect.creaTwoSections() 
sections.append(LeftWallRCSect)


RightWallRCSect= def_simple_RC_section.RCSlabBeamSection('rightWallRCSect',"underpass.",concrete, reinfSteel,0.45)
#[0]: horizontal rebars
#[1]: vertical rebars
RightWallRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s250r46])
RightWallRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s250r46])
RightWallRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s125r30])
RightWallRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s125r30])

RightWallRCSect.creaTwoSections() 
sections.append(RightWallRCSect)

DeckExtSlabRCSect= def_simple_RC_section.RCSlabBeamSection('deckExtSlabRCSect',"underpass.",concrete, reinfSteel,0.35)
#[0]: transversal rebars
#[1]: longitudinal rebars
DeckExtSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s250r30,fi20s125r30])
DeckExtSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi26s250r30])
DeckExtSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s250r50])
DeckExtSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s250r56])

DeckExtSlabRCSect.creaTwoSections() 
sections.append(DeckExtSlabRCSect)



DeckIntSlabRCSect= def_simple_RC_section.RCSlabBeamSection('deckIntSlabRCSect',"underpass.",concrete, reinfSteel,0.35)
#[0]: transversal rebars
#[1]: longitudinal rebars
DeckIntSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s250r30])
DeckIntSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s250r30,fi26s250r50])
DeckIntSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi10s250r42])
DeckIntSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s250r56])

DeckIntSlabRCSect.creaTwoSections() 
sections.append(DeckIntSlabRCSect)




