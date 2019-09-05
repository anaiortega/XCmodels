# -*- coding: utf-8 -*-
from __future__ import division

rnomZap=50 #recubrimiento nominal (zapata)
rnomMur=35 #recubrimiento nominal (muros)
#    Muros
#Dir. 1: vertical
#Dir. 2: horizontal
#    Zapata
#Dir. 1: longitudinal
#Dir. 2: transversal

#Definición armaduras estribo [diámetro,separación] en mm 
#   ***Armadura zapata ***
lnSup_zapEstr=[[20,100]]  #longitudinal superior (admite varias capas)
trSup_zapEstr=[20,200]  #transversal superior
lnInf_zapEstr=[[16,100]]  #longitudinal inferior (admite varias capas)
trInf_zapEstr=[20,200]  #transversal inferior

#  ***Armadura muro estribo [zona1,zona2,zona3] , para cada zona [diam.,sep.]***
vertExt_murEstr=[[[16,200]], 
                 [[16,200]],
                 [[16,200]]] #admite varias capas
horzExt_murEstr=[[16,200],
                 [16,200],
                 [16,200]]
vertInt_murEstr=[[[25,200],[20,200]],
                 [[20,200]],
                 [[20,200]]] #admite varias capas
horzInt_murEstr=[[16,200],
                 [16,200],
                 [16,200]]
                 
#Armadura aleta izquierda [zona1,zona2,zona3] , para cada zona [diam.,sep.]***
if LaletaIzq>0:
    vertExt_aletIzq=[[16,200],
                     [16,200],
                     [20,200]]
    horzExt_aletIzq=[[20,200],
                     [20,200],
                     [20,200]]
    vertInt_aletIzq=[[25,200],
                     [25,200],
                     [25,200]]
    horzInt_aletIzq=[[20,200],
                     [20,200],
                     [20,200]]
    vertInt_ref_aletIzqZ1=list()  #armadura de refuerzo vertical interior en zona inferior
    vertInt_ref_aletIzqZ1=[25,200]  #comentar si no existe refuerzo


#Armadura aleta derecha [zona1,zona2,zona3] , para cada zona [diam.,sep.]***
if LaletaDer>0:
    vertExt_aletDer=[[16,200],
                     [16,200],
                     [16,200]]
    horzExt_aletDer=[[16,200],
                     [16,200],
                     [16,200]]
    vertInt_aletDer=[[20,200],
                     [20,200],
                     [20,200]]
    horzInt_aletDer=[[20,200],
                     [20,200],
                     [20,200]]
    vertInt_ref_aletDerZ1=list()  #armadura de refuerzo vertical interior en zona inferior
    vertInt_ref_aletDerZ1=[25,200]  #comentar si no existe refuerzo
