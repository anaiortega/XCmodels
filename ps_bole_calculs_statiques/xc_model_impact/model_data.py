# -*- coding: utf-8 -*-

import xc_base
import geom
import xc
from model import predefined_spaces
from materials import typical_materials as tm
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc

cantileverWidth= 0.73
modelLength= 10
deckThickness= 0.35
parapetHeight= 1.54
parapetHeadHeight= 0.4
parapetBodyThickness= 0.38
parapetBodyHeight= parapetHeight-parapetHeadHeight
parapetHeadThickness= 0.5

FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor
modelSpace= predefined_spaces.StructuralMechanics3D(prep.getNodeHandler)

points= prep.getMultiBlockTopology.getPoints
# Deck cantilever
pt1= points.newPoint(geom.Pos3d(-cantileverWidth,0.0,0.0))
pt2= points.newPoint(geom.Pos3d(-cantileverWidth,modelLength,0.0))
pt3= points.newPoint(geom.Pos3d(0.0,modelLength,0.0))
pt4= points.newPoint(geom.Pos3d(0.0,0.0,0.0))

# Parapet body
pt5= points.newPoint(geom.Pos3d(0.0,0.0,parapetBodyHeight))
pt6= points.newPoint(geom.Pos3d(0.0,modelLength,parapetBodyHeight))

# Parapet head
pt7= points.newPoint(geom.Pos3d(0.0,modelLength,parapetHeight))
pt8= points.newPoint(geom.Pos3d(0.0,0.0,parapetHeight))


surfaces= prep.getMultiBlockTopology.getSurfaces
deck= surfaces.newQuadSurfacePts(pt1.tag,pt2.tag,pt3.tag,pt4.tag)
parapetBody= surfaces.newQuadSurfacePts(pt3.tag,pt4.tag,pt5.tag,pt6.tag)
parapetHead= surfaces.newQuadSurfacePts(pt6.tag,pt5.tag,pt8.tag,pt7.tag)

model_surfaces= [deck,parapetBody,parapetHead]
for s in model_surfaces:
    #print s.name, s.getIVector, s.getJVector
    s.setElemSizeIJ(0.15,0.2)

# *** Materials *** 
fcmConcr=50e6
EcConcr=8500*(fcmConcr/1e6)**(1/3.0)*1e6
cpoisConcr=0.2                #Poisson's coefficient of concrete
densConcr= 2500               #specific mass of concrete (kg/m3)
concrete=tm.MaterialData(name='concrete',E=EcConcr,nu=cpoisConcr,rho=densConcr)

deck.material= tm.defElasticMembranePlateSection(prep, "deckMat",EcConcr,cpoisConcr,0.0,deckThickness)
parapetBody.material= tm.defElasticMembranePlateSection(prep, "parapetBodyMat",EcConcr,cpoisConcr,0.0,parapetBodyThickness)
parapetHead.material= tm.defElasticMembranePlateSection(prep, "parapetHeadMat",EcConcr,cpoisConcr,0.0,parapetHeadThickness)

# *** Meshing ***
seedElemHandler= prep.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "deckMat"
elem= seedElemHandler.newElement("ShellMITC4",xc.ID([0,0,0,0]))

for s in model_surfaces:
    seedElemHandler.defaultMaterial= s.material.name
    s.genMesh(xc.meshDir.I)

# *** Constraints ***
cl1= prep.getMultiBlockTopology.getLineWithEndPoints(pt1.tag,pt2.tag)
cl2= prep.getMultiBlockTopology.getLineWithEndPoints(pt2.tag,pt3.tag)
cl3= prep.getMultiBlockTopology.getLineWithEndPoints(pt3.tag,pt6.tag)
cl4= prep.getMultiBlockTopology.getLineWithEndPoints(pt6.tag,pt7.tag)
constrainedLines= [cl1,cl2,cl3,cl4]

for l in constrainedLines:
  for i in l.getNodeTags():
    modelSpace.fixNode000_F00(i)

# *** Sets **
totalSet= prep.getSets.getSet('total')
shells= totalSet
deckSet= prep.getSets.defSet('deckSet')
for e in deck.elements:
    deckSet.elements.append(e)
deckSet.fillDownwards()
parapetBodySet= prep.getSets.defSet('parapetBodySet')
for e in parapetBody.elements:
    parapetBodySet.elements.append(e)
parapetBodySet.fillDownwards()
parapetHeadSet= prep.getSets.defSet('parapetHeadSet')
for e in parapetHead.elements:
    parapetHeadSet.elements.append(e)
parapetHeadSet.fillDownwards()
impactOnHead= prep.getSets.defSet('impactOnHead')
impactOnBody= prep.getSets.defSet('impactOnBody')

for e in totalSet.elements:
    pos= e.getPosCentroid(True)
    if(pos.y<1.5):
        if(pos.z>1.5-0.4):
            impactOnHead.elements.append(e)
        else:
            if((pos.z<(0.75+0.2)) and (pos.z>(0.75-0.2))):
                impactOnBody.elements.append(e)

impactOnHead.fillDownwards()
impactOnBody.fillDownwards()

# ***ACTIONS***
impactUniformLoad= 300e3/1.5/0.4
# Impact on parapet head:
impactOnHeadLoad= loads.UniformLoadOnSurfaces(name= 'impactOnHeadLoad',xcSet=impactOnHead,loadVector=xc.Vector([impactUniformLoad,0,0]),refSystem='Global')
impactOnBodyLoad= loads.UniformLoadOnSurfaces(name= 'impactOnBodyLoad',xcSet=impactOnBody,loadVector=xc.Vector([impactUniformLoad,0,0]),refSystem='Global')
    
# ***LOAD CASES***
A1=lcases.LoadCase(preprocessor=prep,name="A1",loadPType="default",timeSType="constant_ts")
A1.create()
A1.addLstLoads([impactOnHeadLoad])

A2=lcases.LoadCase(preprocessor=prep,name="A2",loadPType="default",timeSType="constant_ts")
A2.create()
A2.addLstLoads([impactOnBodyLoad])

# ***LOAD COMBINATIONS***
combContainer= cc.CombContainer()  #Container of load combinations
# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
combContainer.ULS.perm.add('ULSA1', '1.00*A1')
combContainer.ULS.perm.add('ULSA2', '1.00*A2')

