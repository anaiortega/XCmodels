# -*- coding: utf-8 -*-
from __future__ import division

import math
from materials.ehe import EHE_materials

#Auxiliary data
 #Geometry
LvanoCent=17
LvanosExtr=13
Ltablero=LvanoCent+2*LvanosExtr

anchoCalz=10.70
anchoTot=13.80
anchoAcera=(anchoTot-anchoCalz)/2.0   

#  losa
distEjesAlig=1.10  #distancia entre ejes de aligeramientos
diamAlig=0.8   #diámetro aligeramientos
lRectEqAlig=round(math.pi**0.5*diamAlig/2.,3)
numAlig=6      #número de aligeramientos
cantoLosa=1.15
maxCantoVoladz=0.5 #canto máximo del voladizo
minCantoVoladz=0.20
anchVoladz=2.85
anchLosaAlig=7.0
ladoCartab=0.55

espRiostrEstr=1.0

LriostrPil=2  #longitud del macizado sobre pilas
nDiafRP=3 #número de diafragmas a definir en la zona macizada sobre pilas

#  Pilas
distEjPilas=4.00
hTotPilas=15.0   #altura total
diamPilas=1.0
lRectEqPila=round(math.pi**0.5*diamPilas/2.,3)
hInfPilas=hTotPilas/2.0   #altura zona armado inferior
    
#Apoyos estribos
distNeopr=3  #distancia entre neoprenos
numNeopr=4   #número de aparatos de apoyo
xCoordNeopr=[-1.5*distNeopr,-0.5*distNeopr,0.5*distNeopr,1.5*distNeopr]
hNetoNeopr=48e-3 #espesor neto neopreno
aNeopr=0.25       #dimensión y (sentido longitudinal) del neopreno
bNeopr=0.40       #dimensión x (sentido transversal) del neopreno

#materials
concrete=EHE_materials.HA30
reinfSteel= EHE_materials.B500S
Gneopr=1000e3  #módulo de cortante del material elastomérico

# Cargas
grav=9.81     #[m/s2]
pav_inf=1150  #pavimento, valor inferior [N/m2]
pav_sup=1725  #pavimento, valor superior [N/m2]
Lbarrera=8e3  #barrera rígida [N/m]
Limposta=4e3  #imposta [N/m]
Lacera=round(4e3/anchoAcera,0)  #acera [N/m2]
Lantivand=1e3   #protección antivandálica [N/m]

qunifmax=9e3    #carga uniforme en vía virtual 1
qunifmin=2.5e3    #carga uniforme en resto
qunifacera=2.5e3    #carga uniforme en acera concomitante con cargas de tráfico

Qfrenado=476e3 #carga total de frenado a aplicar en via fictícea 1 [N]
QCentrif=0  #carga uniforme debida a la fuerza centrífuga [N/m2]
#  viento
qWpilas=2.56e3 #carga lineal viento sobre pilas [N/m]
qWTablero=8.05e3 #carga lineal viento sobre tablero [N/m]
qWTableroSCuso=7.0e3 #carga lineal viento sobre tablero actuando con SC uso [N/m]
coef_ocult=0.46

#Temperaturas
Tunif_contr=-16  #Incremento uniforme temperatura contracción ºC
Tunif_dilat=35   #Incremento uniforme temperatura dilatación ºC
Tfibrsup_cal=15  #Temperatura fibra superior más caliente (T fibra inf.=0ºC)
Tfibrsup_fria=-8  #Temperatura fibra superior más fría (T fibra inf.=0ºC)
coefDilat=1e-5    #coeficiente de dilatación térmica lineal del hormigón

Tunif_contr_neopr=-16-15  #Incremento uniforme temperatura contracción ºC
Tunif_dilat_neopr=35+15   #Incremento uniforme temperatura dilatación ºC


#Retracción
eps_retracc=-531e-6  #deformación por reracción

#Magnitudes derivadas
# espesores
espLosAlig=round((cantoLosa-lRectEqAlig)/2.,3)
espEntreAlig=round(distEjesAlig-lRectEqAlig,3)
espExtAlig=2*espEntreAlig
espVoladzMax=round((3*maxCantoVoladz+minCantoVoladz)/4.,3)
espVoladzMin=round((maxCantoVoladz+3*minCantoVoladz)/4.,3)
espPuntMaz=distEjesAlig/2.

hDistrQ=espLosAlig/2.+0.05


# Coord. x (transversal)
xBordeCalz=round(anchoCalz/2.0,2)
xViaFict1=round(xBordeCalz-3,2)
xViaFict2=round(xViaFict1-3,2)
xViaFict3=round(xViaFict2-3,2)

xBordeVoladz=round(anchoTot/2.0,2)
xMedVoladz=round(xBordeVoladz-anchVoladz/2.0,2)
xArranqVoladz=round(xBordeVoladz-anchVoladz,2)

xAlig1=1.1
xAlig2=2*1.1

xPila=round(distEjPilas/2.0,2)

#espesor diafragmas riostra pila
ValigRP=LriostrPil*numAlig*math.pi*diamAlig**2/4.
LdiafRP=2*xAlig2
espDiafRP=ValigRP/nDiafRP/LdiafRP/(cantoLosa-2*espLosAlig)

#Coord. Y (longitudinal)
yPil1=LvanosExtr
yminRiostrP1=yPil1-LriostrPil/2.0+espDiafRP/2.
ymaxRiostrP1=yPil1+LriostrPil/2.0-espDiafRP/2.
yPil2=LvanosExtr+LvanoCent
yminRiostrP2=yPil2-LriostrPil/2.0+espDiafRP/2.
ymaxRiostrP2=yPil2+LriostrPil/2.0-espDiafRP/2.
yEstr2=yPil2+LvanosExtr

#Coord. Z (vertical)
zLosInf=round(espLosAlig/2.0,3)
zLosSup=round(cantoLosa-espLosAlig/2.0,3)
zArrVoladz=round(cantoLosa-maxCantoVoladz/2.0,3)
zInfPilas=-hTotPilas+hInfPilas  #arranque tramo superior 
zInfPilAer=-hTotPilas+2  #aprox. 2 m enterrado


#peso propio
grav=9.81 #Gravity acceleration (m/s2)
pespConcr=grav*concrete.density() #peso específico hormigón armado [N/m3]

AvolExt=(minCantoVoladz+(maxCantoVoladz+minCantoVoladz)/2.0)/2.0*anchVoladz/2.0
AvolCent=(maxCantoVoladz+(maxCantoVoladz+minCantoVoladz)/2.0)/2.0*anchVoladz/2.0
ALos=2*(maxCantoVoladz+cantoLosa)/2.*ladoCartab+anchLosaAlig*cantoLosa
ALosAlig=ALos-numAlig*math.pi*diamAlig**2/4.
Apilas=math.pi*diamPilas**2/4.
AriostrEstr=cantoLosa*espRiostrEstr
qPPvolExt=pespConcr*AvolExt/(anchVoladz/2.)  #[N/m2]
qPPvolCent=pespConcr*AvolCent/(anchVoladz/2.)  #[N/m2]
qPPlos=pespConcr*ALos/(2*anchLosaAlig+2*ladoCartab) #[N/m2] a aplicar en cara superior e inferior de losa maciza sobre pilas
qPPlosAlig=pespConcr*ALosAlig/(2*anchLosaAlig+2*ladoCartab) #[N/m2] a aplicar en cara superior e inferior de losa aligeradda
qlPPriostrEstr=pespConcr*AriostrEstr #[N/m]
#
eSize= 0.4     #length of elements

# coordinates in global X,Y,Z axes for the grid generation
#xinterm1=round((xViaFict1+xArranqVoladz)/2.,2)
xList=[-xBordeVoladz,-xMedVoladz,-xBordeCalz,-xArranqVoladz,xViaFict3,-xAlig2,-xPila,-xAlig1,xViaFict2,0,xAlig1,xPila,xAlig2,xViaFict1,xArranqVoladz,xBordeCalz,xMedVoladz,xBordeVoladz]

yList=[0,yminRiostrP1,yPil1,ymaxRiostrP1,yminRiostrP2,yPil2,ymaxRiostrP2,yEstr2]

zinterm1=round(zLosInf+(zArrVoladz-zLosInf)/3.,3)
zriostrEstr=round((zLosInf+zLosSup)/2.,3)

zList=[-hTotPilas,zInfPilAer,zInfPilas,zLosInf,zinterm1,zriostrEstr,zArrVoladz,zLosSup]

#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

XYZLists=(xList,yList,zList)

XvoladzExtrI=(-xBordeVoladz,-xMedVoladz)
XvoladzExtrD=(xMedVoladz,xBordeVoladz)
XvoladzCentI=(-xMedVoladz,-xArranqVoladz)
XvoladzCentD=(xArranqVoladz,xMedVoladz)
XLosa=(-xArranqVoladz,xArranqVoladz)

Yvano1=(0,yPil1)
Yvano2=(yPil1,yPil2)
Yvano3=(yPil2,yEstr2)
YLosligVano1=(0,yminRiostrP1)
YLosligVano2=(ymaxRiostrP1,yminRiostrP2)
YLosligVano3=(ymaxRiostrP2,yEstr2)
YriostrPil1=(yminRiostrP1,ymaxRiostrP1)
YriostrPil2=(yminRiostrP2,ymaxRiostrP2)

ZmurAlig=(zLosInf,zLosSup)
Zvoladz=(zArrVoladz,zArrVoladz)


