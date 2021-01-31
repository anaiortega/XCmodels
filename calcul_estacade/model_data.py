# -*- coding: utf-8 -*-
import math
import xc_base
import geom
import xc
from postprocess import utils_display

#Material definition
from materials import typical_materials
from materials.sia262 import SIA262_materials
from materials.sections import section_properties

#Parts definition
import re

#Mesh definition
from model import predefined_spaces

#Loads
from actions import load_cases as lcm
from actions import combinations as combs

#Solution
from solution import predefined_solutions


gilamontDock= xc.FEProblem()
exec(open('./xc_model_blocks.py').read()))


xcTotalSet= preprocessor.getSets.getSet('total')

quakeAccel= 1.25 #m/s2

#Material definition.
concrete= SIA262_materials.c30_37
nu= 0.3 # Poisson coefficient.
dens= 2500 # Density kg/m3.

#Deck.
#reductionFactor= 1.0 #
reductionFactor= 7.0 #Reduction factor
Econcrete= concrete.getEcm()/reductionFactor
EcDeck= Econcrete # Concrete's Young modulus.
hDeck= 0.20 # Deck thickness.
rhoDeck= hDeck*dens

shellDeck= typical_materials.defElasticMembranePlateSection(preprocessor,"shellDeck",EcDeck,nu,rhoDeck,hDeck)

#Dock.
EcDock= Econcrete # Concrete's Young modulus.
hDock= 0.18 # Dock thickness.
rhoDock= hDock*dens

shellDock= typical_materials.defElasticMembranePlateSection(preprocessor,"shellDock",EcDock,nu,rhoDock,hDock)

#Parapet.
EcParapet= Econcrete # Concrete's Young modulus.
bParapet= 0.25 # Parapet thickness.
rhoParapet= bParapet*dens

shellParapet= typical_materials.defElasticMembranePlateSection(preprocessor,"shellParapet",EcParapet,nu,rhoParapet,bParapet)

#Columns.
rColumns= 0.25/2.0 # Column radius.
aColumns= math.pi*rColumns**2 # Column area.
rhoColumns= aColumns*dens # Mass per unit length.
cColumns= typical_materials.BasicElasticMaterial(Econcrete,nu,rho= rhoColumns) #Concrete elastic representation.
sccColumns= section_properties.CircularSection("sccColumns",rColumns)
beamColumns= sccColumns.defElasticShearSection3d(preprocessor,cColumns)

#Transverse reinforcement
hTrsvReinf= 0.1 # Reinforcement height.
bTrsvReinf= 0.25 # Reinforcement width.
aTrsvReinf= hTrsvReinf*bTrsvReinf
rhoTrsvReinf= aTrsvReinf*dens
cTrsvReinf= typical_materials.BasicElasticMaterial(Econcrete,nu,rho= rhoTrsvReinf) #Concrete elastic representation.
sccTrsvReinf= section_properties.RectangularSection("sccTrsvReinf",bTrsvReinf,hTrsvReinf)
beamTrsvReinf= sccTrsvReinf.defElasticShearSection3d(preprocessor,cTrsvReinf)

#Model parts.
modelParts= []
modelSurfaces=[]
modelLines= []
totalSurfSet= xcTotalSet.getSurfaces
totalLineSet= xcTotalSet.getLines

#Deck
setDeck= preprocessor.getSets.defSet("setDeck")
setDeck.genDescr= 'dalle quai'
setDeck.sectDescr=['armature longitudinale','armature transversale']
setDeck.material= shellDeck
setDeck.elemSize= 0.3
setDeck.selfWeight= xc.Vector([0.0,0.0,-9.81*rhoDeck])
rhoAsphalt= (1e3+2.4e3)/9.81
setDeck.deadLoad= xc.Vector([0.0,0.0,-9.81*rhoAsphalt])
setDeck.quake= xc.Vector([quakeAccel*(rhoDeck+rhoAsphalt),0.0,-0.7*quakeAccel*(rhoDeck+rhoAsphalt)])
modelSurfaces.append(setDeck)
#Dock
setDock= preprocessor.getSets.defSet("setDock")
setDock.genDescr= 'mur quai'
setDock.sectDescr=['armature transversale','armature longitudinale']
setDock.material= shellDock
setDock.elemSize= 0.3
setDock.selfWeight= xc.Vector([0.0,0.0,-9.81*rhoDock])
rhoPrefab= 1360/2.0/0.75
setDock.deadLoad= xc.Vector([0.0,0.0,-9.81*rhoPrefab]) #Elément en equerre pour quai per area unit.
setDock.quake= xc.Vector([quakeAccel*(rhoDock+rhoPrefab),0.0,-0.7*quakeAccel*(rhoDock+rhoPrefab)])
modelSurfaces.append(setDock)
#Parapet
setParapet= preprocessor.getSets.defSet("setParapet")
setParapet.genDescr= 'parapet'
setParapet.sectDescr=['armature transversale','armature longitudinale']
setParapet.material= shellParapet
setParapet.elemSize= 0.3
setParapet.selfWeight= xc.Vector([0.0,0.0,-9.81*rhoParapet])
rhoRailing= 0.5e3/0.5/9.81
setParapet.deadLoad= xc.Vector([0.0,0.0,-9.81*rhoRailing]) #Railing per area unit.
setParapet.quake= xc.Vector([quakeAccel*(rhoParapet+rhoRailing),0.0,-0.7*quakeAccel*(rhoParapet+rhoRailing)])
modelSurfaces.append(setParapet)

trfs= preprocessor.getTransfCooHandler

#Columns
columnTrf= trfs.newLinearCrdTransf3d('columnTrf')
columnTrf.xzVector= xc.Vector([0,1,0])
setColumns= preprocessor.getSets.defSet("setColumns")
setColumns.genDescr= 'columns'
setColumns.sectDescr=['noeud i','noeud j']
setColumns.material= beamColumns
setColumns.coordTransf= columnTrf
setColumns.elementLength= 0.5
setColumns.selfWeight= xc.Vector([0.0,0.0,-9.81*rhoColumns])
modelLines.append(setColumns)
#Transverse reinforcements
trsvReinfTrf= trfs.newLinearCrdTransf3d('trsvReinfTrf')
trsvReinfTrf.xzVector= xc.Vector([1,0,0])
setTransverseReinforcements= preprocessor.getSets.defSet("setTransverseReinforcements")
setTransverseReinforcements.material= beamTrsvReinf
setTransverseReinforcements.coordTransf= trsvReinfTrf
setTransverseReinforcements.elementLength= setDeck.elemSize
setTransverseReinforcements.selfWeight= xc.Vector([0.0,0.0,-9.81*rhoTrsvReinf])
modelLines.append(setTransverseReinforcements)

modelParts.extend(modelSurfaces)
modelParts.extend(modelLines)

#we populate the parts sets
for s in totalSurfSet:
  labels= s.getProp("labels")
  layerName= labels[0]
  if(re.match('deck.*',layerName)):
    s.setElemSizeIJ(setDeck.elemSize,setDeck.elemSize)
    s.setProp("label",layerName)
    setDeck.getSurfaces.append(s)
  if(re.match('dock.*',layerName)):
    s.setElemSizeIJ(setDock.elemSize,setDock.elemSize)
    setDock.getSurfaces.append(s)
  if(re.match('parapet.*',layerName)):
    s.setElemSizeIJ(setParapet.elemSize,setParapet.elemSize)
    setParapet.getSurfaces.append(s)
    
for l in totalLineSet:
  if(l.hasProp("labels")):
    labels= l.getProp("labels")
    layerName= labels[0]
    if(re.match('P.*',layerName)):
      l.setElemSize(setColumns.elementLength)
      setColumns.getLines.append(l)
    if(re.match('T.*',layerName)):
      l.setElemSize(setTransverseReinforcements.elementLength)
      setTransverseReinforcements.getLines.append(l)

print 'number of columns: ', len(setColumns.getLines)
# length= 0.0
# for l in setColumns.getLines:
#   length+= l.getLength()
# print 'length= ', length
# exit()
  
print 'number of short beams: ', len(setTransverseReinforcements.getLines)
  
for part in modelParts:
  part.fillDownwards()

preprocessor.getMultiBlockTopology.getSurfaces.conciliaNDivs()

#Mesh generation.
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics3D(nodes)

seedElemHandler= preprocessor.getElementHandler.seedElemHandler
#seedElemHandler.defaultTag= 1

for part in modelSurfaces:
  seedElemHandler.defaultMaterial= part.material.getName()
  for s in part.getSurfaces:
    elem= seedElemHandler.newElement("ShellMITC4",xc.ID([0,0,0,0]))
    s.genMesh(xc.meshDir.I)

for part in modelLines:
  seedElemHandler.defaultMaterial= part.material.getName()
  for l in part.getLines:
    seedElemHandler.defaultTransformation= part.coordTransf.getName()
    elem= seedElemHandler.newElement("ElasticBeam3d",xc.ID([0,0]))
    l.genMesh(xc.meshDir.I)

print 'number of nodes= ', len(xcTotalSet.nodes)

# Constraints
fixedNodes= list()
constraints= preprocessor.getBoundaryCondHandler
for pos in footingPositions:
  n= xcTotalSet.getNearestNode(geom.Pos3d(pos[0],pos[1],pos[2]))
  modelSpace.fixNode000_FFF(n.tag)
  fixedNodes.append(n)

for pos in bearingPositions:
  n= xcTotalSet.getNearestNode(geom.Pos3d(pos[0],pos[1],pos[2]))
  modelSpace.constraints.newSPConstraint(n.tag,2,0.0) #Zero z displacement.
  fixedNodes.append(n)

springLines= preprocessor.getSets.defSet("springLines")
for l in xcTotalSet.getLines:
  kPoints= l.getKPoints()
  if((kPoints[0] in springKeyPoints) and (kPoints[1] in springKeyPoints)):
    springLines.getLines.append(l)

springLines.fillDownwards()

print 'number of spring lines: ', len(springLines.getLines)

length= 0.0
springNodes= preprocessor.getSets.defSet("springLines")
for l in springLines.getLines:
  length+= l.getLength()
  for n in l.nodes:
    springNodes.nodes.append(n)

tributaryLength= length/len(springNodes.nodes)

print 'length= ', length
print 'number of spring nodes= ', len(springNodes.nodes)
print 'tributaryLength= ', tributaryLength

kV= typical_materials.defElasticMaterial(preprocessor, "kV",40e6)
kH= typical_materials.defElasticMaterial(preprocessor, "kH",4e6)

for n in springNodes.nodes:
  #print "before k= ", kY.E
  kV.E= 40e6*tributaryLength
  kH.E= 4e6*tributaryLength
  fixedNode, newElem= modelSpace.setBearing(n.tag,['kH','kH','kV'])
  fixedNodes.append(fixedNode)

#Shell elements.
shellElements= preprocessor.getSets.defSet("shellElements")
beamElements= preprocessor.getSets.defSet("beamElements")
for e in xcTotalSet.elements:
  if(e.type()=='XC::ShellMITC4'):
    shellElements.elements.append(e)
  elif(e.type()=='XC::ElasticBeam3d'):
    beamElements.elements.append(e)
shellElements.fillDownwards()
beamElements.fillDownwards()

#Loads
loadManager= preprocessor.getLoadHandler
loadCases= loadManager.getLoadPatterns
#Load modulation.
ts= loadCases.newTimeSeries("constant_ts","ts")
loadCases.currentTimeSeries= "ts"

#Load case definition
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['selfWeight','deadLoad','shrinkage','liveLoadA', 'liveLoadB','temperature','snowLoad','earthquake']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

for part in modelParts:
  part.fillDownwards()

## Self weight.
cLC= loadCaseManager.setCurrentLoadCase('selfWeight')
for part in modelSurfaces:
  weight= part.selfWeight
  for e in part.elements:
    e.vector3dUniformLoadGlobal(weight)

for part in modelLines:
  weight= part.selfWeight
  for e in part.elements:
    e.vector3dUniformLoadGlobal(weight)

## Dead load.
cLC= loadCaseManager.setCurrentLoadCase('deadLoad')
for part in modelSurfaces:
  weight= part.deadLoad
  for e in part.elements:
    e.vector3dUniformLoadGlobal(weight)

for part in modelLines:
  if hasattr(part,'deadLoad'):
    weight= part.deadLoad
    for e in part.elements:
      e.vector3dUniformLoadGlobal(weight)

#Shrinkage.
cLC= loadCaseManager.setCurrentLoadCase('shrinkage')
shrinkage= -4.6e-4
for part in modelSurfaces:
  eleLoad= cLC.newElementalLoad("shell_strain_load")
  eleLoad.elementTags= part.elements.getTags()
  eleLoad.setStrainComp(0,0,shrinkage) #(id of Gauss point, id of component, value)
  eleLoad.setStrainComp(0,1,shrinkage) 
  eleLoad.setStrainComp(1,0,shrinkage)
  eleLoad.setStrainComp(1,1,shrinkage)
  eleLoad.setStrainComp(2,0,shrinkage)
  eleLoad.setStrainComp(2,1,shrinkage)
  eleLoad.setStrainComp(3,0,shrinkage)
  eleLoad.setStrainComp(3,1,shrinkage)

for part in modelLines:
  eleLoad= cLC.newElementalLoad("beam_strain_load")
  eleLoad.elementTags= part.elements.getTags()
  defPlane= xc.DeformationPlane(shrinkage)
  eleLoad.backEndDeformationPlane= defPlane
  eleLoad.frontEndDeformationPlane= defPlane

#Live load A.
cLC= loadCaseManager.setCurrentLoadCase('liveLoadA')
qk= -4e3
for s in setDeck.getSurfaces:
  label= s.getProp('label')
  if(label=='deck04' or label=='deck06' or label=='deck07'):
    for e in s.elements:
      e.vector3dUniformLoadGlobal(xc.Vector([-0.1*qk,0.0,qk]))
  else:
    for e in s.elements:
      e.vector3dUniformLoadGlobal(xc.Vector([-0.05*qk,0.0,qk/2.0]))
      
#Live load B.
cLC= loadCaseManager.setCurrentLoadCase('liveLoadB')
Qk= -10e3
for s in setDeck.getSurfaces:
  label= s.getProp('label')
  if(label=='deck06'):
    pos= s.getContour().getCenterOfMass()
    n= s.getNearestNode(pos)
    cLC.newNodalLoad(n.tag,xc.Vector([-0.6*Qk,0,Qk,0,0,0]))

#Temperature.
cLC= loadCaseManager.setCurrentLoadCase('temperature')
alphaAT= -20*10e-6
for part in modelSurfaces:
  eleLoad= cLC.newElementalLoad("shell_strain_load")
  eleLoad.elementTags= part.elements.getTags()
  eleLoad.setStrainComp(0,0,alphaAT) #(id of Gauss point, id of component, value)
  eleLoad.setStrainComp(0,1,alphaAT)
  eleLoad.setStrainComp(1,0,alphaAT)
  eleLoad.setStrainComp(1,1,alphaAT)
  eleLoad.setStrainComp(2,0,alphaAT)
  eleLoad.setStrainComp(2,1,alphaAT)
  eleLoad.setStrainComp(3,0,alphaAT)
  eleLoad.setStrainComp(3,1,alphaAT)

for part in modelLines:
  eleLoad= cLC.newElementalLoad("beam_strain_load")
  eleLoad.elementTags= part.elements.getTags()
  defPlane= xc.DeformationPlane(alphaAT)
  eleLoad.backEndDeformationPlane= defPlane
  eleLoad.frontEndDeformationPlane= defPlane

#Snow load.
cLC= loadCaseManager.setCurrentLoadCase('snowLoad')
qkSnow= -0.72e3
for s in setDeck.getSurfaces:
  for e in s.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,qkSnow]))

#Earthquake.
cLC= loadCaseManager.setCurrentLoadCase('earthquake')
for part in modelSurfaces:
  quake= part.quake
  for e in part.elements:
    e.vector3dUniformLoadGlobal(quake)

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
