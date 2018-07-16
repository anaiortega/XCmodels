# -*- coding: utf-8 -*-
#Shrinkage verification test. 
#Data for comparison from the JRC technical report: 
#"Bridge design to Eurocodes. Worked examples"
#Sect. 4.5.3
from __future__ import division

__author__= "Ana Ortega (AOO) and Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2015, AOO and LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@gmail.com"

from materials.ec2 import EC2_materials


#Data
#Type of concrete used in the deck slab
concrDeck=EC2_materials.EC2Concrete("C25/30",-25e6,1.5)
concrDeck.cemType='N'   #class N cement
RH=50                   #ambient relative humidity(%)

#Shrinkage deformation at traffic openning
t= 100*365.25     #age of the concrete
ts= 1        #drying shrinkage begins at the age 1 day
Ac= 2.99     #area of the concrete slab (m2)
u= (17.79-5.19)     #perimeter exposed to drying (m)
h0mm=2*Ac/u*1000    #notional size of the member h0 (mm)
#   autogenous shrinkage
Epscainf=concrDeck.getShrEpscainf(t)  #coefficient for calculating the autogenous shrinkage strain
Betaast=concrDeck.getShrBetaast(t)    #coefficient for calculating the autogenous shrinkage strain
Epsca=concrDeck.getShrEpsca(t)        #Autogenous shrinkage strain
#   drying shrinkage
BetaRH=concrDeck.getShrBetaRH(RH)   #Coefficient for the calculation of the basic drying shrinkage strain
Alfads1=concrDeck.getShrAlfads1()   #Coefficient for the calculation of the basic drying shrinkage strain
Alfads2=concrDeck.getShrAlfads2()   #Coefficient for the calculation of the basic drying shrinkage strain
Epscd0=concrDeck.getShrEpscd0(RH)   #Basic drying shrinkage strain
Kh=concrDeck.getShrKh(h0mm)         #coefficient  for the calculation of the drying shrinkage strain
Betadstts=concrDeck.getShrBetadstts(t,ts,h0mm)   #coefficient  for the calculation of the drying shrinkage strain

Epscd=concrDeck.getShrEpscd(t,ts,RH,h0mm)   #Drying shrinkage strain

Epscs=concrDeck.getShrEpscs(t,ts,RH,h0mm)   #Total shrinkage 

print 'Autogenous shrinkage strain: ', Epsca*1000, 'e-3'
print 'Drying shrinkage strain: ', Epscd*1000, 'e-3'
print 'Total shrinkage: ', Epscs*1000, 'e-3'

T= 100
EpscsT=concrDeck.getShrEpscs(T,ts,90,h0mm)   #Total shrinkage 
print 'shrinkage (T= '+str(T)+'): ', EpscsT*1000, 'e-3'
print (EpscsT-0.8*Epscs)*1000

import matplotlib.pyplot as plt
import numpy as np

tRange= np.arange(0.0, t, t/10.0)
sRange= list()
for t in tRange:
    sRange.append(concrDeck.getShrEpscs(t,ts,90,h0mm)*1e3)

plt.plot(tRange, sRange)

plt.xlabel('time (days)')
plt.ylabel('shrinkage (per mil)')
plt.title('Shrinkage')
plt.grid(True)
plt.savefig("test.png")
plt.show()
