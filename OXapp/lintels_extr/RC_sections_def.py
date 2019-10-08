# -*- coding: utf-8 -*-

#import os
#import xc_base
#import geom
#import xc
from materials.sections.fiber_section import defSimpleRCSection as rcs
from materials.aci import ACI_materials
ft2m=0.3048
in2m=0.0254

concrete= ACI_materials.c3000
concrete.gmmC= 1.0/0.75
reinfSteel= ACI_materials.A615G60

# **Concrete sections
#instances of rcs.RecordRCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element


beamCentRCsect=rcs.RecordRCSlabBeamSection(name='beamCentRCsect',sectionDescr='beam elements',concrType=concrete, reinfSteelType=reinfSteel,width=wBeam,depth=hBeam,elemSetName=beamCent.name)
beamCentRCsect.dir1PositvRebarRows=[rcs.rebLayerByNumFi_mm(5,22.225,35,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(2,22.225,hBeam/3.*1e3,35,wBeam*1e3)]
beamCentRCsect.dir1NegatvRebarRows=[rcs.rebLayerByNumFi_mm(5,25.4,35,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(5,25.4,100,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(2,22.225,hBeam/3.*1e3,35,wBeam*1e3)]
beamCentRCsect.dir2PositvRebarRows=[rcs.rebLayerByNumFi_mm(5,22.225,35,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(2,22.225,hBeam/3.*1e3,35,wBeam*1e3)]
beamCentRCsect.dir2NegatvRebarRows=[rcs.rebLayerByNumFi_mm(5,25.4,35,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(5,25.4,100,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(2,22.225,hBeam/3.*1e3,35,wBeam*1e3)]

fiCercosCent=6.35
sepCercosCent=8*in2m
beamCentRCsect.dir1ShReinfY=rcs.RecordShearReinforcement(familyName= "sh",nShReinfBranches=2,areaShReinfBranch= math.pi*(fiCercosCent*1e-3)**2/4.,shReinfSpacing=sepCercosCent,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)
beamCentRCsect.dir2ShReinfY=rcs.RecordShearReinforcement(familyName= "sh",nShReinfBranches=2,areaShReinfBranch= math.pi*(fiCercosCent*1e-3)**2/4.,shReinfSpacing=sepCercosCent,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)

beamExtrRCsect=rcs.RecordRCSlabBeamSection(name='beamExtrRCsect',sectionDescr='beam elements',concrType=concrete, reinfSteelType=reinfSteel,width=wBeam,depth=hBeam,elemSetName=beamExtr.name)
beamExtrRCsect.dir1PositvRebarRows=[rcs.rebLayerByNumFi_mm(5,22.225,35,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(2,22.225,hBeam/3.*1e3,35,wBeam*1e3)]
beamExtrRCsect.dir1NegatvRebarRows=[rcs.rebLayerByNumFi_mm(5,25.4,35,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(2,22.225,hBeam/3.*1e3,35,wBeam*1e3)]
beamExtrRCsect.dir2PositvRebarRows=[rcs.rebLayerByNumFi_mm(5,22.225,35,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(2,22.225,hBeam/3.*1e3,35,wBeam*1e3)]
beamExtrRCsect.dir2NegatvRebarRows=[rcs.rebLayerByNumFi_mm(5,25.4,35,35,wBeam*1e3),rcs.rebLayerByNumFi_mm(2,22.225,hBeam/3.*1e3,35,wBeam*1e3)]

fiCercosExtr=9.525
sepCercosExtr=8*in2m
beamExtrRCsect.dir1ShReinfY=rcs.RecordShearReinforcement(familyName= "sh",nShReinfBranches=2,areaShReinfBranch= math.pi*(fiCercosExtr*1e-3)**2/4.,shReinfSpacing=sepCercosExtr,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)
beamExtrRCsect.dir2ShReinfY=rcs.RecordShearReinforcement(familyName= "sh",nShReinfBranches=2,areaShReinfBranch= math.pi*(fiCercosExtr*1e-3)**2/4.,shReinfSpacing=sepCercosExtr,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)

columnRCsect=rcs.RecordRCSlabBeamSection(name='columnRCsect',sectionDescr='column',concrType=concrete, reinfSteelType=reinfSteel,width=wColumn,depth=dimYColumn,elemSetName=column.name)

columnRCsect.dir1PositvRebarRows=[rcs.rebLayerByNumFi_mm(2,15.875,35,35,wColumn*1e3)]
columnRCsect.dir1NegatvRebarRows=[rcs.rebLayerByNumFi_mm(2,15.875,35,35,wColumn*1e3)]
columnRCsect.dir2PositvRebarRows=[rcs.rebLayerByNumFi_mm(2,15.875,35,35,wColumn*1e3)]
columnRCsect.dir2NegatvRebarRows=[rcs.rebLayerByNumFi_mm(2,15.875,35,35,wColumn*1e3)]



