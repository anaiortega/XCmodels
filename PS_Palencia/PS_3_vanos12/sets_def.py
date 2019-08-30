# -*- coding: utf-8 -*-

tablero=riostrEstr1+riostrEstr2+losa+cartabInt+cartabExt+voladzInt+voladzExt
tablero.description='Tablero'
#Vías ficticias
x=xViasFict[0]
y=[0,yListTabl[-1]]
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
x=xAceras
y=[0,yListTabl[-1]]
z=zLosa[0]
acerIzq=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0][0],y[0],z),(x[0][-1],y[-1],z)), nameSet='acerIzqIzq')
acerIzq.description='Acera izquierda'
acerDer=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[1][0],y[0],z),(x[1][-1],y[-1],z)), nameSet='acerDer')
acerDer.description='Acera derecha'
aceras=acerIzq+acerDer
aceras.description='Aceras'

#Tablero vano 1
z=zLosa[0]
tablVano1=gridTabl.getSetSurfOneXYZRegion(xyzRange=((xListTabl[0],yListTabl[0],z),(xListTabl[-1],yPil[0],z)),nameSet='tablVano1')
tablVano1.description='Tablero vano 1'
#Tablero vano 2
z=zLosa[0]
tablVano2=gridTabl.getSetSurfOneXYZRegion(xyzRange=((xListTabl[0],yPil[0],z),(xListTabl[-1],yPil[1],z)),nameSet='tablVano2')
tablVano2.description='Tablero vano 2'
#Tablero vano 3
z=zLosa[0]
tablVano3=gridTabl.getSetSurfOneXYZRegion(xyzRange=((xListTabl[0],yPil[1],z),(xListTabl[-1],yListTabl[-1],z)),nameSet='tablVano3')
tablVano3.description='Tablero vano 3'

#Vías ficticias (vano 2)
x=xViasFict[0]
y=yPil
z=zLosa[0]
viaFictDer_vano2=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[1],z)), nameSet='viaFictDer_vano2')
x=xViasFict[1]
viaFictIzq_vano2=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[1],z)), nameSet='viaFictIzq_vano2')
x=xViasFict[2]
viaFictResto_vano2=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[1],z)), nameSet='viaFictResto_vano2')

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

#Sets para armados losa [setZonaArm1,[setZonaArm2, ...]
z=zLosa[0]
x=[0,xLosa[-1]]
sets_arm_losa=[]
for j in range(1,len(yArm)):
    sets_arm_losa.append(gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],yArm[j-1],z),(x[1],yArm[j],z)),nameSet='setArmLos_Z'+str(j)))
#Sets para armados cartabón derecho interno [setZonaArm1,[setZonaArm2, ...]
x=[xCartab[-1][0],xCartab[-1][1]]
sets_arm_cartInt=[]
for j in range(1,len(yArm)):
    sets_arm_cartInt.append(gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],yArm[j-1],z),(x[1],yArm[j],z)),nameSet='setArmCartInt_Z'+str(j)))
#Sets para armados cartabón derecho externo [setZonaArm1,[setZonaArm2, ...]
x=[xCartab[-1][1],xCartab[-1][-1]]
sets_arm_cartExt=[]
for j in range(1,len(yArm)):
    sets_arm_cartExt.append(gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],yArm[j-1],z),(x[1],yArm[j],z)),nameSet='setArmCartExt_Z'+str(j)))
#Sets para armados voladizo derecho interno [setZonaArm1,[setZonaArm2, ...]
x=[xVoladz[-1][0],xVoladz[-1][1]]
sets_arm_volInt=[]
for j in range(1,len(yArm)):
    sets_arm_volInt.append(gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],yArm[j-1],z),(x[1],yArm[j],z)),nameSet='setArmVolInt_Z'+str(j)))
#Sets para armados voladizo derecho externo [setZonaArm1,[setZonaArm2, ...]
x=[xVoladz[-1][1],xVoladz[-1][-1]]
sets_arm_volExt=[]
for j in range(1,len(yArm)):
    sets_arm_volExt.append(gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],yArm[j-1],z),(x[1],yArm[j],z)),nameSet='setArmVolExt_Z'+str(j)))

#set armado riostra estribo
z=zLosa[0]
x=[0,xListTabl[-1]]
y=yRiostrEstr[0]
setArmREstr=gridTabl.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)), nameSet='setArmREstr')
setArmREstr.description='Estribo 1'
#Set armados pilas
setArmPil=pilasBarlov+pilasSotav
setArmPil.description='Pilas'

setArmLosa=sets_arm_losa[0]+sets_arm_losa[1]+sets_arm_losa[2]+sets_arm_losa[3]+sets_arm_losa[4]+sets_arm_losa[5]
setArmLosa.name='setArmLosa'
setArmLosa.description='Losa'
setArmCart=sets_arm_cartInt[0]+sets_arm_cartInt[1]+sets_arm_cartInt[2]+sets_arm_cartInt[3]+sets_arm_cartInt[4]+sets_arm_cartInt[5]+sets_arm_cartExt[0]+sets_arm_cartExt[1]+sets_arm_cartExt[2]+sets_arm_cartExt[3]+sets_arm_cartExt[4]+sets_arm_cartExt[5]
setArmCart.name='setArmCart'
setArmCart.description='Cartabón'
setArmVol=sets_arm_volInt[0]+sets_arm_volInt[1]+sets_arm_volInt[2]+sets_arm_volInt[3]+sets_arm_volInt[4]+sets_arm_volInt[5]+sets_arm_volExt[0]+sets_arm_volExt[1]+sets_arm_volExt[2]+sets_arm_volExt[3]+sets_arm_volExt[4]+sets_arm_volExt[5]
setArmVol.name='setArmVol'
setArmVol.description='Voladizo'
setArmados=setArmLosa+setArmCart+setArmVol+setArmREstr
setArmados.name='setArmados'
setArmados.description='Tabl.'

if abutment.lower()[0]=='y':
    setArmadosEstr=zapEstr+murEstrSet
    if LaletaIzq>0:
        setArmadosEstr+=aletIzqSet
    if LaletaDer>0:
        setArmadosEstr+=aletDerSet
    setArmadosEstr.name='setArmadosEstr'
    setArmadosEstr.description='Estribo'
