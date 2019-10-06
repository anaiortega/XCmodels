# -*- coding: utf-8 -*-

#import os
#import xc_base
#import geom
#import xc
from materials.sections.fiber_section import defSimpleRCSection as rcs

# **Concrete sections
#instances of rcs.RecordRCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element


beamRCsect=rcs.RecordRCSlabBeamSection(name='beamRCsect',sectionDescr='beam elements',concrType=concrete, reinfSteelType=reinfSteel,width=wBeam,depth=hBeam,elemSetName=beam.name)
'''
beamRCsect.dir1PositvRebarRows=[rcs.rebLayerByNumFi_mm(4,25,30,wBeam*1e3),rcs.rebLayerByNumFi_mm(4,20,60,wBeam*1e3)]
beamRCsect.dir1NegatvRebarRows=[rcs.rebLayerByNumFi_mm(4,16,30,wBeam*1e3)]
beamRCsect.dir2PositvRebarRows=[rcs.rebLayerByNumFi_mm(5,25,30,wBeam*1e3),rcs.rebLayerByNumFi_mm(4,20,60,wBeam*1e3)]
beamRCsect.dir2NegatvRebarRows=[rcs.rebLayerByNumFi_mm(4,16,30,wBeam*1e3)]
'''
beamRCsect.dir1PositvRebarRows=[rcs.rebLayerByNumFi_mm(4,16,30,wBeam*1e3)]
beamRCsect.dir1NegatvRebarRows=[rcs.rebLayerByNumFi_mm(4,25,30,wBeam*1e3),rcs.rebLayerByNumFi_mm(4,20,60,wBeam*1e3)]
beamRCsect.dir2PositvRebarRows=[rcs.rebLayerByNumFi_mm(4,16,30,wBeam*1e3)]
beamRCsect.dir2NegatvRebarRows=[rcs.rebLayerByNumFi_mm(5,25,30,wBeam*1e3),rcs.rebLayerByNumFi_mm(4,20,60,wBeam*1e3)]

columnRCsect=rcs.RecordRCSlabBeamSection(name='columnRCsect',sectionDescr='column',concrType=concrete, reinfSteelType=reinfSteel,width=wColumn,depth=dimYColumn,elemSetName=column.name)

columnRCsect.dir1PositvRebarRows=[rcs.rebLayer_mm(12,150,35)]
columnRCsect.dir1NegatvRebarRows=[rcs.rebLayer_mm(12,150,35)]
columnRCsect.dir2PositvRebarRows=[rcs.rebLayer_mm(12,150,35)]
columnRCsect.dir2NegatvRebarRows=[rcs.rebLayer_mm(12,150,35)]



