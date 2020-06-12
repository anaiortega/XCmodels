# -*- coding: utf-8 -*-

#import os
import xc_base
import geom
import xc
from materials.sections.fiber_section import def_simple_RC_section as rcs
from materials.ehe import EHE_materials
import math
from postprocess import element_section_map

#Auxiliary data
execfile('../basic_data.py')

rnom=35 #recubrimiento nominal (todos los elementos)


#instances of element_section_map.RCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element


zapRCSects= element_section_map.RCSlabBeamSection(name='zapRCSects',sectionDescr='zapata',concrType=concrete, reinfSteelType=reinfSteel,depth=cantoZap,elemSetName='zap')
#D1: longitudinal rebars
#D2:  transversal rebars
#positiv: top face
#negativ: bottom face
zapRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,200,rnom)])
zapRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom+25)])
zapRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,200,rnom)])
zapRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom+25)])

murestrZ1RCSects= element_section_map.RCSlabBeamSection(name='murestrZ1RCSects',sectionDescr='muro de estribo, zona Z1 (inferior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espMurEstr,elemSetName='murestrZ1')
#D1: vertical rebars
#D2: horizontal rebars
#positiv: interior
#negativ: exterior
murestrZ1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom),rcs.rebLayer_mm(25,200,rnom)])
murestrZ1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,200,rnom+25)])
murestrZ1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
murestrZ1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])

murestrZ2RCSects= element_section_map.RCSlabBeamSection(name='murestrZ2RCSects',sectionDescr='muro de estribo, zona Z2 (superior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espMurEstr,elemSetName='murestrZ2')
#D1: vertical rebars
#D2: horizontal rebars
#positiv: trasdós
#negativ: intradós
murestrZ2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom)])
murestrZ2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,200,rnom+25)])
murestrZ2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
murestrZ2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])

aletiZ1RCSects= element_section_map.RCSlabBeamSection(name='aletiZ1RCSects',sectionDescr='aleta izquierda, zona Z1 (inferior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ1,elemSetName='aletiZ1')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: interior
#negativ: exterior
aletiZ1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom+20)])
aletiZ1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom),rcs.rebLayer_mm(20,200,rnom)])
aletiZ1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
aletiZ1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])

aletiZ2RCSects= element_section_map.RCSlabBeamSection(name='aletiZ2RCSects',sectionDescr='aleta izquierda, zona Z2 (central)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ2,elemSetName='aletiZ2')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: interior
#negativ: exterior
aletiZ2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom+20)])
aletiZ2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom)])
aletiZ2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
aletiZ2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])

aletiZ3RCSects= element_section_map.RCSlabBeamSection(name='aletiZ3RCSects',sectionDescr='aleta izquierda, zona Z3 (superior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ3,elemSetName='aletiZ3')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: interior
#negativ: exterior
aletiZ3RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
aletiZ3RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
aletiZ3RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
aletiZ3RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])

voladziRCSects= element_section_map.RCSlabBeamSection(name='voladziRCSects',sectionDescr='aleta izquierda, voladizo',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ3,elemSetName='voladzi')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: trasdós
#negativ: intradós
voladziRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
voladziRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
voladziRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
voladziRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])

aletdZ1RCSects= element_section_map.RCSlabBeamSection(name='aletdZ1RCSects',sectionDescr='aleta izquierda, zona Z1 (inferior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ1,elemSetName='aletdZ1')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: exterior
#negativ: interior
aletdZ1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
aletdZ1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
aletdZ1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom+20)])
aletdZ1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom),rcs.rebLayer_mm(20,200,rnom)])

aletdZ2RCSects= element_section_map.RCSlabBeamSection(name='aletdZ2RCSects',sectionDescr='aleta izquierda, zona Z2 (central)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ2,elemSetName='aletdZ2')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: exterior
#negativ: interior
aletdZ2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
aletdZ2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
aletdZ2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom+20)])
aletdZ2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom)])

aletdZ3RCSects= element_section_map.RCSlabBeamSection(name='aletdZ3RCSects',sectionDescr='aleta izquierda, zona Z3 (superior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ3,elemSetName='aletdZ3')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: exterior
#negativ: interior
aletdZ3RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
aletdZ3RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
aletdZ3RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+16)])
aletdZ3RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])

