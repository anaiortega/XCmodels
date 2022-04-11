# -*- coding: utf-8 -*-

#Lateral-torsional buckling (see Aitziber López, Danny J. Yong and Miguel A. Serna article)
from __future__ import division
import math
import geom
import xc
import scipy.interpolate


from materials.ec3 import EC3_materials
from rough_calculations import ng_simple_beam as sb

S235JR= EC3_materials.S235JR
S235JR.gammaM= 1.00
IPE450A= EC3_materials.IPEShape(S235JR,'IPE_A_450')


# Geometry
# k1=lateral bending and warping coefficient at first end (free:1, prevented:0.5)
# k2=lateral bending and warping coefficient at last end (free:1, prevented:0.5)
k1= 1.0; k2= 1.0

#Check results pages 34 and 35
L= 3.2 # Bar length (m)
x= [0.0,L]
M= [0.0,-1296e3]  #values of the moment at sections in x abcissae, each of them
                  #with the corresponding sign.
overlineLambdaLT= IPE450A.getLateralBucklingNonDimensionalBeamSlenderness(sectionClass=1,xi=x,Mi=M) #xi: abcissae for the moment diagram,  ordinates for the moment diagram
alphaLT= IPE450A.getLateralBucklingImperfectionFactor()
# phiLT= IPE450A.getLateralBucklingIntermediateFactor(1,x,M)
chiLT= IPE450A.getLateralBucklingReductionFactor(1,x,M)
# chiLT= IPE450A.getLateralBucklingReductionFactor(1,x,M)
MbRd= IPE450A.getLateralTorsionalBucklingResistance(1,x,M)

# print 'overlineLambdaLT= ', overlineLambdaLT
# print 'alphaLT= ', alphaLT
# print 'phiLT= ', phiLT
print 'chiLT= ', chiLT     # Lateral buckling reduction factor
print 'MbRd= ', MbRd/1e3, 'kN m'  #Lateral torsional buckling resistance

