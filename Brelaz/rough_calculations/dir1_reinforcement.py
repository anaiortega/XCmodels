# -*- coding: utf-8 -*-
from rough_calculations import ng_cantilever
from rough_calculations import ng_simple_bending_reinforcement
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from materials.sia262 import SIA262_limit_state_checking

beam= ng_cantilever.Cantilever()
beam.l= 2.45+0.5

#Loads
Qa= -2*135e3/2.5 #N/m
qa= -0.25*2500*9.81-2.35e3-8.1e3 # N/m2
Qd= 1.5*Qa # N
qd= 1.35*qa # N/m

Md= beam.getBendingMomentUnderUniformLoad(qd,0.0)+beam.getBendingMomentUnderConcentratedLoad(Qd,1.0-0.2,0.0)
Ma= beam.getBendingMomentUnderUniformLoad(qa,0.0)+beam.getBendingMomentUnderConcentratedLoad(Qa,2.45-0.2,0.0)
MdMax= min(Md,Ma)
print 'Md= ', Md/1e3, ' kN m/m Ma= ', Ma/1e3, 'kN m/m MdMax= ', MdMax/1e3, ' kN m/m'

Vd= beam.getShearUnderUniformLoad(qd,0.25)+beam.getShearUnderConcentratedLoad(Qd,1.0-0.2,0.25)
Va= beam.getShearUnderUniformLoad(qa,0.25)+beam.getShearUnderConcentratedLoad(Qa,2.45-0.2,0.25)
MVRd= beam.getBendingMomentUnderUniformLoad(qd,0.25)+beam.getBendingMomentUnderConcentratedLoad(Qd,1.0-0.2,0.25)
VdMax= max(Vd,Va)
print 'Vd= ', Vd/1e3, ' kN/m MVRd= ', MVRd/1e3, ' kN m/m Va= ', Va/1e3, 'kN/m VdMax= ', VdMax/1e3, ' kN/m'


#Reinforcement
from materials.sia262 import SIA262_materials

concrete= SIA262_materials.c50_60
reinfSteel= SIA262_materials.B500A

d= 0.25-0.035-20e-3/2.0

As= ng_simple_bending_reinforcement.AsSimpleBending(-MdMax,-concrete.fcd(),reinfSteel.fyd(),1.0,d)

print 'As= ', As*1e6, ' mm2'
VRd= SIA262_limit_state_checking.VuNoShearRebars(concrete,reinfSteel,0.0,-MVRd,As,2.5/2.0,d)

print 'VRd= ', VRd/1e3, ' kN VdMax= ', VdMax/1e3, ' kN'

#Reinforcement 2
Md2= beam.getBendingMomentUnderUniformLoad(qd,0.0)+beam.getBendingMomentUnderConcentratedLoad(Qd,1.0-0.2,1.2)
Ma2= beam.getBendingMomentUnderUniformLoad(qa,0.0)+beam.getBendingMomentUnderConcentratedLoad(Qa,2.45-0.2,1.2)
MdMax2= min(Md2,Ma2)
print 'Md2= ', Md2/1e3, ' kN m/m Ma2= ', Ma2/1e3, 'kN m/m MdMax2= ', MdMax2/1e3, ' kN m/m'
As2= ng_simple_bending_reinforcement.AsSimpleBending(-MdMax2,-concrete.fcd(),reinfSteel.fyd(),1.0,d)

print 'As2= ', As2*1e6, ' mm2'

#Fatigue 
Mf= beam.getBendingMomentUnderConcentratedLoad(Qa,0.5,0.0)
print 'Mf= ', Mf/1e3, ' kN m/m'

