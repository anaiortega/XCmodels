# -*- coding: utf-8 -*-
pilas=pilasBarlov+pilasSotav
pilas.description='Pilas'
pilas.color=cfg.colors['brown03']



pilasInf=gridPil.getSetLinOneXYZRegion(((xPil[0],yPil[0],-hTotPilas),(xPil[-1],yPil[-1],zInfPilas)),'pilasInf')
pilasInf.description='Pilas, zona inferior'
pilasInf.color=cfg.colors['brown04']
pilasSup=gridPil.getSetLinOneXYZRegion(((xPil[0],yPil[0],zInfPilas),(xPil[-1],yPil[-1],zLosInf)),'pilasSup')
pilasSup.description='Pilas, zona superior'
pilasSup.color=cfg.colors['brown01']
if abutment.lower()[0]=='y':
    #zapata
    x=[0,xExtrAletaD]
    y=Yzap
    z=Zzap
    setArmZapEstr=gridAbutment.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z[0]),(x[-1],y[-1],z[-1])), setName='setArmZapEstr')
    #muro estribo
    x=[0,xAletaD]
    y=Ymurestr
    z=[zZapata,zMurEstr]
    setArmMurEstr=gridAbutment.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z[0]),(x[-1],y[-1],z[-1])), setName='setArmMurEstr')
    setArmadosEstr=setArmZapEstr+setArmMurEstr
    # No se incluye la aleta izquierda en el set de armados al ser simétrica
    # de la derecha
    # if LaletaIzq>0:
    #     setArmadosEstr+=aletIzqSet
    if LaletaDer>0:
        setArmadosEstr+=aletDerSet
    setArmadosEstr.name='setArmadosEstr'
    setArmadosEstr.description='Estribo'


#Bordes de tablero
x=xVoladz
y=yEstr
z=zArrVoladz
setPntBordTabl=gridTabl.getSetPntMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][0],y[-1],z)),((x[1][-1],y[0],z),(x[1][-1],y[-1],z))],setName='setPntBordTabl')
bordTabl=sets.get_lines_on_points(setPoints=setPntBordTabl,setLinName='bordTabl',onlyIncluded=True)

setPntBordizqTabl=gridTabl.getSetPntMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][0],y[-1],z))],setName='setPntBordizqTabl')
bordizqTabl=sets.get_lines_on_points(setPoints=setPntBordizqTabl,setLinName='bordizqTabl',onlyIncluded=True)

#Vías ficticias
# En el voladizo
x=xViasFict[0]
y=[0,yListTabl[-1]]
z=zArrVoladz
viaFictDerVol=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), setName='viaFictDerVol')
x=xViasFict[1]
viaFictIzqVol=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), setName='viaFictIzqVol')
x=xViasFict[2]
viaFictRestoVol=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), setName='viaFictRestoVol')
# En la losa
x=xViasFict[0]
y=[0,yListTabl[-1]]
z=zLosSup
viaFictDerLos=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), setName='viaFictDerLos')
x=xViasFict[1]
viaFictIzqLos=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), setName='viaFictIzqLos')
x=xViasFict[2]
viaFictRestoLos=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), setName='viaFictRestoLos')

viaFictDer=viaFictDerVol+viaFictDerLos
viaFictDer.description='Vía ficticia derecha'
viaFictIzq=viaFictIzqVol+viaFictIzqLos
viaFictIzq.description='Vía ficticia izquierda'
viaFictResto=viaFictRestoVol+viaFictRestoLos
viaFictResto.description='Resto vías ficticias'

#Vías ficticias (vano 2)
# En el voladizo
x=xViasFict[0]
y=yPil
z=zArrVoladz
viaFictDer_vano2_vol=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[1],z)), setName='viaFictDer_vano2_vol')
x=xViasFict[1]
viaFictIzq_vano2_vol=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[1],z)), setName='viaFictIzq_vano2_vol')
x=xViasFict[2]
viaFictResto_vano2_vol=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[1],z)), setName='viaFictResto_vano2_vol')
# En la losa
x=xViasFict[0]
y=yPil
z=zLosSup
viaFictDer_vano2_los=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[1],z)), setName='viaFictDer_vano2_los')
x=xViasFict[1]
viaFictIzq_vano2_los=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[1],z)), setName='viaFictIzq_vano2_los')
x=xViasFict[2]
viaFictResto_vano2_los=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[1],z)), setName='viaFictResto_vano2_los')

viaFictDer_vano2=viaFictDer_vano2_vol+viaFictDer_vano2_los
viaFictIzq_vano2=viaFictIzq_vano2_vol+viaFictIzq_vano2_los
viaFictResto_vano2=viaFictResto_vano2_vol+viaFictResto_vano2_los




acerIzq_rg=list()
acerIzq_rg.append(gm.IJKRange((0,0,zListTabl.index(zArrVoladz)),(xListTabl.index(xCalzada[0]),len(yListTabl)-1,zListTabl.index(zArrVoladz))))
acerIzq=gridTabl.getSetSurfMultiRegion(lstIJKRange=acerIzq_rg,setName='acerIzq')

acerDer_rg=list()
acerDer_rg.append(gm.IJKRange((xListTabl.index(xCalzada[-1]),0,zListTabl.index(zArrVoladz)),(len(xListTabl)-1,len(yListTabl)-1,zListTabl.index(zArrVoladz))))
acerDer=gridTabl.getSetSurfMultiRegion(lstIJKRange=acerDer_rg,setName='acerDer')

aceras=acerIzq+acerDer
aceras.name='aceras'

calzada_rg=gm.IJKRange((xListTabl.index(xCalzada[0]),0,zListTabl.index(zArrVoladz)),(xListTabl.index(xCalzada[-1]),len(yListTabl)-1,zListTabl.index(zLosSup))).extractIncludedIJranges()
calzada=gridTabl.getSetSurfMultiRegion(lstIJKRange=calzada_rg,setName='calzada')
#Imposta
auxSetPnt1=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((0,0,zListTabl.index(zArrVoladz)),(0,len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='auxSetPnt1')
auxSetPnt2=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((len(xListTabl)-1,0,zListTabl.index(zArrVoladz)),(len(xListTabl)-1,len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='auxSetPnt2')
auxSetPnt=auxSetPnt1+auxSetPnt2
auxSetPnt.name='auxSetPnt'
imposta=sets.get_lines_on_points(setPoints=auxSetPnt,setLinName='imposta',onlyIncluded=True)
barrera_rg=list()
auxSetPnt1=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((xListTabl.index(xCalzada[0]),0,zListTabl.index(zArrVoladz)),(xListTabl.index(xCalzada[0]),len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='auxSetPnt1')
auxSetPnt2=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((xListTabl.index(xCalzada[-1]),0,zListTabl.index(zArrVoladz)),(xListTabl.index(xCalzada[-1]),len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='auxSetPnt2')
auxSetPnt=auxSetPnt1+auxSetPnt2
auxSetPnt.name='auxSetPnt'
barrera=sets.get_lines_on_points(setPoints=auxSetPnt,setLinName='barrera',onlyIncluded=True)
#línea arranque voladizo izquierdo (aplicación W)
arrqVolPnt=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((xListTabl.index(xVoladz[0][-1]),0,zListTabl.index(zArrVoladz)),(xListTabl.index(xVoladz[0][-1]),len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='arrqVolPnt')
arrqVol=sets.get_lines_on_points(setPoints=arrqVolPnt,setLinName='arrqVol',onlyIncluded=True)


losInf.description='Losa aligerada, cordón inferior'
losInf.color=cfg.colors['purple03']
losSup.description='Losa aligerada, cordón superior'
losSup.color=cfg.colors['purple01']
murAlig.description='Losa aligerada, nervios'
murAlig.name='murAlig'
murAlig.color=cfg.colors['orange02']
murExtAlig.description='Losa aligerada, almas borde'
murExtAlig.color=cfg.colors['yellow02']
voladzCent.description='Voladizo, zona central'
voladzCent.color=cfg.colors['brown01']
voladzExtr.description='Voladizo, zona de borde'
voladzExtr.color=cfg.colors['brown02']
supTablero.description='Losa tablero, cordón superior y voladizos'
supTablero.color=cfg.colors['yellow02']
total=prep.getSets.getSet('total')
tablero=losInf+losSup+murAlig+murExtAlig+murRP+diafRP
tablero.name='Tablero'
tablero.description='Tablero'
tablero.color=cfg.colors['purple01']
allLosas=losInf+losSup+voladzCent+voladzExtr
allLosas.name='allLosas'
allLosas.description='Losa tablero, cordones superior e inferior y voladizos'

ThermalUnifSetDirY=losInf+losSup+murAlig+murExtAlig #set al que aplicar deformación térmica uniforme en dirección Y (longitudinal de tablero)
RheoSetDirY=losInf+losSup+murAlig+murExtAlig #set al que aplicar deformación por retracción en dirección Y

overallSet=riostrEstr1+riostrEstr2+losInfV1+losInfV2+losInfV3+losInfRP1+losInfRP2+losSupV1+losSupV2+losSupV3+losSupRP1+losSupRP2+murAligV1+murAligV2+murAligV3+murExtAligV1+murExtAligV2+murExtAligV3+murRP1+murRP2+diafRP1+diafRP2+voladzCentV1+voladzCentV2+voladzCentV3+voladzCentRP1+voladzCentRP2+voladzExtrV1+voladzExtrV2+voladzExtrV3+voladzExtrRP1+voladzExtrRP2
overallSet.description='Estructura'
overallSet.name='overallSet'
overallSet.color=cfg.colors['purple01']

#Coordinates for traffic point loads
ycent_vano1=(yEstr[0]+yPil[0])/2.
ycent_vano2=(yPil[0]+yPil[1])/2.
yextr_vano1=yEstr[0]+0.5
yextr_vano2=yPil[0]+0.5
xcent_VFder=(xViasFict[0][0]+xViasFict[0][-1])/2.    #via ficticea derecha
xcent_VFizq=(xViasFict[1][0]+xViasFict[1][-1])/2.    #via ficticea izquierda

centVFd_vano1=[xcent_VFder,ycent_vano1]  #centro via ficticea derecha, vano 1
centVFd_vano2=[xcent_VFder,ycent_vano2]  #centro via ficticea derecha, vano 2
centVFi_vano1=[xcent_VFizq,ycent_vano1]  #centro via ficticea izqu., vano 1
centVFi_vano2=[xcent_VFizq,ycent_vano2]  #centro via ficticea izqu., vano 2

extrVFd_vano1=[xcent_VFder,yextr_vano1]  #extr via ficticea derecha, vano 1
extrVFd_vano2=[xcent_VFder,yextr_vano2]  #extr via ficticea derecha, vano 2
extrVFi_vano1=[xcent_VFizq,yextr_vano1]  #extr via ficticea izqu., vano 1
extrVFi_vano2=[xcent_VFizq,yextr_vano2]  #extr via ficticea izqu., vano 2
