# -*- coding: utf-8 -*-
from rough_calculations import ng_simple_beam as sb
from rough_calculations import ng_simple_bending_reinforcement
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

beam= sb.SimpleBeam()
beam.l= 2.5


#Loads
Q= 1.5*-135e3 # N
d= 1.2
q= 1.35*(-0.25*2500*9.81-2.35e3-8.1e3) # N/m

MdMax= -1e15
aMdMax= 0.0
xMdMax= 0.0
VMdMax= 0.0

VdMax= -1e15
aVdMax= 0.0
xVdMax= 0.0
MVdMax= 0.0

sequence_containing_x_vals = list()
sequence_containing_y_vals = list()
sequence_containing_z_vals = list()


for i in range(0,60):
    a= beam.l/40.0*i-d
    for j in range(0,40):
        x= beam.l/40.0*j
        Md= beam.getBendingMomentUnderUniformLoad(q,x)
        Vd= beam.getShearUnderUniformLoad(q,x)
        if(a>0):
            Md+=beam.getBendingMomentUnderConcentratedLoad(Q,a,x)
            Vd+=beam.getShearUnderConcentratedLoad(Q,a,x)
        if((a+d)<beam.l):
            Md+=beam.getBendingMomentUnderConcentratedLoad(Q,a+d,x)
            Vd+=beam.getShearUnderConcentratedLoad(Q,a+d,x)
        
        #print 'a= ',a, ' x= ', x, ' Md= ', Md/1e3, ' kN m/m Vd= ', Vd/1e3, ' kN m/m'
        sequence_containing_x_vals.append(a)
        sequence_containing_y_vals.append(x)
        sequence_containing_z_vals.append(Vd/1e3)
        if(Md>MdMax):
            MdMax= Md
            VdMdMax= Vd
            aMdMax= a
            xMdMax= x
        if(Vd>VdMax):
            VdMax= Vd
            MdVdMax= Md
            aVdMax= a
            xVdMax= x

print 'aMdMax= ',aMdMax, ' xMdMax= ', xMdMax, ' MdMax= ', MdMax/1e3, ' kN m/m VdMdMax= ', VMdMax/1e3, ' kN m/m'
print 'aVdMax= ',aVdMax, ' xVdMax= ', xVdMax, ' VdMax= ', VdMax/1e3, ' kN/m MVdMax= ', MVdMax/1e3, ' kN m/m'

# fig = pyplot.figure()
# ax = Axes3D(fig)
# ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
# pyplot.show()

#Reinforcement
from materials.sia262 import SIA262_materials
from materials.sia262 import SIA262_limit_state_checking

concrete= SIA262_materials.c50_60
reinfSteel= SIA262_materials.B500A

b= 1.0
d= 0.8*0.25
As= ng_simple_bending_reinforcement.AsSimpleBending(MdMax,-concrete.fcd(),reinfSteel.fyd(),b,d)

print 'Bending As= ', As*1e6, ' mm2'

VRd= SIA262_limit_state_checking.VuNoShearRebars(concrete,reinfSteel,0.0,MVdMax,As,b,d)

print 'Situation Accidentelle VRd= ', VRd/1e3, ' kN VdMax= ', VdMax/1.35e3, ' kN'
