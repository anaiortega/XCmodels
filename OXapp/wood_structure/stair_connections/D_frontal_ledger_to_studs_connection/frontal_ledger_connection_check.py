# -*- coding: utf-8 -*-
''' Main LVL bearing connection check.'''
from __future__ import division
from __future__ import print_function


inch2meter= 0.0254
pound2Newton=  4.4482216282509
pa2psi= 145.038e-6
psi2pa= 1.0/pa2psi
psf2pa= 47.880208 # N/m2

studSpacing= 12*inch2meter
landingWidth= 1.9 # meters
deadLoad= 1197*studSpacing*landingWidth/2.0 # Dead load.
liveLoad= 4788*studSpacing*landingWidth/2.0 # Live load.
maxLoad= deadLoad+liveLoad # Bearing load.

connectionAllowableLoad= 555*pound2Newton
capacityFactor= maxLoad/connectionAllowableLoad

print('Max. load: ',maxLoad/1e3,'kN (', maxLoad/pound2Newton,'pounds)')
print('Connection allowable load: ',connectionAllowableLoad/1e3,'kN (', connectionAllowableLoad/pound2Newton,'pounds)')
print('Connection capacity factor: ',capacityFactor)


