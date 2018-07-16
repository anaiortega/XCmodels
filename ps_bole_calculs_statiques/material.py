# -*- coding: utf-8 -*-
# Home made test.

from __future__ import division
import sys
from materials.sia262 import SIA262_materials

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2016, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@gmail.com"

concrete= SIA262_materials.c25_30
fcd= concrete.fcd()
fcdTeor= pow((-25e6/concrete.fck),(1.0/3.0))*concrete.fck/concrete.gmmC
ratio1= (fcd-fcdTeor)/fcdTeor

print "fcd= ", fcd/1e6, " MPa"
print "fcdTeor= ", fcdTeor/1e6, " MPa"
print "ratio1= ", ratio1
print 'fctm= ', concrete.fctm()/1e6, ' MPa'
print 'taucd= ', concrete.taucd()/1e6, ' MPa'
print 'Ecm= ', concrete.getEcm()/1e9, ' GPa'
# print '\epsilon_{c1}= ', concrete.getEpsc1()*1e3, ' \permil'
# print '\epsilon_{c2}= ', concrete.getEpsc2()*1e3, ' \permil'
# print '\epsilon_{cu2}= ', concrete.getEpscu2()*1e3, ' \permil'
print '\epsilon_{c1d}= ', concrete.getEpsc1d()*1e3, ' \permil'
print '\epsilon_{c2d}= ', concrete.getEpsc2d()*1e3, ' \permil'

