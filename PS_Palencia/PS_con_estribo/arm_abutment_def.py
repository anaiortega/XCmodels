# -*- coding: utf-8 -*-
from __future__ import division

rnomZap=35 #recubrimiento nominal (zapata)
rnomMur=35 #recubrimiento nominal (muros)

#Definición armadurasestribo [diámetro,separación] en mm 
#   ***Armadura zapata ***
lnSup_zapEstr=[25,100]  #longitudinal superior
trSup_zapEstr=[20,200]  #longitudinal inferior
lnInf_zapEstr=[25,100]  #transversal superior
trInf_zapEstr=[20,200]  #transversal inferior

#   ***Armadura muro estribo ***
vertExt_murEstr=[[16,200],
                 [16,200],
                 [20,200]]
horzExt_murEstr=[[20,200],
                 [20,200],
                 [20,200]]
vertInt_murEstr=[[25,200],
                 [25,200],
                 [25,200]]
horzInt_murEstr=[[20,200],
                 [20,200],
                 [20,200]]
vertInt_ref_murEstrZ1=list()  #armadura de refuerzo vertical interior en zona inferior
vertInt_ref_murEstrZ1=[25,200]  #comentar si no existe refuerzo

                 
#Armadura aleta izquierda
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


#Armadura aleta derecha
if LaletaDer>0:
    vertExt_aletDer=[[16,200],
                     [16,200],
                     [20,200]]
    horzExt_aletDer=[[20,200],
                     [20,200],
                     [20,200]]
    vertInt_aletDer=[[25,200],
                     [25,200],
                     [25,200]]
    horzInt_aletDer=[[20,200],
                     [20,200],
                     [20,200]]
    vertInt_ref_aletDerZ1=list()  #armadura de refuerzo vertical interior en zona inferior
    vertInt_ref_aletDerZ1=[25,200]  #comentar si no existe refuerzo
