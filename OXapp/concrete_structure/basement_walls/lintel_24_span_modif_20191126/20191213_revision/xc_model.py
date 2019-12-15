# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import math
import xc_base
import geom
import xc

from model import predefined_spaces
from materials.aci import ACI_materials
from materials import typical_materials
from postprocess import output_handler

inch2meter= 0.0254

FEcase= xc.FEProblem()
execfile('./xc_model_blocks.py')


xcTotalSet= preprocessor.getSets.getSet('total')

surfSet= preprocessor.getSets.defSet('surfSet')
for s in xcTotalSet.getSurfaces:
    surfSet.getSurfaces.append(s)

rebarSets= dict()
rebarSets[6]= preprocessor.getSets.defSet('rebars06')
rebarSets[6].setProp('rebarArea',ACI_materials.num2Area)
rebarSets[10]= preprocessor.getSets.defSet('rebars06')
rebarSets[10].setProp('rebarArea',ACI_materials.num2Area)
rebarSets[13]= preprocessor.getSets.defSet('rebars13')
rebarSets[13].setProp('rebarArea',ACI_materials.num4Area)
rebarSets[16]= preprocessor.getSets.defSet('rebars16')
rebarSets[16].setProp('rebarArea',ACI_materials.num5Area)
rebarSets[22]= preprocessor.getSets.defSet('rebars22')
rebarSets[22].setProp('rebarArea',ACI_materials.num5Area)
for l in xcTotalSet.getLines:
    if(l.hasProp('labels')):
        labels= l.getProp('labels')
        if(labels.count('rebar_segments_13')>0):
            rebarSets[13].getLines.append(l)
        elif(labels.count('rebar_segments_16')>0):
            rebarSets[16].getLines.append(l)
        elif(labels.count('rebar_segments_22')>0):
            rebarSets[22].getLines.append(l) 
        elif(labels.count('rebars_06')>0):
            rebarSets[06].getLines.append(l)
        elif(labels.count('rebars_10')>0):
            rebarSets[10].getLines.append(l)

linkSet= preprocessor.getSets.defSet('links')
for l in xcTotalSet.getLines:
    if(l.hasProp('labels')):
        labels= l.getProp('labels')
        if(labels.count('link_lines')>0):
            linkSet.getLines.append(l)

# Problem type
preprocessor=FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) 
## Graphic stuff.
oh= output_handler.OutputHandler(modelSpace)

# Materials
concrete=ACI_materials.c4000
reinfSteel=ACI_materials.A615G60
lintelThickness= 10*inch2meter
shellMaterial= typical_materials.defElasticMembranePlateSection(preprocessor, 'shellMaterial', concrete.Ecm(), 0.25, 0.0, lintelThickness)
trussMaterial= typical_materials.defElasticMaterial(preprocessor, 'trussMaterial',reinfSteel.Es)

# Mesh generation
elementSize= 10.0
for s in xcTotalSet.getSurfaces:
    s.setElemSizeIJ(elementSize,elementSize)
    if((s.nDivI!=1) or (s.nDivJ!=1)):
        print('tag: ', s.tag, ' nDivI= ', s.nDivI,' nDivJ= ', s.nDivJ) 
for l in xcTotalSet.getLines:
    l.setElemSize(elementSize)
    if(l.nDiv!=1):
        print('tag: ', l.tag, ' ', l.tipo(), ' nDiv= ', l.nDiv)

## Concrete  
seedElemHandler = preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= shellMaterial.name
seedElem= seedElemHandler.newElement('ShellMITC4', xc.ID([0,0,0,0]))

preprocessor.getMultiBlockTopology.getSurfaces.conciliaNDivs()
surfSet.genMesh(xc.meshDir.I)
surfSet.fillDownwards()

## Reinforcement
seedElemHandler.defaultMaterial= trussMaterial.name
seedElemHandler.dimElem= 3
seedElem= seedElemHandler.newElement('Truss', xc.ID([0,0]))
seedElem.sectionArea= 1

for key in rebarSets:
    rebarSet= rebarSets[key]
    seedElem.sectionArea= rebarSet.getProp('rebarArea')
    for l in rebarSet.getLines:
       l.genMesh(xc.meshDir.I)

# Constraints

## Links
for l in linkSet.getLines:
    n1= l.firstNode
    if(not n1):
        print('line: ',l.tag, ' is not connected at its origin.')
    n2= l.lastNode
    if(not n2):
        print('line: ',l.tag, ' is not connected at its end.')
    
    preprocessor.getBoundaryCondHandler.newRigidBeam(n1.tag,n2.tag)


# Graphics
#oh.displayBlocks()
#oh.displayLocalAxes()
oh.displayFEMesh()

#oh.displayDispRot(itemToDisp='uY')
#oh.displayReactions()
#oh.displayIntForc('M2')
#oh.displayLoads()
