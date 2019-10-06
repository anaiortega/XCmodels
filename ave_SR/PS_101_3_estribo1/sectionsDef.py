# -*- coding: utf-8 -*-

#import os
import xc_base
import geom
import xc
from materials.sections.fiber_section import defSimpleRCSection as rcs
from materials.ehe import EHE_materials
import math

#Auxiliary data
execfile('../basic_data.py')

rnom=35 #recubrimiento nominal (todos los elementos)


#instances of rcs.RecordRCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element


zapRCSects= rcs.RecordRCSlabBeamSection(name='zapRCSects',sectionDescr='zapata',concrType=concrete, reinfSteelType=reinfSteel,depth=cantoZap,elemSetName='zap')
#D1: longitudinal rebars
#D2:  transversal rebars
#positiv: top face
#negativ: bottom face
zapRCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(25,100,rnom)]
zapRCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(20,200,rnom+25)]
zapRCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(25,200,rnom)]
zapRCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(20,200,rnom+25)]

murestrZ1RCSects= rcs.RecordRCSlabBeamSection(name='murestrZ1RCSects',sectionDescr='muro de estribo, zona Z1 (inferior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espMurEstr,elemSetName='murestrZ1')
#D1: vertical rebars
#D2: horizontal rebars
#positiv: interior
#negativ: exterior
murestrZ1RCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom),rcs.rebLayer_mm(25,200,rnom)]
murestrZ1RCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom+25)]
murestrZ1RCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(16,200,rnom)]
murestrZ1RCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(20,200,rnom+16)]

murestrZ2RCSects= rcs.RecordRCSlabBeamSection(name='murestrZ2RCSects',sectionDescr='muro de estribo, zona Z2 (superior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espMurEstr,elemSetName='murestrZ2')
#D1: vertical rebars
#D2: horizontal rebars
#positiv: trasdós
#negativ: intradós
murestrZ2RCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom)]
murestrZ2RCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom+25)]
murestrZ2RCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(16,200,rnom)]
murestrZ2RCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(20,200,rnom+16)]

aletiZ1RCSects= rcs.RecordRCSlabBeamSection(name='aletiZ1RCSects',sectionDescr='aleta izquierda, zona Z1 (inferior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ1,elemSetName='aletiZ1')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: interior
#negativ: exterior
aletiZ1RCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom+25)]
aletiZ1RCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom),rcs.rebLayer_mm(25,200,rnom)]
aletiZ1RCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(20,200,rnom+20)]
aletiZ1RCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(20,200,rnom)]

aletiZ2RCSects= rcs.RecordRCSlabBeamSection(name='aletiZ2RCSects',sectionDescr='aleta izquierda, zona Z2 (central)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ2,elemSetName='aletiZ2')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: interior
#negativ: exterior
aletiZ2RCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom+25)]
aletiZ2RCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom)]
aletiZ2RCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(20,200,rnom+20)]
aletiZ2RCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(20,200,rnom)]

aletiZ3RCSects= rcs.RecordRCSlabBeamSection(name='aletiZ3RCSects',sectionDescr='aleta izquierda, zona Z3 (superior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ3,elemSetName='aletiZ3')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: interior
#negativ: exterior
aletiZ3RCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom+25)]
aletiZ3RCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(25,200,rnom)]
aletiZ3RCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(20,200,rnom+20)]
aletiZ3RCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(20,200,rnom)]

aletdZ1RCSects= rcs.RecordRCSlabBeamSection(name='aletdZ1RCSects',sectionDescr='aleta izquierda, zona Z1 (inferior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ1,elemSetName='aletdZ1')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: exterior
#negativ: interior
aletdZ1RCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(20,200,rnom+20)]
aletdZ1RCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(20,200,rnom)]
aletdZ1RCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(25,200,rnom+25)]
aletdZ1RCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(25,200,rnom),rcs.rebLayer_mm(25,200,rnom)]

aletdZ2RCSects= rcs.RecordRCSlabBeamSection(name='aletdZ2RCSects',sectionDescr='aleta izquierda, zona Z2 (central)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ2,elemSetName='aletdZ2')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: exterior
#negativ: interior
aletdZ2RCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(20,200,rnom+20)]
aletdZ2RCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(20,200,rnom)]
aletdZ2RCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(25,200,rnom+25)]
aletdZ2RCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(25,200,rnom)]

aletdZ3RCSects= rcs.RecordRCSlabBeamSection(name='aletdZ3RCSects',sectionDescr='aleta izquierda, zona Z3 (superior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ3,elemSetName='aletdZ3')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: exterior
#negativ: interior
aletdZ3RCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(20,200,rnom+20)]
aletdZ3RCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(20,200,rnom)]
aletdZ3RCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(25,200,rnom+25)]
aletdZ3RCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(25,200,rnom)]

voladzdRCSects= rcs.RecordRCSlabBeamSection(name='voladzdRCSects',sectionDescr='aleta izquierda, zona Z3 (superior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ3,elemSetName='voladzd')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: exterior
#negativ: interior
voladzdRCSects.dir1PositvRebarRows=[rcs.rebLayer_mm(16,200,rnom+16)]
voladzdRCSects.dir2PositvRebarRows=[rcs.rebLayer_mm(16,200,rnom)]
voladzdRCSects.dir1NegatvRebarRows=[rcs.rebLayer_mm(16,200,rnom+16)]
voladzdRCSects.dir2NegatvRebarRows=[rcs.rebLayer_mm(16,200,rnom)]
