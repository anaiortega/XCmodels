# -*- coding: utf-8 -*-

#import os
#import xc_base
#import geom
#import xc
import math
from materials.sections.fiber_section import def_simple_RC_section as rcs

# **Concrete sections
#instances of rcs.RecordRCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

lCol=0.4
colB1RCsect=rcs.RecordRCSlabBeamSection(name='colB1RCsect',sectionDescr='colB1',concrType=concrete, reinfSteelType=reinfSteel,width=lCol,depth=lCol,elemSetName=colB1.name)
fi=15.875*1e-3
layer=rcs.MainReinfLayer(rebarsDiam=fi,areaRebar=math.pi*fi**2/4.,nominalCover=0.03)
layer.nRebars=3

colB1RCsect.dir1PositvRebarRows=[layer]
colB1RCsect.dir1NegatvRebarRows=[layer]
colB1RCsect.dir2PositvRebarRows=[layer]
colB1RCsect.dir2NegatvRebarRows=[layer]

fiCercosExtr=9.525
sepCercosExtr=8*in2m
colB1RCsect.dir1ShReinfY=rcs.RecordShearReinforcement(familyName= "sh",nShReinfBranches=2,areaShReinfBranch= math.pi*(fiCercosExtr*1e-3)**2/4.,shReinfSpacing=sepCercosExtr,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)
colB1RCsect.dir2ShReinfY=rcs.RecordShearReinforcement(familyName= "sh",nShReinfBranches=2,areaShReinfBranch= math.pi*(fiCercosExtr*1e-3)**2/4.,shReinfSpacing=sepCercosExtr,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)



