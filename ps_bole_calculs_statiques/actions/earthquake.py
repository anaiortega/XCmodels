# -*- coding: utf-8 -*-

from actions.quake import seismeSIA
import math

# Earthquake according to SIA 261
soilClass= 'C' # Tableau 24 SIA231 et rapport géotechnique Géotest 23/03/1978
accelTerrain= 0.6 # Bex->Zone 3a. Article 16.2.1.2 SIA 261:214
CO= 2 #CO II Classe d'ouvrage. Tableau 25 SIA 231:2014 et CU 6.5.1
q= 1.5 #SIA 266 Clause 4.7.1.4

Ts= [0.742907, 0.205817, 0.190719, 0.165157, 0.160587]
ah= []
av= []
for T in Ts:
    a= seismeSIA.designSpectrum(soilClass,accelTerrain,CO,T,q)
    ah.append(a)
    av.append(0.7*a)

print 'T= ', Ts, 's'
print ' a_h= ', ah, ' m/s2'
print ' a_v= ', av, ' m/s2'

