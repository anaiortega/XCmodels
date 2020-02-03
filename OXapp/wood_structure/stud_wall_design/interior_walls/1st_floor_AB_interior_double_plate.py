# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function

import xc_base
import geom
import xc
from model import predefined_spaces
from solution import predefined_solutions
from materials.awc_nds import AWCNDS_materials as mat
from materials.awc_nds import dimensional_lumber
from materials import typical_materials
from materials.sections import section_properties
import check

inchToMeter= 0.0254
psiToPa= 6894.76

# Loads
from actions import load_cases as lcm
from actions import combinations as combs

# Problem type
sheathingBeam= xc.FEProblem()
sheathingBeam.title= 'Sheating design'
preprocessor= sheathingBeam.getPreprocessor   
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)

studSpacing= 12*inchToMeter
trussSpacing= 12*inchToMeter

# Materials
# Mechanical properties taken from:
# Spruce-pine-fir No. 2 
wood= dimensional_lumber.SprucePineFirWood(grade= 'no_2')
xc_material= wood.defXCMaterial()
plateSection= mat.DimensionLumber(name= '2x6',b= 5.5*inchToMeter, h= 1.5*inchToMeter, woodMaterial= wood)
section= plateSection.defElasticShearSection2d(preprocessor)

span= studSpacing
pointHandler= preprocessor.getMultiBlockTopology.getPoints
infPoints= list()
supPoints= list()
for i in range(0,14):
    x= i*span
    infPoints.append(pointHandler.newPntFromPos3d(geom.Pos3d(x,0.0,0.0)))
    supPoints.append(pointHandler.newPntFromPos3d(geom.Pos3d(x,plateSection.h,0.0)))

lines= preprocessor.getMultiBlockTopology.getLines
infSet= preprocessor.getSets.defSet("inf")
infLines= list()
p0= infPoints[0]
for p in infPoints[1:]:
    l= lines.newLine(p0.tag,p.tag)
    infLines.append(l)
    infSet.getLines.append(l)
    p0= p
supSet= preprocessor.getSets.defSet("sup")
supLines= list()
p0= supPoints[0]
for p in supPoints[1:]:
    l= lines.newLine(p0.tag,p.tag)
    supLines.append(l)
    supSet.getLines.append(l)
    p0= p
infSet.fillDownwards()
supSet.fillDownwards()

# Mesh
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)
# nodes.newSeedNode() DEPRECATED
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= section.name
seedElemHandler.defaultTransformation= "lin"
elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

xcTotalSet= preprocessor.getSets.getSet("total")
mesh= infSet.genMesh(xc.meshDir.I)
infSet.fillDownwards()
mesh= supSet.genMesh(xc.meshDir.I)
supSet.fillDownwards()

## Loaded nodes.
loadedNodes= list()
pos= supPoints[0].getPos+geom.Vector3d(trussSpacing/2.0,0,0) #Position of the first loaded node
xLast= supPoints[-1].getPos.x
while pos.x<xLast:
    n= supSet.getNearestNode(pos)
    loadedNodes.append(supSet.getNearestNode(pos))
    pos+= geom.Vector3d(trussSpacing,0.0,0.0)

# Constraints
supportedNodes= list()
for p in infPoints:
    n= p.getNode()
    modelSpace.fixNode00F(n.tag)
    supportedNodes.append(n)

for n in supSet.nodes:
    pos= n.getInitialPos3d
    nInf= infSet.getNearestNode(pos)
    modelSpace.constraints.newEqualDOF(nInf.tag,n.tag,xc.ID([1]))

for p in supPoints[1:-1]:
    n= p.getNode()
    pos= n.getInitialPos3d
    nInf= infSet.getNearestNode(pos)
    modelSpace.constraints.newEqualDOF(nInf.tag,n.tag,xc.ID([0]))


# Actions
trussLoad= 9.13e3 # N/truss (two trusses here)
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['totalLoad']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

# Total load.
cLC= loadCaseManager.setCurrentLoadCase('totalLoad')
for n in loadedNodes:
    n.newLoad(xc.Vector([0.0,-trussLoad,0.0]))

#We add the load case to domain.
preprocessor.getLoadHandler.getLoadPatterns.addToDomain("totalLoad")

# Solution
# Linear static analysis.
analisis= predefined_solutions.simple_static_linear(sheathingBeam)
result= analisis.analyze(1)

# Checking
check.checkPlates(span, plateSection, section, infSet, supSet, supportedNodes)
