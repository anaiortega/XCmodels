# -*- coding: utf-8 -*-
from __future__ import division
import math
# Estribo con aletas  en prolongación o formando ángulo < 90º  
#Abutment geometry
cantoZap=1.5
espCoronAlet=0.4
espMurEstr=1.35
anchoEstr=9.20
hMurEstr=8.4  #altura del muro del estribo 
hMuret=1.35
Lpunt=1.8+0.5*espMurEstr #puntera
Lzap=7.4+0.5*espMurEstr #talón
LaletaIzq=4  # longitud aleta izquierda (=0 si no existe)
pendCoronAletaIzq=2/3.9  #V:H pendiente de la coronación de la aleta izquierda
                         # =0 si horizontal
LaletaDer=4  # longitud aleta derecha (=0 si no existe)
pendCoronAletaDer=2/3.8  #V:H pendiente de la coronación de la aleta derecha
                         # =0 si horizontal
pendTrasdosAlet=1/12.  #H:V
hBrutoNeopr=0.2  #Espesor bruto de neopreno
excNeop=espMurEstr/2.+0.5 #excentricidad de los aparatos de apoyo respecto al plano medio del muro

#ángulo que forman las aletas con el plano del muro del estribo
angAletaIzq=20  #can be =0
angAletaDer=-20 

eSizeAbut= 0.45     #length of elements

#Loads
# K30: roca blanda o alterada 100 kg/cm3 
K30=1000e6        #(N/m3)
Kcuadr=(K30*0.3)/Lzap #suelo cohesivo Lzap en [m]
Kcuadr=K30*((Lzap+0.3)/2./Lzap)**2 #suelo arenoso Lzap en [m]
Krectang=2/3.*Kcuadr*(1+Lzap/(2*anchoEstr)) # Lzap y anchoEstr en [m]
Kbalasto=Krectang                  #coef. balasto (N/m3)
# empuje del terreno
fi_terr=30                            #ángulo de rozamiento interno
K0=1-math.sin(math.radians(fi_terr))  #coeficiente de empuje al reposo
Ksoil=K0
densrell=2e3                  #densidad del relleno (kg/m3)
zGround=0
qunifTerr=10e3 #carga uniforme sobre el terreno [N/m2]

# Coord. x (transversal)
xAletaI=round(-anchoEstr/2.0,2)
xAletaD=round(anchoEstr/2.0,2)
xExtrAletaI=xAletaI-LaletaIzq
xExtrAletaD=xAletaD+LaletaDer

#Coord. Y (longitudinal)
yMurEstr=-excNeop
yPuntera=yMurEstr+Lpunt
yZapata=round(yMurEstr-Lzap,2)

#Coord. Z (vertical)
zZapata=round(-hMurEstr-cantoZap/2.-hBrutoNeopr,2)
zMurEstr=round(zZapata+cantoZap/2.+hMurEstr,2)
zAletas=round(zMurEstr+hMuret,2)
zArm1=round(zZapata+hMurEstr/3.0,2) #cota superior de la zona de armado (y espesor) 1
zArm2=round(zZapata+2*hMurEstr/3.0,2) #cota superior de la zona de armado (y espesor) 2

#pteMurEstr=(zMurEstrDer-zMurEstrIzq)/(xAletaD-xAletaI)

# espesores
def espZ1_Z2(zCoron,eCoron,pend,Z1,Z2):
    '''espesor medio del muro en vuelta entre cotas Z1 y Z2
    '''
    espZ1=eCoron+(zCoron-Z1)*pend
    espZ2=eCoron+(zCoron-Z2)*pend
    return (espZ1+espZ2)/2.0

espAletiZ1=espZ1_Z2(zAletas,espCoronAlet,pendTrasdosAlet,0,zArm1)
espAletiZ2=espZ1_Z2(zAletas,espCoronAlet,pendTrasdosAlet,zArm1,zArm2)
espAletiZ3=espZ1_Z2(zAletas,espCoronAlet,pendTrasdosAlet,zArm2,zAletas)

espAletdZ1=espZ1_Z2(zAletas,espCoronAlet,pendTrasdosAlet,0,zArm1)
espAletdZ2=espZ1_Z2(zAletas,espCoronAlet,pendTrasdosAlet,zArm1,zArm2)
espAletdZ3=espZ1_Z2(zAletas,espCoronAlet,pendTrasdosAlet,zArm2,zAletas)


#ranges coordinates
Xmurestr=[xAletaI,xAletaD]
Xaleti=[xExtrAletaI,xAletaI]
Xaletd=[xAletaD,xExtrAletaD]
Xzap=[xExtrAletaI,xExtrAletaD]

Yzap=[yZapata,yPuntera]
Ymurestr=[yMurEstr,yMurEstr]
Yaleti=[yMurEstr,yMurEstr]
Yaletd=[yMurEstr,yMurEstr]

Zzap=[zZapata,zZapata]
zZ1=[zZapata,zArm1]
zZ2mur=[zArm1,zArm2]
zZ3mur=[zArm2,zMurEstr]
zZ2alet=[zArm1,zArm2]
zZ3alet=[zArm2,zAletas]
# coordinates in global X,Y,Z axes for the grid generation
#xinterm1=round((xViaFict1+xArranqVoladz)/2.,2)
xListAbut_aux=Xmurestr+xNeopr+Xaleti+Xaletd+Xzap
xListAbut=[]
for i in xListAbut_aux:
    if i not in xListAbut:
        xListAbut.append(i)
xListAbut.sort()
yListAbut_aux=Yzap+Ymurestr+Yaleti+Yaletd
yListAbut=[]
for i in yListAbut_aux:
    if i not in yListAbut:
        yListAbut.append(i)
yListAbut.sort()

zListAbut_aux=Zzap+zZ1+zZ2mur+zZ3mur+zZ2alet+zZ3alet
zListAbut=[]
for i in zListAbut_aux:
    if i not in zListAbut:
        zListAbut.append(i)
zListAbut.sort()

XYZListsAbut=(xListAbut,yListAbut,zListAbut)
