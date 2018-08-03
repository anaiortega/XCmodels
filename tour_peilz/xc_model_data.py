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
from geotechnics import earth_pressure as ep
from actions.earth_pressure import earth_pressure

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

gravity=9.81 #Aceleración de la gravedad (m/s2)

# *** Materials *** 
concrete= SIA262_materials.c30_37
nu= 0.3 # Poisson coefficient.
dens= 2500 # Density kg/m3.
reductionFactor= 1.0 
#reductionFactor= 7.0 #Reduction factor
Econcrete= concrete.getEcm()/reductionFactor

#Soil
kS= 30e6 #Module de réaction du sol (estimé).
backFillSoilModel= ep.RankineSoil(phi= math.radians(32),rho= 2000) #Characteristic values.
gSoil= backFillSoilModel.rho*gravity

#Floor.
EcFloor= Econcrete # Concrete's Young modulus.
hFloor= 0.30 # Floor thickness.
rhoFloor= hFloor*dens

shellFloor= typical_materials.defElasticMembranePlateSection(preprocessor,"shellFloor",EcFloor,nu,rhoFloor,hFloor)

floor_set= layerSets['floor_a_middle']+layerSets['floor_a_middle']+layerSets['floor_stairs']+layerSets['floor_middle_b']

for s in floor_set.getSurfaces:
    s.setProp('material', shellFloor)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoFloor]))

#Sides.
EcSides= Econcrete # Concrete's Young modulus.
hSides= 0.30 # Sides thickness.
rhoSides= hSides*dens

shellSides= typical_materials.defElasticMembranePlateSection(preprocessor,"shellSides",EcSides,nu,rhoSides,hSides)

sides_set= layerSets['middle']+layerSets['side_a']+layerSets['side_b']+layerSets['side_b_stairs']+layerSets['side_a_stairs']

for s in sides_set.getSurfaces:
    s.setProp('material', shellSides)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoSides]))

#Bulkheads
EcBulkheads= Econcrete # Concrete's Young modulus.
hBulkheads= 0.30 # Bulkheads thickness.
rhoBulkheads= hBulkheads*dens

shellBulkheads= typical_materials.defElasticMembranePlateSection(preprocessor,"shellBulkheads",EcBulkheads,nu,rhoBulkheads,hBulkheads)

bulkheads_set= layerSets['bulkhead_01']+layerSets['bulkhead_03']

for s in bulkheads_set.getSurfaces:
    s.setProp('material', shellBulkheads)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoBulkheads]))

#Parapets
EcParapets= Econcrete # Concrete's Young modulus.
hParapets= 0.25 # Parapets thickness.
rhoParapets= hParapets*dens

shellParapets= typical_materials.defElasticMembranePlateSection(preprocessor,"shellParapets",EcParapets,nu,rhoParapets,hParapets)

parapets_set= layerSets['parapets_01']

for s in parapets_set.getSurfaces:
    s.setProp('material', shellParapets)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoParapets]))


#Roof.
EcRoof= Econcrete # Concrete's Young modulus.
hRoof= 0.40 # Roof thickness.
rhoRoof= hRoof*dens

shellRoof= typical_materials.defElasticMembranePlateSection(preprocessor,"shellRoof",EcRoof,nu,rhoRoof,hRoof)

roof_set= layerSets['roof_01']

for s in roof_set.getSurfaces:
    s.setProp('material', shellRoof)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoRoof]))

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
shell_elements.genDescr= 'Model shell elements.'
        
print 'number of nodes= ', len(xcTotalSet.getNodes)

# *** Sets ***

floor_elements= preprocessor.getSets.defSet('floor_elements')
for s in floor_set.getSurfaces:
    for e in s.getElements():
        floor_elements.getElements.append(e)
floor_elements.fillDownwards()

roof_elements= preprocessor.getSets.defSet('roof_elements')
for s in roof_set.getSurfaces:
    for e in s.getElements():
        roof_elements.getElements.append(e)
roof_elements.fillDownwards()

sides_elements= preprocessor.getSets.defSet('sides_elements')
for s in sides_set.getSurfaces:
    for e in s.getElements():
        sides_elements.getElements.append(e)
sides_elements.fillDownwards()

bulkheads_elements= preprocessor.getSets.defSet('bulkheads_elements')
for s in bulkheads_set.getSurfaces:
    for e in s.getElements():
        bulkheads_elements.getElements.append(e)
bulkheads_elements.fillDownwards()

lateral_elements= sides_elements+bulkheads_elements

# *** Constraints ***
foundation= sprbc.ElasticFoundation(wModulus=kS,cRoz=0.002)
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
loadCaseNames= ['selfWeight','deadLoad','passengers_shelter','earthPressure', 'liveLoadA', 'liveLoadB', 'railway','snow','earthquake']
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

#Dead load: passenger shelter dead load.
passengerShelterCorners= [geom.Pos3d(46.5900,11.6750,10.2360),geom.Pos3d(46.5900, 9.3250, 10.2360), geom.Pos3d(41.8400, 9.3250, 10.2360), geom.Pos3d(41.8400, 11.6750, 10.2360)]

for p in passengerShelterCorners:
    n= roof_elements.getNearestNode(p)
    cLC.newNodalLoad(n.tag,xc.Vector([0.0,0.0,-6.65e3,0,0,0]))

#Dead load on the shelter perimeter.
segments= [(0,1), (1,2), (2,3), (3,0)]
for s in segments:
    sI= geom.Segment3d(passengerShelterCorners[s[0]],passengerShelterCorners[s[1]])
    sI_nodes= []
    for n in roof_elements.getNodes:
        pos= n.getInitialPos3d
        dist= sI.distPto(pos)
        if dist<0.21:
            sI_nodes.append(n)
    node_load= -4e3*sI.getLength()/len(sI_nodes)
    for n in sI_nodes:
        cLC.newNodalLoad(n.tag,xc.Vector([0.0,0.0,node_load,0,0,0]))

#Dead load: earth pressure.
cLC= loadCaseManager.setCurrentLoadCase('earthPressure')
K0= backFillSoilModel.K0Jaky()
zGroundBackFill= 10.23 #Back fill
backFillPressureModel=  earth_pressure.EarthPressureModel(K= K0, zGround= zGroundBackFill, gammaSoil= gSoil, zWater= -1e3, gammaWater= 1000*gravity)

modelCentroid= lateral_elements.getNodes.getCentroid(0.0)
for e in lateral_elements.getElements:
    elemCentroid= e.getPosCentroid(True)
    v= elemCentroid-modelCentroid
    localKVector= e.getCoordTransf.getG3Vector
    sign= v.dot(geom.Vector3d(localKVector[0],localKVector[1],localKVector[2]))
    if sign<0:
        sign= -1
    else:
        sign= 1
    pressure= -sign*backFillPressureModel.getPressure(elemCentroid.z)*localKVector
    e.vector3dUniformLoadGlobal(pressure) #SIA 261:2014 table 8
    

#Live load: passenger shelter load perimeter.
cLC= loadCaseManager.setCurrentLoadCase('liveLoadA')


poly_shelter_load_perimeter=geom.Polygon2d()
for p in passengerShelterCorners:
    poly_shelter_load_perimeter.agregaVertice(geom.Pos2d(p.x,p.y))
shelter_elements= sets.set_included_in_orthoPrism(preprocessor,setInit=roof_elements,prismBase= poly_shelter_load_perimeter,prismAxis='Z',setName='shelter_elements')
for e in shelter_elements.getElements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,5.0e3])) #SIA 261:2014 table 8

