# -*- coding: utf-8 -*-
from __future__ import division
from materials.ec2 import EC2_materials
import math

execfile("./data.py")
area_deck=cantoLosa*anchoLosa+2*maxCantoVoladz*anchoCartab+(cantoLosa-maxCantoVoladz)*anchoCartab+(minCantoVoladz+maxCantoVoladz)*anchoVoladz
perim_deck=anchoTot+2*minCantoVoladz+2*math.sqrt(anchoVoladz**2+(maxCantoVoladz-minCantoVoladz)**2)+2*math.sqrt(anchoCartab**2*(cantoLosa-maxCantoVoladz)**2)+anchoLosa
#Data
#Type of concrete used in the deck slab
concrDeck=EC2_materials.EC2Concrete("C30/37",-30e6,1.5)
concrDeck.cemType='N'   #class N cement
RH=50                   #ambient relative humidity(%)

#Shrinkage deformation at traffic openning
t=10000     #age of the concrete t infinito
ts=1     #drying shrinkage begins at the age 1 day
Ac=area_deck     #area of the concrete slab (m2)
u=perim_deck     #perimeter exposed to drying (m)
h0mm=2*Ac/u*1000    #notional size of the member h0 (mm)
#   autogenous shrinkage
Epscainf=concrDeck.getShrEpscainf(t)  #coefficient for calculating the autogenous shrinkage strain
#print 'Epscainf=',Epscainf
Betaast=concrDeck.getShrBetaast(t)    #coefficient for calculating the autogenous shrinkage strain
#print 'Betaast=',Betaast
Epsca=concrDeck.getShrEpsca(t)        #Autogenous shrinkage strain
#print 'Epsca=',Epsca
#   drying shrinkage
BetaRH=concrDeck.getShrBetaRH(RH)   #Coefficient for the calculation of the basic drying shrinkage strain
#print 'BetaRH=',BetaRH
Alfads1=concrDeck.getShrAlfads1()   #Coefficient for the calculation of the basic drying shrinkage strain
#print 'Alfads1=',Alfads1
Alfads2=concrDeck.getShrAlfads2()   #Coefficient for the calculation of the
                                    #basic drying shrinkage strain
#print 'Alfads2=',Alfads2
Epscd0=concrDeck.getShrEpscd0(RH)   #Basic drying shrinkage strain
#print 'Epscd0=',Epscd0
Kh=concrDeck.getShrKh(h0mm)         #coefficient  for the calculation of the
                                    #drying shrinkage strain
#print 'Kh=',Kh
Betadstts=concrDeck.getShrBetadstts(t,ts,h0mm)   #coefficient  for the
                                    #calculation of the drying shrinkage strain
#print 'Betadstts=',Betadstts
Epscd=concrDeck.getShrEpscd(t,ts,RH,h0mm)   #Drying shrinkage strain
#print 'Epscd=',Epscd
Epscs=concrDeck.getShrEpscs(t,ts,RH,h0mm)   #Total shrinkage 
print 'Epscs=',Epscs
