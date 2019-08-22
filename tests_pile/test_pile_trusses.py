# -*- coding: utf-8 -*-
from __future__ import division

import xc_base
import geom
import xc
from model import predefined_spaces
from model.boundary_cond import spring_bound_cond as sbc
from solution import predefined_solutions
from materials import typical_materials

#Data
fiPile=1  #pile diameter [m]
Emat=24e6    #elastic modulus of pile material [Pa]
bearCap=22e3 #total bearing capacity of the pile [N]
pType='endBearing' #type of pile
zGround=0  #ground elevation
soils=[(-1.5,'sandy',1e6),(-5,'sandy',2e6),(-15,'sandy',10e6),(-100,'sandy',15e6)] #Properties of the sandy
# soils [(zBottom,type, nh), ...]  where 'zBottom' is the global Z coordinate
#           of the bottom level of the soil and 'nh' [Pa/m] is the coefficient 
#           corresponding to the compactness of the sandy soil.

feProblem= xc.FEProblem()
preprocessor=  feProblem.getPreprocessor
nodes= preprocessor.getNodeHandler
elems=preprocessor.getElementHandler

# Problem type
modelSpace= predefined_spaces.SolidMechanics3D(nodes)

nodes.defaultTag= 1 #First node number.
setPile=preprocessor.getSets.defSet('setPile')
for z in range(-20,3):
    n=nodes.newNodeXYZ(0,0.0,z)
    setPile.getNodes.append(n)
for z in range(-20,-15):
    nodes.newNodeXYZ(0,0.0,z)
    setPile.getNodes.append(n)
for z in range(-15,0):
    nodes.newNodeXYZ(0,0.0,z)
    setPile.getNodes.append(n)

#Trusses: elementos 0 a 21
elast= typical_materials.defElasticMaterial(preprocessor, "elast",Emat)
elements= preprocessor.getElementHandler
elements.dimElem= 3 #Bars defined ina a 3 dimensional space.
elements.defaultMaterial= "elast"
for i in range(1,23):
    truss=elements.newElement("Truss",xc.ID([i,i+1]))
    truss.area= 1
    setPile.getElements.append(truss)

pile=sbc.PileFoundation(setPile=setPile,pileDiam=fiPile,E=Emat,pileType='endBearing',pileBearingCapacity=bearCap,groundLevel=zGround,soilsProp=soils)
pile.generateSpringsPile(alphaKh_x=1,alphaKh_y=0.5,alphaKv_z=1)

for i in range(22,43):
    e=elems.getElement(i)
    print 'elem:', e.tag, ' z:',e.getCooCentroid(True)[0]
    mats=e.getMaterials()
    matx=mats[0]
    maty=mats[1]
    matz=mats[2]
    print 'Ex:',matx.E,' Ey:',maty.E, ' Ez:',matz.E
    
'''
constraints= preprocessor.getBoundaryCondHandler
for i in range(20,24):
    modelSpace.fixNode('000',i)
for i in range(2,20):
    modelSpace.fixNode('FF0',i)
#modelSpace.fixNode('FFF',1)

'''
'''
#Element 0 (vertical stiffness at end of pile elevation -20)
e0=elems.getElement(0)

#Elements 1 to 20 (horizontal stiffness at elevations 0 to -20)
e1=elems.getElement(1)
e2=elems.getElement(2)
e3=elems.getElement(3)
e4=elems.getElement(4)
e5=elems.getElement(5)
e6=elems.getElement(6)
e7=elems.getElement(7)
e8=elems.getElement(8)
e9=elems.getElement(9)
e10=elems.getElement(10)
e11=elems.getElement(11)
e12=elems.getElement(12)
e13=elems.getElement(13)
e44=elems.getElement(14)
e15=elems.getElement(15)
e16=elems.getElement(16)
e17=elems.getElement(17)
e18=elems.getElement(18)
e19=elems.getElement(19)
e20=elems.getElement(20)
'''
# Loads definition
loadHandler= preprocessor.getLoadHandler
lPatterns= loadHandler.getLoadPatterns
#Load modulation.
ts= lPatterns.newTimeSeries("constant_ts","ts")
lPatterns.currentTimeSeries= "ts"
#Load case definition
lp0= lPatterns.newLoadPattern("default","0")
for i in range(1,20):
    lp0.newNodalLoad(i,xc.Vector([1,1,0]))
lp0.newNodalLoad(1,xc.Vector([0,0,-1]))
#We add the load case to domain.
lPatterns.addToDomain(lp0.name)

# Solution
analisis= predefined_solutions.simple_static_linear(feProblem)
result= analisis.analyze(1)

nodes.calculateNodalReactions(True,1e-7)
