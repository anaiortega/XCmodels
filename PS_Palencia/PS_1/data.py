# -*- coding: utf-8 -*-
from __future__ import division

import math
from materials.ehe import EHE_materials

#Auxiliary data
dec=2 # número de posiciones decimales para redondear coordenadas
 #Geometry
Lvanos=[11.50,16.10,11.50]
Ltablero=0
for v in Lvanos:
    Ltablero+=v

anchoCalz=6.0
anchoTot=9.20
anchoAcera=(anchoTot-anchoCalz)/2.0   

#  losa
cantoLosa=0.9
maxCantoVoladz=0.4 #canto máximo del voladizo
minCantoVoladz=0.20
anchoVoladz=1.90
anchoLosa=4.20
anchoCartab=0.60
LriostrEstr=1.0
LriostrPil=2  #longitud de riostra sobre pilas
cantoRiostrEstr=0.90

#  Pilas
#distEjPilas=4.00
hTotPilas=10.0   #altura total
diamPilas=1.0
lRectEqPila=round(math.pi**0.5*diamPilas/2.,3)
#hInfPilas=hTotPilas/2.0   #altura zona armado inferior
    
#Apoyos estribos
distNeopr=4.4  #distancia entre neoprenos
numNeopr=2   #número de aparatos de apoyo
xCoordNeopr=[-0.5*distNeopr,0.5*distNeopr]
hNetoNeopr=32e-3 #espesor neto neopreno
aNeopr=0.25       #dimensión y (sentido longitudinal) del neopreno
bNeopr=0.40       #dimensión x (sentido transversal) del neopreno

#     Coordenadas sección transversal
#Aceras
xAceras=[[round(-anchoTot/2.,dec),round(-anchoCalz/2.,dec)],
         [round(anchoCalz/2.,dec),round(anchoTot/2.,dec)]] #iqda., drcha.
#Voladizos
xVoladz=[[round(-anchoTot/2.,dec),round(-anchoTot/2.+anchoVoladz,dec)],
         [round(anchoTot/2.-anchoVoladz,dec),round(anchoTot/2.,dec)]] #iqda., drcha.
xVoladz[0].insert(1,round((xVoladz[0][0]+xVoladz[0][1])/2.,2)) #intermedio
xVoladz[1].insert(1,round((xVoladz[1][0]+xVoladz[1][1])/2.,2)) #intermedio
#Cartabones
xCartab=[[round(xVoladz[0][-1],dec),round(xVoladz[0][-1]+anchoCartab,dec)],
         [round(xVoladz[1][0]-anchoCartab,dec),round(xVoladz[1][0],dec)]] #iqda., drcha.
xCartab[0].insert(1,round((xCartab[0][0]+xCartab[0][-1])/2.,2)) #intermedio
xCartab[1].insert(1,round((xCartab[1][0]+xCartab[1][-1])/2.,2))#intermedio

#Losa espesor constante
xLosa=[xCartab[0][-1],xCartab[1][0]]
#Riostras estribos
xRiostrEstr=[[xVoladz[0][-1],xVoladz[1][0]],
             [xVoladz[0][-1],xVoladz[1][0]]]   #riostra estribo 1, riostra estribo 2
#Pila
xPil=[0]
#Vias ficticeas
xViasFict=[[0,round(anchoCalz/2.,dec)],
           [round(-anchoCalz/2.,dec),0]] #vía 1, vía 2, ...

xNeopr=[-distNeopr/2.,distNeopr/2.]

#   Coordenadas perfil longitudinal
#Estribos
yEstr=[0,Ltablero] #eje estribo 1, eje estribo 2
#Riostra estribos
yRiostrEstr=[[round(yEstr[0]-LriostrEstr/2.,dec),round(yEstr[0]+LriostrEstr/2.,dec)],
             [round(yEstr[1]-LriostrEstr/2.,dec),round(yEstr[1]+LriostrEstr/2.,dec)]]  #riostra estribo 1, riostra estribo 2
#Pilas
yPil=[Lvanos[0],Lvanos[0]+Lvanos[1]]
#Riostra pilas
yRiostrPil=[[round(yPil[0]-LriostrPil/2.,dec),round(yPil[0]+LriostrPil/2.,dec)],
            [round(yPil[1]-LriostrPil/2.,dec),round(yPil[1]+LriostrPil/2.,dec)]]  #riostra pila 1, riostra pila 2
yLosa=[yRiostrEstr[0][1],yRiostrEstr[-1][0]]
#   Coordenadas en Z
zPil=[[-hTotPilas,0],[-hTotPilas,0]] # pila 1, pila 2
zLosa=[0]

#materials
concrete=EHE_materials.HA30
reinfSteel= EHE_materials.B500S
Gneopr=1000e3  #módulo de cortante del material elastomérico

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

Qfrenado=470.7e3 #carga total de frenado a aplicar en via fictícea 1 [N]
QCentrif=0  #carga uniforme debida a la fuerza centrífuga [N/m2]
vQfren=[0,Qfrenado/3/Ltablero] #componentes X,y de la carga uniforme de frenado
#  viento
qWpilas=2.56e3 #carga lineal viento sobre pilas [N/m]
qWTablero=7.73e3 #carga lineal viento sobre tablero [N/m]
qWTableroSCuso=6.7e3 #carga lineal viento sobre tablero actuando con SC uso [N/m]
#coef_ocult=0.46

#Temperaturas
Tunif_contr=-24  #Incremento uniforme temperatura contracción ºC
Tunif_dilat=31   #Incremento uniforme temperatura dilatación ºC
Tfibrsup_cal=15  #Temperatura fibra superior más caliente (T fibra inf.=0ºC)
Tfibrsup_fria=-8  #Temperatura fibra superior más fría (T fibra inf.=0ºC)
coefDilat=1e-5    #coeficiente de dilatación térmica lineal del hormigón

Tunif_contr_neopr=-24-15  #Incremento uniforme temperatura contracción ºC
Tunif_dilat_neopr=31+15   #Incremento uniforme temperatura dilatación ºC


#Retracción
eps_retracc=-531e-6  #deformación por retracción #!!!!!REPASAR


# espesores derivados
#Voladizo externo
e1=minCantoVoladz
e2=maxCantoVoladz
eVolExt=(3*e1+e2)/4.
#Voladizo interno
e2=minCantoVoladz
e1=maxCantoVoladz
eVolInt=(3*e1+e2)/4.
# cartabón externo
e1=maxCantoVoladz
e2=cantoLosa
eCartExt=(3*e1+e2)/4.
# cartabón interno
e2=maxCantoVoladz
e1=cantoLosa
eCartInt=(3*e1+e2)/4.

#peso propio
grav=9.81 #Gravity acceleration (m/s2)
pespConcr=grav*concrete.density() #peso específico hormigón armado [N/m3]

eSize= 0.4     #length of elements

# coordinates in global X,Y,Z axes for the grid generation
def flatten(l):
    return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]

xList_aux=flatten(xAceras+xVoladz+xCartab+xLosa+xPil+xViasFict+xRiostrEstr)
xList=[]
for i in xList_aux:
    if i not in xList:
        xList.append(i)
xList.sort()

yList_aux=flatten(yEstr+yRiostrEstr+yRiostrPil+yPil)
yList=[]
for i in yList_aux:
    if i not in yList:
        yList.append(i)
yList.sort()

zList_aux=flatten(zPil+zLosa)
zList=[]
for i in zList_aux:
    if i not in zList:
        zList.append(i)
zList.sort()

#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1
XYZlists=(xList,yList,zList)


