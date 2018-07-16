#-*- coding: utf-8 -*-

from __future__ import division
import math
import sys
import numpy as np
import pydoc
import rough_calculations.masonry_bridge
import basicClasses as bc
from scipy.optimize import minimize

def fun(x):
  arcGeom=bc.archGeometry()
  arcGeom.coefPolArch=[-1.46682427e-03,4.40110960e-02,-5.45992023e-01,3.23805584e+00] #[f,j,k,r] coefficients of polynomial y=fx^4+jx^3+kx^2+rx+u (u=0)
  arcGeom.XRot=x     #X coordinates rotules A,B,C,D [m]
  arcGeom.arcThick=1             #arch thickness (m)
  arcGeom.arcSpan=15             #arch span [m]

  fillChar= bc.FillingCharacteristics()
  fillChar.angPhi= math.radians(30)   #angle de frottement interne
  fillChar.cohesion=0                 #cohésion
  fillChar.mp= 0.33                   #Correction factor.
  fillChar.mc= 0.01                   #Correction factor.
  fillChar.alpha= 0.726
  fillChar.beta= 6.095
  fillChar.swFill=18e3      #specific weight of filling material [N/m3]
  fillChar.swSupStr=20e3    #specific weight or superstructure [N/m3]
  fillChar.fillThick=9     #thickness of filling material in the endpoint of the arch [m]
  fillChar.eqThickRoad=0.5  #equivalent thickness of road material [m]

  trLoad=bc.trafficLoad()
  trLoad.delta= math.radians(30)
  trLoad.fillThickKeys= 1.5 # Hauteur du remplissage sur la clé de la voûte (m).
  trLoad.Q= 160000 # Charge ponctuelle due au trafic (N).
  trLoad.qrep= 0.005e6 # Charge uniformément repartie due au trafic (Pa).

  permLoadRes=bc.permLoadResult(arcGeom,fillChar)

  trafLoadRes=bc.trafficLoadResult(arcGeom,trLoad)

  Nadmis=-1.25e6 #Effort axial admisible
  resist=bc.resistance(Nadmis,arcGeom,fillChar,trLoad,permLoadRes,trafLoadRes)
  return resist.getSafCoef()

#print fun([3.156,14.001,6.175,10.996])
x0=[15/6,15*5/6,15*4/6,15*4/6] 
bnds = ((0,15/2),(15/2,15),(0,15/2),(15/2,15))
#res=minimize(fun,x0,method='SLSQP',bounds=bnds)
res=minimize(fun,x0,method='Nelder-Mead')
print res
