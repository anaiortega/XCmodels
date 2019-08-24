# -*- coding: utf-8 -*-
from __future__ import division

import math
from materials.ehe import EHE_materials

#Auxiliary data
 #Geometry
cantoZap=1.5
espCoronAlet=0.4
espMurEstr=1.35
anchoEstr=13.5-espCoronAlet
hMuri=8.4
hMurd=9.25
hMuret=1.35
Lpunt=1.8+0.5*espMurEstr
Lzap=7.4+0.5*espMurEstr
Lvoladzi=0
Hminvoladzi=0
Hmaxvoladzi=0
Lvoladzd=5.0
Hminvoladzd=0.5
Hmaxvoladzd=0.5+3.3
pendMurAlet=1/12.  #H:V

#Apoyos estribos
distNeopr=3  #distancia entre neoprenos
numNeopr=4   #número de aparatos de apoyo
# hNetoNeopr=48e-3 #espesor neto neopreno
# aNeopr=0.25       #dimensión y (sentido longitudinal) del neopreno
# bNeopr=0.40       #dimensión x (sentido transversal) del neopreno

#materials
concrete=EHE_materials.HA30
reinfSteel= EHE_materials.B500S

#excentricidad de los aparatos de apoyo respecto al plano medio del muro
excNeop=espMurEstr/2.-0.5

#Magnitudes derivadas
# Coord. x (transversal)
xAletaI=-anchoEstr/2.0
xNeop1=-1.5*distNeopr
xNeop2=-0.5*distNeopr
xNeop3=0.5*distNeopr
xNeop4=1.5*distNeopr
xAletaD=anchoEstr/2.0
xCoordNeopr=[xNeop1,xNeop2,xNeop3,xNeop4]

#Coord. Y (longitudinal)
yPuntera=-Lpunt
yMurEstr=0
yZap=round(Lzap,2)
yVoladzi=round(Lzap+Lvoladzi,2)
yVoladzd=round(Lzap+Lvoladzd,2)
yVoladz=max(yVoladzi,yVoladzd)

#Coord. Z (vertical)
zZap=0
zMuri=round(cantoZap/2.+hMuri,2)
zAleti=round(zMuri+hMuret,2)
zMurd=round(cantoZap/2.+hMurd,2)
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

#ángulo que forman muros laterales y aletas con el plano ortogonal al muro del
#estribo
angMuri=30
angMurd=-30
print 'angmuri=', angMuri

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


#peso propio
grav=9.81 #Gravity acceleration (m/s2)
pespConcr=grav*concrete.density() #peso específico hormigón armado [N/m3]

K30=10e6        #(N/m3)
Kcuadr=(K30+0.3)/Lzap
Krectang=2/3.*Kcuadr*(1+Lzap/(2*anchoEstr))
Kbalasto=Krectang                  #coef. balasto (N/m3)
# empuje del terreno
fi_terr=30                            #ángulo de rozamiento interno
K0=1-math.sin(math.radians(fi_terr))  #coeficiente de empuje al reposo
densrell=2e3                  #densidad del relleno (kg/m3)
zGround=(zAleti+zAletd)/2.0
qunifTerr=10e3 #carga uniforme sobre el terreno [N/m2]

#
eSize= 0.4     #length of elements

# coordinates in global X,Y,Z axes for the grid generation
#xinterm1=round((xViaFict1+xArranqVoladz)/2.,2)
xList=[xAletaI,xNeop1,xNeop2,xNeop3,xNeop4,xAletaD]
yList=[yPuntera,yMurEstr,yZap,yVoladz]
zList=[zZap,zRefrz,zArrVoladz,zMur,zAlet]

#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

XYZLists=(xList,yList,zList)

#ranges coordinates
Xmurestr=(xAletaI,xAletaD)
Xaleti=(xAletaI,xAletaI)
Xaletd=(xAletaD,xAletaD)

Yzap=(yPuntera,yZap)
Ymurestr=(yMurEstr,yMurEstr)
Yalet=(yMurEstr,yZap)
Yvoladz=(yZap,yVoladz)

zZ1=(zZap,zRefrz)
zZ2mur=(zRefrz,zMur)
zZ2alet=(zRefrz,zArrVoladz)
zZ3alet=(zArrVoladz,zAlet)

#Cargas tablero
#execfile('../../PS_101_3_curvo/calcReact/results.py')

