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


dxfLayerNames= ['roof_01', 'floor_a_middle', 'bulkhead_03', 'middle', 'middle_ramp', 'parapets_01', 'bulkhead_01', 'floor_stairs', 'floor_middle_b', 'side_b', 'side_b_stairs', 'side_a', 'side_a_stairs']

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
#reductionFactor= 1.0 
reductionFactor= 6.0 #Reduction factor
Econcrete= concrete.getEcm()/reductionFactor

#Soil
kS= 30e6 #Module de réaction du sol (estimé).
backFillSoilModel= ep.RankineSoil(phi= math.radians(32),rho= 2000) #Characteristic values.
gSoil= backFillSoilModel.rho*gravity

#Floor.
EcFloor= Econcrete # Concrete's Young modulus.


floor_set= layerSets['floor_a_middle']+layerSets['floor_stairs']+layerSets['floor_middle_b']

floor40_set= layerSets['floor_a_middle']
hFloor40= 0.40 # Floor thickness.
rhoFloor40= hFloor40*dens
shellFloor40= typical_materials.defElasticMembranePlateSection(preprocessor,"shellFloor40",EcFloor,nu,rhoFloor40,hFloor40)
for s in floor40_set.getSurfaces:
    s.setProp('material', shellFloor40)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoFloor40]))

floor30_set= layerSets['floor_stairs']+layerSets['floor_middle_b']
hFloor30= 0.30 # Floor thickness.
rhoFloor30= hFloor30*dens
shellFloor30= typical_materials.defElasticMembranePlateSection(preprocessor,"shellFloor30",EcFloor,nu,rhoFloor30,hFloor30)
for s in floor30_set.getSurfaces:
    s.setProp('material', shellFloor30)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoFloor30]))

floor_centroids= []

for s in floor_set.getSurfaces:
    plg= s.getPolygon()
    area= plg.getArea()
    perimeter= plg.getPerimeter()
    if (area>2 and (area/perimeter)>0.1):
        floor_centroids.append(s.getCentroid())



#Sides.
EcSides= Econcrete # Concrete's Young modulus.

sides_set= layerSets['middle']+layerSets['middle_ramp']+layerSets['side_a']+layerSets['side_b']+layerSets['side_b_stairs']+layerSets['side_a_stairs']

sides40_set= layerSets['side_a']+layerSets['middle']
hSides40= 0.40 # Sides thickness.
rhoSides40= hSides40*dens
shellSides40= typical_materials.defElasticMembranePlateSection(preprocessor,"shellSides40",EcSides,nu,rhoSides40,hSides40)
for s in sides40_set.getSurfaces:
    s.setProp('material', shellSides40)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoSides40]))

sides30_set= layerSets['middle_ramp']+layerSets['side_b']+layerSets['side_b_stairs']+layerSets['side_a_stairs']
hSides30= 0.30 # Sides thickness.
rhoSides30= hSides30*dens
shellSides30= typical_materials.defElasticMembranePlateSection(preprocessor,"shellSides30",EcSides,nu,rhoSides30,hSides30)
for s in sides30_set.getSurfaces:
    s.setProp('material', shellSides30)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoSides30]))

#Bulkheads
EcBulkheads= Econcrete # Concrete's Young modulus.

bulkheads_set= layerSets['bulkhead_01']+layerSets['bulkhead_03']

bulkheads40_set= layerSets['bulkhead_03']
hBulkheads40= 0.40 # Bulkheads thickness.
rhoBulkheads40= hBulkheads40*dens
shellBulkheads40= typical_materials.defElasticMembranePlateSection(preprocessor,"shellBulkheads40",EcBulkheads,nu,rhoBulkheads40,hBulkheads40)
for s in bulkheads_set.getSurfaces:
    s.setProp('material', shellBulkheads40)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoBulkheads40]))

bulkheads30_set= layerSets['bulkhead_01']
hBulkheads30= 0.30 # Bulkheads thickness.
rhoBulkheads30= hBulkheads30*dens
shellBulkheads30= typical_materials.defElasticMembranePlateSection(preprocessor,"shellBulkheads30",EcBulkheads,nu,rhoBulkheads30,hBulkheads30)
for s in bulkheads_set.getSurfaces:
    s.setProp('material', shellBulkheads30)
    s.setProp('selfWeight', xc.Vector([0.0,0.0,-gravity*rhoBulkheads30]))


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
        for e in s.elements:
            shell_elements.elements.append(e)
shell_elements.fillDownwards()
shell_elements.genDescr= 'Model shell elements.'
        
# *** Sets ***

floor_elements= preprocessor.getSets.defSet('floor_elements')
for s in floor_set.getSurfaces:
    for e in s.elements:
        floor_elements.elements.append(e)
floor_elements.fillDownwards()

floor30_elements= preprocessor.getSets.defSet('floor30_elements')
for s in floor30_set.getSurfaces:
    for e in s.elements:
        floor30_elements.elements.append(e)
floor30_elements.fillDownwards()

floor40_elements= preprocessor.getSets.defSet('floor40_elements')
for s in floor40_set.getSurfaces:
    for e in s.elements:
        floor40_elements.elements.append(e)
floor40_elements.fillDownwards()

roof_elements= preprocessor.getSets.defSet('roof_elements')
for s in roof_set.getSurfaces:
    for e in s.elements:
        roof_elements.elements.append(e)
roof_elements.fillDownwards()
roof_centroids= []
roof_bnd= roof_elements.nodes.getBnd(0.0)
roof_center= roof_bnd.getCenterOfMass()
roof_centroids.append(roof_center+geom.Vector3d(-0.9,0,0))
roof_centroids.append(roof_center+geom.Vector3d(+0.9,0,0))


sides_elements= preprocessor.getSets.defSet('sides_elements')
for s in sides_set.getSurfaces:
    for e in s.elements:
        sides_elements.elements.append(e)
sides_elements.fillDownwards()

sides30_elements= preprocessor.getSets.defSet('sides30_elements')
for s in sides30_set.getSurfaces:
    for e in s.elements:
        sides30_elements.elements.append(e)
sides30_elements.fillDownwards()

sides40_elements= preprocessor.getSets.defSet('sides40_elements')
for s in sides40_set.getSurfaces:
    for e in s.elements:
        sides40_elements.elements.append(e)
sides40_elements.fillDownwards()

bulkheads_elements= preprocessor.getSets.defSet('bulkheads_elements')
for s in bulkheads_set.getSurfaces:
    for e in s.elements:
        bulkheads_elements.elements.append(e)
bulkheads_elements.fillDownwards()


bulkheads30_elements= preprocessor.getSets.defSet('bulkheads30_elements')
for s in bulkheads_set.getSurfaces:
    for e in s.elements:
        bulkheads30_elements.elements.append(e)
bulkheads30_elements.fillDownwards()

bulkheads40_elements= preprocessor.getSets.defSet('bulkheads40_elements')
for s in bulkheads_set.getSurfaces:
    for e in s.elements:
        bulkheads40_elements.elements.append(e)
bulkheads40_elements.fillDownwards()

lateral_elements= sides_elements+bulkheads_elements
lateral40_elements= sides40_elements+bulkheads40_elements
lateral30_elements= lateral_elements-lateral40_elements

side_a_set= layerSets['side_a']
side_a_elements= preprocessor.getSets.defSet('side_a_elements')
for s in side_a_set.getSurfaces:
    for e in s.elements:
        side_a_elements.elements.append(e)
side_a_elements.fillDownwards()

side_b_set= layerSets['side_b']
side_b_elements= preprocessor.getSets.defSet('side_b_elements')
for s in side_b_set.getSurfaces:
    for e in s.elements:
        side_b_elements.elements.append(e)
side_b_elements.fillDownwards()

# *** Constraints ***

#Underpass frame.
underpassFrame= [geom.Pos3d(24.4821,7.075,8.4793),geom.Pos3d(30.2246,7.075,8.4793),geom.Pos3d(30.2246,7.075,5.3593),geom.Pos3d(24.4821,7.075,5.3593)]

frameBC= sprbc.SpringBC('frameBC',modelSpace,Ky= 1e8)
segments= [(0,1), (1,2), (2,3), (3,0)]
frame_nodes= []
for s in segments:
    sI= geom.Segment3d(underpassFrame[s[0]],underpassFrame[s[1]])
    for n in shell_elements.nodes:
        pos= n.getInitialPos3d
        dist= sI.distPos3d(pos)
        if dist<0.1:
            frame_nodes.append(n)
frameBC.applyOnNodesLst(frame_nodes)

#Foundation.
foundation= sprbc.ElasticFoundation(wModulus=kS,cRoz=0.002)
foundation.generateSprings(xcSet=floor_elements)


# *** Loads ***
loadManager= preprocessor.getLoadHandler
loadCases= loadManager.getLoadPatterns
#Load modulation.
ts= loadCases.newTimeSeries("constant_ts","ts")
loadCases.currentTimeSeries= "ts"

#Load case definition
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['selfWeight','deadLoad','passengers_shelter','earthPressure', 'pedestrianLoad', 'singleAxeLoad', 'LM1', 'DLM1', 'nosingLoad', 'roadTrafficLoad', 'earthquake']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

#Self weight.
cLC= loadCaseManager.setCurrentLoadCase('selfWeight')
for key in layerSets:
    layerSet= layerSets[key]
    for s in layerSet.getSurfaces:
        weight= s.getProp('selfWeight')
        for e in s.elements:
            e.vector3dUniformLoadGlobal(weight)

#Dead load: pavement.
cLC= loadCaseManager.setCurrentLoadCase('deadLoad')
deadLoadVector=xc.Vector([0.0,0.0,-0.11*24e3]) #Pavement load.
for s in floor_set.getSurfaces:
    for e in s.elements:
        e.vector3dUniformLoadGlobal(deadLoadVector)
for s in roof_set.getSurfaces:
    for e in s.elements:
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
    for n in roof_elements.nodes:
        pos= n.getInitialPos3d
        dist= sI.distPos3d(pos)
        if dist<0.21:
            sI_nodes.append(n)
    node_load= -4e3*sI.getLength()/len(sI_nodes)
    for n in sI_nodes:
        cLC.newNodalLoad(n.tag,xc.Vector([0.0,0.0,node_load,0,0,0]))

#Dead load: earth pressure.
cLC= loadCaseManager.setCurrentLoadCase('earthPressure')
K0= backFillSoilModel.K0Jaky()
zGroundBackFill= 10.23 #Back fill
backFillPressureModel=  earth_pressure.EarthPressureModel( zGround= zGroundBackFill, zBottomSoils=[-10], KSoils= [K0], gammaSoils= [gSoil], zWater= -1e3, gammaWater= 1000*gravity)

modelCentroid= lateral_elements.nodes.getCentroid(0.0)
for e in lateral_elements.elements:
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
    

#Live load: pedestrian loads.
cLC= loadCaseManager.setCurrentLoadCase('pedestrianLoad')

uniformLoad= xc.Vector([0.0,0.0,-5.0e3])
# poly_shelter_load_perimeter=geom.Polygon2d()
# for p in passengerShelterCorners:
#     poly_shelter_load_perimeter.appendVertex(geom.Pos2d(p.x,p.y))
# shelter_elements= sets.set_included_in_orthoPrism(preprocessor,setInit=roof_elements,prismBase= poly_shelter_load_perimeter,prismAxis='Z',setName='shelter_elements')
for e in roof_elements.elements:
    e.vector3dUniformLoadGlobal(uniformLoad) #SIA 261:2014 table 8
for s in floor_set.getSurfaces:
    for e in s.elements:
        e.vector3dUniformLoadGlobal(uniformLoad)
pedestrianLoadOnPlatform= earth_pressure.LineVerticalLoadOnBackfill(qLoad= 25e3,zLoad= 10.23, distWall= 2.45/2.0)
for e in side_a_elements.elements:
    elemCentroid= e.getPosCentroid(True)
    localKVector= e.getCoordTransf.getG3Vector
    pressure= pedestrianLoadOnPlatform.getPressure(elemCentroid.z)*localKVector
    e.vector3dUniformLoadGlobal(pressure) #SIA 261:2014 table 8

cLC= loadCaseManager.setCurrentLoadCase('singleAxeLoad')
for p in floor_centroids:
    n= floor_elements.getNearestNode(p)
    cLC.newNodalLoad(n.tag,xc.Vector([0.0,0.0,-45e3,0,0,0]))
for p in roof_centroids:
    n= roof_elements.getNearestNode(p)
    cLC.newNodalLoad(n.tag,xc.Vector([0.0,0.0,-45e3,0,0,0]))

#Live load: road traffic load.
cLC= loadCaseManager.setCurrentLoadCase('roadTrafficLoad')
roadTrafficLoadEarthPressure= earth_pressure.UniformLoadOnBackfill(K= K0,qLoad= 11.02e3)
for e in side_b_elements.elements:
    elemCentroid= e.getPosCentroid(True)
    localKVector= e.getCoordTransf.getG3Vector
    pressure= -roadTrafficLoadEarthPressure.getPressure(elemCentroid.z)*localKVector
    e.vector3dUniformLoadGlobal(pressure) #SIA 261:2014 table 8


#Live load: rail traffic load.

railLoad= loadCaseManager.setCurrentLoadCase('LM1')
distRailCLWall= 4.5 #Distance from the center line of the rail track to the wall
railLoadEarthPressure= earth_pressure.StripLoadOnBackfill(qLoad= 50e3,zLoad= 10.23-0.7, distWall= distRailCLWall, stripWidth= 3.0)

for e in side_a_elements.elements:
    elemCentroid= e.getPosCentroid(True)
    localKVector= e.getCoordTransf.getG3Vector
    pressure= railLoadEarthPressure.getPressure(elemCentroid.z)*localKVector
    e.vector3dUniformLoadGlobal(pressure) #SIA 261:2014 table 8

derailmentLoad= loadCaseManager.setCurrentLoadCase('DLM1')
derailmentLoadStripWidth= 0.45
platformWidth= 2.5
distDerailmentLoadWall= platformWidth+derailmentLoadStripWidth/2.0 #Distance from the center line of the derailment load to the wall
derailmentLoadEarthPressure= earth_pressure.StripLoadOnBackfill(qLoad= 145e3/derailmentLoadStripWidth,zLoad= 10.23-0.4, distWall= distDerailmentLoadWall, stripWidth= derailmentLoadStripWidth)

for e in side_a_elements.elements:
    elemCentroid= e.getPosCentroid(True)
    if(elemCentroid.x>24.5 and elemCentroid.x<44.5):
        localKVector= e.getCoordTransf.getG3Vector
        pressure= derailmentLoadEarthPressure.getPressure(elemCentroid.z)*localKVector
        e.vector3dUniformLoadGlobal(pressure)

#Nosing load
railLoad= loadCaseManager.setCurrentLoadCase('nosingLoad')
fNosingLoad= 100e3
nosingLoadLength= 3*0.6+(distRailCLWall-1.435/2.0)
nosingLoadSurface= nosingLoadLength*3.0
qNosingLoad= fNosingLoad/nosingLoadSurface
horizontalLoad= earth_pressure.HorizontalLoadOnBackfill(backFillSoilModel.phi,qLoad= qNosingLoad,zLoad= 10.23-0.7, distWall= distRailCLWall, widthLoadArea= 2.0)
horizontalLoad.setup()
centerNosingLoad= side_a_elements.nodes.getCentroid(0.0)
xMinNosingLoad= centerNosingLoad.x-nosingLoadLength/2.0
xMaxNosingLoad= centerNosingLoad.x+nosingLoadLength/2.0
for e in side_a_elements.elements:
    elemCentroid= e.getPosCentroid(True)
    if(elemCentroid.x>xMinNosingLoad and elemCentroid.x<=xMaxNosingLoad):
        localKVector= e.getCoordTransf.getG3Vector
        pressure= horizontalLoad.getPressure(elemCentroid.z)
        e.vector3dUniformLoadGlobal(pressure*localKVector) #SIA 261:2014 table 8

#Accidental actions. Earthquake
quakeLoad= loadCaseManager.setCurrentLoadCase('earthquake')
xLimit= 24.5
structureHeightA= zGroundBackFill-8.5518 #m height of the structure zone A.
structureHeightB= zGroundBackFill-5.3593 #m height of the structure zone B.
# kh: seismic coefficient of horizontal acceleration.
# kv: seismic coefficient of vertical acceleration.
# psi: back face inclination of the structure (<= PI/2)
# delta_ad angle of friction soil - structure.
# beta slope inclination of backfill.
# Kas: static earth pressure coefficient 
mononobeOkabeA= earth_pressure.MononobeOkabePressureDistribution(zGround= zGroundBackFill, gamma_soil= gSoil, H= structureHeightA, kv= 0.11/2.0, kh= 0.11, psi= math.radians(90), phi= backFillSoilModel.phi, delta_ad= 0.0, beta= 0.0, Kas= K0)
mononobeOkabeB= earth_pressure.MononobeOkabePressureDistribution(zGround= zGroundBackFill, gamma_soil= gSoil, H= structureHeightB, kv= 0.11/2.0, kh= 0.11, psi= math.radians(90), phi= backFillSoilModel.phi, delta_ad= 0.0, beta= 0.0, Kas= K0)

for e in lateral_elements.elements:
    elemCentroid= e.getPosCentroid(True)
    v= elemCentroid-modelCentroid
    localKVector= e.getCoordTransf.getG3Vector
    sign= v.dot(geom.Vector3d(localKVector[0],localKVector[1],localKVector[2]))
    if sign<0:
        sign= -1
    else:
        sign= 1
    pressure= 0.0
    if(elemCentroid.x<xLimit):
      pressure= sign*mononobeOkabeA.getPressure(elemCentroid.z)*localKVector
    else:
      pressure= sign*mononobeOkabeB.getPressure(elemCentroid.z)*localKVector
    e.vector3dUniformLoadGlobal(pressure) 

#Load combinations
combContainer= combs.CombContainer()

#Quasi-permanent situations.
combContainer.SLS.qp.add('SLSQP_1','1.00*selfWeight + 1.00*deadLoad + 0.70*earthPressure + 0.50*pedestrianLoad + 0.30*singleAxeLoad')
combContainer.SLS.qp.add('SLSQP_2','1.00*selfWeight + 1.00*deadLoad + 0.70*earthPressure + 0.30*pedestrianLoad + 0.50*singleAxeLoad')

#Frequent
combContainer.SLS.freq.add('SLSF_1','1.00*selfWeight + 1.00*deadLoad + 0.70*earthPressure + 0.70*pedestrianLoad + 0.50*singleAxeLoad')
combContainer.SLS.freq.add('SLSF_2','1.00*selfWeight + 1.00*deadLoad + 0.70*earthPressure + 0.50*pedestrianLoad + 0.70*singleAxeLoad')
combContainer.SLS.freq.add('SLSF_3','1.00*selfWeight + 1.00*deadLoad + 1.00*earthPressure + 0.75 * roadTrafficLoad')
combContainer.SLS.freq.add('SLSF_4','1.00*selfWeight + 1.00*deadLoad + 1.00*earthPressure + 1.00*LM1 + 1.00*nosingLoad + 0.75 * roadTrafficLoad')
combContainer.SLS.freq.add('SLSF_5','1.00*selfWeight + 1.00*deadLoad + 1.00*earthPressure + 1.00*LM1 + 1.00*nosingLoad + 0.3 * pedestrianLoad')

#Rare
combContainer.SLS.rare.add('SLSR_1','1.00*selfWeight + 1.00*deadLoad + 0.70*earthPressure + 1.00*pedestrianLoad')
combContainer.SLS.rare.add('SLSR_2','1.00*selfWeight + 1.00*deadLoad + 0.70*earthPressure + 1.00*pedestrianLoad + 0.70*singleAxeLoad')
combContainer.SLS.rare.add('SLSR_3','1.00*selfWeight + 1.00*deadLoad + 0.70*earthPressure + 1.00*singleAxeLoad')
combContainer.SLS.rare.add('SLSR_4','1.00*selfWeight + 1.00*deadLoad + 0.70*earthPressure + 0.70*pedestrianLoad + 1.00*singleAxeLoad')
combContainer.SLS.rare.add('SLSR_5','1.00*selfWeight + 1.00*deadLoad + 1.00*earthPressure + 1.00*LM1 + 1.00*nosingLoad')
combContainer.SLS.rare.add('SLSR_6','1.00*selfWeight + 1.00*deadLoad + 1.00*earthPressure + 1.00*roadTrafficLoad')

#Permanent and transitory situations.
combContainer.ULS.perm.add('ULS_01','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.50*pedestrianLoad + 1.05*singleAxeLoad')
combContainer.ULS.perm.add('ULS_02','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.05*pedestrianLoad + 1.50*singleAxeLoad')
combContainer.ULS.perm.add('ULS_03','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.50*LM1 + 1.50*nosingLoad')
combContainer.ULS.perm.add('ULS_04','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.05*singleAxeLoad + 1.50*LM1 + 1.50*nosingLoad')
combContainer.ULS.perm.add('ULS_05','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.05*pedestrianLoad + 1.50*LM1 + 1.50*nosingLoad')
combContainer.ULS.perm.add('ULS_06','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.05*pedestrianLoad + 1.05*singleAxeLoad + 1.50*LM1 + 1.50*nosingLoad')
combContainer.ULS.perm.add('ULS_07','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.5*roadTrafficLoad')
combContainer.ULS.perm.add('ULS_08','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.05*singleAxeLoad + 1.5*roadTrafficLoad')
combContainer.ULS.perm.add('ULS_09','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.05*pedestrianLoad + 1.5*roadTrafficLoad')
combContainer.ULS.perm.add('ULS_10','1.35*selfWeight + 1.35*deadLoad + 0.70*earthPressure + 1.05*pedestrianLoad + 1.05*singleAxeLoad + 1.5*roadTrafficLoad')
combContainer.ULS.perm.add('ULS_11','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.50*pedestrianLoad + 1.05*singleAxeLoad')
combContainer.ULS.perm.add('ULS_12','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.05*pedestrianLoad + 1.50*singleAxeLoad')
combContainer.ULS.perm.add('ULS_13','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.50*LM1 + 1.50*nosingLoad')
combContainer.ULS.perm.add('ULS_14','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.05*singleAxeLoad + 1.50*LM1 + 1.50*nosingLoad')
combContainer.ULS.perm.add('ULS_15','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.05*pedestrianLoad + 1.50*LM1 + 1.50*nosingLoad')
combContainer.ULS.perm.add('ULS_16','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.05*pedestrianLoad + 1.05*singleAxeLoad + 1.50*LM1 + 1.50*nosingLoad')
combContainer.ULS.perm.add('ULS_17','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.5*roadTrafficLoad')
combContainer.ULS.perm.add('ULS_18','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.05*singleAxeLoad + 1.5*roadTrafficLoad')
combContainer.ULS.perm.add('ULS_19','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.05*pedestrianLoad + 1.5*roadTrafficLoad')
combContainer.ULS.perm.add('ULS_20','1.35*selfWeight + 1.35*deadLoad + 1.35*earthPressure + 1.05*pedestrianLoad + 1.05*singleAxeLoad + 1.5*roadTrafficLoad')

#Accidental
combContainer.ULS.perm.add('ULSA_1','1.00*selfWeight + 1.00*deadLoad + 1.00*earthPressure + 1.00*earthquake')
combContainer.ULS.perm.add('ULSA_2','1.00*selfWeight + 1.00*deadLoad + 1.00*earthPressure + 1.00*DLM1')

