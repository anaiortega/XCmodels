# -*- coding: utf-8 -*-

#import os
import xc_base
import geom
import xc
from materials.sections.fiber_section import def_simple_RC_section
#from materials.ehe import EHE_materials
from materials.ec2 import EC2_materials
import math

#Auxiliary data
execfile('../basic_data.py')

def rebars(fi,s,c):
    '''fi: bar diameter [mm], s: spacing [mm], c: cover [mm]
    '''
    return def_simple_RC_section.MainReinfLayer(rebarsDiam=fi*1e-3,areaRebar= math.pi*(fi*1e-3)**2/4.0,rebarsSpacing=s*1e-3,width=1.0,nominalCover=c*1e-3)

rnom=35 #recubrimiento nominal 


#instances of def_simple_RC_section.RCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

losSupV2RCSects= def_simple_RC_section.RCSlabBeamSection(name='losSupV2RCSects',sectionDescr='losa aligerada, cara superior.',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSetName='losSupV2')
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losSupV2RCSects.dir1PositvRebarRows=[rebars(16,200,rnom)]
losSupV2RCSects.dir1NegatvRebarRows=[rebars(12,200,rnom)]
losSupV2RCSects.dir2PositvRebarRows=[rebars(16,200,rnom+20)]
losSupV2RCSects.dir2NegatvRebarRows=[rebars(12,200,rnom+20)]


losInfV2RCSects= def_simple_RC_section.RCSlabBeamSection(name='losInfV2RCSects',sectionDescr='losa aligerada, cara superior',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSetName='losInfV2')
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losInfV2RCSects.dir1NegatvRebarRows=[rebars(14,200,rnom)]
losInfV2RCSects.dir1PositvRebarRows=[rebars(8,200,rnom)]
losInfV2RCSects.dir2NegatvRebarRows=[rebars(20,100,rnom+16)]
losInfV2RCSects.dir2PositvRebarRows=[rebars(15,100,rnom+16)]

voladzCentV2RCSects= def_simple_RC_section.RCSlabBeamSection(name='voladzCentV2RCSects',sectionDescr='voladizo, zona central vano',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMax,elemSetName='voladzCentV2')
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
voladzCentV2RCSects.dir1PositvRebarRows=[rebars(20,200,rnom)]
voladzCentV2RCSects.dir2PositvRebarRows=[rebars(20,200,rnom+20)]
voladzCentV2RCSects.dir1NegatvRebarRows=[rebars(12,200,rnom)]
voladzCentV2RCSects.dir2NegatvRebarRows=[rebars(16,200,rnom+12)]

voladzExtrV2RCSects= def_simple_RC_section.RCSlabBeamSection(name='voladzExtrV2RCSects',sectionDescr='voladizo, zona exterior vano',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMin,elemSetName='voladzExtrV2')
#D1: transversal rebars
#D2: longitudinal rebars
voladzExtrV2RCSects.dir1PositvRebarRows=[rebars(20,200,rnom)]
voladzExtrV2RCSects.dir2PositvRebarRows=[rebars(20,200,rnom+20)]
voladzExtrV2RCSects.dir1NegatvRebarRows=[rebars(12,200,rnom)]
voladzExtrV2RCSects.dir2NegatvRebarRows=[rebars(16,200,rnom+12)]


losSupRP1RCSects= def_simple_RC_section.RCSlabBeamSection(name='losSupRP1RCSects',sectionDescr='riostra sobre pila, cara superior.',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSetName='losSupRP1')
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losSupRP1RCSects.dir1PositvRebarRows=[rebars(25,125,rnom)]
losSupRP1RCSects.dir1NegatvRebarRows=[rebars(25,125,rnom+40)]
losSupRP1RCSects.dir2PositvRebarRows=[rebars(32,100,rnom),rebars(20,200,rnom)]
losSupRP1RCSects.dir2NegatvRebarRows=[rebars(16,200,rnom+40)]

losInfRP1RCSects= def_simple_RC_section.RCSlabBeamSection(name='losInfRP1RCSects',sectionDescr='riostra sobre pila, cara inferior',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSetName='losInfRP1')
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losInfRP1RCSects.dir1NegatvRebarRows=[rebars(16,125,rnom),rebars(25,125,rnom+16)]
losInfRP1RCSects.dir1PositvRebarRows=[rebars(16,50,rnom+40)]
losInfRP1RCSects.dir2NegatvRebarRows=[rebars(25,200,rnom)]
losInfRP1RCSects.dir2PositvRebarRows=[rebars(16,50,rnom+40)]

voladzCentRP1RCSects= def_simple_RC_section.RCSlabBeamSection(name='voladzCentRP1RCSects',sectionDescr='voladizo, zona central riostra pila',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMax,elemSetName='voladzCentRP1')
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
voladzCentRP1RCSects.dir1PositvRebarRows=[rebars(25,125,rnom)]
voladzCentRP1RCSects.dir2PositvRebarRows=[rebars(20,200,rnom+25)]
voladzCentRP1RCSects.dir1NegatvRebarRows=[rebars(12,125,rnom)]
voladzCentRP1RCSects.dir2NegatvRebarRows=[rebars(16,200,rnom+12)]

voladzExtrRP1RCSects= def_simple_RC_section.RCSlabBeamSection(name='voladzExtrRP1RCSects',sectionDescr='voladizo, zona exterior riostra pila',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMax,elemSetName='voladzExtrRP1')
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
voladzExtrRP1RCSects.dir1PositvRebarRows=[rebars(25,125,rnom)]
voladzExtrRP1RCSects.dir2PositvRebarRows=[rebars(20,200,rnom+25)]
voladzExtrRP1RCSects.dir1NegatvRebarRows=[rebars(12,125,rnom)]
voladzExtrRP1RCSects.dir2NegatvRebarRows=[rebars(16,200,rnom+12)]

murAligV2RCSects= def_simple_RC_section.RCSlabBeamSection(name='murAligV2RCSects',sectionDescr='diafragmas entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espEntreAlig,elemSetName='murAligV2')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: top face
#negativ: bottom face
murAligV2RCSects.dir1PositvRebarRows=[rebars(8,100,rnom +12)]
murAligV2RCSects.dir1NegatvRebarRows=[rebars(8,100,rnom+12)]
murAligV2RCSects.dir2PositivRebarRows=[rebars(12,200,rnom)]
murAligV2RCSects.dir2NegatvRebarRows=[rebars(12,200,rnom)]
'''
murExtAligRCSects= def_simple_RC_section.RCSlabBeamSection(name='murExtAligRCSects',sectionDescr='diafragma entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espExtAlig,elemSetName='murExtAlig')
#D1: horizontal rebars
#D2: vertical rebars
#positiv: top face
#negativ: bottom face
murExtAligRCSects.dir1PositvRebarRows=[rebars(20,150,rnom)]
murExtAligRCSects.dir2PositvRebarRows=[rebars(12,200,rnom),rebars(16,200,rnom)]
murExtAligRCSects.dir2NegatvRebarRows=[rebars(12,200,rnom)]

riostrEstr1RCSects= def_simple_RC_section.RCSlabBeamSection(name='riostrEstr1RCSects',sectionDescr='diafragma entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espRiostrEstr,elemSetName='riostrEstr1')
#D1: vertical rebars
#D2: horizontal rebars
#positiv: cara +y
#negativ: cara -y
riostrEstr1RCSects.dir1PositvRebarRows=[rebars(12,200,rnom),rebars(12,200,rnom+150)]
riostrEstr1RCSects.dir1NegatvRebarRows=[rebars(12,200,rnom),rebars(12,200,rnom+150)]
riostrEstr1RCSects.dir2PositvRebarRows=[rebars(12,200,rnom+12),rebars(16,200,rnom+12)]
riostrEstr1RCSects.dir2NegatvRebarRows=[rebars(12,200,rnom+12)]

riostrPilRCSects= def_simple_RC_section.RCSlabBeamSection(name='riostrPilRCSects',sectionDescr='diafragma entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espRiostrPila,elemSetName='riostrPil')
#D1: vertical rebars
#D2: horizontal rebars
#positiv: cara +y
#negativ: cara -y
riostrPilRCSects.dir1PositvRebarRows=[rebars(12,200,rnom),rebars(12,200,rnom+150)]
riostrPilRCSects.dir1NegatvRebarRows=[rebars(12,200,rnom),rebars(12,200,rnom+150)]
riostrPilRCSects.dir2PositvRebarRows=[rebars(12,200,rnom+12),rebars(16,200,rnom+12)]
riostrPilRCSects.dir2NegatvRebarRows=[rebars(12,200,rnom+12)]
'''

