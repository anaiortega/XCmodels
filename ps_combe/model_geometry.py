# -*- coding: utf-8 -*-

asphaltThickness= 0.11
beamDepth= 0.65
deckDepth= 0.16 # Deck thickness [m]
bearingThickness= 0.02
MassongexPierFoundationLevel= 6.95
BexPierFoundationLevel= 7.9

beamCentroids= [geom.Pos3d(-4.49681840223057, 0.0, 0.392346547056209),
                geom.Pos3d(-3.250, 0.0, 0.411174893092701),
                geom.Pos3d(-1.950, 0.0, 0.411174893092701),
                geom.Pos3d(-0.650, 0.0, 0.411174893092701),
                geom.Pos3d(0.650, 0.0, 0.411174893092701),
                geom.Pos3d(1.950, 0.0, 0.411174893092701),
                geom.Pos3d(3.250, 0.0, 0.411174893092701),
                geom.Pos3d(4.49681840223057, 0.0, 0.392346547056209)]

beamBottoms= [geom.Pos3d(-4.49681840223057, 0.0, 0.0),
              geom.Pos3d(-3.250, 0.0, 0.0),
              geom.Pos3d(-1.950, 0.0, 0.0),
              geom.Pos3d(-0.650, 0.0, 0.0),
              geom.Pos3d(0.650, 0.0, 0.0),
              geom.Pos3d(1.950, 0.0, 0.0),
              geom.Pos3d(3.250, 0.0, 0.0),
              geom.Pos3d(4.49681840223057, 0.0, 0.0)]

beamSupports= [geom.Pos3d(-4.49681840223057, 0.0, -0.01),
              geom.Pos3d(-3.250, 0.0, -0.01),
              geom.Pos3d(-1.950, 0.0, -0.01),
              geom.Pos3d(-0.650, 0.0, -0.01),
              geom.Pos3d(0.650, 0.0, -0.01),
              geom.Pos3d(1.950, 0.0, -0.01),
              geom.Pos3d(3.250, 0.0, -0.01),
              geom.Pos3d(4.49681840223057, 0.0, -0.01)]

deckLines= [geom.Pos3d(-5.0, 0.0,beamDepth+deckDepth/2.0),
            geom.Pos3d(-4.49681840223057, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(-3.250, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(-1.950, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(-0.650, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(0.650, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(1.950, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(3.250, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(4.49681840223057, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(5.0, 0.0, beamDepth+deckDepth/2.0)]

# Lines for load distribution (lane contours and lane axis).
laneLines=  [geom.Pos3d(-4.5, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(-1.5, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(1.5, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(4.5, 0.0, beamDepth+deckDepth/2.0)]

laneAxisLines=  [geom.Pos3d(-3.0, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(0.0, 0.0, beamDepth+deckDepth/2.0),
            geom.Pos3d(3.0, 0.0, beamDepth+deckDepth/2.0)]


#Massongex abutment.
aMassongex= geom.Pos3d(45.795, 42.633, 0.0)
vAMassongex= (geom.Pos3d(32.1000234984885, 40.5187002427488, 0.0)-geom.Pos3d(59.4899765015115, 44.7472997572513, 0.0)).normalizado()
O= aMassongex+geom.Vector3d(0.0, 0.0, 16.498)
VI= -4.5*vAMassongex+geom.Vector3d(0.0,0.0,16.332-O.z)
VJ= geom.Vector3d(-vAMassongex.y,vAMassongex.x,0.0)
refMassongexAbutment= geom.Ref3d3d(O,VI,-VJ)
# print 'O= ', O
# print 'P1= ', O+VI
# print 'I= ',refMassongexAbutment.getI()
# print 'J= ',refMassongexAbutment.getJ()
# print 'K= ',refMassongexAbutment.getK()

#Massongex pier.
pMassongex= geom.Pos3d(42.843, 55.293, 0.0) 
vPMassongex= (geom.Pos3d(29.0916831682014, 53.5830496404986, 0.0)-geom.Pos3d(56.5943168317984, 57.0029503595014, 0.0)).normalizado()
O= pMassongex+geom.Vector3d(0.0, 0.0, 16.751)
VI= -4.5*vPMassongex+geom.Vector3d(0.0,0.0,16.597-O.z)
VJ= geom.Vector3d(-vPMassongex.y,vPMassongex.x,0.0)
refMassongexPier= geom.Ref3d3d(O,VI,-VJ)
# print 'O= ', O
# print 'P1= ', O+VI
# print 'I= ',refMassongexPier.getI()
# print 'J= ',refMassongexPier.getJ()
# print 'K= ',refMassongexPier.getK()

#Bex pier.
pBex= geom.Pos3d(38.9231965683346, 70.7225756927112, 0.0) 
vPBex= -1.0*(geom.Pos3d(52.6567060878268, 72.5701040736782, 0.0)-geom.Pos3d(25.1896870488423, 68.8750473117442, 0.0)).normalizado()
O= pBex+geom.Vector3d(0.0, 0.0, 16.986)
VI= -4.5*vPBex+geom.Vector3d(0.0,0.0,16.866-O.z)
VJ= geom.Vector3d(-vPBex.y,vPBex.x,0.0)
refBexPier= geom.Ref3d3d(O,VI,-VJ)
# print 'O= ', O
# print 'P1= ', O+VI
# print 'I= ',refBexPier.getI()
# print 'J= ',refBexPier.getJ()
# print 'K= ',refBexPier.getK()

aBex= geom.Pos3d(35.9086283257252, 81.9222972209748, 0.0) #Bex abutment.
vABex= -1.0*(geom.Pos3d(49.7860089786179, 83.8917781158251, 0.0)-geom.Pos3d(22.335356708299, 80.077034442144, 0.0)).normalizado()
O= aBex+geom.Vector3d(0.0, 0.0, 17.099)
VI= -4.5*vABex+geom.Vector3d(0.0,0.0,17.008-O.z)
VJ= geom.Vector3d(-vABex.y,vABex.x,0.0)
refBexAbutment= geom.Ref3d3d(O,VI,-VJ)
# print 'O= ', O
# print 'P1= ', O+VI
# print 'I= ',refBexAbutment.getI()
# print 'J= ',refBexAbutment.getJ()
# print 'K= ',refBexAbutment.getK()

referenceOffset= geom.Vector3d(0.0,0.0,-asphaltThickness+beamDepth+deckDepth)
refMassongexAbutment.Org+= referenceOffset
refMassongexPier.Org+= referenceOffset
MassongexPierOffset= refMassongexPier.getCooGlobales(geom.Vector3d(0.0,0.25,0.0))
refMassongexPierA= geom.Ref3d3d(refMassongexPier.Org-MassongexPierOffset,refMassongexPier.Trf)
refMassongexPierB= geom.Ref3d3d(refMassongexPier.Org+MassongexPierOffset,refMassongexPier.Trf)
refBexPier.Org+= referenceOffset
BexPierOffset= refBexPier.getCooGlobales(geom.Vector3d(0.0,0.25,0.0))
refBexPierA= geom.Ref3d3d(refBexPier.Org-BexPierOffset,refBexPier.Trf)
refBexPierB= geom.Ref3d3d(refBexPier.Org+BexPierOffset,refBexPier.Trf)
refBexAbutment.Org+= referenceOffset


print 'L1= ', pMassongex.distPos3d(aMassongex)
print 'L2= ', pMassongex.distPos3d(pBex)
print 'L3= ', pBex.distPos3d(aBex)
print 'vAMassongex= ', vAMassongex
print 'vPMassongex= ', vPMassongex
print 'vPBex= ', vPBex
print 'vABex= ', vABex

model= xc.FEProblem()
preprocessor=  model.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics3D(nodes)
points= preprocessor.getMultiBlockTopology.getPoints

def createPoints(refSys):
    retval= {}
    retval['beamCentroids']= []
    centroids= retval['beamCentroids']
    for p in beamCentroids:
        pGlobal= refSys.getPosGlobal(p)
        centroids.append(points.newPntFromPos3d(pGlobal))
    retval['beamBottoms']= []
    bottoms= retval['beamBottoms']
    for p in beamBottoms:
        pGlobal= refSys.getPosGlobal(p)
        bottoms.append(points.newPntFromPos3d(pGlobal))
    retval['beamSupports']= []
    supports= retval['beamSupports']
    for p in beamSupports:
        pGlobal= refSys.getPosGlobal(p)
        supports.append(points.newPntFromPos3d(pGlobal))
    retval['deckLines']= []
    deck= retval['deckLines']
    for p in deckLines:
        pGlobal= refSys.getPosGlobal(p)
        deck.append(points.newPntFromPos3d(pGlobal))
    return retval
       

deckSurfaces= preprocessor.getSets.defSet("deckSurfaces")
def createDeckSurfaces(posA,posB):
    pointsA= posA['deckLines']
    pointsB= posB['deckLines']
    sz= len(pointsA)
    for i in range(0,sz-1):
      deckSurfaces.getSurfaces.append(surfaces.newQuadSurfacePts(pointsA[i].tag,pointsA[i+1].tag,pointsB[i+1].tag,pointsB[i].tag))

beamSurfaces= list()
beamLinesType4= preprocessor.getSets.defSet("beamLinesType4")
beamLinesType5= preprocessor.getSets.defSet("beamLinesType5")
beamLinesType6= preprocessor.getSets.defSet("beamLinesType6")
pairedLines= list()
def createBeamSurfaces(posA,posB):
    pointsDeckA= posA['deckLines']
    pointsBeamsA= posA['beamCentroids']
    pointsDeckB= posB['deckLines']
    pointsBeamsB= posB['beamCentroids']
    sz= len(pointsDeckA)
    for i in range(0,sz-2):
        pointDeckA= pointsDeckA[i+1]
        pointDeckB= pointsDeckB[i+1]
        pointBeamA= pointsBeamsA[i]
        pointBeamB= pointsBeamsB[i]
        s= surfaces.newQuadSurfacePts(pointDeckA.tag,pointBeamA.tag,pointBeamB.tag,pointDeckB.tag)
        deckLine= preprocessor.getMultiBlockTopology.getLineWithEndPoints(pointDeckA.tag,pointDeckB.tag)
        beamLine= preprocessor.getMultiBlockTopology.getLineWithEndPoints(pointBeamA.tag,pointBeamB.tag)
        if(i==0):
            beamLinesType4.getLines.append(beamLine)
        elif(i==7):
            beamLinesType5.getLines.append(beamLine)
        else:
            beamLinesType6.getLines.append(beamLine)
        beamSurfaces.append(s)
        pairedLines.append((beamLine,deckLine))
    
abutmentLegLines= preprocessor.getSets.defSet("abutmentLegLines")
abutmentBraceLines= preprocessor.getSets.defSet("abutmentBraceLines")
def createLegLinesAbutment(pos):
    pointsBeams= pos['beamCentroids']
    supportsBeams= pos['beamSupports']
    yVector= -(pointsBeams[-1].getPos-pointsBeams[0].getPos)
    xVector= yVector.cross(geom.Vector3d(0,0,1))
    #print 'xVector= ', xVector, ' yVector= ', yVector
    sz= len(pointsBeams)
    for i in range(0,sz):
        legLine= lines.newLine(pointsBeams[i].tag,supportsBeams[i].tag)
        legLine.setProp("orientation",[xc.Vector([xVector.x,xVector.y,xVector.z]),xc.Vector([yVector.x,yVector.y,yVector.z])])
        abutmentLegLines.getLines.append(legLine)
    for i in range(0,sz-1):
        abutmentBraceLines.getLines.append(lines.newLine(pointsBeams[i].tag,pointsBeams[i+1].tag))

pierSurfaces= preprocessor.getSets.defSet("pierSurfaces")
def createPier(posPier,foundationLevel):
    offset= geom.Vector3d(0.0,0.0,beamDepth+deckDepth/2.0+bearingThickness)
    deckPoints= posPier['deckLines']
    supportPoints= list()
    bottomPoints= list()
    for p in deckPoints:
        supportPoint= p.getPos-offset
        supportPoints.append(points.newPntFromPos3d(supportPoint))
        bottomPoint= geom.Pos3d(supportPoint.x,supportPoint.y,foundationLevel)
        bottomPoints.append(points.newPntFromPos3d(bottomPoint))
    sz= len(supportPoints)
    for i in range(0,sz-1):
        pierSurfaces.getSurfaces.append(surfaces.newQuadSurfacePts(supportPoints[i].tag,bottomPoints[i].tag,bottomPoints[i+1].tag,supportPoints[i+1].tag))
    return supportPoints,bottomPoints

pierLegLines= preprocessor.getSets.defSet("pierLegLines")
corbelLines= preprocessor.getSets.defSet("corbelLines")
pierBraceLines= preprocessor.getSets.defSet("pierBraceLines")
pairedPoints= []
def createLegLinesPier(pos,pierSupports):
    pointsBeams= pos['beamCentroids']
    supportsBeams= pos['beamSupports']
    sz= len(pointsBeams)
    for i in range(0,sz):
        pierLegLines.getLines.append(lines.newLine(pointsBeams[i].tag,supportsBeams[i].tag))
        dupPoint= points.newPntFromPos3d(supportsBeams[i].getPos)
        corbelLine= lines.newLine(dupPoint.tag,pierSupports[i+1].tag)
        tgVector= corbelLine.getTang(0.0)
        xVector= geom.Vector3d(tgVector[0],tgVector[1],tgVector[2])
        yVector= geom.Vector3d(0,0,1).cross(xVector)
        orientation= [xc.Vector([xVector.x,xVector.y,xVector.z]),xc.Vector([yVector.x,yVector.y,yVector.z])]
        pairedPoints.append((supportsBeams[i],dupPoint,orientation))
        corbelLines.getLines.append(corbelLine)
    for i in range(0,sz-1):
        pierBraceLines.getLines.append(lines.newLine(pointsBeams[i].tag,pointsBeams[i+1].tag))


MassongexAbutment= createPoints(refMassongexAbutment)
MassongexPierA= createPoints(refMassongexPierA)
MassongexPier= createPoints(refMassongexPier)
MassongexPierB= createPoints(refMassongexPierB)
BexPierA= createPoints(refBexPierA)
BexPier= createPoints(refBexPier)
BexPierB= createPoints(refBexPierB)
BexAbutment= createPoints(refBexAbutment)

surfaces= preprocessor.getMultiBlockTopology.getSurfaces
createDeckSurfaces(MassongexAbutment,MassongexPierA)
createDeckSurfaces(MassongexPierA,MassongexPierB)
createDeckSurfaces(MassongexPierB,BexPierA)
createDeckSurfaces(BexPierA,BexPierB)
createDeckSurfaces(BexPierB,BexAbutment)

createBeamSurfaces(MassongexAbutment,MassongexPierA)
createBeamSurfaces(MassongexPierA,MassongexPierB)
createBeamSurfaces(MassongexPierB,BexPierA)
createBeamSurfaces(BexPierA,BexPierB)
createBeamSurfaces(BexPierB,BexAbutment)

lines= preprocessor.getMultiBlockTopology.getLines
createLegLinesAbutment(MassongexAbutment)
createLegLinesAbutment(BexAbutment)

supportsPierMassongex, bottomPointsPierMassongex= createPier(MassongexPier,MassongexPierFoundationLevel)
supportsPierBex, bottomPointsPierBex= createPier(BexPier,BexPierFoundationLevel)
createLegLinesPier(MassongexPierA,supportsPierMassongex)
createLegLinesPier(MassongexPierB,supportsPierMassongex)
createLegLinesPier(BexPierA,supportsPierBex)
createLegLinesPier(BexPierB,supportsPierBex)

legLines= abutmentLegLines+pierLegLines

# Load regions.

stations= [refMassongexAbutment,refMassongexPier,refBexPier,refBexAbutment]

def createLaneAxisLines():
    retval= [geom.Polilinea3d(),geom.Polilinea3d(),geom.Polilinea3d()]
    for s in stations:
        index= 0
        for p in laneAxisLines:
            pGlobal= s.getPosGlobal(p)
            retval[index].agregaVertice(pGlobal)
            index+= 1
    return retval

def createLaneRegionsPolygons():
    lines= [geom.Polilinea3d(),geom.Polilinea3d(),geom.Polilinea3d(),geom.Polilinea3d()]
    for s in stations:
        index= 0
        for p in laneLines:
            pGlobal= s.getPosGlobal(p)
            lines[index].agregaVertice(pGlobal)
            index+= 1
    polygons= [geom.Poligono2d(),geom.Poligono2d(),geom.Poligono2d()]
    sz= len(stations)
    for i in range(0,sz):
        for j in [0,1,2]:
          pt= lines[j][i]
          polygons[j].agregaVertice(geom.Pos2d(pt.x,pt.y))
    for i in range(0,sz):
        j= sz-i-1
        for k in [1,2,3]:
          pt= lines[k][j]
          polygons[k-1].agregaVertice(geom.Pos2d(pt.x,pt.y))
    return polygons

    

pointStations= [MassongexAbutment, MassongexPierA, MassongexPierB, BexPierA, BexPierB, BexAbutment]

def getEdgeLines():
    retval= []
    ptsEdge0= list()
    ptsEdge1= list()
    for s in pointStations:
        pts= s['deckLines']
        ptsEdge0.append(pts[0])
        ptsEdge1.append(pts[-1])
    sz= len(pointStations)
    for i in range(0,sz-1):
        edge0= preprocessor.getMultiBlockTopology.getLineWithEndPoints(ptsEdge0[i].tag,ptsEdge0[i+1].tag)
        edge1= preprocessor.getMultiBlockTopology.getLineWithEndPoints(ptsEdge1[i].tag,ptsEdge1[i+1].tag)
        retval.append(edge0)
        retval.append(edge1)
    return retval

def getTransverseSlopes():
    retval= []
    ptsEdge0= list()
    ptsEdge1= list()
    for s in [MassongexAbutment, MassongexPier, BexPier, BexAbutment]:
        pts= s['deckLines']
        ptA= pts[0].getPos
        ptB= pts[-1].getPos
        retval.append((ptA-ptB).normalizado())
    return retval

laneAxisLines= createLaneAxisLines()
laneRegions= createLaneRegionsPolygons()
edgeLines= getEdgeLines()
transverseSlopes= getTransverseSlopes()


# for l in laneRegions:
#     print l.getArea()
# for e in edgeLines:
#     print e.getLong()

xcTotalSet= preprocessor.getSets.getSet('total')

