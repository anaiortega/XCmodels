# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import math
import vtk
import xc_base
import geom
import xc
from solution import predefined_solutions
from model import predefined_spaces
from materials import typical_materials
from materials.aci import ACI_materials

from materials.sections import section_properties
from actions import load_cases as lcm
from actions import combinations as combs

# Problem type
precastPlanks= xc.FEProblem()
precastPlanks.title= 'Precast planks on ramp cover'
preprocessor= precastPlanks.getPreprocessor   
nodes= preprocessor.getNodeHandler

#Materials
## Concrete material
concrete= ACI_materials.c4000

## Rectangular cross-section definition
plankSectionGeometry= section_properties.RectangularSection(name="plankSection",b=1.0,h=.30) # Section geometry.
plankSectionMaterial= concrete.getElasticMaterialData() # Section material.
plankSection= plankSectionGeometry.defElasticShearSection2d(preprocessor,plankSectionMaterial)

# Model geometry

## Points.
d1= 1.55170909090909
d2= 3.32509090909091
span= 6.20683636363636

print('d1= ', d1, ' m')
print('d2= ', d2, ' m')
print('span= ', span, ' m')

pointHandler= preprocessor.getMultiBlockTopology.getPoints
p0= pointHandler.newPntFromPos3d(geom.Pos3d(0.0,0.0,0.0))
p1= pointHandler.newPntFromPos3d(geom.Pos3d(d1,0.0,0.0))
p2= pointHandler.newPntFromPos3d(geom.Pos3d(d1+d2,0.0,0.0))
p3= pointHandler.newPntFromPos3d(geom.Pos3d(span,0.0,0.0))

## Lines
lineHandler= preprocessor.getMultiBlockTopology.getLines
l1= lineHandler.newLine(p0.tag,p1.tag)
l2= lineHandler.newLine(p1.tag,p2.tag)
l2= lineHandler.newLine(p2.tag,p3.tag)

# Mesh
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)
nodes.newSeedNode()
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= plankSection.name
seedElemHandler.defaultTransformation= "lin"
elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

xcTotalSet= preprocessor.getSets.getSet('total')
mesh= xcTotalSet.genMesh(xc.meshDir.I)

# Constraints
modelSpace.fixNode00F(p0.getNode().tag)
modelSpace.fixNode00F(p3.getNode().tag)

# Actions
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['load']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)
