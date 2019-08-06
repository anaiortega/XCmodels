# -*- coding: utf-8 -*-

tablero=riostrEstr1+riostrEstr2+losa+cartabInt+cartabExt+voladzInt+voladzExt
tablero.description='Tablero'
#Vías ficticias
x=xViasFict[0]
y=[0,yList[-1]]
z=zLosa[0]
viaFictDer=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), nameSet='viaFictDer')
viaFictDer.description='Vía ficticia derecha'
x=xViasFict[1]
viaFictIzq=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), nameSet='viaFictIzq')
viaFictIzq.description='Vía ficticia izquierda'
x=xViasFict[2]
viaFictResto=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), nameSet='viaFictResto')
viaFictResto.description='Resto vías ficticias'

#calzada
calzada=viaFictIzq+viaFictDer+viaFictResto
calzada.description='Calzada'
#aceras
aceras=tablero-calzada
aceras.description='Aceras'

x=[xViasFict[0][-1],xList[-1]]
y=[0,yList[-1]]
z=zLosa[0]
acerDer=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), nameSet='acerDer')
acerDer.description='Acera derecha'

#Tablero vano 1
z=zLosa[0]
tablVano1=gridTabl.getSetSurfOneXYZRegion(xyzRange=((xList[0],yList[0],z),(xList[-1],yPil[0],z)),nameSet='tablVano1')
tablVano1.description='Tablero vano 1'
#Tablero vano 2
z=zLosa[0]
tablVano2=gridTabl.getSetSurfOneXYZRegion(xyzRange=((xList[0],yPil[0],z),(xList[-1],yPil[1],z)),nameSet='tablVano2')
tablVano2.description='Tablero vano 2'
#Tablero vano 3
z=zLosa[0]
tablVano3=gridTabl.getSetSurfOneXYZRegion(xyzRange=((xList[0],yPil[1],z),(xList[-1],yList[-1],z)),nameSet='tablVano3')
tablVano3.description='Tablero vano 3'

#Vías ficticias (vano central)
x=xViasFict[0]
y=yPil
z=zLosa[0]
viaFictDer_cent=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), nameSet='viaFictDer_cent')
x=xViasFict[1]
viaFictIzq_cent=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), nameSet='viaFictIzq_cent')
x=xViasFict[2]
viaFictResto_cent=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), nameSet='viaFictResto_cent')

#Coordinates for traffic point loads
ycent_vano1=(yRiostrEstr[0][0]+yPil[0])/2.
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

#Barrera
x=xAceras
y=yEstr
z=zLosa[0]
setPntBarr=gridTabl.getSetPntMultiXYZRegion(lstXYZRange=[((x[0][-1],y[0],z),(x[0][-1],y[-1],z)),((x[1][0],y[0],z),(x[1][0],y[-1],z))],setName='setPntBarr')
barrera=sets.get_lines_on_points(setPoints=setPntBarr,setLinName='barrera',onlyIncluded=True)

#Bordes de tablero
x=xVoladz
y=yEstr
z=zLosa[0]
setPntBordTabl=gridTabl.getSetPntMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][0],y[-1],z)),((x[1][-1],y[0],z),(x[1][-1],y[-1],z))],setName='setPntBordTabl')
bordTabl=sets.get_lines_on_points(setPoints=setPntBordTabl,setLinName='bordTabl',onlyIncluded=True)

setPntBordizqTabl=gridTabl.getSetPntMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][0],y[-1],z))],setName='setPntBordizqTabl')
bordizqTabl=sets.get_lines_on_points(setPoints=setPntBordizqTabl,setLinName='bordizqTabl',onlyIncluded=True)
