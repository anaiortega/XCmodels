# -*- coding: utf-8 -*-
import math
from rough_calculations import ng_simple_beam as sb
from rough_calculations import ng_pinned_fixed_beam as pfb
from materials.sections.structural_shapes import arcelor_metric_shapes
from materials.ec3 import EC3_materials

S355JR= EC3_materials.S355JR
S355JR.gammaM= 1.05
IPE450A= arcelor_metric_shapes.IPEShape(S355JR,'IPE_A_450')

#beam= sb.SimpleBeam(205e9,IPE450A.Iz())
beam= pfb.PinnedFixedBeam(205e9,IPE450A.Iz())
beam.l= math.sqrt(15.5**2+1**2)

b= 15.5/5.0

x3= beam.l/2.0
x2= x3-b
x1= x2-b
x4= x3+b
x5= x4+b

pos= [x1,x2,x3,x4,x5]

w= IPE450A.getRho()*9.81
P0= 14.5063917522e3
defl0= 0.0
P1= 19.9114175252e3
defl1= 0.0

for x in pos:
  def0= beam.getDeflectionUnderUniformLoad(w,x)
  defl0+= def0+beam.getDeflectionUnderConcentratedLoad(P0,x,beam.l/2.0)
  defl1+= def0+beam.getDeflectionUnderConcentratedLoad(P1,x,beam.l/2.0)

print 'L= ', beam.l
print 'pos= ', pos
print 'defl0= ', defl0*1e3, ' mm'
print 'defl1= ', defl1*1e3, ' mm'
print 'incF= ', (defl1-defl0)*1e3, ' mm'
print 'fLim= ', beam.l/300.0*1e3, ' mm'
