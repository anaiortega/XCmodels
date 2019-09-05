def gen_pile_found_1column_4piles(preprocessor,nodCol,distXpile,distYpile,Hpilecap,nameSetStruts,nameSetTies):
    '''Generate pile cap for one column with a pile foundation of 4 piles. Return the two sets of elements generated (struts and ties)

    :param preprocessor: preprocessor
    :param nodCol: node of the column
    :param distXpile: distance between piles in X direction
    :param distYpile: distance between piles in Y direction
    :param Hpilecap: pile-cap height
    :param nameSetStruts: name of the set of struts
    :param nameSetTies: name of the set of ties
    '''
    
    (xNodCol,yNodCol,zNodCol)=(nodCol.get3dCoo[0],nodCol.get3dCoo[1],nodCol.get3dCoo[2])
    struts=preprocessor.getSets.defSet(nameSetStruts)
    ties=preprocessor.getSets.defSet(nameSetTies)
    Lx=distXpile/2.
    Ly=distYpile/2.

    nod1= nodes.newNodeXYZ(xNodCol-Lx,yNodCol-Ly,zNodCol-Hpilecap)
    nod2= nodes.newNodeXYZ(xNodCol+Lx,yNodCol-Ly,zNodCol-Hpilecap)
    nod3= nodes.newNodeXYZ(xNodCol+Lx,yNodCol+Ly,zNodCol-Hpilecap)
    nod4= nodes.newNodeXYZ(xNodCol-Lx,yNodCol+Ly,zNodCol-Hpilecap)

    #Elements
    str1= modelSpace.setHugeTrussBetweenNodes(nodCol.tag,nod1.tag)
    str2= modelSpace.setHugeTrussBetweenNodes(nodCol.tag,nod2.tag)
    str3= modelSpace.setHugeTrussBetweenNodes(nodCol.tag,nod3.tag)
    str4= modelSpace.setHugeTrussBetweenNodes(nodCol.tag,nod4.tag)

    struts.getElements.append(str1)
    struts.getElements.append(str2)
    struts.getElements.append(str3)
    struts.getElements.append(str4)

    tie1= modelSpace.setHugeTrussBetweenNodes(nod1.tag,nod2.tag)
    tie2= modelSpace.setHugeTrussBetweenNodes(nod2.tag,nod3.tag)
    tie3= modelSpace.setHugeTrussBetweenNodes(nod3.tag,nod4.tag)
    tie4= modelSpace.setHugeTrussBetweenNodes(nod4.tag,nod1.tag)

    ties.getElements.append(tie1)
    ties.getElements.append(tie2)
    ties.getElements.append(tie3)
    ties.getElements.append(tie4)

    # Constraints
    modelSpace.fixNode('FFF_000',nodCol.tag)
    modelSpace.fixNode('F00_000',nod1.tag)
    modelSpace.fixNode('0F0_000',nod2.tag)
    modelSpace.fixNode('F00_000',nod3.tag)
    modelSpace.fixNode('0F0_000',nod4.tag)

    struts.fillDownwards()
    ties.fillDownwards()
    return struts,ties

def gen_pile_found_2columns_3X2Ypiles(preprocessor,nodCols,distXpile,distYpile,Hpilecap,nameSetStruts,nameSetTies):
    '''Generate pile cap for one column with a pile foundation of 3 piles in X direction and 2 piles in Y direction. Return the two sets of elements generated (struts and ties)

    :param preprocessor: preprocessor
    :param nodCols: [nodeCol1,nodeCol2] nodes of columns 1 and 2 where X 
                  coordinate of node 1 is less than X coord.of node 2
    :param distXpile: distance between piles in X direction
    :param distYpile: distance between piles in Y direction
    :param Hpilecap: pile-cap height
    :param nameSetStruts: name of the set of struts
    :param nameSetTies: name of the set of ties
    '''
    nodCol1=nodCols[0]
    nodCol2=nodCols[1]
    (xCent,yCent,zCent)=((nodCol1.get3dCoo[0]+nodCol2.get3dCoo[0])/2.,
                         (nodCol1.get3dCoo[1]+nodCol2.get3dCoo[1])/2.,
                         nodCol1.get3dCoo[2])
    struts=preprocessor.getSets.defSet(nameSetStruts)
    ties=preprocessor.getSets.defSet(nameSetTies)
    Lx=distXpile
    Ly=distYpile/2.

    nod1= nodes.newNodeXYZ(xCent-Lx,yCent-Ly,zCent-Hpilecap)
    nod2= nodes.newNodeXYZ(xCent,yCent-Ly,zCent-Hpilecap)
    nod3= nodes.newNodeXYZ(xCent+Lx,yCent-Ly,zCent-Hpilecap)
    nod4= nodes.newNodeXYZ(xCent+Lx,yCent+Ly,zCent-Hpilecap)
    nod5= nodes.newNodeXYZ(xCent,yCent+Ly,zCent-Hpilecap)
    nod6= nodes.newNodeXYZ(xCent-Lx,yCent+Ly,zCent-Hpilecap)

    #Elements
    str1= modelSpace.setHugeTrussBetweenNodes(nodCol1.tag,nod1.tag)
    str2= modelSpace.setHugeTrussBetweenNodes(nodCol1.tag,nod2.tag)
    str3= modelSpace.setHugeTrussBetweenNodes(nodCol1.tag,nod5.tag)
    str4= modelSpace.setHugeTrussBetweenNodes(nodCol1.tag,nod6.tag)

    str5= modelSpace.setHugeTrussBetweenNodes(nodCol2.tag,nod2.tag)
    str6= modelSpace.setHugeTrussBetweenNodes(nodCol2.tag,nod3.tag)
    str7= modelSpace.setHugeTrussBetweenNodes(nodCol2.tag,nod4.tag)
    str8= modelSpace.setHugeTrussBetweenNodes(nodCol2.tag,nod5.tag)

    struts.getElements.append(str1)
    struts.getElements.append(str2)
    struts.getElements.append(str3)
    struts.getElements.append(str4)
    struts.getElements.append(str5)
    struts.getElements.append(str6)
    struts.getElements.append(str7)
    struts.getElements.append(str8)

    tie1= modelSpace.setHugeTrussBetweenNodes(nod1.tag,nod2.tag)
    tie2= modelSpace.setHugeTrussBetweenNodes(nod2.tag,nod3.tag)
    tie3= modelSpace.setHugeTrussBetweenNodes(nod3.tag,nod4.tag)
    tie4= modelSpace.setHugeTrussBetweenNodes(nod4.tag,nod5.tag)
    tie5= modelSpace.setHugeTrussBetweenNodes(nod5.tag,nod6.tag)
    tie6= modelSpace.setHugeTrussBetweenNodes(nod6.tag,nod1.tag)
    tie7= modelSpace.setHugeTrussBetweenNodes(nod2.tag,nod5.tag)


    ties.getElements.append(tie1)
    ties.getElements.append(tie2)
    ties.getElements.append(tie3)
    ties.getElements.append(tie4)
    ties.getElements.append(tie5)
    ties.getElements.append(tie6)
    ties.getElements.append(tie7)

    # Constraints
    modelSpace.fixNode('FFF_000',nodCol1.tag)
    modelSpace.fixNode('FFF_000',nodCol2.tag)
    modelSpace.fixNode('F00_000',nod1.tag)
    modelSpace.fixNode('FF0_000',nod2.tag)
    modelSpace.fixNode('0F0_000',nod3.tag)
    modelSpace.fixNode('F00_000',nod4.tag)
    modelSpace.fixNode('FF0_000',nod5.tag)
    modelSpace.fixNode('0F0_000',nod6.tag)

    struts.fillDownwards()
    ties.fillDownwards()
    return struts,ties

