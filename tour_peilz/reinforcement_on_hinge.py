# -*- coding: utf-8 -*-
from rough_calculations import ng_simple_bending_reinforcement

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2015, LCPT and AOO"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@gmail.com"

M=20e3
fcd= 21e6
fsd= 420e6
b= 1.0
d= 0.3

As= ng_simple_bending_reinforcement.AsSimpleBending(M,fcd,fsd,b,d)
T= As*fsd
xpl= T/0.85/fcd/b
z= d-xpl/2.0
C= 0.85*fcd*b*xpl

l= As*1e6*42.0*16.0/1340.0
print "As= ", As*1e4," cm2"
print "l= ", l," mm"
print "T= ", T/1e3," kN"

