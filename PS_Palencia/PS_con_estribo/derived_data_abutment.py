# -*- coding: utf-8 -*-
from __future__ import division

#Magnitudes derivadas
# Coord. x (transversal)
xAletaI=-anchoEstr/2.0
xAletaD=anchoEstr/2.0
#Coord. Y (longitudinal)
yMurEstr=-excNeop
yPuntera=yMurEstr+Lpunt
yZap=yMurEstr-round(Lzap,2)
yVoladzi=yMurEstr-round(Lzap+Lvoladzi,2)
yVoladzd=yMurEstr-round(Lzap+Lvoladzd,2)
yVoladz=yMurEstr-max(yVoladzi,yVoladzd)

#Coord. Z (vertical)
zZap=-(hMuri+hMurd)/2.-cantoZap/2.-hNetoNeopr
zMuri=zZap+round(cantoZap/2.+hMuri,2)
zAleti=round(zMuri+hMuret,2)
zMurd=zZap+round(cantoZap/2.+hMurd,2)
zAletd=round(zMurd+hMuret,2)
zRefrz=round((zMuri+zMurd)/4.0,2)
if Lvoladzi >0:
    zMur=zMuri
    zAlet=zAleti
    zArrVoladz=zAleti-Hmaxvoladzi
else:
    zMur=zMurd
    zAlet=zAletd
    zArrVoladz=zAletd-Hmaxvoladzd
pteMurEstr=(zMurd-zMuri)/(xAletaD-xAletaI)
# espesores
def espZ1_Z2(zCoron,eCoron,pend,Z1,Z2):
    '''espesor medio del muro en vuelta entre cotas Z1 y Z2
    '''
    espZ1=eCoron+(zCoron-Z1)*pend
    espZ2=eCoron+(zCoron-Z2)*pend
    return (espZ1+espZ2)/2.0

espAletiZ1=espZ1_Z2(zAleti,espCoronAlet,pendMurAlet,0,zRefrz)
espAletiZ2=espZ1_Z2(zAleti,espCoronAlet,pendMurAlet,zRefrz,zArrVoladz)
espAletiZ3=espZ1_Z2(zAleti,espCoronAlet,pendMurAlet,zArrVoladz,zAleti)

espAletdZ1=espZ1_Z2(zAletd,espCoronAlet,pendMurAlet,0,zRefrz)
espAletdZ2=espZ1_Z2(zAletd,espCoronAlet,pendMurAlet,zRefrz,zArrVoladz)
espAletdZ3=espZ1_Z2(zAletd,espCoronAlet,pendMurAlet,zArrVoladz,zAletd)

# coordinates in global X,Y,Z axes for the grid generation
#xinterm1=round((xViaFict1+xArranqVoladz)/2.,2)
xListAbut=[xAletaI]+xNeopr+[xAletaD]
yListAbut=[yVoladz,yZap,yMurEstr,yPuntera]
zListAbut=[zZap,zRefrz,zArrVoladz,zMur,zAlet]

XYZListsAbut=(xListAbut,yListAbut,zListAbut)

#ranges coordinates
Xmurestr=(xAletaI,xAletaD)
Xaleti=(xAletaI,xAletaI)
Xaletd=(xAletaD,xAletaD)

Yzap=(yZap,yPuntera)
Ymurestr=(yMurEstr,yMurEstr)
Yalet=(yZap,yMurEstr)
Yvoladz=(yVoladz,yZap)

zZ1=(zZap,zRefrz)
zZ2mur=(zRefrz,zMur)
zZ2alet=(zRefrz,zArrVoladz)
zZ3alet=(zArrVoladz,zAlet)
