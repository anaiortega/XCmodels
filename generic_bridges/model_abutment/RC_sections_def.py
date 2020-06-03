# -*- coding: utf-8 -*-

#import os


#instances of rcs.RCSlabBeamSection that define the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element


zapEstrRCSects= rcs.RCSlabBeamSection(name='zapEstrRCSects',sectionDescr='zapata',concrType=concrete, reinfSteelType=reinfSteel,depth=cantoZap,elemSetName='zapEstr')
#D1: transversal rebars
#D2:  longitudianl rebars
#positiv: top face
#negativ: bottom face
#        transversal superior
zapEstrRCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(trSup_zapEstr[0],trSup_zapEstr[1],rnomZap+lnSup_zapEstr[0][0])])
#        longitudinal superior
zapEstrRCSects.dir2PositvRebarRows=def_simple_RC_section.LongReinfLayers() 
for rLay in lnSup_zapEstr:
    zapEstrRCSects.dir2PositvRebarRows.append(rcs.rebLayer_mm(rLay[0],rLay[1],rnomZap))
#        transversal inferior
zapEstrRCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(trInf_zapEstr[0],trInf_zapEstr[1],rnomZap+lnInf_zapEstr[0][0])])
#        longitudinal inferior
zapEstrRCSects.dir2NegatvRebarRows=def_simple_RC_section.LongReinfLayers()
for rLay in lnInf_zapEstr:
    zapEstrRCSects.dir2NegatvRebarRows.append(rcs.rebLayer_mm(rLay[0],rLay[1],rnomZap))

#MURO ESTRIBO - ZONA 1
murEstrZ1RCSects= rcs.RCSlabBeamSection(name='murEstrZ1RCSects',sectionDescr='muro de estribo, zona Z1 (inferior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espMurEstr,elemSetName='murestrZ1')
#D1: vertical rebars
#D2: horizontal rebars
#positiv: exterior
#negativ: interior
#           zona 1
#vertical exterior
murEstrZ1RCSects.dir1PositvRebarRows=def_simple_RC_section.LongReinfLayers()
for rLay in vertExt_murEstr[0]:
    murEstrZ1RCSects.dir1PositvRebarRows.append(rcs.rebLayer_mm(rLay[0],rLay[1],rnomZap))
#horizontal exterior
murEstrZ1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzExt_murEstr[0][0],horzExt_murEstr[0][1],rnomMur+vertExt_murEstr[0][0][0])])
#vertical interior
murEstrZ1RCSects.dir1NegatvRebarRows=def_simple_RC_section.LongReinfLayers()
for rLay in vertInt_murEstr[0]:
    murEstrZ1RCSects.dir1NegatvRebarRows.append(rcs.rebLayer_mm(rLay[0],rLay[1],rnomMur))
#horizontal interior
murEstrZ1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzInt_murEstr[0][0],horzInt_murEstr[0][1],rnomMur+vertInt_murEstr[0][0][0])])

#MURO ESTRIBO - ZONA 2
murEstrZ2RCSects= rcs.RCSlabBeamSection(name='murEstrZ2RCSects',sectionDescr='muro de estribo, zona Z2 ',concrType=concrete, reinfSteelType=reinfSteel,depth=espMurEstr,elemSetName='murestrZ2')
#D1: vertical rebars
#D2: horizontal rebars
#positiv: exterior
#negativ: interior
#vertical exterior
murEstrZ2RCSects.dir1PositvRebarRows=def_simple_RC_section.LongReinfLayers()
for rLay in vertExt_murEstr[1]:
    murEstrZ2RCSects.dir1PositvRebarRows.append(rcs.rebLayer_mm(rLay[0],rLay[1],rnomZap))
#horizontal exterior
murEstrZ2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzExt_murEstr[1][0],horzExt_murEstr[1][1],rnomMur+vertExt_murEstr[1][0][0])])
#vertical interior
murEstrZ2RCSects.dir1NegatvRebarRows=def_simple_RC_section.LongReinfLayers()
for rLay in vertInt_murEstr[1]:
    murEstrZ2RCSects.dir1NegatvRebarRows.append(rcs.rebLayer_mm(rLay[0],rLay[1],rnomMur))
#horizontal interior
murEstrZ2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzInt_murEstr[1][0],horzInt_murEstr[1][1],rnomMur+vertInt_murEstr[1][0][0])])
                                                
#MURO ESTRIBO - ZONA 3
murEstrZ3RCSects= rcs.RCSlabBeamSection(name='murEstrZ3RCSects',sectionDescr='muro de estribo, zona Z3 ',concrType=concrete, reinfSteelType=reinfSteel,depth=espMurEstr,elemSetName='murestrZ3')
#D1: vertical rebars
#D2: horizontal rebars
#positiv: exterior
#negativ: interior
#vertical exterior
murEstrZ3RCSects.dir1PositvRebarRows=def_simple_RC_section.LongReinfLayers()
for rLay in vertExt_murEstr[2]:
    murEstrZ3RCSects.dir1PositvRebarRows.append(rcs.rebLayer_mm(rLay[0],rLay[1],rnomZap))
#horizontal exterior
murEstrZ3RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzExt_murEstr[2][0],horzExt_murEstr[2][1],rnomMur+vertExt_murEstr[2][0][0])])
#vertical interior
murEstrZ3RCSects.dir1NegatvRebarRows=def_simple_RC_section.LongReinfLayers()
for rLay in vertInt_murEstr[2]:
    murEstrZ3RCSects.dir1NegatvRebarRows.append(rcs.rebLayer_mm(rLay[0],rLay[1],rnomMur))

#horizontal interior                
murEstrZ3RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzInt_murEstr[2][0],horzInt_murEstr[2][1],rnomMur+vertInt_murEstr[2][0][0])])

estriboRCSects=[zapEstrRCSects,murEstrZ1RCSects,murEstrZ2RCSects,murEstrZ3RCSects]

if LaletaIzq>0:
    aletIzqZ1RCSects= rcs.RCSlabBeamSection(name='aletIzqZ1RCSects',sectionDescr='aleta izquierda, zona Z1 (inferior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ1,elemSetName='aletiZ1')
    #D1: vertical rebars
    #D2: horizontal rebars
    #positiv: exterior
    #negativ: interior
    aletIzqZ1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertExt_aletIzq[0][0],vertExt_aletIzq[0][1],rnomMur)])
    aletIzqZ1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzExt_aletIzq[0][0],horzExt_aletIzq[0][1],rnomMur+vertExt_aletIzq[0][0])])
    aletIzqZ1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertInt_aletIzq[0][0],vertInt_aletIzq[0][1],rnomMur)])
    aletIzqZ1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzInt_aletIzq[0][0],horzInt_aletIzq[0][1],rnomMur+vertInt_aletIzq[0][0])])
    if len(vertInt_ref_aletIzqZ1)>0:
        aletIzqZ1RCSects.dir1NegatvRebarRows.append(rcs.rebLayer_mm(vertInt_ref_aletIzqZ1[0],vertInt_ref_aletIzqZ1[1],rnomMur+vertInt_aletIzq[0][0]+horzInt_aletIzq[0][0]))
                                                
    aletIzqZ2RCSects= rcs.RCSlabBeamSection(name='aletIzqZ2RCSects',sectionDescr='aleta izquierda, zona Z2',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ2,elemSetName='aletiZ2')
    #D1: vertical rebars
    #D2: horizontal rebars
    #positiv: exterior
    #negativ: interior
    aletIzqZ2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertExt_aletIzq[1][0],vertExt_aletIzq[1][1],rnomMur)])
    aletIzqZ2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzExt_aletIzq[1][0],horzExt_aletIzq[1][1],rnomMur+vertExt_aletIzq[1][0])])
    aletIzqZ2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertInt_aletIzq[1][0],vertInt_aletIzq[1][1],rnomMur)])
    aletIzqZ2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzInt_aletIzq[1][0],horzInt_aletIzq[1][1],rnomMur+vertInt_aletIzq[1][0])])

    aletIzqZ3RCSects= rcs.RCSlabBeamSection(name='aletIzqZ3RCSects',sectionDescr='aleta izquierda, zona Z3',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletiZ3,elemSetName='aletiZ3')
    aletIzqZ3RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertExt_aletIzq[2][0],vertExt_aletIzq[2][1],rnomMur)])
    aletIzqZ3RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzExt_aletIzq[2][0],horzExt_aletIzq[2][1],rnomMur+vertExt_aletIzq[2][0])])
    aletIzqZ3RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertInt_aletIzq[2][0],vertInt_aletIzq[2][1],rnomMur)])
    aletIzqZ3RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzInt_aletIzq[2][0],horzInt_aletIzq[2][1],rnomMur+vertInt_aletIzq[2][0])])
    
    estriboRCSects+=[aletIzqZ1RCSects,aletIzqZ2RCSects,aletIzqZ3RCSects]

if LaletaDer>0:
    aletDerZ1RCSects= rcs.RCSlabBeamSection(name='aletDerZ1RCSects',sectionDescr='aleta derecha, zona Z1 (inferior)',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ1,elemSetName='aletdZ1')
                     
    #D1: vertical rebars
    #D2: horizontal rebars
    #positiv: exterior
    #negativ: interior
    aletDerZ1RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertExt_aletDer[0][0],vertExt_aletDer[0][1],rnomMur)])
    aletDerZ1RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzExt_aletDer[0][0],horzExt_aletDer[0][1],rnomMur+vertExt_aletDer[0][0])])
    aletDerZ1RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertInt_aletDer[0][0],vertInt_aletDer[0][1],rnomMur)])
    aletDerZ1RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzInt_aletDer[0][0],horzInt_aletDer[0][1],rnomMur+vertInt_aletDer[0][0])])
    if len(vertInt_ref_aletDerZ1)>0:
        aletDerZ1RCSects.dir1NegatvRebarRows.append(rcs.rebLayer_mm(vertInt_ref_aletDerZ1[0],vertInt_ref_aletDerZ1[1],rnomMur+vertInt_aletDer[0][0]+horzInt_aletDer[0][0]))
                     
    aletDerZ2RCSects= rcs.RCSlabBeamSection(name='aletDerZ2RCSects',sectionDescr='aleta derecha, zona Z2',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ2,elemSetName='aletdZ2')
    #D1: horizontal rebars
    #D2: vertical rebars
    #positiv: exterior
    #negativ: interior
    aletDerZ2RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertExt_aletDer[1][0],vertExt_aletDer[1][1],rnomMur)])
    aletDerZ2RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzExt_aletDer[1][0],horzExt_aletDer[1][1],rnomMur+vertExt_aletDer[1][0])])
    aletDerZ2RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertInt_aletDer[1][0],vertInt_aletDer[1][1],rnomMur)])
    aletDerZ2RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzInt_aletDer[1][0],horzInt_aletDer[1][1],rnomMur+vertInt_aletDer[1][0])])

    aletDerZ3RCSects= rcs.RCSlabBeamSection(name='aletDerZ3RCSects',sectionDescr='aleta derecha, zona Z3',concrType=concrete, reinfSteelType=reinfSteel,depth=espAletdZ3,elemSetName='aletdZ3')
    aletDerZ3RCSects.dir1PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertExt_aletDer[2][0],vertExt_aletDer[2][1],rnomMur)])
    aletDerZ3RCSects.dir2PositvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzExt_aletDer[2][0],horzExt_aletDer[2][1],rnomMur+vertExt_aletDer[2][0])])
    aletDerZ3RCSects.dir1NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(vertInt_aletDer[2][0],vertInt_aletDer[2][1],rnomMur)])
    aletDerZ3RCSects.dir2NegatvRebarRows= def_simple_RC_section.LongReinfLayers([rcs.rebLayer_mm(horzInt_aletDer[2][0],horzInt_aletDer[2][1],rnomMur+vertInt_aletDer[2][0])])
    
    estriboRCSects+=[aletDerZ1RCSects,aletDerZ2RCSects,aletDerZ3RCSects]
