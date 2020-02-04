
from __future__ import division
from __future__ import print_function

import xc_base
import geom
import xc
from model import predefined_spaces
# Loads
from actions import load_cases as lcm
from actions import combinations as combs

def genMesh(modelSpace, plateSection, studSpacing, trussSpacing, trussLoad):
    pointHandler= modelSpace.preprocessor.getMultiBlockTopology.getPoints
    infPoints= list()
    supPoints= list()
    for i in range(0,14):
        x= i*studSpacing
        infPoints.append(pointHandler.newPntFromPos3d(geom.Pos3d(x,0.0,0.0)))
        supPoints.append(pointHandler.newPntFromPos3d(geom.Pos3d(x,plateSection.h,0.0)))

    lines= modelSpace.preprocessor.getMultiBlockTopology.getLines
    infSet= modelSpace.preprocessor.getSets.defSet("inf")
    infLines= list()
    p0= infPoints[0]
    for p in infPoints[1:]:
        l= lines.newLine(p0.tag,p.tag)
        infLines.append(l)
        infSet.getLines.append(l)
        p0= p
    supSet= modelSpace.preprocessor.getSets.defSet("sup")
    supLines= list()
    p0= supPoints[0]
    for p in supPoints[1:]:
        l= lines.newLine(p0.tag,p.tag)
        supLines.append(l)
        supSet.getLines.append(l)
        p0= p
    infSet.fillDownwards()
    supSet.fillDownwards()

    # Mesh
    section= plateSection.defElasticShearSection2d(modelSpace.preprocessor)
    trfs= modelSpace.preprocessor.getTransfCooHandler
    lin= trfs.newLinearCrdTransf2d("lin")
    seedElemHandler= modelSpace.preprocessor.getElementHandler.seedElemHandler
    seedElemHandler.defaultMaterial= plateSection.xc_material.name
    seedElemHandler.defaultTransformation= "lin"
    elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

    xcTotalSet= modelSpace.preprocessor.getSets.getSet("total")
    mesh= infSet.genMesh(xc.meshDir.I)
    infSet.fillDownwards()
    mesh= supSet.genMesh(xc.meshDir.I)
    supSet.fillDownwards()

    ## Loaded nodes.
    loadedNodes= list()
    pos= supPoints[0].getPos+geom.Vector3d(studSpacing/2.0,0,0) #Position of the first loaded node
    xLast= supPoints[-1].getPos.x
    while pos.x<xLast:
        n= supSet.getNearestNode(pos)
        loadedNodes.append(supSet.getNearestNode(pos))
        pos+= geom.Vector3d(trussSpacing,0.0,0.0)
    print('loaded nodes: ', len(loadedNodes))

    # Constraints
    supportedNodes= list()
    for p in infPoints:
        n= p.getNode()
        modelSpace.fixNode00F(n.tag)
        supportedNodes.append(n)

    for n in supSet.nodes:
        pos= n.getInitialPos3d
        nInf= infSet.getNearestNode(pos)
        modelSpace.constraints.newEqualDOF(nInf.tag,n.tag,xc.ID([1]))

    for p in supPoints[1:-1]:
        n= p.getNode()
        pos= n.getInitialPos3d
        nInf= infSet.getNearestNode(pos)
        modelSpace.constraints.newEqualDOF(nInf.tag,n.tag,xc.ID([0]))


    # Actions
    loadCaseManager= lcm.LoadCaseManager(modelSpace.preprocessor)
    loadCaseNames= ['totalLoad']
    loadCaseManager.defineSimpleLoadCases(loadCaseNames)

    # Total load.
    cLC= loadCaseManager.setCurrentLoadCase('totalLoad')
    for n in loadedNodes:
        n.newLoad(xc.Vector([0.0,-trussLoad,0.0]))

    return infSet, supSet, supportedNodes
