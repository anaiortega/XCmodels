# -*- coding: utf-8 -*-
# Test de funcionamiento del comando reg_cuad

import xc_base
import geom
import xc
from model import predefined_spaces
from solution import predefined_solutions
from materials import typical_materials

width= 1
depth= 2
areaTeor= width*depth
iyTeor= 1/12.0*width*depth**3
izTeor= 1/12.0*depth*width**3
y0= 0
z0= 0
F= 1000 # Force.

# Problem type
prueba= xc.FEProblem()
preprocessor= prueba.getPreprocessor


# Materials definition
E= 2.1e6 # steel Young modulus.
elast= typical_materials.defElasticMaterial(preprocessor,"elast",E)

# Section
geomSCC= preprocessor.getMaterialHandler.newSectionGeometry("geomSCC")
y1= width/2.0
z1= depth/2.0
regiones= geomSCC.getRegions
rg= regiones.newQuadRegion("elast")
rg.nDivIJ= 1
rg.nDivJK= 2
nFibTeor= rg.nDivIJ*rg.nDivJK
rg.pMin= geom.Pos2d(y0-y1,z0-z1)
rg.pMax= geom.Pos2d(y0+y1,z0+z1)

import os
quadFibers= preprocessor.getMaterialHandler.newMaterial("fiber_section_3d","quadFibers")
fiberSectionRepr= quadFibers.getFiberSectionRepr()
fiberSectionRepr.setGeomNamed("geomSCC")
quadFibers.setupFibers()
fibers= quadFibers.getFibers()

nfibers= fibers.getNumFibers()
Iz= fibers.getIz
Iy= fibers.getIy
zCenterOfMass= fibers.getCenterOfMassZ()
yCenterOfMass= fibers.getCenterOfMassY()

print "nfibers= ", nfibers
'''
print "ratio1= ", ratio1
print "ratio2= ", ratio2
print "ratio3= ", ratio3
'''
  
# fname= os.path.basename(__file__)
# if (abs(ratio1-1.0)<1e-5) & (abs(ratio2-1.0)<1e-5) & (abs(ratio3)<1e-5) :
#   print "test ",fname,": ok."
# else:
#   print "test ",fname,": ERROR."
