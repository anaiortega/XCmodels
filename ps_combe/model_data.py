# -*- coding: utf-8 -*-

import csv
import geom
import xc
from materials.sections import section_properties
from materials import typical_materials
from materials.sia262 import SIA262_materials
from model.mesh import finit_el_model as fem
from model.sets import sets_mng
from model import predefined_spaces
from materials import bridge_bearings
from actions.roadway_traffic import ofrou_report_664 as ofrou664
from actions import load_cases as lcm
from actions import combinations as cc
from actions.roadway_traffic import load_model_base as lmb

exec(open('./model_geometry.py').read())

# Materials.

deckConcr= SIA262_materials.c40_50
deckMat= deckConcr.defElasticMembranePlateSection(preprocessor, "deckMat",deckDepth)
#deckMat.E/=6.0 # Analysis of displacements.

pierThickness= 0.5
pierConcr= SIA262_materials.c55_67
pierMat= pierConcr.defElasticMembranePlateSection(preprocessor, "pierMat",pierThickness)
#pierMat.E/=6.0 # Analysis of displacements.

beamConcr= SIA262_materials.c60_75
polT4= geom.Polygon2d([geom.Pos2d(0.23,0.0), geom.Pos2d(0.23,0.1), geom.Pos2d(0.06,0.14), geom.Pos2d(0.06,0.52), geom.Pos2d(0.35,0.55), geom.Pos2d(0.35,0.65), geom.Pos2d(-0.645,0.65), geom.Pos2d(-0.645,0.59), geom.Pos2d(-0.06,0.52), geom.Pos2d(-0.06,0.14), geom.Pos2d(-0.23,0.1), geom.Pos2d(-0.23,0.0), geom.Pos2d(-0.025,0.0), geom.Pos2d(-0.025,0.03), geom.Pos2d(0.025,0.03), geom.Pos2d(0.025,0.0), geom.Pos2d(0.23,0.0)])
polT5= geom.Polygon2d([geom.Pos2d(0.23,0.0), geom.Pos2d(0.23,0.1), geom.Pos2d(0.06,0.14), geom.Pos2d(0.06,0.52), geom.Pos2d(0.645,0.59), geom.Pos2d(0.645,0.65), geom.Pos2d(-0.35,0.65), geom.Pos2d(-0.35,0.55), geom.Pos2d(-0.06,0.52), geom.Pos2d(-0.06,0.14), geom.Pos2d(-0.23,0.1), geom.Pos2d(-0.23,0.0), geom.Pos2d(-0.025,0.0), geom.Pos2d(-0.025,0.03), geom.Pos2d(0.025,0.03), geom.Pos2d(0.025,0.0), geom.Pos2d(0.23,0.0)])
polT6= geom.Polygon2d([geom.Pos2d(0.23,0.0), geom.Pos2d(0.23,0.1), geom.Pos2d(0.06,0.14), geom.Pos2d(0.06,0.52), geom.Pos2d(0.645,0.59), geom.Pos2d(0.645,0.65), geom.Pos2d(-0.645,0.65), geom.Pos2d(-0.645,0.59), geom.Pos2d(-0.06,0.52), geom.Pos2d(-0.06,0.14), geom.Pos2d(-0.23,0.1), geom.Pos2d(-0.23,0.0), geom.Pos2d(0.23,0.0)])

beamType4Section= section_properties.PolygonalSection('beamType4Contour',geom.Polygon2d(polT4)).defElasticShearSection3d(preprocessor,typical_materials.MaterialData('tmp',beamConcr.Ecm(),beamConcr.nuc,beamConcr.density()))
beamType5Section= section_properties.PolygonalSection('beamType5Contour',geom.Polygon2d(polT5)).defElasticShearSection3d(preprocessor,typical_materials.MaterialData('tmp',beamConcr.Ecm(),beamConcr.nuc,beamConcr.density()))
beamType6Section= section_properties.PolygonalSection('beamType6Contour',geom.Polygon2d(polT6)).defElasticShearSection3d(preprocessor,typical_materials.MaterialData('tmp',beamConcr.Ecm(),beamConcr.nuc,beamConcr.density()))

beamWebSection= section_properties.RectangularSection('beamWebSection',0.5,0.16).defElasticShearSection3d(preprocessor,typical_materials.MaterialData('tmp',beamConcr.Ecm(),beamConcr.nuc,beamConcr.density()))

braceBeamsConcr= deckConcr
pierBraceBeamSection= section_properties.RectangularSection('pierBraceBeamSection',0.4,0.65).defElasticShearSection3d(preprocessor,typical_materials.MaterialData('tmp',braceBeamsConcr.Ecm(),braceBeamsConcr.nuc,braceBeamsConcr.density()))
abutmentBraceBeamSection= section_properties.RectangularSection('abutmentBraceBeamSection',0.89,0.65).defElasticShearSection3d(preprocessor,typical_materials.MaterialData('tmp',braceBeamsConcr.Ecm(),braceBeamsConcr.nuc,braceBeamsConcr.density()))

legsConcr= beamConcr
legsSection= section_properties.RectangularSection('legsSection',0.5,0.5).defElasticShearSection3d(preprocessor,typical_materials.MaterialData('tmp',legsConcr.Ecm(),legsConcr.nuc,legsConcr.density()))

corbelsConcr= beamConcr
corbelsSection= section_properties.RectangularSection('corbelsSection',0.5,1.0).defElasticShearSection3d(preprocessor,typical_materials.MaterialData('tmp',corbelsConcr.Ecm(),corbelsConcr.nuc,corbelsConcr.density()))

# Elastomeric bearings.

neop= bridge_bearings.ElastomericBearing(G= 900e3,a= 0.15,b= 0.2,e= 0.02)
neop.defineMaterials(preprocessor)

# print polT5.getIx(), polT5.getCenterOfMass()
# print polT6.getIx(), polT6.getCenterOfMass()
# print polT4.getIx(), polT4.getCenterOfMass()

# Mesh

deckMesh= fem.SurfSetToMesh(surfSet= deckSurfaces,matSect=deckMat,elemSize=0.5,elemType='ShellMITC4')
deckMesh.generateMesh(preprocessor) #do meshing

#Precast beams.
linX= modelSpace.newLinearCrdTransf("linX",xc.Vector([1,0,0]))
type4Beams= fem.RawLineSetToMesh(linSet= beamLinesType4, matSect= beamType4Section, elemSize= None, coordTransf= linX, elemType='ElasticBeam3d',dimElemSpace=3)
type4Beams.generateMesh(preprocessor) #do meshing
type5Beams= fem.RawLineSetToMesh(linSet= beamLinesType5, matSect= beamType5Section, elemSize= None, coordTransf= linX, elemType='ElasticBeam3d',dimElemSpace=3)
type5Beams.generateMesh(preprocessor) #do meshing
type6Beams= fem.RawLineSetToMesh(linSet= beamLinesType6, matSect= beamType6Section, elemSize= None, coordTransf= linX, elemType='ElasticBeam3d',dimElemSpace=3)
type6Beams.generateMesh(preprocessor) #do meshing

#Precast beam webs.
elements= preprocessor.getElementHandler
elements.defaultMaterial= beamWebSection.getName()
webElements= preprocessor.getSets.defSet("webElements")

for s in pairedLines:
    bl= s[0]
    dl= s[1]
    tg= bl.getTang(0.0)
    trfName= bl.name+'_trf'
    trf= modelSpace.newLinearCrdTransf(trfName,tg)
    #print bl.getLength(), dl.getLength()
    #print bl.nDiv, dl.nDiv
    for n1 in bl.nodes:
        n2= dl.getNearestNode(n1.getInitialPos3d)
        #print n1.tag, n2.tag, n1.getInitialPos3d.dist(n2.getInitialPos3d)
        elements.defaultTransformation= trf.getName()
        webElem= elements.newElement("ElasticBeam3d",xc.ID([n1.tag,n2.tag]))
        webElements.elements.append(webElem)
webElements.fillDownwards()
pierMesh= fem.SurfSetToMesh(surfSet= pierSurfaces,matSect=pierMat,elemSize=0.5,elemType='ShellMITC4')
pierMesh.generateMesh(preprocessor) #do meshing

#Brace beams
linY= modelSpace.newLinearCrdTransf("linY",xc.Vector([0,1,0]))
abutmentBrace= fem.RawLineSetToMesh(linSet= abutmentBraceLines, matSect= abutmentBraceBeamSection, elemSize= None, coordTransf= linY, elemType='ElasticBeam3d',dimElemSpace=3)
abutmentBrace.generateMesh(preprocessor) #do meshing

pierBrace= fem.RawLineSetToMesh(linSet= pierBraceLines, matSect= pierBraceBeamSection, elemSize= None, coordTransf= linY, elemType='ElasticBeam3d',dimElemSpace=3)
pierBrace.generateMesh(preprocessor) #do meshing

#Legs
legs= fem.RawLineSetToMesh(linSet= legLines, matSect= legsSection, elemSize= None, coordTransf= linY, elemType='ElasticBeam3d',dimElemSpace=3)
legs.generateMesh(preprocessor) #do meshing

#Corbels
corbels= fem.RawLineSetToMesh(linSet= corbelLines, matSect= corbelsSection, elemSize= 0.5, coordTransf= linX, elemType='ElasticBeam3d',dimElemSpace=3)
corbels.generateMesh(preprocessor) #do meshing

#Bridge bearings.
abutmentBearingElements= preprocessor.getSets.defSet("abutmentBearingElements")
abutmentFixedNodes= list()
for l in abutmentLegLines.getLines:
    n1= l.firstNode
    z1= n1.getInitialPos3d.z
    n2= l.lastNode
    z2= n2.getInitialPos3d.z
    orientation= l.getProp('orientation')
    fixedNode= None
    freeNode= None
    newElem= None
    if(z1<z2):
        freeNode= n1
    else:
        freeNode= n2
    fixedNode= nodes.duplicateNode(freeNode.tag)
    newElem= neop.setBearingBetweenNodes(modelSpace, fixedNode.tag, freeNode.tag,orientation)
    abutmentBearingElements.elements.append(newElem)
    abutmentFixedNodes.append(fixedNode)

#Guide supports.
MassongexBraceNodes= list()
BexBraceNodes= list()
for n in abutmentBraceLines.nodes:
    x= n.getInitialPos3d.y
    if(x<60): # Massongex abutment
        MassongexBraceNodes.append(n)
    else: # Bex abutment
        BexBraceNodes.append(n)
numMassongexBraceNodes= len(MassongexBraceNodes)
avgY= 0.0
for n in MassongexBraceNodes:
    avgY+= n.getInitialPos3d.x
avgY/=numMassongexBraceNodes
MassongexBraceCenterNode= MassongexBraceNodes[0]
dd= abs(MassongexBraceCenterNode.getInitialPos3d.x-avgY)
for n in MassongexBraceNodes:
    d= abs(n.getInitialPos3d.x-avgY)
    if(d<dd):
      dd= d
      MassongexBraceCenterNode= n
#print 'avgY= ', avgY, 'MassongexBraceCenterNode= ',MassongexBraceCenterNode.getInitialPos3d
BexBraceNodes= list()
BexBraceNodes= list()
for n in abutmentBraceLines.nodes:
    x= n.getInitialPos3d.y
    if(x<60): # Bex abutment
        BexBraceNodes.append(n)
    else: # Bex abutment
        BexBraceNodes.append(n)
numBexBraceNodes= len(BexBraceNodes)
avgY= 0.0
for n in BexBraceNodes:
    avgY+= n.getInitialPos3d.x
avgY/=numBexBraceNodes
BexBraceCenterNode= BexBraceNodes[0]
dd= abs(BexBraceCenterNode.getInitialPos3d.x-avgY)
for n in BexBraceNodes:
    d= abs(n.getInitialPos3d.x-avgY)
    if(d<dd):
      dd= d
      BexBraceCenterNode= n

#print 'avgY= ', avgY, 'BexBraceCenterNode= ',BexBraceCenterNode.getInitialPos3d
preprocessor.getBoundaryCondHandler.newSPConstraint(MassongexBraceCenterNode.tag,0,0.0) #Massongex guide.
preprocessor.getBoundaryCondHandler.newSPConstraint(BexBraceCenterNode.tag,0,0.0) #Bex guide.

    
pierBearingElements= preprocessor.getSets.defSet("pierBearingElements")
for pair in pairedPoints:
    n1= pair[0].getNode()
    n2= pair[1].getNode()
    orientation= pair[2]
    newElem= neop.putBetweenNodes(modelSpace, n1.tag, n2.tag,orientation)
    pierBearingElements.elements.append(newElem)
pierBearingElements.fillDownwards()


#Constraints on piers.
foundationNodesPierMassongex= list()
sz= len(bottomPointsPierMassongex)
for i in range(0,sz-1):
    l= preprocessor.getMultiBlockTopology.getLineWithEndPoints(bottomPointsPierMassongex[i].tag,bottomPointsPierMassongex[i+1].tag)
    for n in l.nodes:
        foundationNodesPierMassongex.append(n)
foundationNodesPierBex= list()
sz= len(bottomPointsPierBex)
for i in range(0,sz-1):
    l= preprocessor.getMultiBlockTopology.getLineWithEndPoints(bottomPointsPierBex[i].tag,bottomPointsPierBex[i+1].tag)
    for n in l.nodes:
        foundationNodesPierBex.append(n)
        
for n in foundationNodesPierMassongex:
    modelSpace.fixNode000_000(n.tag)

#Settlements
BexAbutmentRelativeSettlement= -32e-3 # m
BexPierRelativeSettlement= -13.5e-3
MassongexAbutmentRelativeSettlement= -24.5e-3 # m
# No settlements
# BexAbutmentRelativeSettlement= 0.0
# BexPierRelativeSettlement= 0.0
# MassongexAbutmentRelativeSettlement= 0.0


for n in foundationNodesPierBex:
    modelSpace.setPrescribedDisplacements(n.tag,[0.0,0.0,BexPierRelativeSettlement,0.0,0.0,0.0])

for n in abutmentFixedNodes:
    x= n.getInitialPos3d.y
    if(x<60): # Massongex abutment
        modelSpace.setPrescribedDisplacements(n.tag,[0.0,0.0,MassongexAbutmentRelativeSettlement,0.0,0.0,0.0])
    else: # Bex abutment
        modelSpace.setPrescribedDisplacements(n.tag,[0.0,0.0,BexAbutmentRelativeSettlement,0.0,0.0,0.0])

# Sets
beams= preprocessor.getSets.defSet('beams')
shells= preprocessor.getSets.defSet('shells')
for e in xcTotalSet.elements:
    className= e.type()
    if('Beam' in className):
        beams.elements.append(e)
    elif('Shell' in className):
        shells.elements.append(e)
shells.fillDownwards()
beams.fillDownwards()

beamLines= beamLinesType4+beamLinesType5+beamLinesType6
beamLines.fillDownwards()
beamLines.description= 'prestressed beams'

# Actions
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['GselfWeight','GdeadLoad','liveLoad269_1','liveLoad269_2','liveLoad664Crane_1','liveLoad664Crane_2','liveLoad664Det1_1','liveLoad664Det1_2','liveLoad664Det2_1','liveLoad664Det2_2','temp_up','temp_down','eQuake']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

grav= 9.81 #Gravity acceleration (m/s2)

# Self weight.
shells.computeTributaryAreas(False)
cLC= loadCaseManager.setCurrentLoadCase('GselfWeight')
for e in shells.elements:
    thickness= e.getPhysicalProperties.getVectorMaterials[0].h
    rho= e.getPhysicalProperties.getVectorMaterials[0].rho
    inertialMass= rho*thickness
    load= grav*inertialMass
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-load]))
    #For modal analysis.
    eNodes= e.getNodes
    for n in eNodes:
        tributaryMass= e.getTributaryArea(n)*inertialMass
        if(n.hasProp('tributaryMass')):
          n.setProp('tributaryMass',n.getProp('tributaryMass')+tributaryMass)
        else:
          n.setProp('tributaryMass',tributaryMass)

beams.computeTributaryLengths(False)
for e in beams.elements:
    area= e.sectionProperties.A
    inertialMass= 2500*area
    load=  grav*inertialMass
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-load]))
    #For modal analysis.
    eNodes= e.getNodes
    for n in eNodes:
        tributaryMass= e.getTributaryLength(n)*inertialMass
        if(n.hasProp('tributaryMass')):
          n.setProp('tributaryMass',n.getProp('tributaryMass')+tributaryMass)
        else:
          n.setProp('tributaryMass',tributaryMass)

# Dead load.
cLC= loadCaseManager.setCurrentLoadCase('GdeadLoad')
deadLoad= 23.76e3 #N/m2
deadLoadVector= xc.Vector([0.0, 0.0, -deadLoad])
for e in deckSurfaces.elements:
    e.vector3dUniformLoadGlobal(deadLoadVector)
    #For modal analysis.
    inertialMass= deadLoad/grav
    eNodes= e.getNodes
    for n in eNodes:
        tributaryMass= e.getTributaryLength(n)*inertialMass
        if(n.hasProp('tributaryMass')):
            n.setProp('tributaryMass',n.getProp('tributaryMass')+tributaryMass)
        else:
            n.setProp('tributaryMass',tributaryMass)

for edge in edgeLines:
    nNodes= len(edge.nodes)
    for n in edge.nodes:
        load= 4.87e3 *edge.getLength()/nNodes# N/mbarrier + parapet
        cLC.newNodalLoad(n.tag,xc.Vector([0.0,0.0,-load,0,0,0]))
        #For modal analysis.
        tributaryMass= load/grav
        if(n.hasProp('tributaryMass')):
            n.setProp('tributaryMass',n.getProp('tributaryMass')+tributaryMass)
        else:
            n.setProp('tributaryMass',tributaryMass)

# SIA 269 load model 1 (mid span)
cLC= loadCaseManager.setCurrentLoadCase('liveLoad269_1')
# Traffic point loads.
lane1Axis= laneAxisLines[0]
lane1Sg= lane1Axis.getSegment(2)
lane1Center= lane1Sg.getCenterOfMass()
lane1CenterTrsvSlope= (transverseSlopes[1]+transverseSlopes[2])*0.5
lane1CenterLongSlope= lane1Sg.getVDir().normalized()
loadPositions= [(-0.6,1.0),(0.6,1.0),(-0.6,-1.0),(0.6,-1.0)]
load3DPositions= list()
for p in loadPositions:
    p3D= lane1Center+p[1]*lane1CenterTrsvSlope+p[0]*lane1CenterLongSlope
    load3DPositions.append(p3D)
lane1CenterNodLst= sets_mng.get_lstNod_from_lst3DPos(preprocessor,lst3DPos=load3DPositions)
alphaQ1= 0.7
Qk1= alphaQ1*300e3/2.0 #N
Qk1LongBrake= 1.2*Qk1*lane1CenterLongSlope
Qk1TrsvBrake= -0.25*1.2*Qk1*lane1CenterTrsvSlope
Qk1TrsvCentrif= -0.033*1.2*Qk1*lane1CenterTrsvSlope
Qk1Brake= Qk1LongBrake+Qk1TrsvCentrif+Qk1TrsvBrake
Qk1Vector= geom.Vector3d(0.0,0.0,-Qk1)+Qk1Brake
for n in lane1CenterNodLst:
    cLC.newNodalLoad(n.tag,xc.Vector([Qk1Vector.x,Qk1Vector.y,Qk1Vector.z,0,0,0]))
lane2Axis= laneAxisLines[1]
lane2Sg= lane2Axis.getSegment(2)
lane2Center= lane2Sg.getCenterOfMass()
lane2CenterTrsvSlope= (transverseSlopes[1]+transverseSlopes[2])*0.5
lane2CenterLongSlope= lane2Sg.getVDir().normalized()
load3DPositions= list()
for p in loadPositions:
    p3D= lane2Center+p[1]*lane2CenterTrsvSlope+p[0]*lane2CenterLongSlope
    load3DPositions.append(p3D)
lane2CenterNodLst= sets_mng.get_lstNod_from_lst3DPos(preprocessor,lst3DPos=load3DPositions)
alphaQ2= 0.5
Qk2= alphaQ2*200e3/2.0 #N
for n in lane2CenterNodLst:
    cLC.newNodalLoad(n.tag,xc.Vector([0.0,0.0,-Qk2,0,0,0]))

#Traffic uniform loads:
alpha_q= 0.4
qk1= alpha_q*9e3 #N/m
qk1LongBrake= 0.1*qk1*lane1CenterLongSlope
qk1TrsvBrake= -0.25*0.1*qk1*lane1CenterTrsvSlope
qk1Brake= qk1LongBrake+qk1TrsvBrake
qk1Vector= geom.Vector3d(0.0,0.0,-qk1)+qk1Brake
poly_lane1= laneRegions[0]
lane1_elements= sets_mng.set_included_in_orthoPrism(preprocessor,setInit=deckSurfaces,prismBase=poly_lane1,prismAxis='Z',setName='lane1_elements')
for e in lane1_elements.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([qk1Vector.x,qk1Vector.y,qk1Vector.z]))
qk2= alpha_q*2.5e3 #N/m
poly_lane2= laneRegions[1]
lane2_elements= sets_mng.set_included_in_orthoPrism(preprocessor,setInit=deckSurfaces,prismBase=poly_lane2,prismAxis='Z',setName='lane2_elements')
for e in lane2_elements.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-qk2]))
qk3= alpha_q*2.5e3 #N/m
poly_lane3= laneRegions[2]
lane3_elements= sets_mng.set_included_in_orthoPrism(preprocessor,setInit=deckSurfaces,prismBase=poly_lane3,prismAxis='Z',setName='lane3_elements')
for e in lane3_elements.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-qk3]))

# SIA 269 load model 1 (shear control)
cLC= loadCaseManager.setCurrentLoadCase('liveLoad269_2')
# Traffic point loads.
lane1Axis= laneAxisLines[0]
lane1Sg= lane1Axis.getSegment(2)
lane1OriginTrsvSlope= transverseSlopes[1]
lane1OriginLongSlope= lane1Sg.getVDir().normalized()
lane1Origin= lane1Sg.getFromPoint()-1.1*(0.65+0.16+1.2)/2.0*lane1OriginLongSlope
loadPositions= [(-0.6,1.0),(0.6,1.0),(-0.6,-1.0),(0.6,-1.0)]
load3DPositions= list()
for p in loadPositions:
    p3D= lane1Origin+p[1]*lane1OriginTrsvSlope+p[0]*lane1OriginLongSlope
    load3DPositions.append(p3D)
lane1OriginNodLst= sets_mng.get_lstNod_from_lst3DPos(preprocessor,lst3DPos=load3DPositions)
alphaQ1= 0.7
Qk1= alphaQ1*300e3/2.0 #N
Qk1LongBrake= 1.2*Qk1*lane1OriginLongSlope
Qk1TrsvBrake= -0.25*1.2*Qk1*lane1OriginTrsvSlope
Qk1TrsvCentrif= -0.033*1.2*Qk1*lane1OriginTrsvSlope
Qk1Brake= Qk1LongBrake+Qk1TrsvCentrif+Qk1TrsvBrake
Qk1Vector= geom.Vector3d(0.0,0.0,-Qk1)+Qk1Brake
for n in lane1OriginNodLst:
    cLC.newNodalLoad(n.tag,xc.Vector([Qk1Vector.x,Qk1Vector.y,Qk1Vector.z,0,0,0]))
lane2Axis= laneAxisLines[1]
lane2Sg= lane2Axis.getSegment(2)
lane2OriginTrsvSlope= (transverseSlopes[1]+transverseSlopes[2])*0.5
lane2OriginLongSlope= lane2Sg.getVDir().normalized()
lane2Origin= lane2Sg.getFromPoint()-1.1*(0.65+0.16+1.2)/2.0*lane2OriginLongSlope
load3DPositions= list()
for p in loadPositions:
    p3D= lane2Origin+p[1]*lane2OriginTrsvSlope+p[0]*lane2OriginLongSlope
    load3DPositions.append(p3D)
lane2OriginNodLst= sets_mng.get_lstNod_from_lst3DPos(preprocessor,lst3DPos=load3DPositions)
alphaQ2= 0.5
Qk2= alphaQ2*200e3/2.0 #N
for n in lane2OriginNodLst:
    cLC.newNodalLoad(n.tag,xc.Vector([0.0,0.0,-Qk2,0,0,0]))

#Traffic uniform loads:
qk1Vector= geom.Vector3d(0.0,0.0,-qk1)
for e in lane1_elements.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([qk1Vector.x,qk1Vector.y,qk1Vector.z]))
for e in lane2_elements.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-qk2]))
for e in lane3_elements.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-qk3]))

def putNodalLoads(vLoad):
    nodLst= sets_mng.get_lstNod_from_lst3DPos(preprocessor,lst3DPos= vLoad.getLoadPositions())
    wheelsLoad= vLoad.loadModel.getLoads()
    loadIndex= 0
    for n in nodLst:
        cLC.newNodalLoad(n.tag,xc.Vector([0.0,0.0,-wheelsLoad[loadIndex],0,0,0]))
        loadIndex+=1
    
def putTruckAt(position, longSlope, trsvSlope, truckLoadModel):
    vLoad= lmb.VehicleLoad(truckLoadModel,geom.Ref2d3d(position,longSlope,trsvSlope))
    putNodalLoads(vLoad)
    return vLoad

def putTruckAtOrigin(origin, longSlope, trsvSlope, truckLoadModel):
    bnd= ofrou664.CraneTruckLoadModel.getCenteredLoadBoundary()
    vDisp= (bnd.getMax(1)-0.6)*longSlope
    vLoad= lmb.VehicleLoad(truckLoadModel,geom.Ref2d3d(origin-vDisp,-longSlope,trsvSlope))
    putNodalLoads(vLoad)
    return vLoad

# Crane model as in the Report OFROU number 664
cLC= loadCaseManager.setCurrentLoadCase('liveLoad664Crane_1')
putTruckAt(lane1Center,lane1CenterLongSlope,lane1CenterTrsvSlope,ofrou664.CraneTruckLoadModel)

# Shear control
cLC= loadCaseManager.setCurrentLoadCase('liveLoad664Crane_2')
putTruckAtOrigin(lane1Origin,lane1OriginLongSlope,lane1OriginTrsvSlope,ofrou664.CraneTruckLoadModel)

# DET1 model as in the Report OFROU number 664
cLC= loadCaseManager.setCurrentLoadCase('liveLoad664Det1_1')
vLoadDet11= putTruckAt(lane1Center,lane1CenterLongSlope,lane1CenterTrsvSlope,ofrou664.Det11TruckLoadModel)
vLoadDet12= putTruckAt(lane2Center,lane2CenterLongSlope,lane2CenterTrsvSlope,ofrou664.Det12TruckLoadModel)
# Shear control
cLC= loadCaseManager.setCurrentLoadCase('liveLoad664Det1_2')
vLoadDet11= putTruckAtOrigin(lane1Origin,lane1OriginLongSlope,lane1OriginTrsvSlope,ofrou664.Det11TruckLoadModel.getRotatedPi())
vLoadDet12= putTruckAtOrigin(lane2Origin,lane2OriginLongSlope,lane2OriginTrsvSlope,ofrou664.Det12TruckLoadModel.getRotatedPi())

# DET2 model as in the Report OFROU number 664
cLC= loadCaseManager.setCurrentLoadCase('liveLoad664Det2_1')
vLoadDet21= putTruckAt(lane1Center,lane1CenterLongSlope,lane1CenterTrsvSlope,ofrou664.Det21TruckLoadModel)
vLoadDet22= putTruckAt(lane2Center,lane2CenterLongSlope,lane2CenterTrsvSlope,ofrou664.Det22TruckLoadModel)
# DET2 uniform loads:
qkDet2= 10e3 #N/m
qkDet2Vector= geom.Vector3d(0.0,0.0,-qkDet2)
lane1_det2_loaded_elements= sets_mng.set_not_included_in_orthoPrism(preprocessor,setInit=lane1_elements,prismBase=vLoadDet21.getVehicleBoundary() ,prismAxis='Z',setName='lane1_det2_loaded_elements')
for e in lane1_det2_loaded_elements.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([qkDet2Vector.x,qkDet2Vector.y,qkDet2Vector.z]))
lane2_det2_loaded_elements= sets_mng.set_not_included_in_orthoPrism(preprocessor,setInit=lane2_elements,prismBase=vLoadDet22.getVehicleBoundary(),prismAxis='Z',setName='lane1_det2_loaded_elements')
for e in lane2_det2_loaded_elements.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([qkDet2Vector.x,qkDet2Vector.y,qkDet2Vector.z]))

# Shear control
cLC= loadCaseManager.setCurrentLoadCase('liveLoad664Det2_2')
vLoadDet21Shear= putTruckAtOrigin(lane1Origin,lane1OriginLongSlope,lane1OriginTrsvSlope,ofrou664.Det21TruckLoadModel.getRotatedPi())
vLoadDet22Shear= putTruckAtOrigin(lane2Origin,lane2OriginLongSlope,lane2OriginTrsvSlope,ofrou664.Det22TruckLoadModel.getRotatedPi())
lane1_det2_loaded_elements_shear= sets_mng.set_not_included_in_orthoPrism(preprocessor,setInit=lane1_elements,prismBase=vLoadDet21Shear.getVehicleBoundary() ,prismAxis='Z',setName='lane1_det2_loaded_elements_shear')
for e in lane1_det2_loaded_elements_shear.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([qkDet2Vector.x,qkDet2Vector.y,qkDet2Vector.z]))
lane2_det2_loaded_elements_shear= sets_mng.set_not_included_in_orthoPrism(preprocessor,setInit=lane2_elements,prismBase=vLoadDet22Shear.getVehicleBoundary(),prismAxis='Z',setName='lane1_det2_loaded_elements_shear')
for e in lane2_det2_loaded_elements_shear.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([qkDet2Vector.x,qkDet2Vector.y,qkDet2Vector.z]))


#Temperature.
cLC= loadCaseManager.setCurrentLoadCase('temp_down')
alphaAT= -20.0*10e-6

eleLoad= cLC.newElementalLoad("shell_strain_load")
eleLoad.elementTags= shells.elements.getTags()
eleLoad.setStrainComp(0,0,alphaAT) #(id of Gauss point, id of component, value)
eleLoad.setStrainComp(0,1,alphaAT)
eleLoad.setStrainComp(1,0,alphaAT)
eleLoad.setStrainComp(1,1,alphaAT)
eleLoad.setStrainComp(2,0,alphaAT)
eleLoad.setStrainComp(2,1,alphaAT)
eleLoad.setStrainComp(3,0,alphaAT)
eleLoad.setStrainComp(3,1,alphaAT)

eleLoad= cLC.newElementalLoad("beam_strain_load")
eleLoad.elementTags= beams.elements.getTags()
defPlane= xc.DeformationPlane(alphaAT)
eleLoad.backEndDeformationPlane= defPlane
eleLoad.frontEndDeformationPlane= defPlane

cLC= loadCaseManager.setCurrentLoadCase('temp_up')
alphaAT= 20.0*10e-6

eleLoad= cLC.newElementalLoad("shell_strain_load")
eleLoad.elementTags= shells.elements.getTags()
eleLoad.setStrainComp(0,0,alphaAT) #(id of Gauss point, id of component, value)
eleLoad.setStrainComp(0,1,alphaAT)
eleLoad.setStrainComp(1,0,alphaAT)
eleLoad.setStrainComp(1,1,alphaAT)
eleLoad.setStrainComp(2,0,alphaAT)
eleLoad.setStrainComp(2,1,alphaAT)
eleLoad.setStrainComp(3,0,alphaAT)
eleLoad.setStrainComp(3,1,alphaAT)

eleLoad= cLC.newElementalLoad("beam_strain_load")
eleLoad.elementTags= beams.elements.getTags()
defPlane= xc.DeformationPlane(alphaAT)
eleLoad.backEndDeformationPlane= defPlane
eleLoad.frontEndDeformationPlane= defPlane

#Earthquake.
cLC= loadCaseManager.setCurrentLoadCase('eQuake')
f= open('earthquake_loads.csv','r')
next(f) # ignore header on csv file.
reader= csv.reader(f)
for row in reader:
    nodeTag= int(row[0])
    Fy= float(row[2])
    cLC.newNodalLoad(n.tag,xc.Vector([0.0,Fy,-0.7*Fy,0.0,0.0,0.0]))
    

#LOAD COMBINATIONS
combContainer= cc.CombContainer()  #Container of load combinations
# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
#Characteristic combinations.
#combContainer.SLS.rare.add('ELSR01', '1.0*GselfWeight+1.0*GdeadLoad+1.5*temperature')

#Frequent combinations.
#combContainer.SLS.freq.add('ELSF01', '1.0*GselfWeight+1.0*GdeadLoad+0.75*QliveLoadA')
#Quasi permanent combinations.
#combContainer.SLS.qp.add('ELSQP01', '1.0*GselfWeight+1.0*GdeadLoad')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELU01','1.2*GselfWeight+1.2*GdeadLoad+1.5*liveLoad269_1')
combContainer.ULS.perm.add('ELU02','1.2*GselfWeight+1.2*GdeadLoad+1.5*liveLoad269_2')
combContainer.ULS.perm.add('ELU03','1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Crane_1')
combContainer.ULS.perm.add('ELU04','1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Crane_2')
combContainer.ULS.perm.add('ELU05','1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det1_1')
combContainer.ULS.perm.add('ELU06','1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det1_2')
combContainer.ULS.perm.add('ELU07','1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det2_1')
combContainer.ULS.perm.add('ELU08','1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det2_2')
combContainer.ULS.acc.add('A','1.0*GselfWeight+1.0*GdeadLoad+1.1*eQuake')


#Fatigue.
# Combinations' names must be:
#        - ELUF0: unloaded structure (permanent loads)
#        - ELUF1: fatigue load in position 1.
# combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*GdeadLoad')
# combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*QfatigueLoad')


