# -*- coding: utf-8 -*-

from __future__ import division
import math
import xc_base
import geom
import xc
import scipy.interpolate


from materials.ec3 import EC3_materials
from rough_calculations import ng_simple_beam as sb

S235JR= EC3_materials.S235JR
S235JR.gammaM= 1.00
IPE450A= EC3_materials.IPEShape(S235JR,'IPE_A_450')


# Geometry
k1= 1.0; k2= 1.0

#Check results pages 34 and 35
L= 3.2 # Bar length (m)
x= [0.0,L]
M= [0.0,-1296e3]
overlineLambdaLT= IPE450A.getLateralBucklingNonDimensionalBeamSlenderness(1,x,M)
alphaLT= IPE450A.getLateralBucklingImperfectionFactor()
# phiLT= IPE450A.getLateralBucklingIntermediateFactor(1,x,M)
chiLT= IPE450A.getLateralBucklingReductionFactor(1,x,M)
# chiLT= IPE450A.getLateralBucklingReductionFactor(1,x,M)
MbRd= IPE450A.getLateralTorsionalBucklingResistance(1,x,M)

# print 'overlineLambdaLT= ', overlineLambdaLT
# print 'alphaLT= ', alphaLT
# print 'phiLT= ', phiLT
print 'chiLT= ', chiLT
print 'MbRd= ', MbRd/1e3, 'kN m'

