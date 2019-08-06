# -*- coding: utf-8 -*-

#import os
#import xc_base
#import geom
#import xc
from materials.sections.fiber_section import defSimpleRCSection as rcs
from materials.aci import ACI_materials
from postprocess import RC_material_distribution

concrete= ACI_materials.c3000
concrete.gmmC= 1.0/0.75
reinfSteel= ACI_materials.A615G60
#Define available sections for the elements (spatial distribution of RC sections).
reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

# **Concrete sections
#instances of rcs.RecordRCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

rampRCSects= rcs.RecordRCSlabBeamSection(name='rampRCSects',sectionDescr='slab of shell elements',concrType=concrete, reinfSteelType=reinfSteel,depth=rampTh,elemSetName=ramp.name)  
#rampRCSects.dir1PositvRebarRows=[ACI_materials.n3s150r50]
rampRCSects.dir1NegatvRebarRows=[ACI_materials.n3s150r45] #transv
#rampRCSects.dir2PositvRebarRows=[rcs.rebLayer(16,250,35)]
rampRCSects.dir2NegatvRebarRows=[ACI_materials.n3s150r50] #long
