# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function

import xc_base
import geom
import xc
from model import predefined_spaces
from solution import predefined_solutions
from materials.awc_nds import AWCNDS_materials
from materials import typical_materials

# Loads
from actions import load_cases as lcm
from actions import combinations as combs

# Problem type
sheathingBeam= xc.FEProblem()
sheathingBeam.title= 'Sheating design'
preprocessor= sheathingBeam.getPreprocessor   
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)

# Materials
# Mechanical properties taken from:
# http://www.pfsteco.com/techtips/pdf/tt_plywooddesigncapacities
structuralPanelGeom= AWCNDS_materials.PlywoodPanel('TECO 32/16', b=1.0, h= 0.594*0.0254, shear_constant= 3)
plywood= typical_materials.MaterialData(name='TECO 32/16',E=4161501119.15,nu=0.2,rho=500)
section= structuralPanelGeom.defElasticShearSection2d(preprocessor,plywood)
EI= section.sectionProperties.EI()
EIRef= 126500*4.44822*(0.0254)**2/0.3048
print(EIRef/EI*4.16e9)
print((EI-EIRef)/EIRef)

thickness= structuralPanelGeom.h

span= (32-1.5+0.25)*0.0254 # 32
pointHandler= preprocessor.getMultiBlockTopology.getPoints
pt1= pointHandler.newPntFromPos3d(geom.Pos3d(0.0,0.0,0.0))
pt2= pointHandler.newPntFromPos3d(geom.Pos3d(span,0.0,0.0))
pt3= pointHandler.newPntFromPos3d(geom.Pos3d(2.0*span,0.0,0.0))
pt4= pointHandler.newPntFromPos3d(geom.Pos3d(3.0*span,0.0,0.0))

lines= preprocessor.getMultiBlockTopology.getLines
l1= lines.newLine(pt1.tag,pt2.tag)
l2= lines.newLine(pt2.tag,pt3.tag)
l3= lines.newLine(pt3.tag,pt4.tag)

infSet= preprocessor.getSets.defSet("inf")
infSet.getLines.append(l1)
infSet.getLines.append(l2)
infSet.getLines.append(l3)

# Mesh
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)
nodes.newSeedNode()
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= section.name
seedElemHandler.defaultTransformation= "lin"
elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

xcTotalSet= preprocessor.getSets.getSet("total")
mesh= infSet.genMesh(xc.meshDir.I)
infSet.fillDownwards()

# Constraints
for p in [pt1,pt2,pt3,pt4]:
    n= p.getNode()
    modelSpace.fixNode00F(n.tag)

for n in infSet.getNodes:
    pos= n.getInitialPos3d
    nInf= infSet.getNearestNode(pos)
    modelSpace.constraints.newEqualDOF(nInf.tag,n.tag,xc.ID([1]))

# Actions
L= 32.88108719285194*47.88026 # Live load N/m2
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['liveLoad']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

# Live load.
cLC= loadCaseManager.setCurrentLoadCase('liveLoad')
for e in infSet.getElements:
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-L]))

#We add the load case to domain.
preprocessor.getLoadHandler.getLoadPatterns.addToDomain("liveLoad")

# Solution
# Linear static analysis.
analisis= predefined_solutions.simple_static_linear(sheathingBeam)
result= analisis.analyze(1)

uYMax= -1e6
for n in infSet.getNodes:
    uY= -n.getDisp[1]
    uYMax= max(uY,uYMax)

r= span/uYMax
print('uYMax= ', uYMax*1e3, ' mm (L/'+str(r)+')')

DeltaLL= 12*L*span**4/1743.0/section.sectionProperties.EI()
r= span/DeltaLL
print('DeltaLL= ', DeltaLL*1e3, ' mm (L/'+str(r)+')')

