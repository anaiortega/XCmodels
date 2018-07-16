#-*- coding: utf-8 -*-

from __future__ import division
import math
import sys
import numpy as np
import pydoc
import rough_calculations.masonryVault as masonryVault

#Obtención de los coeficientes del polinomio a partir de 4 points del arco 
x1= 2.90
x2= 6.83
x3= 11.12
x4= 15.05

h1= 3.17
h2= 4.91
h3= 4.91
h4= 3.18

a = np.array([[pow(x1,4),pow(x1,3),pow(x1,2),x1], [pow(x2,4),pow(x2,3),pow(x2,2),x2],[pow(x3,4),pow(x3,3),pow(x3,2),x3],[pow(x4,4),pow(x4,3),pow(x4,2),x4]])
b = np.array([h1,h2,h3,h4])

bEff= 1.0+2.0*math.tan(math.radians(30))
arcGeom=masonryVault.archGeometry(arcThick= 0.8,arcSpan= 17.95,arcEffL=bEff)
arcGeom.coefPolArch=np.linalg.solve(a, b) #[f,j,k,r] coefficients of polynomial y=fx^4+jx^3+kx^2+rx+u (u=0)

fillChar= masonryVault.FillingCharacteristics()
fillChar.angPhi= math.radians(30)   #angle de frottement interne
fillChar.cohesion=0                 #cohésion
fillChar.mp= 0.33                   #Correction factor.
fillChar.mc= 0.01                   #Correction factor.
fillChar.alpha= 0.726
fillChar.beta= 6.095
fillChar.swFill=18e3      #specific weight of filling material [N/m3]
fillChar.swSupStr=24e3    #specific weight or superstructure [N/m3]
fillChar.fillThick=2.36     #thickness of filling material at the endpoint of the arch [m]
fillChar.eqThickRoad=0.35+0.11  #equivalent thickness of road material [m]

#Traffic load.
trLoad= masonryVault.trafficLoad()
trLoad.delta= math.radians(30)
trLoad.fillThickKeys= 0.35 # Hauteur du remplissage sur la clé de la voûte (m).
#trLoad.Q= 1.5*120e3 # Charge ponctuelle due au trafic (N) (véhicule EC1).
trLoad.Q= 1.5*143.97e3 # Charge ponctuelle due au trafic (N) (véhicule EC1).
trLoad.qrep= 0.0#1.5*4e3# Charge uniformément repartie due au trafic (Pa).

permLoadRes=masonryVault.permLoadResult(arcGeom,fillChar)

trafLoadRes=masonryVault.trafficLoadResult(arcGeom,trLoad)

Nadmis=-1.1/0.8*1.25e6 #Effort axial admisible XXX triché
resist= masonryVault.resistance(Nadmis,arcGeom,fillChar,trLoad,permLoadRes,trafLoadRes)


resist.verbose= True
res= resist.minimize()

#Results printing
resist.printResults()

