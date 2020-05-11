# -*- coding: utf-8 -*-
from __future__ import division
import math

#Pile data
#nXpile=2 #number of piles in X direction
distXpile=4 #distance between piles in X direction
#nYpile=2 #number of piles in Y direction
distYpile=4 #distance between piles in Y direction

pileDiam=1  #pile diameter
pileLength=20   #pile length
pileType='endBearing' #type of pile 'endBearing' or 'friction'
soils=[(-1.5,'sandy',1e6),(-5,'sandy',2e6),(-15,'sandy',10e6),(-100,'sandy',20e6)] #Properties of the sandy
# soils [(zBottom,type, nh), ...]  where 'zBottom' is the global Z coordinate
#           of the bottom level of the soil and 'nh' [Pa/m] is the coefficient 
#           corresponding to the compactness of the sandy soil.
pileConcr=EHE_materials.HA25  #pile concrete
LeqPile=round(math.pi**0.5*pileDiam/2.,3)
bearingCapPile=22e3 #total bearing capacity of the pile [N]

#Pile cap data
Hpilecap=2 #pile-cap thickness

# Pile material and section
pileConcrProp=tm.MaterialData(name='pileConcrProp',E=pileConcr.Ecm(),nu=pileConcr.nuc,rho=pileConcr.density())
geomSectPile=sectpr.RectangularSection(name='geomSectPile',b=LeqPile,h=LeqPile)
pile_mat=tm.BeamMaterialData(name='pile_mat', section=geomSectPile, material=pileConcrProp)
pile_mat.setupElasticShear3DSection(preprocessor=prep)
piles=prep.getSets.defSet('piles')

#Pile-cap and piles column 1
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
(struts1,ties1,topNodPiles)=gen_pile_cap_2columns_3X2Ypiles(preprocessor=prep,nodCols=[nPil1,nPil2],distXpile=distXpile,distYpile=distYpile,Hpilecap=Hpilecap,nameSetStruts='struts1',nameSetTies='ties1')

piles1=gen_piles(preprocessor,topNodPiles,pileLength,pile_mat,eSize,pileType,bearingCapPile,soils,nameSetPiles='piles1')

#Pile-cap and piles column 2
indy=1
indx=0
j=gridPil.gridCoo[1].index(yPil[indy])
i=gridPil.gridCoo[0].index(xPil[indx])
k=gridPil.gridCoo[2].index(zPil[indy][0])
p=gridPil.getPntGrid((i,j,k))
nPil1=p.getNode()
indx=1
j=gridPil.gridCoo[1].index(yPil[indy])
i=gridPil.gridCoo[0].index(xPil[indx])
k=gridPil.gridCoo[2].index(zPil[indy][0])
p=gridPil.getPntGrid((i,j,k))
nPil2=p.getNode()

execfile(path_foundation+'pile_foundation.py')
(struts2,ties2,topNodPiles)=gen_pile_cap_2columns_3X2Ypiles(preprocessor=prep,nodCols=[nPil1,nPil2],distXpile=distXpile,distYpile=distYpile,Hpilecap=Hpilecap,nameSetStruts='struts2',nameSetTies='ties2')

piles2=gen_piles(preprocessor,topNodPiles,pileLength,pile_mat,eSize,pileType,bearingCapPile,soils,nameSetPiles='piles2')

#Pile-cap and piles column 3
indy=2
indx=0
j=gridPil.gridCoo[1].index(yPil[indy])
i=gridPil.gridCoo[0].index(xPil[indx])
k=gridPil.gridCoo[2].index(zPil[indy][0])
p=gridPil.getPntGrid((i,j,k))
nPil1=p.getNode()
indx=1
j=gridPil.gridCoo[1].index(yPil[indy])
i=gridPil.gridCoo[0].index(xPil[indx])
k=gridPil.gridCoo[2].index(zPil[indy][0])
p=gridPil.getPntGrid((i,j,k))
nPil2=p.getNode()

execfile(path_foundation+'pile_foundation.py')
(struts3,ties3,topNodPiles)=gen_pile_cap_2columns_3X2Ypiles(preprocessor=prep,nodCols=[nPil1,nPil2],distXpile=distXpile,distYpile=distYpile,Hpilecap=Hpilecap,nameSetStruts='struts3',nameSetTies='ties3')

piles3=gen_piles(preprocessor,topNodPiles,pileLength,pile_mat,eSize,pileType,bearingCapPile,soils,nameSetPiles='piles3')

# Sets
ties=ties1+ties2+ties3
struts=struts1+struts2+struts3
piles=piles1+piles2+piles3

#añadir la acción del peso propio del encepado y del terreno que gravita sobre él
