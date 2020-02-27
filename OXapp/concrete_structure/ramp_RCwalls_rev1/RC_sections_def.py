# -*- coding: utf-8 -*-

#import os
#import xc_base
#import geom
#import xc
from materials.sections.fiber_section import def_simple_RC_section as rcs
in2mm=25.4
#diameters
fi_3=9.525 #diameter [mm] #3
fi_4=12.7
fi_5=15.875
fi_6=19.05

# **Concrete sections
#instances of rcs.RecordRCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

#EB: East basement
#WB: West basement
#E1F: East first floor
#S1F: South first floor
#W1F: West first floor

EBwallRCSects= rcs.RecordRCSlabBeamSection(name='EBwallRCSects',sectionDescr='East basement wall',concrType=concrete, reinfSteelType=reinfSteel,depth=wallThBasement,elemSetName=EastBasementWall.name)
#dir1: horizontal
#dir2: vertical
EBwallRCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior
EBwallRCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior
EBwallRCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior
EBwallRCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior

WBwallRCSects= rcs.RecordRCSlabBeamSection(name='WBwallRCSects',sectionDescr='West basement wall',concrType=concrete, reinfSteelType=reinfSteel,depth=wallThBasement,elemSetName=WestBasementWall.name)
#dir1: horizontal
#dir2: vertical
WBwallRCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior
WBwallRCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior
WBwallRCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior
WBwallRCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior

E1FwallRCSects= rcs.RecordRCSlabBeamSection(name='E1FwallRCSects',sectionDescr='East first floor wall',concrType=concrete, reinfSteelType=reinfSteel,depth=wallThFirstFloor,elemSetName=East1FloorWall.name)
#dir1: horizontal
#dir2: vertical
E1FwallRCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior
E1FwallRCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior
E1FwallRCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior
E1FwallRCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior

W1FwallRCSects= rcs.RecordRCSlabBeamSection(name='W1FwallRCSects',sectionDescr='West first floor wall',concrType=concrete, reinfSteelType=reinfSteel,depth=wallThFirstFloor,elemSetName=West1FloorWall.name)
#dir1: horizontal
#dir2: vertical
W1FwallRCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior
W1FwallRCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior
W1FwallRCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior
W1FwallRCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior

S1FwallRCSects= rcs.RecordRCSlabBeamSection(name='S1FwallRCSects',sectionDescr='South first floor wall',concrType=concrete, reinfSteelType=reinfSteel,depth=wallThFirstFloor,elemSetName=South1FloorWall.name)
#dir1: vertical
#dir2: horizontal
S1FwallRCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior
S1FwallRCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior
S1FwallRCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #exterior
S1FwallRCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(fi_4,8*in2mm,35)] #interior
