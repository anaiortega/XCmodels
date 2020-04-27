# -*- coding: utf-8 -*-
from __future__ import division
from misc_utils import units_utils as uu
from postprocess.config import default_config

import math
from materials.ehe import EHE_materials

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

#Auxiliary data
dec=2 # número de posiciones decimales para redondear coordenadas
tol=0.25 # mínima distancia entre coordenadas en un eje (por debajo de esta 
 #Geometry
LvanoCent=17
LvanosExtr=13
Ltablero=LvanoCent+2*LvanosExtr

anchoCalz=10.70
anchoTot=13.80
anchoAcera=(anchoTot-anchoCalz)/2.0   

#  losa
distEjesAlig=2.10  #distancia entre ejes de aligeramientos
diamAlig=0.8   #diámetro aligeramientos
lRectEqAlig=round(math.pi**0.5*diamAlig/2.,3)
numAlig=3      #número de aligeramientos
cantoTabl=1.15
maxCantoVoladz=0.5 #canto máximo del voladizo
minCantoVoladz=0.20
anchVoladz=2.85
anchLosaAlig=7.0
ladoCartab=0.55

cantoRiostrEstr=cantoTabl
LriosrEstr=1.0  #ancho riostra estribo (sentido longitudinal)

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
xNeopr=[-1.5*distNeopr,-0.5*distNeopr,0.5*distNeopr,1.5*distNeopr]
hNetoNeopr=48e-3 #espesor neto neopreno
aNeopr=0.25       #dimensión y (sentido longitudinal) del neopreno
bNeopr=0.40       #dimensión x (sentido transversal) del neopreno

#materials
concrete=EHE_materials.HA30
reinfSteel= EHE_materials.B500S
Gneopr=1000e3  #módulo de cortante del material elastomérico
Eneopr=600e6      #módulo elástico material elastomérico

# Cargas
grav=9.81     #[m/s2]
pav_inf=1150  #pavimento, valor inferior [N/m2]
pav_sup=1725  #pavimento, valor superior [N/m2]
qBarrera=8e3  #barrera rígida [N/m]
#Limposta=4e3  #imposta [N/m]
qDeadAcera=round(4e3/anchoAcera,0)  #acera [N/m2]
qAntivand=1e3   #protección antivandálica [N/m]

qunifmax=9e3    #carga uniforme en vía virtual 1
qunifmin=2.5e3    #carga uniforme en resto
qunifacera=2.5e3    #carga uniforme en acera concomitante con cargas de tráfico

Qfrenado=497.7e3 #carga total de frenado a aplicar en via fictícea 1 [N]
QCentrif=0  #carga uniforme debida a la fuerza centrífuga [N/m2]
vQfren=[0,Qfrenado/3/Ltablero] #componentes X,y de la carga uniforme de frenado
#  viento
qWpilasBarlov=2.56e3 #carga lineal viento sobre pilas a barlovento [N/m]
qWTablero=7.73e3 #carga lineal viento sobre tablero [N/m]
qWTableroSCuso=6.7e3 #carga lineal viento sobre tablero actuando con SC uso [N/m]
coef_ocult=0.46
qWpilasSotav=qWpilasBarlov*coef_ocult #carga lineal viento sobre pilas a sotavento [N/m]

#Temperaturas
Tunif_contr=-24  #Incremento uniforme temperatura contracción ºC
Tunif_dilat=31   #Incremento uniforme temperatura dilatación ºC
Tfibrsup_cal=15  #Temperatura fibra superior más caliente (T fibra inf.=0ºC)
Tfibrsup_fria=-8  #Temperatura fibra superior más fría (T fibra inf.=0ºC)
coefDilat=1e-5    #coeficiente de dilatación térmica lineal del hormigón

Tunif_contr_neopr=-24-15  #Incremento uniforme temperatura contracción ºC
Tunif_dilat_neopr=31+15   #Incremento uniforme temperatura dilatación ºC


#Retracción
area_deck=1   #!!!Corregir
perim_deck=1  #!!!Corregir
execfile(workingDirectory+'retraccion.py')  #cálculo de la retracción
eps_retracc=Epscs  #deformación por retracción #


#Magnitudes derivadas
# espesores
espLosAlig=round((cantoTabl-lRectEqAlig)/2.,3)
espEntreAlig=round(distEjesAlig-lRectEqAlig,3)
espExtAlig=2*espEntreAlig
espVoladzMax=round((3*maxCantoVoladz+minCantoVoladz)/4.,3)
espVoladzMin=round((maxCantoVoladz+3*minCantoVoladz)/4.,3)
espPuntMaz=distEjesAlig/2.

hDistrPL=espLosAlig  #height of distribution of traffic point loads

hDistrQ=espLosAlig/2.+0.05

# Espesor de la losa a efecto de distribución de cargas puntuales de tráfico
cantoLosa=espLosAlig

# Coord. x (transversal)
xBordeCalz=round(anchoCalz/2.0,2)
#xViasFict1=round(xBordeCalz-3,2)
#xViasFict2=round(xViasFict1-3,2)
#xViasFict3=round(xViasFict2-3,2)

xViasFict=[[round(xBordeCalz-3,2),round(anchoCalz/2.0,2)], 
          [round(xBordeCalz-2*3,2),round(xBordeCalz-3,2)],
          [round(xBordeCalz-3*3,2),round(xBordeCalz-2*3,2)],
          [-xBordeCalz,round(xBordeCalz-2*3,2)]]
          # vias ficticeas
          # 1, 2 , 3 y remanente  (xmin,xmax) 

xBordeVoladz=round(anchoTot/2.0,2)
xMedVoladz=round(xBordeVoladz-anchVoladz/2.0,2)
xArranqVoladz=round(xBordeVoladz-anchVoladz,2)

xAlmasAlig=[-(numAlig/2)*distEjesAlig]  #min. coord. x alma aligeramiento
for i in range(numAlig):
    xAlmasAlig.append(xAlmasAlig[-1]+distEjesAlig)
xAlmasAlig=uu.roundLst(xAlmasAlig,dec)

xPila=round(distEjPilas/2.0,2)
xPil=[-xPila,xPila]
#espesor diafragmas riostra pila
ValigRP=LriostrPil*numAlig*math.pi*diamAlig**2/4.
LdiafRP=xAlmasAlig[-1]-xAlmasAlig[0]
espDiafRP=ValigRP/nDiafRP/LdiafRP/(cantoTabl-2*espLosAlig)

#Coord. Y (longitudinal)
yPil1=LvanosExtr
yminRiostrP1=yPil1-LriostrPil/2.0+espDiafRP/2.
ymaxRiostrP1=yPil1+LriostrPil/2.0-espDiafRP/2.
yPil2=LvanosExtr+LvanoCent
yminRiostrP2=yPil2-LriostrPil/2.0+espDiafRP/2.
ymaxRiostrP2=yPil2+LriostrPil/2.0-espDiafRP/2.
yEstr2=yPil2+LvanosExtr
yEstr=[0,yEstr2] #eje estribo 1, eje estribo 2

yPil=[yPil1,yPil2]

#Coord. Z (vertical)
zLosInf=round(espLosAlig/2.0,3)
zLosSup=round(cantoTabl-espLosAlig/2.0,3)
zArrVoladz=round(cantoTabl-maxCantoVoladz/2.0,3)
zInfPilas=-hTotPilas+hInfPilas  #arranque tramo superior 
zInfPilAer=-hTotPilas+2  #aprox. 2 m enterrado

zPil=[[-hTotPilas,zInfPilAer,zInfPilas,zLosInf],[-hTotPilas,zInfPilAer,zInfPilas,zLosInf]]  #Pila 1, pila 2
#peso propio
grav=9.81 #Gravity acceleration (m/s2)
pespConcr=grav*concrete.density() #peso específico hormigón armado [N/m3]

AvolExt=(minCantoVoladz+(maxCantoVoladz+minCantoVoladz)/2.0)/2.0*anchVoladz/2.0
AvolCent=(maxCantoVoladz+(maxCantoVoladz+minCantoVoladz)/2.0)/2.0*anchVoladz/2.0
ALos=2*(maxCantoVoladz+cantoTabl)/2.*ladoCartab+anchLosaAlig*cantoTabl
ALosAlig=ALos-numAlig*math.pi*diamAlig**2/4.
Apilas=math.pi*diamPilas**2/4.
AriostrEstr=cantoTabl*cantoRiostrEstr
qPPvolExt=pespConcr*AvolExt/(anchVoladz/2.)  #[N/m2]
qPPvolCent=pespConcr*AvolCent/(anchVoladz/2.)  #[N/m2]
qPPlos=pespConcr*ALos/(2*anchLosaAlig+2*ladoCartab) #[N/m2] a aplicar en cara superior e inferior de losa maciza sobre pilas
qPPlosAlig=pespConcr*ALosAlig/(2*anchLosaAlig+2*ladoCartab) #[N/m2] a aplicar en cara superior e inferior de losa aligeradda
qlPPriostrEstr=pespConcr*AriostrEstr #[N/m]
#
eSize= 0.45     #length of elements

# coordinates in global X,Y,Z axes for the grid generation
#xinterm1=round((xViaFict1+xArranqVoladz)/2.,2)
xCalzada=[-xBordeCalz,xBordeCalz]
xVoladz=[[-xBordeVoladz,-xMedVoladz,-xArranqVoladz],
         [xArranqVoladz,xMedVoladz,xBordeVoladz]]   #izq.,drcho.


def insert2DList(baseList,list2Insert,tolerance):
    '''Iterates through the list of two lists list2Insert doing the following for each item:
       - if its distance to the closest value in baseList is greater than tolerance, appends the item to baseList,
       - otherwise, the item is replaced by its closest value in baseList  

    '''
    for i in range(len(list2Insert)):
        for j in range(len(list2Insert[i])):
            coor=list2Insert[i][j]
            clVal=closest(baseList,coor)
            if abs(coor-clVal)<=tolerance:
                list2Insert[i][j]=clVal
            else:
                baseList.append(coor)

def insert1DList(baseList,list2Insert,tolerance):
    '''Iterates through the list list2Insert doing the following for each item:
       - if its distance to the closest value in baseList is greater than tolerance, appends the item to baseList,
       - otherwise, the item is replaced by its closest value in baseList  

    '''
    for i in range(len(list2Insert)):
        coor=list2Insert[i]
        clVal=closest(baseList,coor)
        if abs(coor-clVal)<=tolerance:
            list2Insert[i]=clVal
        else:
            baseList.append(coor)

xListTabl=[]
xListTabl+=xAlmasAlig
insert1DList(xListTabl,xPil,tol)
insert2DList(xListTabl,xVoladz,tol)
insert1DList(xListTabl,xCalzada,tol)
insert2DList(xListTabl,xViasFict,tol)
xListTabl.sort()

yListTabl=[]
yListTabl+=yPil
yListTabl+=yEstr
yListTabl+=[yminRiostrP1,ymaxRiostrP1,yminRiostrP2,ymaxRiostrP2]
yListTabl.sort()

zinterm1=round(zLosInf+(zArrVoladz-zLosInf)/3.,3)
zriostrEstr=round((zLosInf+zLosSup)/2.,3)

zListTabl=[zLosInf,zinterm1,zriostrEstr,zArrVoladz,zLosSup]
zListTabl.sort()


#auxiliary data

XYZListsTabl=(xListTabl,yListTabl,zListTabl)

XvoladzExtrI=(xVoladz[0][0],xVoladz[0][1])
XvoladzExtrD=(xVoladz[1][1],xVoladz[1][-1])
XvoladzCentI=(xVoladz[0][1],xVoladz[0][-1])
XvoladzCentD=(xVoladz[1][0],xVoladz[1][1])
XLosa=(xVoladz[0][-1],xVoladz[1][0])

Yvano1=(0,yPil[0])
Yvano2=(yPil[0],yPil[1])
Yvano3=(yPil[1],yEstr[-1])
YLosligVano1=(0,yminRiostrP1)
YLosligVano2=(ymaxRiostrP1,yminRiostrP2)
YLosligVano3=(ymaxRiostrP2,yEstr[-1])
YriostrPil1=(yminRiostrP1,ymaxRiostrP1)
YriostrPil2=(yminRiostrP2,ymaxRiostrP2)

ZmurAlig=(zLosInf,zLosSup)
Zvoladz=(zArrVoladz,zArrVoladz)

xListPil=[]
xListPil+=xPil
yListPil=[]
yListPil+=yPil

def flatten(l):
    return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]

zListPil_aux=flatten(zPil)
zListPil=[]
for i in zListPil_aux:
    if i not in zListPil:
        zListPil.append(i)
zListPil.sort()
