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

from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets

#Parts definition
import re

#Mesh definition
from model import predefined_spaces

#Loads
from actions import load_cases as lcm
from actions import combinations as combs

#Solution
from solution import predefined_solutions


tourRamps= xc.FEProblem()
execfile('./xc_model_blocks.py')
xcTotalSet= preprocessor.getSets.getSet('total')
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)


dxfLayerNames= ['roof_01', 'floor_a_middle', 'bulkhead_03', 'middle', 'parapets_01', 'bulkhead_01', 'floor_stairs', 'floor_middle_b', 'side_b', 'side_b_stairs', 'side_a', 'side_a_stairs']

layerSets= {}
for layerName in dxfLayerNames:
    layerSets[layerName]= preprocessor.getSets.defSet(layerName)

for s in xcTotalSet.getSurfaces:
    layerName= s.getProp('labels')[0]
    layerSet= layerSets[layerName]
    layerSet.getSurfaces.append(s)
    s.setElemSizeIJ(0.5,0.45)

for key in layerSets:
    layerSet= layerSets[key]
    layerSets[key].fillDownwards()

preprocessor.getMultiBlockTopology.getSurfaces.conciliaNDivs()
    
# *** Materials *** 
concrete= SIA262_materials.c30_37
nu= 0.3 # Poisson coefficient.
dens= 2500 # Density kg/m3.
reductionFactor= 1.0 
#reductionFactor= 7.0 #Reduction factor
Econcrete= concrete.getEcm()/reductionFactor

#Floor.
EcFloor= Econcrete # Concrete's Young modulus.
hFloor= 0.30 # Floor thickness.
rhoFloor= hFloor*dens

shellFloor= typical_materials.defElasticMembranePlateSection(preprocessor,"shellFloor",EcFloor,nu,rhoFloor,hFloor)

floor_set= layerSets['floor_a_middle']+layerSets['floor_a_middle']+layerSets['floor_stairs']+layerSets['floor_middle_b']

for s in floor_set.getSurfaces:
    s.setProp('material', shellFloor)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-9.81*rhoFloor]))

#Sides.
EcSides= Econcrete # Concrete's Young modulus.
hSides= 0.30 # Sides thickness.
rhoSides= hSides*dens

shellSides= typical_materials.defElasticMembranePlateSection(preprocessor,"shellSides",EcSides,nu,rhoSides,hSides)

sides_set= layerSets['middle']+layerSets['side_a']+layerSets['side_b']+layerSets['side_b_stairs']+layerSets['side_a_stairs']

for s in sides_set.getSurfaces:
    s.setProp('material', shellSides)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-9.81*rhoSides]))

#Bulkheads
EcBulkheads= Econcrete # Concrete's Young modulus.
hBulkheads= 0.30 # Bulkheads thickness.
rhoBulkheads= hBulkheads*dens

shellBulkheads= typical_materials.defElasticMembranePlateSection(preprocessor,"shellBulkheads",EcBulkheads,nu,rhoBulkheads,hBulkheads)

bulkheads_set= layerSets['bulkhead_01']+layerSets['bulkhead_03']

for s in bulkheads_set.getSurfaces:
    s.setProp('material', shellBulkheads)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-9.81*rhoBulkheads]))

#Parapets
EcParapets= Econcrete # Concrete's Young modulus.
hParapets= 0.25 # Parapets thickness.
rhoParapets= hParapets*dens

shellParapets= typical_materials.defElasticMembranePlateSection(preprocessor,"shellParapets",EcParapets,nu,rhoParapets,hParapets)

parapets_set= layerSets['parapets_01']

for s in parapets_set.getSurfaces:
    s.setProp('material', shellParapets)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-9.81*rhoParapets]))


#Roof.
EcRoof= Econcrete # Concrete's Young modulus.
hRoof= 0.40 # Roof thickness.
rhoRoof= hRoof*dens

shellRoof= typical_materials.defElasticMembranePlateSection(preprocessor,"shellRoof",EcRoof,nu,rhoRoof,hRoof)

roof_set= layerSets['roof_01']

for s in roof_set.getSurfaces:
    s.setProp('material', shellRoof)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-9.81*rhoRoof]))

# *** Meshing ***
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "shellRoof"
elem= seedElemHandler.newElement("ShellMITC4",xc.ID([0,0,0,0]))

for key in layerSets:
    layerSet= layerSets[key]
    for s in layerSet.getSurfaces:
        seedElemHandler.defaultMaterial= s.getProp('material').name
        s.genMesh(xc.meshDir.I)

shell_elements= preprocessor.getSets.defSet('shell_elements')
for key in layerSets:
    layerSet= layerSets[key]
    for s in layerSet.getSurfaces:
        for e in s.getElements():
            shell_elements.getElements.append(e)
shell_elements.fillDownwards()
        
print 'number of nodes= ', len(xcTotalSet.getNodes)

# *** Constraints ***
wModulus= 3e7 #[N/m3]

floor_elements= preprocessor.getSets.defSet('floor_elements')
for s in floor_set.getSurfaces:
    for e in s.getElements():
        floor_elements.getElements.append(e)
floor_elements.fillDownwards()

foundation= sprbc.ElasticFoundation(wModulus=wModulus,cRoz=0.002)
foundation.generateSprings(xcSet=floor_elements)


print 'number of nodes= ', len(xcTotalSet.getNodes)

# *** Loads ***
loadManager= preprocessor.getLoadHandler
loadCases= loadManager.getLoadPatterns
#Load modulation.
ts= loadCases.newTimeSeries("constant_ts","ts")
loadCases.currentTimeSeries= "ts"

#Load case definition
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['selfWeight','deadLoad','passengers_shelter','earth_pressure', 'liveLoadA', 'liveLoadB', 'railway','snow','earthquake']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

#Self weight.
cLC= loadCaseManager.setCurrentLoadCase('selfWeight')
for key in layerSets:
    layerSet= layerSets[key]
    for s in layerSet.getSurfaces:
        weight= s.getProp('selfWeight')
        for e in s.getElements():
            e.vector3dUniformLoadGlobal(weight)

#Dead load: pavement.
cLC= loadCaseManager.setCurrentLoadCase('deadLoad')
deadLoadVector=xc.Vector([0.0,0.0,-0.11*24e3]) #Pavement load.
for s in floor_set.getSurfaces:
    for e in s.getElements():
        e.vector3dUniformLoadGlobal(deadLoadVector)
for s in roof_set.getSurfaces:
    for e in s.getElements():
        e.vector3dUniformLoadGlobal(deadLoadVector)

#Dead load:


#Live load: passenger shelter load perimeter.
cLC= loadCaseManager.setCurrentLoadCase('liveLoadA')
passengerShelterCorners= [geom.Pos3d(46.5900,11.6750,10.2360),geom.Pos3d(46.5900, 9.3250, 10.2360), geom.Pos3d(41.8400, 9.3250, 10.2360), geom.Pos3d(41.8400, 11.6750, 10.2360)]

roof_elements= preprocessor.getSets.defSet('roof_elements')
for s in roof_set.getSurfaces:
    for e in s.getElements():
        roof_elements.getElements.append(e)

poly_shelter_load_perimeter=geom.Polygon2d()
for p in passengerShelterCorners:
    poly_shelter_load_perimeter.agregaVertice(geom.Pos2d(p.x,p.y))
shelter_elements= sets.set_included_in_orthoPrism(preprocessor,setInit=roof_elements,prismBase= poly_shelter_load_perimeter,prismAxis='Z',setName='shelter_elements')
for e in shelter_elements.getElements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,5.0e3])) #SIA 261:2014 table 8

