# -*- coding: utf-8 -*-
from __future__ import division

import math
import xc_base
import geom
import xc
from model import predefined_spaces
from model.geometry import grid_model as gm
from model.mesh import finit_el_model as fem
from materials.ehe import EHE_materials
from materials import typical_materials as tm
from model.boundary_cond import spring_bound_cond as sbc
from solution import predefined_solutions

#Data
fiPile=1  #pile diameter [m]
Emat=24e6    #elastic modulus of pile material [Pa]
bearCap=22e3 #total bearing capacity of the pile [N]
pType='endBearing' #type of pile
zGround=0  #ground elevation
zGround=2  #ground elevation
soils=[(-1.5,'sandy',1e6),(-5,'sandy',2e6),(-15,'sandy',10e6),(-100,'sandy',15e6)] #Properties of the sandy
# soils [(zBottom,type, nh), ...]  where 'zBottom' is the global Z coordinate
#           of the bottom level of the soil and 'nh' [Pa/m] is the coefficient 
#           corresponding to the compactness of the sandy soil.
eSize= 1     #length of elements
LeqPile=round(math.pi**0.5*fiPile/2.,3)

#Materials
concrete=EHE_materials.HA30
#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)
# coordinates in global X,Y,Z axes for the grid generation
xList=[0]
yList=[0]
zList=[-20,2]
# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()
#Lines generation
pile_rg=gm.IJKRange((0,0,0),(0,0,1))
pile=gridGeom.genLinOneRegion(ijkRange=pile_rg,nameSet='pile')

#                         *** MATERIALS *** 
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())
#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectPile=sectpr.RectangularSection(name='geomSectPile',b=LeqPile,h=LeqPile)
# Elastic material-section
pile_mat=tm.BeamMaterialData(name='pile_mat', section=geomSectPile, material=concrProp)
pile_mat.setupElasticShear3DSection(preprocessor=prep)

#                         ***FE model - MESH***
pile_mesh=fem.LinSetToMesh(linSet=pile,matSect=pile_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
fem.multi_mesh(preprocessor=prep,lstMeshSets=[pile_mesh])


#                       ***BOUNDARY CONDITIONS***
pileBC=sbc.PileFoundation(setPile=pile,pileDiam=fiPile,E=concrete.Ecm(),pileType='endBearing',pileBearingCapacity=bearCap,groundLevel=zGround,soilsProp=soils)
pileBC.generateSpringsPile(alphaKh_x=1,alphaKh_y=0.5,alphaKv_z=1)
springs=pileBC.springs
springSet=preprocessor.getSets.defSet('springSet')
for e in springs:
    springSet.getElements.append(e)
    print 'elem:', e.tag, ' z:',e.getCooCentroid(True)[2], ' Kx:',e.getMaterials()[0].E, ' Ky:',e.getMaterials()[1].E,' Kz:',e.getMaterials()[2].E
springSet.fillDownwards()
allSets=pile+springSet

from postprocess.xcVtk.FE_model import vtk_FE_graphic
defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
defDisplay.displayMesh(xcSets=allSets,fName= None,caption='Mesh',nodeSize=0.5,scaleConstr=0.10)
'''
modelSpace.fixNode000_000(0)
'''
# Loads definition
loadHandler= preprocessor.getLoadHandler
lPatterns= loadHandler.getLoadPatterns
#Load modulation.
ts= lPatterns.newTimeSeries("constant_ts","ts")
lPatterns.currentTimeSeries= "ts"
#Load case definition
lp0= lPatterns.newLoadPattern("default","0")

for tg in range(1,10):
    lp0.newNodalLoad(tg,xc.Vector([1e3,1e3,0,0,0,0]))
lp0.newNodalLoad(0,xc.Vector([0,0,-1e3,0,0,0]))

#We add the load case to domain.
lPatterns.addToDomain(lp0.name)

# Solution
analisis= predefined_solutions.simple_static_linear(FEcase)
result= analisis.analyze(1)

nodes.calculateNodalReactions(True,1e-7)
'''
for n in pile.getNodes:
    print 'node:', n.tag, ' ux:', n.getDisp[0], ' uy:',n.getDisp[1], ' uy:',n.getDisp[2]
'''
