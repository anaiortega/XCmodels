# -*- coding: utf-8 -*-

#import os
import geom
import xc
from materials.sections.fiber_section import def_simple_RC_section as rcs
from postprocess import element_section_map
#from materials.ehe import EHE_materials
from materials.ec2 import EC2_materials
import math

#Auxiliary data
exec(open('../basic_data.py').read())

rnom=35 #recubrimiento nominal 

areaFi16= math.pi*(16*1e-3)**2/4.0

#instances of element_section_map.RCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element

losSupV2RCSects= element_section_map.RCSlabBeamSection(name='losSupV2RCSects',sectionDescr='losa aligerada, cara superior.',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSet=losSupV2)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losSupV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,400,rnom)])
losSupV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,400,rnom+espLosAlig/2.)])
losSupV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom+20)])
losSupV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom+espLosAlig/2.)])


losInfV2RCSects= element_section_map.RCSlabBeamSection(name='losInfV2RCSects',sectionDescr='losa aligerada, cara superior',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSet=losInfV2)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losInfV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,400,rnom)])
losInfV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,400,rnom++espLosAlig/2.0)])
losInfV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(32,200,rnom+16)])
losInfV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom+espLosAlig/2.0)])

losInfV1RCSects= element_section_map.RCSlabBeamSection(name='losInfV1RCSects',sectionDescr='losa aligerada, cara superior',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSet=losInfV1)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losInfV1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,400,rnom)])
losInfV1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,400,rnom++espLosAlig/2.0)])
losInfV1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,200,rnom+16)])
losInfV1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,200,rnom+espLosAlig/2.0)])

voladzCentV2RCSects= element_section_map.RCSlabBeamSection(name='voladzCentV2RCSects',sectionDescr='voladizo, zona central vano',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMax,elemSet=voladzCentV2)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
voladzCentV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,400,rnom),rcs.rebLayer_mm(25,400,rnom)])
voladzCentV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,20,rnom+25)])
voladzCentV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom)])
voladzCentV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom+12)])

voladzExtrV2RCSects= element_section_map.RCSlabBeamSection(name='voladzExtrV2RCSects',sectionDescr='voladizo, zona exterior vano',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMin,elemSet=voladzExtrV2)
#D1: transversal rebars
#D2: longitudinal rebars
voladzExtrV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,400,rnom),rcs.rebLayer_mm(25,400,rnom)])
voladzExtrV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,200,rnom+25)])
voladzExtrV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom)])
voladzExtrV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom+12)])



losSupRP1RCSects= element_section_map.RCSlabBeamSection(name='losSupRP1RCSects',sectionDescr='riostra sobre pila, cara superior.',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSet=losSupRP1)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losSupRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,130,rnom)])
losSupRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,130,rnom+espLosAlig/2.0)])
losSupRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,200,rnom)])
losSupRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,200,rnom+espLosAlig/2.0)])

losInfRP1RCSects= element_section_map.RCSlabBeamSection(name='losInfRP1RCSects',sectionDescr='riostra sobre pila, cara inferior',concrType=concrete, reinfSteelType=reinfSteel,depth=espLosAlig,elemSet=losInfRP1)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
losInfRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,130,rnom),rcs.rebLayer_mm(25,130,rnom+16)])
losInfRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,130,rnom++espLosAlig/2.0)])
losInfRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,200,rnom)])
losInfRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,130,rnom+40)])

voladzCentRP1RCSects= element_section_map.RCSlabBeamSection(name='voladzCentRP1RCSects',sectionDescr='voladizo, zona central riostra pila',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMax,elemSet=voladzCentRP1)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
voladzCentRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,125,rnom)])
voladzCentRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,100,rnom+25)])
voladzCentRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,125,rnom)])
voladzCentRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom+12)])

voladzExtrRP1RCSects= element_section_map.RCSlabBeamSection(name='voladzExtrRP1RCSects',sectionDescr='voladizo, zona exterior riostra pila',concrType=concrete, reinfSteelType=reinfSteel,depth=espVoladzMax,elemSet=voladzExtrRP1)
#D1: transversal rebars
#D2: longitudinal rebars
#positiv: top face
#negativ: bottom face
voladzExtrRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,125,rnom)])
voladzExtrRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(25,100,rnom+25)])
voladzExtrRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,125,rnom)])
voladzExtrRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom+12)])

murAligV2RCSects= element_section_map.RCSlabBeamSection(name='murAligV2RCSects',sectionDescr='nervios losa aligerada',concrType=concrete, reinfSteelType=reinfSteel,depth=espEntreAlig,elemSet=murAligV2)
#D1: horizontal rebars
#D2: vertical rebars
#positiv: top face
#negativ: bottom face
# murAligV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom+12)])
# murAligV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
# murAligV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom+12)])
# murAligV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
murAligV2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom+12)])
murAligV2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom)])
murAligV2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom+12)])
murAligV2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom)])
shear2=rcs.ShearReinforcement(familyName= "shear2",nShReinfBranches= 2.0,areaShReinfBranch= areaFi16,shReinfSpacing= 0.10,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)
murAligV2RCSects.dir2ShReinfY=shear2

diafRP1RCSects= element_section_map.RCSlabBeamSection(name='diafRP1RCSects',sectionDescr='diafragmas riostra pila',concrType=concrete, reinfSteelType=reinfSteel,depth=espDiafRP,elemSet=diafRP1)
#D1: horizontal rebars
#D2: vertical rebars
#positiv: top face
#negativ: bottom face
# diafRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom+12)])
# diafRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
# diafRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom+12)])
# diafRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(16,200,rnom)])
diafRP1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom+12)])
diafRP1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom)])
diafRP1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom+12)])
diafRP1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(8,200,rnom)])
shear3=rcs.ShearReinforcement(familyName= "shear3",nShReinfBranches=4.0,areaShReinfBranch= areaFi16,shReinfSpacing= 0.20,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)
diafRP1RCSects.dir2ShReinfY=shear3
diafRP1RCSects.dir2ShReinfZ=shear3

pilasInfRCSects= element_section_map.RCSlabBeamSection(name='pilasInfRCSects',sectionDescr='pilas ',concrType=concrete, reinfSteelType=reinfSteel,width=lRectEqPila,depth=lRectEqPila,elemSet=pilasInf)
#Comprobación cortante
#pilasInfRCSects= element_section_map.RCSlabBeamSection(name='pilasInfRCSects',sectionDescr='pilas ',concrType=concrete, reinfSteelType=reinfSteel,width=1.0,depth=lRectEqPila**2,elemSet=pilasInf)
#D1: cara dorsal
#D2: cara frontal
#positiv: top face
#negativ: bottom face
sep_mm=(lRectEqPila*1e3-2*(rnom +16+25/2.))/7.
capa1=rcs.rebLayer_mm(25,100,rnom +16)
capa1.nRebars=8
capa2=rcs.rebLayer_mm(25,100,rnom +29+sep_mm)
capa2.nRebars=2
capa3=rcs.rebLayer_mm(25,100,rnom +29+2*sep_mm)
capa3.nRebars=2
capa4=rcs.rebLayer_mm(25,100,rnom +29+3*sep_mm)
capa4.nRebars=2
areaFi16= math.pi*(16*1e-3)**2/4.0
shear1=rcs.ShearReinforcement(familyName= "shear1",nShReinfBranches= 2.0,areaShReinfBranch= areaFi16,shReinfSpacing= 0.15,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)

pilasInfRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([capa1,capa2,capa3,capa4])
pilasInfRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([capa1,capa2,capa3,capa4])
pilasInfRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([capa1,capa2,capa3,capa4])
pilasInfRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([capa1,capa2,capa3,capa4])
pilasInfRCSects.dir1ShReinfY=shear1 
pilasInfRCSects.dir2ShReinfY=shear1 

pilasSupRCSects= element_section_map.RCSlabBeamSection(name='pilasSupRCSects',sectionDescr='pilas ',concrType=concrete, reinfSteelType=reinfSteel,width=lRectEqPila,depth=lRectEqPila,elemSet=pilasSup)
#comprobación a cortante
#pilasSupRCSects= element_section_map.RCSlabBeamSection(name='pilasSupRCSects',sectionDescr='pilas ',concrType=concrete, reinfSteelType=reinfSteel,width=1.0,depth=lRectEqPila**2,elemSet=pilasSup)
pilasSupRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([capa1,capa2,capa3,capa4])
pilasSupRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([capa1,capa2,capa3,capa4])
pilasSupRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([capa1,capa2,capa3,capa4])
pilasSupRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([capa1,capa2,capa3,capa4])
pilasSupRCSects.dir1ShReinfY=shear1 
pilasSupRCSects.dir2ShReinfY=shear1 


riostrEstr1RCSects= element_section_map.RCSlabBeamSection(name='riostrEstr1RCSects',sectionDescr='riostra estribo 1 ',concrType=concrete, reinfSteelType=reinfSteel,width=espRiostrEstr,depth=cantoLosa,elemSet=riostrEstr1)
sep_mm=(cantoLosa*1e3-2*(rnom +16+25/2.))/6.
capa5=rcs.rebLayer_mm(25,100,rnom +16)
capa5.nRebars=9
capa6=rcs.rebLayer_mm(12,100,rnom +29+sep_mm)
capa6.nRebars=2
capa7=rcs.rebLayer_mm(12,100,rnom +29+2*sep_mm)
capa7.nRebars=2
capa8=rcs.rebLayer_mm(12,100,rnom +29+3*sep_mm)
capa8.nRebars=2
shear2=rcs.ShearReinforcement(familyName= "shear2",nShReinfBranches= 3.0,areaShReinfBranch= areaFi16,shReinfSpacing= 0.20,angAlphaShReinf= math.pi/2.0,angThetaConcrStruts= math.pi/4.0)

riostrEstr1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([capa5,capa6,capa7])
riostrEstr1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([capa5,capa6,capa7,capa8])
riostrEstr1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([capa5,capa6,capa7])
riostrEstr1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([capa5,capa6,capa7,capa8])
riostrEstr1RCSects.dir1ShReinfY=shear2
riostrEstr1RCSects.dir2ShReinfY=shear2

'''
murExtAligRCSects= element_section_map.RCSlabBeamSection(name='murExtAligRCSects',sectionDescr='diafragma entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espExtAlig,elemSet=murExtAlig)
#D1: horizontal rebars
#D2: vertical rebars
#positiv: top face
#negativ: bottom face
murExtAligRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(20,150,rnom)])
murExtAligRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom),rcs.rebLayer_mm(16,200,rnom)])
murExtAligRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom)])

riostrEstr1RCSects= element_section_map.RCSlabBeamSection(name='riostrEstr1RCSects',sectionDescr='diafragma entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espRiostrEstr,elemSet=riostrEstr1)
#D1: vertical rebars
#D2: horizontal rebars
#positiv: cara +y
#negativ: cara -y
riostrEstr1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom),rcs.rebLayer_mm(12,200,rnom+150)])
riostrEstr1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom),rcs.rebLayer_mm(12,200,rnom+150)])
riostrEstr1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom+12),rcs.rebLayer_mm(16,200,rnom+12)])
riostrEstr1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom+12)])

riostrPilRCSects= element_section_map.RCSlabBeamSection(name='riostrPilRCSects',sectionDescr='diafragma entre aligeramientos',concrType=concrete, reinfSteelType=reinfSteel,depth=espRiostrPila,elemSet=riostrPil)
#D1: vertical rebars
#D2: horizontal rebars
#positiv: cara +y
#negativ: cara -y
riostrPilRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom),rcs.rebLayer_mm(12,200,rnom+150)])
riostrPilRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom),rcs.rebLayer_mm(12,200,rnom+150)])
riostrPilRCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom+12),rcs.rebLayer_mm(16,200,rnom+12)])
riostrPilRCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(12,200,rnom+12)])
'''

