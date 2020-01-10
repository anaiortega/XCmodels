# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
import xc_base
import geom
import xc
from model import predefined_spaces
from solution import predefined_solutions
from materials.sections import section_properties
from materials import typical_materials
from materials.awc_nds import AWCNDS_materials


# Loads
from actions import load_cases as lcm

# Units
inchToMeter= 2.54/100.0
footToMeter= 0.3048
poundToN= 4.44822
psiToPa= 6894.76

# Problem type
xcProblem= xc.FEProblem()
xcProblem.title= 'Header L= 7 feet on third floor bearing facades.'
preprocessor= xcProblem.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)

# Materials LSL 1.55E (page 4 of the PDF document from "SolidStart")
header= AWCNDS_materials.LSL155Headers['1.75x11-7/8']
section= header.defElasticShearSection2d(preprocessor)

# Header geometry
headerSpan= 7.5*footToMeter

## Key points
pointHandler= preprocessor.getMultiBlockTopology.getPoints
p0= pointHandler.newPntFromPos3d(geom.Pos3d(0.0,0.0,0.0))
p1= pointHandler.newPntFromPos3d(geom.Pos3d(headerSpan,0.0,0.0))

## Lines
lineHandler= preprocessor.getMultiBlockTopology.getLines
l1= lineHandler.newLine(p0.tag,p1.tag)

# Mesh
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)
nodes.newSeedNode()
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= section.name
seedElemHandler.defaultTransformation= "lin"
elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

xcTotalSet= preprocessor.getSets.getSet('total')

mesh= xcTotalSet.genMesh(xc.meshDir.I)

# Constraints
modelSpace.fixNode00F(p0.getNode().tag)
modelSpace.fixNode00F(p1.getNode().tag)

# Actions
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['load']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

## Loads on nodes.
cLC= loadCaseManager.setCurrentLoadCase('load')
facadeLoad= 16.01e3 # kN/m facade load AB zone
uniformLoad= xc.Vector([0.0,-facadeLoad,0.0]) 
for e in xcTotalSet.elements:
  e.vector2dUniformLoadGlobal(uniformLoad)


#We add the load case to domain.
preprocessor.getLoadHandler.getLoadPatterns.addToDomain('load')

# Solution
# Linear static analysis.
analisis= predefined_solutions.simple_static_linear(xcProblem)
result= analisis.analyze(1)

# Checking
nodes.calculateNodalReactions(True,1e-7)
Vmax= max(p0.getNode().getReaction[1],p1.getNode().getReaction[1])
eMidSpan= xcTotalSet.getNearestElement(geom.Pos3d(headerSpan/2.0,0.0,0.0))
Mmax= max(abs(eMidSpan.getM1),abs(eMidSpan.getM2))
R0= p0.getNode().getReaction[1]
R1= p1.getNode().getReaction[1]
Fc_perp= header.material.Fc_perp # Perpendicular to grain compression stress.
Fc_studs= 800*psiToPa # Parallel to grain compression stress.
bearingNecLength= R0/min(Fc_perp,Fc_studs)/header.b
numberOfJakeStuds= bearingNecLength/(2*inchToMeter)

print('*****',xcProblem.title,'******')
print('Uniform load: ', 2.0*Vmax/headerSpan/1e3, ' kN/m')
print('Header: ', header.sectionName)

## Shear
Vu= header.Vs
print('Vmax= ', Vmax/1e3, ' kN Vu= ', Vu/1e3, ' kN; F= ',Vmax/Vu)

## Bending
Mu= header.Ms
print('Mmax= ', Mmax/1e3, ' kN Mu= ', Mu/1e3, ' kN; F= ',Mmax/Mu)

## Deflection
nMidSpan= l1.getNearestNode(geom.Pos3d(headerSpan/2.0,0.0,0.0))
dMidSpan= nMidSpan.getDisp[1]
ratio1= abs(dMidSpan)/headerSpan
print('dY= ',dMidSpan*1e3,' mm; ratio= L/', 1.0/ratio1)

## Reactions
print('R0= ', R0/1e3, ' kN')
print('R1= ', R1/1e3, ' kN')
print('bearing lenght= ', bearingNecLength, ' m')
print('number of jake studs= ', numberOfJakeStuds)