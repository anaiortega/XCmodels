# -*- coding: utf-8 -*-

ft2m=0.3048
in2m=0.0254

#Geometry
wallThBasement=round(8*in2m,2)
wallThFirstFloor=round(8*in2m,2)
wallLength=round((8+58+8)*ft2m+19.5*in2m,2)
Laux=round((wallLength-(13+2*14)*ft2m-(3+2*8+2*4)*in2m)/2.,2)
LwallBasement=wallLength
LwallFirstFloor=round(wallLength-Laux,2)

yHall=round(5.5*ft2m,2)
xHall=round(-5.0*ft2m,2)
distXwalls=19*ft2m

yCantilv=round(-6.0*ft2m,2)
foundElev=round(-14*ft2m,2)
rampStartElev=round(-(2*ft2m+6*in2m),2)
rampEndElev=round(-(12*ft2m+8*in2m),2)
firstFloorElev=0
secondFloorElev=round(11*ft2m+4*in2m,2)

eSize= 0.35     #length of elements

xEastWall=0
xWestWall=distXwalls
#Materials
from materials.aci import ACI_materials as ACImat
concrete=ACImat.c4000
from materials.astm import ASTM_materials as ASTMmat
A992=ASTMmat.A992
# coordinates in global X,Y,Z axes for the grid generation

xList=[xHall,xEastWall,xWestWall]
xList.sort()

yList=[yCantilv,0,yHall,LwallFirstFloor,LwallBasement]
yList.sort()

zList=[foundElev,firstFloorElev,secondFloorElev]
zList.sort()
