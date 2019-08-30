# -*- coding: utf-8 -*-
#empuje del terreno sobre elmuro del estribo
soil=ep.EarthPressureModel( zGround=zGround,zBottomSoils=[-100],KSoils=[Ksoil], gammaSoils=[densrell*grav], zWater=-100.0, gammaWater=grav)
ep_murEstr= loads.EarthPressLoad(name= 'ep_murEstr', xcSet=murEstrSet,soilData=soil, vDir=xc.Vector([0,1,0]))
rell_zap=loads.UniformLoadOnSurfaces(name= 'rell_zap',xcSet=zapTrasdos,loadVector= xc.Vector([0,0,-grav*densrell*(zGround-zZapata-cantoZap/2.)]))

G4_lstLoads=[ep_murEstr,rell_zap]
# empuje del terreno sobre aleta izquierda
if LaletaIzq>0:
    pnt1=gridAbutment.getPntGrid((xListAbut.index(Xaleti[1]),yListAbut.index(Yaleti[1]),zListAbut.index(Zzap[0])))
    pnt2=gridAbutment.getPntGrid((xListAbut.index(Xaleti[0]),yListAbut.index(Yaleti[1]),zListAbut.index(Zzap[0])))
    zGroundPnt1=zGround
    zGroundPnt2=zGroundPnt1-pendCoronAletaIzq*LaletaIzq
    soil_aletIzq=ep.EarthPressureSlopedWall(Ksoil=Ksoil,gammaSoil=densrell*grav,zGroundPnt1=zGroundPnt1,XYpnt1=(pnt1.getPos.x,pnt1.getPos.y),zGroundPnt2=zGroundPnt2,XYpnt2=(pnt2.getPos.x,pnt2.getPos.y))
    ang=math.radians(angAletaIzq)
    ep_aletIzq= loads.EarthPressLoad(name= 'ep_aletIzq', xcSet=aletIzqSet,soilData=soil_aletIzq, vDir=xc.Vector([-math.sin(ang),math.cos(ang),0]))
    G4_lstLoads.append(ep_aletIzq)
    
if LaletaDer>0:
    pnt1=gridAbutment.getPntGrid((xListAbut.index(Xaletd[0]),yListAbut.index(Yaletd[1]),zListAbut.index(Zzap[0])))
    pnt2=gridAbutment.getPntGrid((xListAbut.index(Xaletd[1]),yListAbut.index(Yaletd[1]),zListAbut.index(Zzap[0])))
    zGroundPnt1=zGround
    zGroundPnt2=zGroundPnt1-pendCoronAletaDer*LaletaDer
    soil_aletDer=ep.EarthPressureSlopedWall(Ksoil=Ksoil,gammaSoil=densrell*grav,zGroundPnt1=zGroundPnt1,XYpnt1=(pnt1.getPos.x,pnt1.getPos.y),zGroundPnt2=zGroundPnt2,XYpnt2=(pnt2.getPos.x,pnt2.getPos.y))
    ang=math.radians(angAletaDer)
    ep_aletDer= loads.EarthPressLoad(name= 'ep_aletDer', xcSet=aletDerSet,soilData=soil_aletDer, vDir=xc.Vector([-math.sin(ang),math.cos(ang),0]))
    G4_lstLoads.append(ep_aletDer)
    

G4=lcases.LoadCase(preprocessor=prep,name="G4",loadPType="default",timeSType="constant_ts")
G4.create()
G4_lstLoads=[ep_aletDer,ep_aletIzq]
G4.addLstLoads(G4_lstLoads)

#Sobrecarga sobre relleno trasdós
SCep_zap=loads.UniformLoadOnSurfaces(name= 'rell_zap',xcSet=zapTrasdos,loadVector= xc.Vector([0,0,-qunifTerr]))
qunifTrasdos=ep.StripLoadOnBackfill(qLoad=qunifTerr, zLoad=zGround,distWall=0, stripWidth=10)
'''
SCep_aletIzq= loads.EarthPressLoad(name= 'SCep_aletIzq', xcSet=aletIzq,soilData=None, vDir=xc.Vector([-1,0,0]))
SCep_aletIzq.stripLoads=[qunifTrasdos]
SCep_aletDer= loads.EarthPressLoad(name= 'SCep_aletDer', xcSet=aletDer,soilData=None, vDir=xc.Vector([1,0,0]))
SCep_aletDer.stripLoads=[qunifTrasdos]
'''
SCep_murEstr= loads.EarthPressLoad(name= 'SCep_murEstr', xcSet=murEstrSet,soilData=None, vDir=xc.Vector([0,1,0]))
SCep_murEstr.stripLoads=[qunifTrasdos]

Q4=lcases.LoadCase(preprocessor=prep,name="Q4",loadPType="default",timeSType="constant_ts")
Q4.create()
Q4.addLstLoads([SCep_murEstr,SCep_zap])
