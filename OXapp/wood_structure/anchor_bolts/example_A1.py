# -*- coding: utf-8 -*-
# Verification test according to ACI 349.2 R-07.
# Guide to the Concrete Capacity Design (CCD) Method—Embedment Design Examples
# Example A1. Single stud, tension only, no edge effects
from __future__ import division
from __future__ import print_function

import math
from materials.aci import ACI_materials
from materials.aci import ACI_limit_state_checking

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2019, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@gmail.com"

inch2meter= 0.0254
feet2meter= 0.3048
kip2N= 4.4482216e3
ksi2MPa= 6.89476

# Data
Nd= 8*kip2N
stud= ACI_limit_state_checking.AnchorBolt(ca1= 12*inch2meter,ca2= 12*inch2meter,ha= 18*inch2meter, concrete= ACI_materials.c4000, steel= ACI_materials.A108, diam= 0.5*inch2meter, hef= 4.60*inch2meter, cast_in= True)

Nsa= stud.getNominalSteelStrength() # Nominal steel strength
Nb= stud.getBasicConcreteBreakoutStrengthTension() # Basic concrete breakout strength
Nb_ref= 1.52*math.pow(stud.hef/inch2meter,1.5)*ACI_materials.pound2Newton*1000
ratio1= abs(Nsa-56.771429952e3)/56.771429952e3
ratio2= abs(Nb-66.6138052976e3)/66.6138052976e3

print('Nsa= ', Nsa/1e3, ' kN, ', Nsa/kip2N, ' kips')
print('Nb= ', Nb/1e3, ' kN, ', Nb/kip2N, ' kips')
print('Nb_ref= ', Nb_ref/1e3, ' kN, ', Nb_ref/kip2N, ' kips')
print('ratio1= ', ratio1)
print('ratio2= ', ratio2)

import os
from miscUtils import LogMessages as lmsg
fname= os.path.basename(__file__)
if((ratio1<1e-12) and (ratio2<1e-12)):
  print("test ",fname,": ok.")
else:
  lmsg.error(fname+' ERROR.')
