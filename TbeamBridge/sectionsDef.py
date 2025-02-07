# -*- coding: utf-8 -*-

import math
import os
import geom
import xc
# Macros
#from materials.ehe import auxEHE
from materials.sections.fiber_section import def_simple_RC_section
from materials.sections import section_properties
from materials.xLamina import membranePlateRCSectionContainer as sc


from materials.sia262 import SIA262_materials
#from materials.ehe import EHE_materials
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

concrete= SIA262_materials.c30_37
reinfSteel= SIA262_materials.B500A
sections= sc.SectionContainer()

#Generic layers (rows of rebars)
fi8s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi8s125r44=def_simple_RC_section.ReinfRow(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing=0.125,width=1.0,nominalCover=0.044)
fi10s200r44=def_simple_RC_section.ReinfRow(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi10s250r42=def_simple_RC_section.ReinfRow(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.250,width=1.0,nominalCover=0.042)
fi12s250r30=def_simple_RC_section.ReinfRow(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.250,width=1.0,nominalCover=0.030)
fi12s250r46=def_simple_RC_section.ReinfRow(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.250,width=1.0,nominalCover=0.046)
fi12s150r35=def_simple_RC_section.ReinfRow(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi14s250r30=def_simple_RC_section.ReinfRow(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing=0.25,width=1.0,nominalCover=0.030)
fi14s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi16s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi16s250r50=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.250,width=1.0,nominalCover=0.050)
fi16s150r35=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi16s250r56=def_simple_RC_section.ReinfRow(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.250,width=1.0,nominalCover=0.056)
fi18s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi18s125r44=def_simple_RC_section.ReinfRow(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing=0.125,width=1.0,nominalCover=0.044)
fi18s150r35=def_simple_RC_section.ReinfRow(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi20s250r30=def_simple_RC_section.ReinfRow(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.250,width=1.0,nominalCover=0.030)
fi20s150r35=def_simple_RC_section.ReinfRow(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi22s150r35=def_simple_RC_section.ReinfRow(rebarsDiam=22e-3,areaRebar= areaFi22,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi20s125r30=def_simple_RC_section.ReinfRow(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi20s125r50=def_simple_RC_section.ReinfRow(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.125,width=1.0,nominalCover=0.050)
fi26s250r30=def_simple_RC_section.ReinfRow(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing=0.250,width=1.0,nominalCover=0.030)
fi26s250r50=def_simple_RC_section.ReinfRow(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing=0.250,width=1.0,nominalCover=0.050)

DeckExtSlabRCSect= element_section_map.RCSlabBeamSection('deckExtSlab',"underpass.",concrete, reinfSteel,0.55)
#D1: transversal rebars
#D2: longitudinal rebars
DeckExtSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35,fi12s150r35])
DeckExtSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
DeckExtSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
DeckExtSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])

sections.append(DeckExtSlabRCSect)

DeckIntSlabRCSect= element_section_map.RCSlabBeamSection('deckIntSlab',"underpass.",concrete, reinfSteel,0.5)
#D1: transversal rebars
#D2: longitudinal rebars
DeckIntSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
DeckIntSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35,fi22s150r35])
DeckIntSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
DeckIntSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi18s150r35])

sections.append(DeckIntSlabRCSect)

FoundExtSlabRCSect= element_section_map.RCSlabBeamSection(name='foundExtSlab',sectionDescr="underpass.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.60)
#D1: transversal rebars
#D2: longitudinal rebars
FoundExtSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
FoundExtSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35,fi12s150r35])
FoundExtSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
FoundExtSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])

sections.append(FoundExtSlabRCSect)

FoundIntSlabRCSect= element_section_map.RCSlabBeamSection('foundIntSlab',"underpass.",concrete, reinfSteel,0.60)
#D1: transversal rebars
#D2: longitudinal rebars
FoundIntSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35,fi20s150r35])
FoundIntSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
FoundIntSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
FoundIntSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])

sections.append(FoundIntSlabRCSect)

LeftWallRCSect= element_section_map.RCSlabBeamSection('leftWall',"underpass.",concrete, reinfSteel,0.45)
#D1: horizontal rebars
#D2: vertical rebars
LeftWallRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
LeftWallRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
LeftWallRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
LeftWallRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35,fi16s150r35])

sections.append(LeftWallRCSect)

RightWallRCSect= element_section_map.RCSlabBeamSection('rightWall',"underpass.",concrete, reinfSteel,0.45)
#D1: horizontal rebars
#D2: vertical rebars
RightWallRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
RightWallRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])
RightWallRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35,fi16s150r35])
RightWallRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi12s150r35])

sections.append(RightWallRCSect)





