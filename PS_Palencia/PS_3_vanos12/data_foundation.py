# -*- coding: utf-8 -*-
from __future__ import division
import math

#Pile data
#nXpile=2 #number of piles in X direction
distXpile=4 #distance between piles in X direction
#nYpile=2 #number of piles in Y direction
distYpile=4 #distance between piles in Y direction

#Pile cap data
Hpilecap=2 #pile-cap thickness
indy=0
indx=0
j=gridPil.gridCoo[1].index(yPil[indy])
i=gridPil.gridCoo[0].index(xPil[indx])
k=gridPil.gridCoo[2].index(zPil[indy][0])
p=gridPil.getPntGrid((i,j,k))
nPil1=p.getNode()
indy=0
indx=1
j=gridPil.gridCoo[1].index(yPil[indy])
i=gridPil.gridCoo[0].index(xPil[indx])
k=gridPil.gridCoo[2].index(zPil[indy][0])
p=gridPil.getPntGrid((i,j,k))
nPil2=p.getNode()


execfile(path_foundation+'pile_foundation.py')
(struts,ties)=gen_pile_found_2columns_3X2Ypiles(preprocessor=prep,nodCols=[nPil1,nPil2],distXpile=distXpile,distYpile=distYpile,Hpilecap=Hpilecap,nameSetStruts='struts',nameSetTies='ties')


#añadir la acción del peso propio del encepado y del terreno que gravita sobre él
