# -*- coding: utf-8 -*-

#import os
import xc_base
import geom
import xc
from materials.sections.fiber_section import def_simple_RC_section
from postprocess import element_section_map
#from materials.ehe import EHE_materials
from materials.ec2 import EC2_materials
import math

#Auxiliary data
exec(open('../basic_data.py').read())

def rebars(fi,s,c):
    '''fi: bar diameter [mm], s: spacing [mm], c: cover [mm]
    '''
    return def_simple_RC_section.ReinfRow(rebarsDiam=fi*1e-3,areaRebar= math.pi*(fi*1e-3)**2/4.0,rebarsSpacing=s*1e-3,width=1.0,nominalCover=c*1e-3)

rnom=35 #recubrimiento nominal 


#instances of element_section_map.RCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

losSupV2RCSects= element_section_map.RCSlabBeamSection(name='losSupV2RCSects',sectionDescr='losa aligerada, cara superior.',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSet=losSupV2)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losSupV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,200,rnom)])
losSupV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom)])
losSupV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,200,rnom+20)])
losSupV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom+20)])


losInfV2RCSects= element_section_map.RCSlabBeamSection(name='losInfV2RCSects',sectionDescr='losa aligerada, cara superior',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSet=losInfV2)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losInfV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(14,200,rnom)])
losInfV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(8,200,rnom)])
losInfV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(20,100,rnom+16)])
losInfV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(15,100,rnom+16)])

voladzCentV2RCSects= element_section_map.RCSlabBeamSection(name='voladzCentV2RCSects',sectionDescr='voladizo, zona central vano',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMax,elemSet=voladzCentV2)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
voladzCentV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(20,200,rnom)])
voladzCentV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(20,200,rnom+20)])
voladzCentV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom)])
voladzCentV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,200,rnom+12)])

voladzExtrV2RCSects= element_section_map.RCSlabBeamSection(name='voladzExtrV2RCSects',sectionDescr='voladizo, zona exterior vano',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMin,elemSet=voladzExtrV2)
#D1: transversal rebars
#D2: longitudinal rebars
voladzExtrV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(20,200,rnom)])
voladzExtrV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(20,200,rnom+20)])
voladzExtrV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom)])
voladzExtrV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,200,rnom+12)])


losSupRP1RCSects= element_section_map.RCSlabBeamSection(name='losSupRP1RCSects',sectionDescr='riostra sobre pila, cara superior.',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSet=losSupRP1)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losSupRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(25,125,rnom)])
losSupRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(25,125,rnom+40)])
losSupRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(32,100,rnom),rebars(20,200,rnom)])
losSupRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,200,rnom+40)])

losInfRP1RCSects= element_section_map.RCSlabBeamSection(name='losInfRP1RCSects',sectionDescr='riostra sobre pila, cara inferior',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSet=losInfRP1)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losInfRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,125,rnom),rebars(25,125,rnom+16)])
losInfRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,50,rnom+40)])
losInfRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(25,200,rnom)])
losInfRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,50,rnom+40)])

voladzCentRP1RCSects= element_section_map.RCSlabBeamSection(name='voladzCentRP1RCSects',sectionDescr='voladizo, zona central riostra pila',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMax,elemSet=voladzCentRP1)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
voladzCentRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(25,125,rnom)])
voladzCentRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(20,200,rnom+25)])
voladzCentRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,125,rnom)])
voladzCentRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,200,rnom+12)])

voladzExtrRP1RCSects= element_section_map.RCSlabBeamSection(name='voladzExtrRP1RCSects',sectionDescr='voladizo, zona exterior riostra pila',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMax,elemSet=voladzExtrRP1)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
voladzExtrRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(25,125,rnom)])
voladzExtrRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(20,200,rnom+25)])
voladzExtrRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,125,rnom)])
voladzExtrRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(16,200,rnom+12)])

murAligV2RCSects= element_section_map.RCSlabBeamSection(name='murAligV2RCSects',sectionDescr='diafragmas entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espEntreAlig,elemSet=murAligV2)
#D1: horizontal rebars
#D2: vertical rebars
#positiv: top face
#negativ: bottom face
murAligV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(8,100,rnom +12)])
murAligV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(8,100,rnom+12)])
murAligV2RCSects.dir2PositivRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom)])
murAligV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom)])
'''
murExtAligRCSects= element_section_map.RCSlabBeamSection(name='murExtAligRCSects',sectionDescr='diafragma entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espExtAlig,elemSet=murExtAlig)
#D1: horizontal rebars
#D2: vertical rebars
#positiv: top face
#negativ: bottom face
murExtAligRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(20,150,rnom)])
murExtAligRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom),rebars(16,200,rnom)])
murExtAligRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom)])

riostrEstr1RCSects= element_section_map.RCSlabBeamSection(name='riostrEstr1RCSects',sectionDescr='diafragma entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espRiostrEstr,elemSet=riostrEstr1)
#D1: vertical rebars
#D2: horizontal rebars
#positiv: cara +y
#negativ: cara -y
riostrEstr1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom),rebars(12,200,rnom+150)])
riostrEstr1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom),rebars(12,200,rnom+150)])
riostrEstr1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom+12),rebars(16,200,rnom+12)])
riostrEstr1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom+12)])

riostrPilRCSects= element_section_map.RCSlabBeamSection(name='riostrPilRCSects',sectionDescr='diafragma entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espRiostrPila,elemSet=riostrPil)
#D1: vertical rebars
#D2: horizontal rebars
#positiv: cara +y
#negativ: cara -y
riostrPilRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom),rebars(12,200,rnom+150)])
riostrPilRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom),rebars(12,200,rnom+150)])
riostrPilRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom+12),rebars(16,200,rnom+12)])
riostrPilRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rebars(12,200,rnom+12)])
'''

