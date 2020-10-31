# -*- coding: utf-8 -*-

# Sets of lines, edges of the deck slabs, to be «glued»  

lin2Glue01_rg=gm.IJKRange((0,1,0),(lastXpos,1,lastZpos))
lin2Glue01_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue01_rg,setName='lin2Glue01_kps')
lin2Glue01=sets.get_lines_on_points(setPoints=lin2Glue01_kps,setLinName='lin2Glue01',onlyIncluded=True)

lin2Glue02_rg=gm.IJKRange((0,2,0),(lastXpos,2,lastZpos))
lin2Glue02_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue02_rg,setName='lin2Glue02_kps')
lin2Glue02=sets.get_lines_on_points(setPoints=lin2Glue02_kps,setLinName='lin2Glue02',onlyIncluded=True)

lin2Glue03_rg=gm.IJKRange((0,3,0),(lastXpos,3,lastZpos))
lin2Glue03_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue03_rg,setName='lin2Glue03_kps')
lin2Glue03=sets.get_lines_on_points(setPoints=lin2Glue03_kps,setLinName='lin2Glue03',onlyIncluded=True)

lin2Glue04_rg=gm.IJKRange((0,4,0),(lastXpos,4,lastZpos))
lin2Glue04_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue04_rg,setName='lin2Glue04_kps')
lin2Glue04=sets.get_lines_on_points(setPoints=lin2Glue04_kps,setLinName='lin2Glue04',onlyIncluded=True)

lin2Glue05_rg=gm.IJKRange((0,5,0),(lastXpos,5,lastZpos))
lin2Glue05_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue05_rg,setName='lin2Glue05_kps')
lin2Glue05=sets.get_lines_on_points(setPoints=lin2Glue05_kps,setLinName='lin2Glue05',onlyIncluded=True)

lin2Glue06_rg=gm.IJKRange((0,6,0),(lastXpos,6,lastZpos))
lin2Glue06_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue06_rg,setName='lin2Glue06_kps')
lin2Glue06=sets.get_lines_on_points(setPoints=lin2Glue06_kps,setLinName='lin2Glue06',onlyIncluded=True)

lin2Glue07_rg=gm.IJKRange((0,7,0),(lastXpos,7,lastZpos))
lin2Glue07_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue07_rg,setName='lin2Glue07_kps')
lin2Glue07=sets.get_lines_on_points(setPoints=lin2Glue07_kps,setLinName='lin2Glue07',onlyIncluded=True)

lin2Glue08_rg=gm.IJKRange((0,8,0),(lastXpos,8,lastZpos))
lin2Glue08_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue08_rg,setName='lin2Glue08_kps')
lin2Glue08=sets.get_lines_on_points(setPoints=lin2Glue08_kps,setLinName='lin2Glue08',onlyIncluded=True)

lin2Glue09_rg=gm.IJKRange((0,9,0),(lastXpos,9,lastZpos))
lin2Glue09_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue09_rg,setName='lin2Glue09_kps')
lin2Glue09=sets.get_lines_on_points(setPoints=lin2Glue09_kps,setLinName='lin2Glue09',onlyIncluded=True)

lin2Glue10_rg=gm.IJKRange((0,10,0),(lastXpos,10,lastZpos))
lin2Glue10_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue10_rg,setName='lin2Glue10_kps')
lin2Glue10=sets.get_lines_on_points(setPoints=lin2Glue10_kps,setLinName='lin2Glue10',onlyIncluded=True)

lin2Glue11_rg=gm.IJKRange((0,11,0),(lastXpos,11,lastZpos))
lin2Glue11_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue11_rg,setName='lin2Glue11_kps')
lin2Glue11=sets.get_lines_on_points(setPoints=lin2Glue11_kps,setLinName='lin2Glue11',onlyIncluded=True)

lin2Glue12_rg=gm.IJKRange((0,12,0),(lastXpos,12,lastZpos))
lin2Glue12_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue12_rg,setName='lin2Glue12_kps')
lin2Glue12=sets.get_lines_on_points(setPoints=lin2Glue12_kps,setLinName='lin2Glue12',onlyIncluded=True)

lin2Glue13_rg=gm.IJKRange((0,13,0),(lastXpos,13,lastZpos))
lin2Glue13_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue13_rg,setName='lin2Glue13_kps')
lin2Glue13=sets.get_lines_on_points(setPoints=lin2Glue13_kps,setLinName='lin2Glue13',onlyIncluded=True)

lin2Glue14_rg=gm.IJKRange((0,14,0),(lastXpos,14,lastZpos))
lin2Glue14_kps=gridDeck.getSetPntRange(ijkRange=lin2Glue14_rg,setName='lin2Glue14_kps')
lin2Glue14=sets.get_lines_on_points(setPoints=lin2Glue14_kps,setLinName='lin2Glue14',onlyIncluded=True)


#Glue the lines.
lines2Glue= [(lin2Glue01, lin2Glue02), (lin2Glue03, lin2Glue04), (lin2Glue05, lin2Glue06), (lin2Glue07, lin2Glue08), (lin2Glue09, lin2Glue10), (lin2Glue11, lin2Glue12), (lin2Glue13, lin2Glue14)]
gluedDOFs= xc.ID([0,1,2]) #Degrees of freedom to "glue".

# def defineConnection(prep,nodes,connectionMaterial,glueMaterial,direction1,direction2):
#     elems= prep.getElementHandler
#     elems.dimElem= prep.getNodeHandler.dimSpace # space dimension.
#     if(elems.dimElem!=3):
#       lmsg.warning("Not a three-dimensional space.")
#     elems.defaultMaterial= connectionMaterial.name
#     zl= elems.newElement("ZeroLength",xc.ID([nodes[0].tag,nodes[1].tag]))
#     zl.setupVectors(xc.Vector([direction1.x,direction1.y,direction1.z]),xc.Vector([direction2.x,direction2.y,direction2.z]))
#     zl.clearMaterials()
#     zl.setMaterial(0,connectionMaterial.name)
#     zl.setMaterial(1,glueMaterial.name)
#     zl.setMaterial(2,glueMaterial.name)
#     return zl.tag

# glueK= 1e6
# #connectionMaterial= typical_materials.defElastNoTensMaterial(prep, "connectionMaterial",glueK)
# connectionMaterial= typical_materials.defElasticMaterial(prep, "connectionMaterial",1e3)
# glueMaterial= typical_materials.defElasticMaterial(prep, "glueMaterial",glueK)

lini=1
for pair in lines2Glue:
#    print 'lines ',lini,',',lini+1
    nodSet0= pair[0].getNodes
    for l in pair[0].getLines:
        ln=l.nodes
        for n in ln:
            nodSet0.append(n)
    nodSet1= pair[1].getNodes
    for l in pair[1].getLines:
        ln=l.nodes
        for n in ln:
            nodSet1.append(n)
    # print nodSet0, nodSet1
    # print 'nnod set0= ',nodSet0.size, 'nnod set1= ',nodSet1.size 
    for n0 in nodSet0:
        pos0= n0.getInitialPos3d #Position of first node.
#        print pos0.x,pos0.y,pos0.z
        n1= nodSet1.getNearestNode(pos0) #Second node.
        pos1= n1.getInitialPos3d
        d= pos1.dist(pos0) #Distance between nodes.
#        print pos1.x,pos1.y,pos1.z
        if d<50*gapSl:
#            print d
            s= geom.LineSegment3d(pos0,pos1)
            newPos= s.getCenterOfMass() #Position for the new nodes.
            #print pos0.dist(newPos),pos1.dist(newPos)
            newNode0= nodes.newNodeXYZ(newPos.x,newPos.y, newPos.z)
            rigidBeam0= prep.getBoundaryCondHandler.newRigidBeam(n0.tag,newNode0.tag)
            newNode1= nodes.newNodeXYZ(newPos.x,newPos.y, newPos.z)
            rigidBeam1= prep.getBoundaryCondHandler.newRigidBeam(n1.tag,newNode1.tag)
            sCoo= geom.CooSysRect3d3d(pos0,pos1)
            glue= prep.getBoundaryCondHandler.newEqualDOF(newNode0.tag,newNode1.tag,gluedDOFs)
            #zl= defineConnection(prep,[newNode0,newNode1],connectionMaterial,glueMaterial,sCoo.getI(),sCoo.getJ())
    lini=lini+2





# lini=1
# for pair in lines2Glue:
#     print 'lines ',lini,',',lini+1
#     for i in range(pair[0].getLines.size):
#         line0= pair[0].getLines[i]
#         line1= pair[1].getLines[i]
#         for n0 in line0.nodes:
#             pos0= n0.getInitialPos3d #Position of first node.
#             n1= line1.getNearestNode(pos0) #Second node.
#             pos1= n1.getInitialPos3d
#             d= pos1.dist(pos0) #Distance between nodes.
#             print d
#             s= geom.LineSegment3d(pos0,pos1)
#             newPos= s.getCenterOfMass() #Position for the new nodes.
#             #print pos0.dist(newPos),pos1.dist(newPos)
#             newNode0= nodes.newNodeXYZ(newPos.x,newPos.y, newPos.z)
#             rigidBeam0= prep.getBoundaryCondHandler.newRigidBeam(n0.tag,newNode0.tag)
#             newNode1= nodes.newNodeXYZ(newPos.x,newPos.y, newPos.z)
#             rigidBeam1= prep.getBoundaryCondHandler.newRigidBeam(n1.tag,newNode1.tag)
#             glue= prep.getBoundaryCondHandler.newEqualDOF(newNode0.tag,newNode1.tag,gluedDOFs)
#     lini=lini+2

