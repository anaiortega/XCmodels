# -*- coding: utf-8 -*-
from __future__ import division
import math

#Pile data
nXpile=2 #number of piles in X direction
distXpile=4 #distance between piles in X direction
nYpile=2 #number of piles in Y direction
distYpile=4 #distance between piles in Y direction

#Pile cap data
Hpilecap=2 #pile-cap thickness
indy=0
indx=0
j=gridPil.gridCoo[1].index(yPil[indy])
i=gridPil.gridCoo[0].index(xPil[indx])
k=gridPil.gridCoo[2].index(zPil[indy][0])
p=gridPil.getPntGrid((i,j,k))
nPil=p.getNode()
xNodPil=nPil.get3dCoo[0]
yNodPil=nPil.get3dCoo[1]
zNodPil=nPil.get3dCoo[2]

struts=prep.getSets.defSet('struts')
ties=prep.getSets.defSet('ties')
Lx=distXpile/2.
Ly=distYpile/2.

nod1= nodes.newNodeXYZ(xNodPil-Lx,yNodPil-Ly,zNodPil-Hpilecap)
nod2= nodes.newNodeXYZ(xNodPil+Lx,yNodPil-Ly,zNodPil-Hpilecap)
nod3= nodes.newNodeXYZ(xNodPil+Lx,yNodPil+Ly,zNodPil-Hpilecap)
nod4= nodes.newNodeXYZ(xNodPil-Lx,yNodPil+Ly,zNodPil-Hpilecap)

# Constraints
#modelSpace.fixNode('FFF_000',nPil.tag)
modelSpace.fixNode('F00_000',nod1.tag)
modelSpace.fixNode('0F0_000',nod2.tag)
modelSpace.fixNode('F00_000',nod3.tag)
modelSpace.fixNode('0F0_000',nod4.tag)

#Elements
str1= modelSpace.setHugeTrussBetweenNodes(nPil.tag,nod1.tag)
str2= modelSpace.setHugeTrussBetweenNodes(nPil.tag,nod2.tag)
str3= modelSpace.setHugeTrussBetweenNodes(nPil.tag,nod3.tag)
str4= modelSpace.setHugeTrussBetweenNodes(nPil.tag,nod4.tag)

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


struts.fillDownwards()
ties.fillDownwards()


#añadir la acción del peso propio del encepado y del terreno que gravita sobre él
