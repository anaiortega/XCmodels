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

# Loads
loadManager= preprocessor.getLoadHandler
loadCases= loadManager.getLoadPatterns
## Load modulation.
ts= loadCases.newTimeSeries("constant_ts","ts")
loadCases.currentTimeSeries= "ts"

## Load case definition
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['deadLoad','liveLoad','snowLoad','windLoad']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

## Dead load.
cLC= loadCaseManager.setCurrentLoadCase('deadLoad')
pfsToN_m2= 0.04788026e3
deadLoad= 4914+20.0*pfsToN_m2
for e in xcTotalSet.elements:
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-deadLoad]))
p1.getNode().newLoad(xc.Vector([0.0,-13.02e3,0.0])) 
p2.getNode().newLoad(xc.Vector([0.0,-13.02e3,0.0]))

## Live load.
cLC= loadCaseManager.setCurrentLoadCase('liveLoad')
liveLoad= 40.0*pfsToN_m2
for e in xcTotalSet.elements:
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-liveLoad]))
p1.getNode().newLoad(xc.Vector([0.0,-18.12e3,0.0]))
p2.getNode().newLoad(xc.Vector([0.0,-18.12e3,0.0])) 

## Snow load.
cLC= loadCaseManager.setCurrentLoadCase('snowLoad')
p1.getNode().newLoad(xc.Vector([0.0,-12.92e3,0.0])) 
p2.getNode().newLoad(xc.Vector([0.0,-12.92e3,0.0]))

## Wind load.
cLC= loadCaseManager.setCurrentLoadCase('windLoad')
p1.getNode().newLoad(xc.Vector([0.0,8.17e3,0.0])) 
p2.getNode().newLoad(xc.Vector([0.0,8.17e3,0.0]))

#Load combinations
combContainer= combs.CombContainer()

#Quasi-permanent situations.
combContainer.SLS.qp.add('ELS08', '1.0*selfWeight+1.0*deadLoad+1.0*shrinkage')
#Frequent
combContainer.SLS.freq.add('ELS09A', '1.0*selfWeight+1.0*deadLoad+1.0*shrinkage+0.4*liveLoadA')
combContainer.SLS.freq.add('ELS09B', '1.0*selfWeight+1.0*deadLoad+1.0*shrinkage+0.4*liveLoadB')
#Rare
combContainer.SLS.rare.add('ELS10A', '1.0*selfWeight+1.0*deadLoad+1.0*shrinkage+1.0*liveLoadA+0.6*temperature')
combContainer.SLS.rare.add('ELS10B', '1.0*selfWeight+1.0*deadLoad+1.0*shrinkage+1.0*liveLoadB+0.6*temperature')

#Permanent and transitory situations.
combContainer.ULS.perm.add('ELU2A', '1.35*selfWeight+1.35*deadLoad+1.0*shrinkage+1.5*liveLoadA')
combContainer.ULS.perm.add('ELU2B', '1.35*selfWeight+1.35*deadLoad+1.0*shrinkage+1.5*liveLoadB')
combContainer.ULS.perm.add('ELU3A', '1.35*selfWeight+1.35*deadLoad+1.0*shrinkage+1.5*liveLoadA+0.6*temperature')
combContainer.ULS.perm.add('ELU3B', '1.35*selfWeight+1.35*deadLoad+1.0*shrinkage+1.5*liveLoadB+0.6*temperature')
combContainer.ULS.perm.add('ELU4A', '1.35*selfWeight+1.35*deadLoad+1.0*shrinkage+0.4*liveLoadA+0.6*temperature+1.5*snowLoad')
combContainer.ULS.perm.add('ELU4B', '1.35*selfWeight+1.35*deadLoad+1.0*shrinkage+0.4*liveLoadB+0.6*temperature+1.5*snowLoad')
combContainer.ULS.perm.add('ELU5A', '1.35*selfWeight+1.35*deadLoad+1.5*shrinkage+0.4*liveLoadA+0.6*temperature')
combContainer.ULS.perm.add('ELU5B', '1.35*selfWeight+1.35*deadLoad+1.5*shrinkage+0.4*liveLoadB+0.6*temperature')
combContainer.ULS.perm.add('ELU6A', '1.35*selfWeight+1.35*deadLoad+1.0*shrinkage+0.4*liveLoadA+1.5*temperature')
combContainer.ULS.perm.add('ELU6B', '1.35*selfWeight+1.35*deadLoad+1.0*shrinkage+0.4*liveLoadB+1.5*temperature')

#Accidental
combContainer.ULS.acc.add('A', '1.0*selfWeight+1.0*deadLoad+1.0*shrinkage+1.0*earthquake')    
