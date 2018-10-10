# -*- coding: utf-8 -*-
import math
import xc_base
import geom
import xc
from solution import predefined_solutions
from model import predefined_spaces
from materials import typical_materials
from materials.sections import section_properties
from model.sets import sets_mng as sUtils
from actions import load_cases as lcm
from materials.sia262 import SIA262_materials
from actions import combinations as cc

deck= xc.FEProblem()
preprocessor= deck.getPreprocessor
nodes= preprocessor.getNodeHandler
elements= preprocessor.getElementHandler
groups= preprocessor.getSets

#Materials
# Concrete.
concrete= SIA262_materials.c25_30
Ec= concrete.getEcm()
deckThickness= 0.35
deckUnitWeight= deckThickness*25e3
parapetUnitWeight= deckUnitWeight
sccDeck= section_properties.RectangularSection("sccDeck",1.0,deckThickness)#,Ec,0.2)
matData= typical_materials.MaterialData(name='deckConcrete',E=Ec,nu=0.2,rho=2500)
matDeck= sccDeck.defElasticShearSection2d(preprocessor,matData)

# Masonry bearing.
kSpandrel= 5e8
#kYSpandrel= typical_materials.defElastNoTensMaterial(preprocessor, "kYSpandrel",kSpandrel)
kYSpandrel= typical_materials.defElasticMaterial(preprocessor, "kYSpandrel",kSpandrel)
kXSpandrel= typical_materials.defElasticMaterial(preprocessor, "kXSpandrel",kSpandrel/10.0)
kFill= 5e7
#kYFill= typical_materials.defElastNoTensMaterial(preprocessor, "kYFill",kFill)
kYFill= typical_materials.defElasticMaterial(preprocessor, "kYFill",kFill)
kXFill= typical_materials.defElasticMaterial(preprocessor, "kXFill",kFill/10.0)

#Mesh
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)
nodes.newSeedNode()
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "sccDeck"
seedElemHandler.defaultTransformation= "lin"
elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

# Bridge deck model:
#
#      A +                                           + H
#        |                                           |
#        |                                           |
#      B +--+----+---------------------------+----+--+
#           C    D                           E    F  G

H= 1.54
W0= 0.23 #C
W1= W0+0.91 #D
W2= W1+3.17 #E
W3= W2+0.91 #F
W4= W3+0.23 #G

xCenter= W4/2.0
totalLength= W4+2.0*H
points= preprocessor.getMultiBlockTopology.getPoints
ptA= points.newPntFromPos3d(geom.Pos3d(0.0,H,0.0)) #Top of left parapet (A).
ptB= points.newPntFromPos3d(geom.Pos3d(0.0,0.0,0.0)) #Bottom of left parapet (B).
ptC= points.newPntFromPos3d(geom.Pos3d(W0,0.0,0.0)) #Begin of left spandrel (C).
ptD= points.newPntFromPos3d(geom.Pos3d(W1,0.0,0.0)) #End of left spandrel (D).
ptE= points.newPntFromPos3d(geom.Pos3d(W2,0.0,0.0)) #Begin of right spandrel (E).
ptF= points.newPntFromPos3d(geom.Pos3d(W3,0.0,0.0)) #End of right spandrel (F).
ptG= points.newPntFromPos3d(geom.Pos3d(W4,0.0,0.0)) #Bottom of right parapet (G).
ptH= points.newPntFromPos3d(geom.Pos3d(W4,H,0.0)) #Top of right parapet (H).
path= [ptA,ptB,ptC,ptD,ptE,ptF,ptG,ptH]

elementLength= 0.20
lines= preprocessor.getMultiBlockTopology.getLines
bridgeSectionLines= []
for points in zip(path, path[1:]):
    newLine= lines.newLine(points[0].tag,points[1].tag)
    newLine.setElemSize(elementLength)
    bridgeSectionLines.append(newLine)

parapetLines= [bridgeSectionLines[0],bridgeSectionLines[-1]]
deckLines= bridgeSectionLines[1:-1]

spandrelSupported= preprocessor.getSets.defSet("spandrelSupported")
spandrelSupported.getLines.append(bridgeSectionLines[2])
spandrelSupported.getLines.append(bridgeSectionLines[4])
fillSupported= preprocessor.getSets.defSet("fillSupported")
fillSupported.getLines.append(bridgeSectionLines[3])

setTotal= preprocessor.getSets.getSet("total")
mesh= setTotal.genMesh(xc.meshDir.I)

deckSet= preprocessor.getSets.defSet("deckSet")
for l in deckLines:
  deckSet.getLines.append(l)
deckSet.fillDownwards()
deckSet.genDescr= 'Dalle.'
deckSet.sectDescr=['noeud i','noeud j']
parapetSet= preprocessor.getSets.defSet("parapetSet")
for l in parapetLines:
  parapetSet.getLines.append(l)
parapetSet.fillDownwards()
parapetSet.genDescr= 'Parapets.'
parapetSet.sectDescr=['noeud i','noeud j']
bridgeSectionSet= preprocessor.getSets.defSet("bridgeSectionSet")
for l in bridgeSectionLines:
  bridgeSectionSet.getLines.append(l)
bridgeSectionSet.fillDownwards()
bridgeSectionSet.genDescr= 'Tablier.'
bridgeSectionSet.sectDescr=['noeud i','noeud j']

#Constraints

# Springs on nodes.
lngTot= 0.0
spandrelFixedNodes= []
spandrelBearingElements= []
spandrelSupported.fillDownwards()
spandrelSupported.computeTributaryLengths(False)
for n in spandrelSupported.getNodes:
    lT= n.getTributaryLength()
    lngTot+= lT
    kYSpandrel.E= kSpandrel*lT
    idFixedNode, idElem= modelSpace.setBearing(n.tag,[kXSpandrel.name,kYSpandrel.name])
    modelSpace.fixNode000(idFixedNode.tag)
    spandrelFixedNodes.append(idFixedNode)
    spandrelBearingElements.append(idElem)

fillFixedNodes= []
fillBearingElements= []
fillSupported.fillDownwards()
fillSupported.computeTributaryLengths(False)
for n in fillSupported.getNodes:
    lT= n.getTributaryLength()
    lngTot+= lT
    kYFill.E= kFill*lT
    idFixedNode, idElem= modelSpace.setBearing(n.tag,[kXFill.name,kYFill.name])
    modelSpace.fixNode000(idFixedNode.tag)    
    fillFixedNodes.append(idFixedNode)
    fillBearingElements.append(idElem)

for n in setTotal.getNodes:
    if n.isFree:
        print n.tag, n.getInitialPos2d
print 'number of free nodes: ', deck.getDomain.getMesh.getNumFreeNodes()

# Actions
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['GselfWeight','GdeadLoad','vehicleLiveLoad','truckLiveLoad','pedestrianLiveLoad','temp_up','temp_down','impactLoad','eQuake']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

# Self weight.
cLC= loadCaseManager.setCurrentLoadCase('GselfWeight')
for e in deckSet.getElements:
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-deckUnitWeight]))
for e in parapetSet.getElements:
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-parapetUnitWeight]))
    
# Dead load
cLC= loadCaseManager.setCurrentLoadCase('GdeadLoad')
dz0= 0.23
dz1= 0.23+0.18 #+0.8 Foot path removed 10/10/2018 LCPT
dz2= dz1+4.64 #Carriageway
dz3= dz2+0.18 #Bordure
deckZones=[dz0,dz1,dz2,dz3]
footpathWeight= 0.25*24e3+1e3 #24 kN/m3 + deck waterproofing (1kN/m2).
wearingWeight= 0.11*24e3+1e3 #24 kN/m3 + deck waterproofing (1kN/m2).
borderWeight= 0.25*24e3+1e3 #24 kN/m3 + deck waterproofing (1kN/m2).
deadLoadsByZone= [footpathWeight,wearingWeight,borderWeight]
def getElementZone(element):
    retval= None
    x= e.getPosCentroid(True).x
    sz= len(deckZones)
    for i in range(0,sz):
        if(x<deckZones[i]):
            retval= i
            break;
    if(retval==0): retval= None
    return retval
  
for e in deckSet.getElements:
    eZone= getElementZone(e)
    if(eZone):
        load= deadLoadsByZone[eZone-1]
        e.vector2dUniformLoadGlobal(xc.Vector([0.0,-load]))

# Live load (vehicle).
cLC= loadCaseManager.setCurrentLoadCase('vehicleLiveLoad')
wheelOffset= (4.0-1.3)/2.0
wheelLoad= 80e3/2.0
wheelPositions= [dz1+wheelOffset,dz1+wheelOffset+1.3]
for p in wheelPositions:
    e= deckSet.getNearestElement(geom.Pos3d(p,0.0,0.0))
    length= e.getLineSegment(True).getLength()
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-wheelLoad/length]))

# Live load (truck).
cLC= loadCaseManager.setCurrentLoadCase('truckLiveLoad')
truckWheelOffset= (4.0-2)/2.0
truckWheelLoad= 160e3/2.0
truckWheelPositions= [dz1+truckWheelOffset,dz1+truckWheelOffset+1.3]
for p in truckWheelPositions:
    e= deckSet.getNearestElement(geom.Pos3d(p,0.0,0.0))
    length= e.getLineSegment(True).getLength()
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-truckWheelLoad/length]))

# Pedestrian live load
cLC= loadCaseManager.setCurrentLoadCase('pedestrianLiveLoad')
pedestrianLoad= 4e3 #Crowded bridge: (4kN/m2).
for e in deckSet.getElements:
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-pedestrianLoad]))

#Temperature increment.
cLC= loadCaseManager.setCurrentLoadCase('temp_up')
alphaAT= 20.0*10e-6

eleLoad= cLC.newElementalLoad("beam_strain_load")
eleLoad.elementTags= bridgeSectionSet.getElements.getTags()
defPlane= xc.DeformationPlane(alphaAT)
eleLoad.backEndDeformationPlane= defPlane
eleLoad.frontEndDeformationPlane= defPlane


# Impact load
cLC= loadCaseManager.setCurrentLoadCase('impactLoad')
impactLoad= 300e3/0.4/(1.5+H-0.4) #Impact load 300kN on 0.4 square meters.
affectedElements= []
for e in parapetSet.getElements:
    c= e.getPosCentroid(True)
    if(c.x>2.5 and c.y>(H-0.4)):
        affectedElements.append(e)
for e in affectedElements:
  e.vector2dUniformLoadGlobal(xc.Vector([impactLoad,0.0]))

#LOAD COMBINATIONS
combContainer= cc.CombContainer()  #Container of load combinations

# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
#Frequent combinations.
combContainer.SLS.freq.add('ELSF01', '1.0*GselfWeight+1.0*GdeadLoad+0.75*vehicleLiveLoad')
#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP01', '1.0*GselfWeight+1.0*GdeadLoad')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
# Type 1: Overall stablity.
# Type 2: Structural strength.
# Type 3: Foundation strength.
# Type 4: Fatigue.
#Persistent and transient design situations. Type 1. Overall stability.
#combContainer.ULS.perm.add('PP', '1.0*truckLiveLoad')
combContainer.ULS.perm.add('ELUT101', '0.9*GselfWeight+0.9*GdeadLoad')
#Persistent and transitory situations. Type 2. Structure strength.
combContainer.ULS.perm.add('ELUT201','1.35*GselfWeight+1.35*GdeadLoad+1.5*vehicleLiveLoad')
combContainer.ULS.perm.add('ELUT202','1.35*GselfWeight+1.35*GdeadLoad+1.5*pedestrianLiveLoad')
#Persistent and transitory situations. Type 4. Fatigue.
combContainer.ULS.fatigue.add('ELUT40','1.00*GselfWeight+1.0*GdeadLoad')
combContainer.ULS.fatigue.add('ELUT41','1.00*GselfWeight+1.0*GdeadLoad+1.0*vehicleLiveLoad')

#Accidental design situation according to SIA 260 section 4.4.3.5.
combContainer.ULS.perm.add('AT101','0.9*GselfWeight+0.9*GdeadLoad+1.0*truckLiveLoad+1.0*impactLoad')
combContainer.ULS.perm.add('AT201','0.8*GselfWeight+0.8*GdeadLoad+1.0*truckLiveLoad+1.0*impactLoad')
combContainer.ULS.perm.add('AT202','1.35*GselfWeight+1.35*GdeadLoad+1.0*truckLiveLoad+1.0*impactLoad')


#We add the load case to domain.
# preprocessor.getLoadHandler.getLoadPatterns.addToDomain("temp_up")


# Solution

# # Linear static analysis.
# analisis= predefined_solutions.simple_static_linear(deck)
# result= analisis.analyze(1)

# #Non linear static analysis
# solution= predefined_solutions.SolutionProcedure()
# solution.convergenceTestTol= 1.0e-2
# analysis= solution.simpleNewtonRaphsonBandGen(deck)
# result= analysis.analyze(10) 



