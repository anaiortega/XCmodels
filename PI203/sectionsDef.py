# -*- coding: utf-8 -*-

import math
import os
import geom
import xc
# Macros

from materials.sections.fiber_section import def_simple_RC_section
from postprocess import RC_material_distribution



from materials.sia262 import SIA262_materials as concrete
from materials.sia262 import SIA262_materials
from materials.sia262 import SIA262_materials
from materials.sia262 import SIA262_limit_state_checking
from postprocess import limit_state_data as lsd
from postprocess import element_section_map

#Thickness of the elements
upDeckTh=1.0
downDeckTh=1.0
upWallTh=0.7
downWallTh=1.0
midWallTh=0.7
baseSlabTh=1.1


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

concrete= concrete.c30_37
reinfSteel= SIA262_materials.B500A

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

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
fi26s150r35=def_simple_RC_section.ReinfRow(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)


UpDeckExtSlabRCSect= element_section_map.RCSlabBeamSection('upDeckExtSlabRCSect',"underpass.",concrete, reinfSteel,upDeckTh)
#[0]: transversal rebars
#[1]: longitudinal rebars
UpDeckExtSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35,fi20s150r35])
UpDeckExtSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])
UpDeckExtSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
UpDeckExtSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(UpDeckExtSlabRCSect)

UpDeckIntSlabRCSect= element_section_map.RCSlabBeamSection('upDeckIntSlabRCSect',"underpass.",concrete, reinfSteel,upDeckTh)
#[0]: transversal rebars
#[1]: longitudinal rebars
UpDeckIntSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
UpDeckIntSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi26s150r35,fi22s150r35])
UpDeckIntSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
UpDeckIntSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi18s150r35])

sections.append(UpDeckIntSlabRCSect)

DownDeckExtSlabRCSect= element_section_map.RCSlabBeamSection('downDeckExtSlabRCSect',"underpass.",concrete, reinfSteel,downDeckTh)
#[0]: transversal rebars
#[1]: longitudinal rebars
DownDeckExtSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35,fi16s150r35])
DownDeckExtSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])
DownDeckExtSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
DownDeckExtSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(DownDeckExtSlabRCSect)

DownDeckIntSlabRCSect= element_section_map.RCSlabBeamSection('downDeckIntSlabRCSect',"underpass.",concrete, reinfSteel,downDeckTh)
#[0]: transversal rebars
#[1]: longitudinal rebars
DownDeckIntSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
DownDeckIntSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi26s150r35,fi22s150r35])
DownDeckIntSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
DownDeckIntSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi18s150r35])

sections.append(DownDeckIntSlabRCSect)

FoundExtSlabRCSect= element_section_map.RCSlabBeamSection(name='foundExtSlabRCSect',sectionDescr="underpass.",depth=baseSlabTh,concrType=concrete, reinfSteelType=reinfSteel)
#[0]: transversal rebars
#[1]: longitudinal rebars
FoundExtSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35])
FoundExtSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35,fi16s150r35])
FoundExtSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
FoundExtSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(FoundExtSlabRCSect)

FoundIntSlabRCSect= element_section_map.RCSlabBeamSection('foundIntSlabRCSect',"underpass.",concrete, reinfSteel,baseSlabTh)
#[0]: transversal rebars
#[1]: longitudinal rebars
FoundIntSlabRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35,fi22s150r35])
FoundIntSlabRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
FoundIntSlabRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi20s150r35])
FoundIntSlabRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(FoundIntSlabRCSect)

LeftUpWallRCSect= element_section_map.RCSlabBeamSection('leftUpWallRCSect',"underpass.",concrete, reinfSteel,upWallTh)
#[0]: horizontal rebars
#[1]: vertical rebars
LeftUpWallRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
LeftUpWallRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
LeftUpWallRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
LeftUpWallRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35,fi20s150r35])

sections.append(LeftUpWallRCSect)

RightUpWallRCSect= element_section_map.RCSlabBeamSection('rightUpWallRCSect',"underpass.",concrete, reinfSteel,upWallTh)
#[0]: horizontal rebars
#[1]: vertical rebars
RightUpWallRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
RightUpWallRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
RightUpWallRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35,fi20s150r35])
RightUpWallRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(RightUpWallRCSect)

LeftDownWallRCSect= element_section_map.RCSlabBeamSection('leftDownWallRCSect',"underpass.",concrete, reinfSteel,downWallTh)
#[0]: horizontal rebars
#[1]: vertical rebars
LeftDownWallRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
LeftDownWallRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
LeftDownWallRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
LeftDownWallRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35,fi20s150r35])

sections.append(LeftDownWallRCSect)

RightDownWallRCSect= element_section_map.RCSlabBeamSection('rightDownWallRCSect',"underpass.",concrete, reinfSteel,downWallTh)
#[0]: horizontal rebars
#[1]: vertical rebars
RightDownWallRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
RightDownWallRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
RightDownWallRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi22s150r35,fi20s150r35])
RightDownWallRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(RightDownWallRCSect)

MidWallRCSect= element_section_map.RCSlabBeamSection('midWallRCSect',"underpass.",concrete, reinfSteel,midWallTh)
#[0]: horizontal rebars
#[1]: vertical rebars
MidWallRCSect.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
MidWallRCSect.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
MidWallRCSect.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])
MidWallRCSect.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([fi16s150r35])

sections.append(MidWallRCSect)





