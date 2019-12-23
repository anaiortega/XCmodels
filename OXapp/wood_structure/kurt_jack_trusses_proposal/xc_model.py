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
from materials.sections import section_properties
from postprocess import output_handler
from solution import predefined_solutions

inchToMeter= 0.0254
pound2N=4.45
ft2m=0.3048
psiToPa= 6894.76

FEcase= xc.FEProblem()
FEcase.title= 'Loads on jack trusses at south facade'
execfile('./xc_model_blocks.py')

xcTotalSet= preprocessor.getSets.getSet('total')

jackTrussesSet= preprocessor.getSets.defSet('jackTrussesSet')
girderSet= preprocessor.getSets.defSet('girderSet')
lvlBlindFasciaSet= preprocessor.getSets.defSet('lvlBlindFasciaSet')
regularTrussesSet= preprocessor.getSets.defSet('regularTrussesSet')
for l in xcTotalSet.getLines:
    if(l.hasProp('labels')):
        labels= l.getProp('labels')
        if(labels.count('xc_jack_trusses')>0):
            jackTrussesSet.getLines.append(l)
        elif(labels.count('xc_blue_girder')>0):
            girderSet.getLines.append(l)
        elif(labels.count('xc_lvl_blind_fascia')>0):
            lvlBlindFasciaSet.getLines.append(l)
        elif(labels.count('xc_regular_trusses')>0):
            regularTrussesSet.getLines.append(l)

supportSet= preprocessor.getSets.defSet('supportSet')
for p in xcTotalSet.getPoints:
    if(p.hasProp('labels')):
        labels= p.getProp('labels')
        if(labels.count('xc_supports')>0):
            supportSet.getPoints.append(p)

southFacadeLoads= preprocessor.getSets.defSet('southFacadeLoads')
for p in xcTotalSet.getPoints:
    if(p.hasProp('labels')):
        labels= p.getProp('labels')
        if(labels.count('xc_south_facade_loads')>0):
           southFacadeLoads.getPoints.append(p)

southFacadeLoads2= preprocessor.getSets.defSet('southFacadeLoads2')
for p in xcTotalSet.getPoints:
    if(p.hasProp('labels')):
        labels= p.getProp('labels')
        if(labels.count('xc_south_facade_loads2')>0):
           southFacadeLoads2.getPoints.append(p)
           
eastFacadeLoads= preprocessor.getSets.defSet('eastFacadeLoads')
for p in xcTotalSet.getPoints:
    if(p.hasProp('labels')):
        labels= p.getProp('labels')
        if(labels.count('xc_east_facade_loads')>0):
           eastFacadeLoads.getPoints.append(p)

# Problem type
preprocessor=FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) 

# Materials

## LVL blind fascia: 1.55E (page 10 of the PDF document from "SolidStart")
LVL= typical_materials.MaterialData(name='LVL',E=2.0e6*psiToPa,nu=0.2,rho=500)
lvlBlindSectionGeometry= section_properties.RectangularSection("lvlBlind",b=1.75*inchToMeter,h=22*inchToMeter)
lvlBlindSection= lvlBlindSectionGeometry.defElasticShearSection2d(preprocessor,LVL)

## Graphic stuff.
oh= output_handler.OutputHandler(modelSpace)


# Graphics

oh.displayBlocks()
#oh.displayLocalAxes()
#oh.displayFEMesh()
#oh.displayLoads()

#oh.displayDispRot(itemToDisp='uY')
# oh.displayDispRot(itemToDisp='uZ')
# oh.displayIntForc(itemToDisp= 'N1', setToDisplay= concreteSet)
# oh.displayIntForcDiag(itemToDisp= 'N', setToDisplay= rebarSets[22])
# oh.displayIntForcDiag(itemToDisp= 'N', setToDisplay= rebarSets[16])
# oh.displayIntForcDiag(itemToDisp= 'N', setToDisplay= rebarSets[13])
# oh.displayIntForcDiag(itemToDisp= 'N', setToDisplay= rebarSets[10])
# oh.displayIntForcDiag(itemToDisp= 'N', setToDisplay= rebarSets[06])
#oh.displayReactions()
#oh.displayIntForc('M2', setToDisplay= concreteSet)
