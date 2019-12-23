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
from materials.awc_nds import AWCNDS_materials
from postprocess import output_handler
from solution import predefined_solutions
from actions import load_cases as lcm

inchToMeter= 0.0254
pound2N=4.45
ft2m=0.3048
psiToPa= 6894.76
psf2N_m2= 0.047880258888889e3

FEcase= xc.FEProblem()
FEcase.title= 'Loads on jack trusses at south facade'
execfile('./xc_model_blocks.py')

xcTotalSet= preprocessor.getSets.getSet('total')

jackTrussesSet= preprocessor.getSets.defSet('jackTrussesSet')
girderSet= preprocessor.getSets.defSet('girderSet')
lvlBlindFasciaSet= preprocessor.getSets.defSet('lvlBlindFasciaSet')
regularTrussesSet= preprocessor.getSets.defSet('regularTrussesSet')
for l in xcTotalSet.getLines:
    l.setProp('spacing',12*inchToMeter)
    if(l.hasProp('labels')):
        labels= l.getProp('labels')
        if(labels.count('xc_jack_trusses')>0):
            if(abs(l.getTang(0.0)[1])<1e-3):
                l.setProp('spacing',24*inchToMeter)
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
lvlBlindSection= lvlBlindSectionGeometry.defElasticShearSection3d(preprocessor,LVL)

## Materials LSL 1.55E (page 10 of the PDF document from "SolidStart")
lslJackTrussSection= AWCNDS_materials.LSL155Headers['1.75x14'].defElasticShearSection3d(preprocessor)

## Girder material.
lvlGirderSectionGeometry= section_properties.RectangularSection("lvlGirder", b=1.25*inchToMeter, h=19.09*inchToMeter)
lvlGirderSection= lvlGirderSectionGeometry.defElasticShearSection3d(preprocessor, LVL)

## Regular trusses.
lvlRegTrussSectionGeometry= section_properties.RectangularSection("lvlRegTruss", b=1.25*inchToMeter, h=12.50*inchToMeter)
lvlRegTrussSection= lvlRegTrussSectionGeometry.defElasticShearSection3d(preprocessor, LVL)

# Mesh generation.
lin= preprocessor.getTransfCooHandler.newLinearCrdTransf3d('lin')
lin.xzVector= xc.Vector([1.0,0,0])

seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultTransformation= "lin"

def createMesh(xcSet, section):
    seedElemHandler.defaultMaterial= section.name

    for l in xcSet.getLines:
        vDir= l.getTang(0.0)
        lin.xzVector= xc.Vector([vDir[1], -vDir[0], vDir[2]])
        elem= seedElemHandler.newElement("ElasticBeam3d",xc.ID([0,0]))
        l.genMesh(xc.meshDir.I)
    xcSet.fillDownwards()

    
## Jack trusses.
createMesh(jackTrussesSet, lslJackTrussSection)
## Girder.
createMesh(girderSet, lvlGirderSection)
## Blind fascia.
createMesh(lvlBlindFasciaSet,lvlBlindSection)
## Regular trusses.
createMesh(regularTrussesSet, lvlRegTrussSection)

## "Remove" torsional stiffness
for e in xcTotalSet.elements:
    sp= e.sectionProperties
    sp.J/=100.0
    e.setSectionProperties(sp)
    

# Constraints
for p in supportSet.getPoints:
    if(not p.hasNode):
        lmsg.warning('point: '+str(p)+' not meshed.')
    n= p.getNode()
    modelSpace.fixNode('000_FFF',n.tag)
    
## Graphic stuff.
oh= output_handler.OutputHandler(modelSpace)

# Loads
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['deadLoad', 'liveLoad', 'windLoad', 'snowLoad']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

def loadOnLines(xcSet, loadVector):
    for l in xcSet.getLines:
        spacing= l.getProp('spacing')
        #print('spacing= '+str(spacing)+' load= '+str(spacing*loadVector))
        for e in l.getElements:
            e.vector3dUniformLoadGlobal(spacing*loadVector)

### Dead load.
cLC= loadCaseManager.setCurrentLoadCase('deadLoad')

#### Dead load on elements.
deadL= 15*psf2N_m2
uniformLoad= xc.Vector([0.0,0.0,-deadL])
loadOnLines(jackTrussesSet,uniformLoad)
loadOnLines(girderSet,uniformLoad)
loadOnLines(lvlBlindFasciaSet,uniformLoad)
loadOnLines(regularTrussesSet,uniformLoad)

#### Dead load on nodes.
for p in southFacadeLoads.getPoints:
    if(not p.hasNode):
        lmsg.warning('point: '+str(p)+' not meshed.')
    n= p.getNode()
    n.newLoad(xc.Vector([0.0,0.0,-726.74*pound2N,0.0,0.0,0.0]))
    
for p in southFacadeLoads2.getPoints:
    if(not p.hasNode):
        lmsg.warning('point: '+str(p)+' not meshed.')
    n= p.getNode()
    n.newLoad(xc.Vector([0.0,0.0,-726.74*pound2N*2.4291/.6096/2.0,0.0,0.0,0.0]))

for p in eastFacadeLoads.getPoints:
    if(not p.hasNode):
        lmsg.warning('point: '+str(p)+' not meshed.')
    n= p.getNode()
    n.newLoad(xc.Vector([0.0,0.0,-1044.55*pound2N,0.0,0.0,0.0]))

### Live load.
cLC= loadCaseManager.setCurrentLoadCase('liveLoad')

#### Live load on elements.
liveL= 40.0*psf2N_m2
uniformLoad= xc.Vector([0.0,0.0,-liveL])
loadOnLines(jackTrussesSet,uniformLoad)
loadOnLines(girderSet,uniformLoad)
loadOnLines(lvlBlindFasciaSet,uniformLoad)
loadOnLines(regularTrussesSet,uniformLoad)

#### Live load on nodes.
for p in eastFacadeLoads.getPoints:
    if(not p.hasNode):
        lmsg.warning('point: '+str(p)+' not meshed.')
    n= p.getNode()
    n.newLoad(xc.Vector([0.0,0.0,-1107.39*pound2N,0.0,0.0,0.0]))

### Wind load.
cLC= loadCaseManager.setCurrentLoadCase('windLoad')

#### Wind load on nodes.
for p in eastFacadeLoads.getPoints:
    if(not p.hasNode):
        lmsg.warning('point: '+str(p)+' not meshed.')
    n= p.getNode()
    n.newLoad(xc.Vector([0.0,0.0,488.33*pound2N,0.0,0.0,0.0]))

### Snow load.
cLC= loadCaseManager.setCurrentLoadCase('snowLoad')

#### Snow load on nodes.
for p in eastFacadeLoads.getPoints:
    if(not p.hasNode):
        lmsg.warning('point: '+str(p)+' not meshed.')
    n= p.getNode()
    n.newLoad(xc.Vector([0.0,0.0,-772.87*pound2N,0.0,0.0,0.0]))

preprocessor.getLoadHandler.getLoadPatterns.addToDomain('snowLoad')

# Solution
# Linear static analysis.
analisis= predefined_solutions.simple_static_linear(FEcase)
result= analisis.analyze(1)


# Graphics

#oh.displayBlocks()
oh.displayLocalAxes(setToDisplay= girderSet)
#oh.displayFEMesh()
oh.displayLoads()#setToDisplay= lvlBlindFasciaSet)

#oh.displayDispRot(itemToDisp='uY')
oh.displayDispRot(itemToDisp='uZ')
oh.displayIntForcDiag(itemToDisp= 'Mz', setToDisplay= jackTrussesSet)
oh.displayIntForcDiag(itemToDisp= 'Vy', setToDisplay= jackTrussesSet)
oh.displayIntForcDiag(itemToDisp= 'Mz', setToDisplay= girderSet)
oh.displayReactions(setToDisplay= girderSet)
oh.displayIntForcDiag(itemToDisp= 'Vy', setToDisplay= girderSet)
oh.displayIntForcDiag(itemToDisp= 'Mz', setToDisplay= regularTrussesSet)
oh.displayReactions(setToDisplay= regularTrussesSet)
oh.displayIntForcDiag(itemToDisp= 'Vy', setToDisplay= regularTrussesSet)
#oh.displayIntForc('Q1')
