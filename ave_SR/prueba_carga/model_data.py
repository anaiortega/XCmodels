# -*- coding: utf-8 -*-
from __future__ import division

import os
import xc_base
import geom
import xc
import math
import numpy as np
from model import predefined_spaces
from model.geometry import grid_model as gm
from model.mesh import finit_el_model as fem
from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets
from materials import typical_materials as tm
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc
from actions.earth_pressure import earth_pressure as ep

# AVE San Rafael-Cuarto de la Jara
# Prueba de carga PF+OD-107.68

#Auxiliary data

Lmarco=18.5                  #longitud del marco (m)
eBalasto=0.5                 #espesor medio de balasto debajo del carri
eRell=1.4                    #espesor medio de rellenos sobre dintel
hTraviesa=0.23               #canto de la traviesa
lTraviesa=2.60               #longitud de la traviesa (m)
distTrav=0.6                 #distancia entre traviesas


 #Geometry
GH=12                          #gálibo horizontal
GV=3.5                        #gálibo vertical
deckTh=1.10                   #espesor dintel
wallTh=0.90                   #espesor hastiales
baseSlabTh=1.10               #espesor losa de cimentación
anchvia=1.435                 #ancho de vía (m)

# Valores auxiliares cargas
alfa=1.21                     #coeficiente de clasificación
coefImp=1.27                  #coeficiente de impacto reducido
densrell=2e3                  #densidad del relleno (kg/m3)
densbal=1.8e3                 #densidad del balasto (kg/m3)
Qptren=alfa*125*1e3           #carga puntual (rueda) tren de cargas (N)
nQptren_carr=4                #nº de cargas puntuales tren de carga en cada carril
xcarr1=6.1
xcarr2=7.6
xcarr3=10.8
xcarr4=12.4

distEjesTren=1.6           #distancia entre cargas puntuales en cada carril
Kbalasto=8.955e4*1e3                  #coef. balasto (N/m3)
Kbalasto=Kbalasto*1e5     #!!!!!borrar
# Empuje de tierras
fi_terr=30                            #ángulo de rozamiento interno
K0=1-math.sin(math.radians(fi_terr))  #coeficiente de empuje al reposo

#  Materiales
#*Auxiliary data
'''
fcmDeck=(30+8)*1e6                       #HA-30 strength  (Pa)
EcDeck=8500*(fcmDeck/1e6)**(1/3.0)*1e6     # elastic modulus (Pa)
fcmWalls=(30+8)*1e6                      #HA-30 strength  (Pa)
EcWalls=8500*(fcmWalls/1e6)**(1/3.0)*1e6   # elastic modulus (Pa)
fcmFound=(30+8)*1e6                      #HA-30 strength  (Pa)
EcFound=8500*(fcmFound/1e6)**(1/3.0)*1e6   #(Pa)
'''

cpoish=0.2                               #Poisson's coefficient of concrete
densh= 2500                              #specific mass of concrete (kg/m3)

# módulo elástico del hormigón para cargas instantáneas o rápidamente
#variables
EcDeck=33577*1e6 
EcWalls=EcDeck
EcFound=EcDeck


#Datos de los camiones para la prueba de carga
nCam=5     #número de camiones
distEjLCam=3.4 # distancia entre ejes longitudinales de camiones
#yEje1Cam=7.85/2.  #coordenada Y del eje 1 de los caminones
yEje1Cam=7.85-3  #coordenada Y del eje 1 de los caminones
yEje2Cam=yEje1Cam-3.5  #coordenada Y del eje 2 de los caminones
yEje3Cam=yEje2Cam-3.0  #coordenada Y del eje 2 de los caminones
yEje4Cam=yEje3Cam-1.35 #coordenada Y del eje 2 de los caminones

distRuedCam=2.0        #distancia entre ruedas del mismo eje
Qeje1Cam=70e3          #carga eje 1 camión (N)
Qeje2Cam=110e3         #carga eje 2 camión (N)
Qeje3Cam=100e3         #carga eje 3 camión (N)
Qeje4Cam=100e3         #carga eje 4 camión (N)

# la carga puntual del camión se reparte en el hormigón a 45º hasta
# el plano medio del dintel. Calculamos la carga uniforme transmitida
# por cada rueda sobre una superficie (deckTh x deckTh)
qunifeje1Cam=Qeje1Cam/2.0/(deckTh**2)
qunifeje2Cam=Qeje2Cam/2.0/(deckTh**2)
qunifeje3Cam=Qeje3Cam/2.0/(deckTh**2)
qunifeje4Cam=Qeje4Cam/2.0/(deckTh**2)

eSize=0.30                             #tamaño medio de los elementos
#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3

# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)

# coordinates in global X,Y,Z axes for the grid generation
xRueda=(Lmarco-(nCam-1)*distEjLCam-distRuedCam)/2.0
xList=[0]
for i in range(1,nCam+1):
    xList.append(xRueda-deckTh/2.0)
    xList.append(xRueda+deckTh/2.0)
    xList.append(xRueda+distRuedCam-deckTh/2.0)
    xList.append(xRueda+distRuedCam+deckTh/2.0)
    xRueda+=distEjLCam
xList.append(Lmarco)
    
yList=[-GH/2-wallTh/2.0]
yList.append(yEje4Cam-deckTh/2.0)
yList.append(yEje4Cam+deckTh/2.0)
yList.append(yEje3Cam-deckTh/2.0)
yList.append(yEje3Cam+deckTh/2.0)
yList.append(yEje2Cam-deckTh/2.0)
yList.append(yEje2Cam+deckTh/2.0)
yList.append(yEje1Cam-deckTh/2.0)
yList.append(yEje1Cam+deckTh/2.0)
yList.append(GH/2+wallTh/2.0)
    
zList=[0,baseSlabTh/2+GV+deckTh/2]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()


#Ranges for lines and surfaces
losCim_rg= [ gm.IJKRange((0,0,0),(lastXpos,lastYpos,0))]
hastiales_rg= [ gm.IJKRange((0,0,0),(lastXpos,0,lastZpos)),gm.IJKRange((0,lastYpos,0),(lastXpos,lastYpos,lastZpos))]
dintel_rg= [ gm.IJKRange((0,0,lastZpos),(lastXpos,lastYpos,lastZpos))]
murete_i_rg=[gm.IJKRange((0,0,lastZpos),(0,lastYpos,lastZpos))]
murete_d_rg=[gm.IJKRange((lastXpos,0,lastZpos),(lastXpos,lastYpos,lastZpos))]

#Surfaces generation
losCim=gridGeom.genSurfMultiRegion(lstIJKRange=losCim_rg,nameSet='losCim')
hastiales=gridGeom.genSurfMultiRegion(lstIJKRange=hastiales_rg,nameSet='hastiales')
dintel=gridGeom.genSurfMultiRegion(lstIJKRange=dintel_rg,nameSet='dintel')

#Lines generation
murete_i=gridGeom.genLinMultiRegion(lstIJKRange=murete_i_rg,nameSet='murete_i')
murete_d=gridGeom.genLinMultiRegion(lstIJKRange=murete_d_rg,nameSet='murete_d')



#                         *** MATERIALS *** 

concrDeck=tm.MaterialData(name='concrDeck',E=EcDeck,nu=cpoish,rho=densh)
concrWalls=tm.MaterialData(name='concrWalls',E=EcWalls,nu=cpoish,rho=densh)
concrFound=tm.MaterialData(name='concrFound',E=EcFound,nu=cpoish,rho=densh)

#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectMuretes=sectpr.RectangularSection(name='geomSectMuretes',b=0.5,h=0.5)

# Elastic material-section appropiate for 3D beam analysis, including shear
  # deformations.
  # Attributes:
  #   name:         name identifying the section
  #   section:      instance of a class that defines the geometric and
  #                 mechanical characteristiscs
  #                 of a section (e.g: RectangularSection, CircularSection,
  #                 ISection, ...)
  #   material:     instance of a class that defines the elastic modulus,
  #                 shear modulus and mass density of the material

muretes_mat= tm.BeamMaterialData(name= 'muretes_mat', section=geomSectMuretes, material=concrDeck)
muretes_mat.setupElasticShear3DSection(preprocessor=prep)

# Isotropic elastic section-material appropiate for plate and shell analysis
deck_mat= tm.DeckMaterialData(name= 'deck_mat', thickness= deckTh,material=concrDeck)
deck_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
wall_mat= tm.DeckMaterialData(name= 'wall_mat', thickness= wallTh,material=concrWalls)
wall_mat.setupElasticSection(preprocessor=prep)   #creates de section-material
found_mat= tm.DeckMaterialData(name= 'found_mat', thickness= baseSlabTh,material=concrFound)
found_mat.setupElasticSection(preprocessor=prep)   #creates de section-material

#                         ***FE model - MESH***

losCim_mesh=fem.SurfSetToMesh(surfSet=losCim,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)
hastiales_mesh=fem.SurfSetToMesh(surfSet=hastiales,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)
dintel_mesh=fem.SurfSetToMesh(surfSet=dintel,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)

fem.multi_mesh(preprocessor=prep,lstMeshSets=[losCim_mesh,hastiales_mesh,dintel_mesh])

murete_i_mesh=fem.LinSetToMesh(linSet=murete_i,matSect=muretes_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,0,1]),elemType='ElasticBeam3d',coordTransfType='linear')
murete_i_mesh.generateMesh(prep)    # mesh this set of lines
murete_d_mesh=fem.LinSetToMesh(linSet=murete_d,matSect=muretes_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,0,1]),elemType='ElasticBeam3d',coordTransfType='linear')
murete_d_mesh.generateMesh(prep)    # mesh this set of lines

overallSet=losCim+hastiales+dintel

#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
#foundationElasticSupports=
from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets
from materials import typical_materials as tm
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc
from actions.earth_pressure import earth_pressure as ep


#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
cRoz=0.5
foundationElasticSupports=sprbc.ElasticFoundation(wModulus=Kbalasto,cRoz=cRoz)
foundationElasticSupports.generateSprings(xcSet=losCim)

#                       ***ACTIONS***
# Auxiliary ranges and sets

surf_eje1_rg=list()
for i in range(nCam):
    surf_eje1_rg.append(gm.IJKRange([4*i+1,7,lastZpos],[4*i+2,8,lastZpos]))
    surf_eje1_rg.append(gm.IJKRange([4*i+3,7,lastZpos],[4*i+4,8,lastZpos]))
surf_eje1_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=surf_eje1_rg,nameSet='surf_eje1_set')
    
surf_eje2_rg=list()
for i in range(nCam):
    surf_eje2_rg.append(gm.IJKRange([4*i+1,5,lastZpos],[4*i+2,6,lastZpos]))
    surf_eje2_rg.append(gm.IJKRange([4*i+3,5,lastZpos],[4*i+4,6,lastZpos]))
surf_eje2_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=surf_eje2_rg,nameSet='surf_eje2_set')

surf_eje3_rg=list()
for i in range(nCam):
    surf_eje3_rg.append(gm.IJKRange([4*i+1,3,lastZpos],[4*i+2,4,lastZpos]))
    surf_eje3_rg.append(gm.IJKRange([4*i+3,3,lastZpos],[4*i+4,4,lastZpos]))
surf_eje3_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=surf_eje3_rg,nameSet='surf_eje3_set')

surf_eje4_rg=list()
for i in range(nCam):
    surf_eje4_rg.append(gm.IJKRange([4*i+1,1,lastZpos],[4*i+2,2,lastZpos]))
    surf_eje4_rg.append(gm.IJKRange([4*i+3,1,lastZpos],[4*i+4,2,lastZpos]))
surf_eje4_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=surf_eje4_rg,nameSet='surf_eje4_set')
'''
#Balasto
bal_tali_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxmxp1,0,lastZpos],[pxcarr1-1,lastYpos,lastZpos]),nameSet='bal_tali_set')
bal_i_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxcarr1-1,0,lastZpos],[pxcarr3-1,lastYpos,lastZpos]),nameSet='bal_i_set')
bal_d_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxcarr3-1,0,lastZpos],[pxcarr4+1,lastYpos,lastZpos]),nameSet='bal_d_set')
bal_tald_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxcarr4+1,0,lastZpos],[pxmnp2,lastYpos,lastZpos]),nameSet='bal_tald_set')
paseos_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange([pxmnp1,pyhast1,lastZpos],[pxmxp1,pyhast2,lastZpos]),gm.IJKRange([pxmnp2,pyhast1,lastZpos],[pxmxp2,pyhast2,lastZpos])],nameSet='paseos_set')
#Losa cimentación interior marco
losc_int_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([0,pyhast1,0],[lastXpos,pyhast2,0]),nameSet='losc_int_set')
'''

#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
selfWeight= loads.InertialLoad(name='selfWeight', lstMeshSets=[hastiales_mesh,losCim_mesh,dintel_mesh,murete_i_mesh,murete_d_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))


# Uniform loads applied on shell elements
#    name:       name identifying the load
#    xcSet:     set that contains the surfaces
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)

# Camiones prueba de carga
sc_cam_eje1=loads.UniformLoadOnSurfaces(name= 'sc_cam_eje1',xcSet=surf_eje1_set,loadVector= xc.Vector([0,0,-qunifeje1Cam,0,0,0]))
sc_cam_eje2=loads.UniformLoadOnSurfaces(name= 'sc_cam_eje2',xcSet=surf_eje2_set,loadVector= xc.Vector([0,0,-qunifeje2Cam,0,0,0]))
sc_cam_eje3=loads.UniformLoadOnSurfaces(name= 'sc_cam_eje3',xcSet=surf_eje3_set,loadVector= xc.Vector([0,0,-qunifeje3Cam,0,0,0]))
sc_cam_eje4=loads.UniformLoadOnSurfaces(name= 'sc_cam_eje4',xcSet=surf_eje4_set,loadVector= xc.Vector([0,0,-qunifeje4Cam,0,0,0]))
# Balasto y relleno sobre dintel
cp_dintel=loads.UniformLoadOnSurfaces(name= 'cp_dintel',xcSet=dintel,loadVector= xc.Vector([0,0,-(eRell*densrell+eBalasto*densbal)*grav,0,0,0]))



# Superficie de reparto sobre el dintel de las cargas puntuales del tren de cargas
# en cada carril
Qptren_carr=nQptren_carr*Qptren
L_Qptren_carr=(nQptren_carr-1)*distEjesTren

def polygon(xCent,yCent,Lx,Ly):
    pol=geom.Polygon2d()
    pol.agregaVertice(geom.Pos2d(xCent-Lx/2.0,yCent-Ly/2.0))
    pol.agregaVertice(geom.Pos2d(xCent-Lx/2.0,yCent+Ly/2.0))
    pol.agregaVertice(geom.Pos2d(xCent+Lx/2.0,yCent+Ly/2.0))
    pol.agregaVertice(geom.Pos2d(xCent+Lx/2.0,yCent-Ly/2.0))
    return pol


def qPuntEjeSobreBalasto(prep,setBusq,hBalast,eDintel,angrepBalastRad,x_punt,y_punt,lTrav,distTrav,Qpunt,nameToLoad):
#   Carga repartida sobre el dintel debida a la carga puntual de un eje del tren de cargas n vías sobre balasto. La carga vertical puntual actuando sobre el carril se reparte a lo largo de tres traviesas consecutivas, (En el hormigón se reparte a 45º)

    Lx=lTrav+2*hBalast*math.tan(angrepBalastRad)+eDintel
    Ly=2*distTrav
    pol=polygon(xCent=x_punt,yCent=y_punt,Lx=Lx,Ly=Ly)
    aux_set=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=setBusq,prismBase=pol,prismAxis='Z',setName='aux_set'+nameToLoad)
    if aux_set.getNumElements==0:
        print 'OJO!! no encuentro elementos para repartir la carga ', nameToLoad
    areaSet=np.sum([e.getArea(False) for e in aux_set.getElements])
    return loads.UniformLoadOnSurfaces(name=nameToLoad,xcSet=aux_set,loadVector=xc.Vector([0,0,-Qpunt/areaSet,0,0,0]),refSystem='Global')
    
angrepBalastRad=math.atan(1/4.)
    

QpuntEje=2*Qptren
y_cent=0
y_e1=y_cent-1.5*distEjesTren
y_e2=y_cent-0.5*distEjesTren
y_e3=y_cent+0.5*distEjesTren
y_e4=y_cent+1.5*distEjesTren
#Cargas puntuales vía 1
x_punt=(xcarr1+xcarr2)/2.0
hBalast=eBalasto+eRell
# eje 1
Qptren_v1_e1=qPuntEjeSobreBalasto(prep=prep,setBusq=dintel,hBalast=hBalast,eDintel=deckTh,angrepBalastRad=angrepBalastRad,x_punt=x_punt,y_punt=y_e1,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v1_e1')
# eje 2
Qptren_v1_e2=qPuntEjeSobreBalasto(prep=prep,setBusq=dintel,hBalast=hBalast,eDintel=deckTh,angrepBalastRad=angrepBalastRad,x_punt=x_punt,y_punt=y_e2,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v1_e2')
# eje 3
Qptren_v1_e3=qPuntEjeSobreBalasto(prep=prep,setBusq=dintel,hBalast=hBalast,eDintel=deckTh,angrepBalastRad=angrepBalastRad,x_punt=x_punt,y_punt=y_e3,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v1_e3')
# eje 4
Qptren_v1_e4=qPuntEjeSobreBalasto(prep=prep,setBusq=dintel,hBalast=hBalast,eDintel=deckTh,angrepBalastRad=angrepBalastRad,x_punt=x_punt,y_punt=y_e4,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v1_e4')

#Cargas puntuales vía 2
x_punt=(xcarr3+xcarr4)/2.0
# eje 1
Qptren_v2_e1=qPuntEjeSobreBalasto(prep=prep,setBusq=dintel,hBalast=hBalast,eDintel=deckTh,angrepBalastRad=angrepBalastRad,x_punt=x_punt,y_punt=y_e1,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v2_e1')
# eje 2
Qptren_v2_e2=qPuntEjeSobreBalasto(prep=prep,setBusq=dintel,hBalast=hBalast,eDintel=deckTh,angrepBalastRad=angrepBalastRad,x_punt=x_punt,y_punt=y_e2,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v2_e2')
# eje 3
Qptren_v2_e3=qPuntEjeSobreBalasto(prep=prep,setBusq=dintel,hBalast=hBalast,eDintel=deckTh,angrepBalastRad=angrepBalastRad,x_punt=x_punt,y_punt=y_e3,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v2_e3')
# eje 4
Qptren_v2_e4=qPuntEjeSobreBalasto(prep=prep,setBusq=dintel,hBalast=hBalast,eDintel=deckTh,angrepBalastRad=angrepBalastRad,x_punt=x_punt,y_punt=y_e4,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v2_e4')



# Earth pressure applied to shell or beam elements
#     Attributes:
#     name:       name identifying the load
#     xcSet:      set that contains the elements to be loaded
#     EarthPressureModel: instance of the class EarthPressureModel, with 
#                 the following attributes:
#                   K:Coefficient of pressure
#                   zGround:global Z coordinate of ground level
#                   gammaSoil: weight density of soil 
#                   zWater: global Z coordinate of groundwater level 
#                   (if zGroundwater<minimum z of model => there is no groundwater)
#                   gammaWater: weight density of water
#     if EarthPressureModel==None no earth thrust is considered
#     vDir: unit xc vector defining pressures direction

# auxiliary sets
#   muro izquierdo
muri_z1_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((0,0,0),(lastXpos,0,lastZpos))],nameSet='muri_z1_set')
#   muro derecho
murd_z1_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((0,lastYpos,0),(lastXpos,lastYpos,lastZpos))],nameSet='murd_z1_set')

# empuje del terreno
zGroundZ1=zList[lastZpos]+deckTh/2.0

soilZ1=ep.EarthPressureModel(K=K0, zGround=zGroundZ1, gammaSoil=densrell*grav, zWater=-10.0, gammaWater=grav)

ep_muri_z1= loads.EarthPressLoad(name= 'ep_muri_z1', xcSet=muri_z1_set,soilData=soilZ1, vDir=xc.Vector([0,1,0]))

ep_murd_z1= loads.EarthPressLoad(name= 'ep_murd_z1', xcSet=murd_z1_set,soilData=soilZ1, vDir=xc.Vector([0,-1,0]))
#    ***LOAD CASES***
# G1: Peso propio
G1=lcases.LoadCase(preprocessor=prep,name="G1",loadPType="default",timeSType="constant_ts")
G1.create()
G1.addLstLoads([selfWeight])
#G2: carga muerta sobre dintel


G2=lcases.LoadCase(preprocessor=prep,name="G2",loadPType="default",timeSType="constant_ts")
G2.create()
G2.addLstLoads([cp_dintel])

# G3: Empuje del terreno
G3=lcases.LoadCase(preprocessor=prep,name="G3",loadPType="default",timeSType="constant_ts")
G3.create()
G3.addLstLoads([ep_muri_z1,ep_murd_z1])

# Q1 Tren de cargas camiones

Q1=lcases.LoadCase(preprocessor=prep,name="Q1",loadPType="default",timeSType="constant_ts")
Q1.create()
Q1.addLstLoads([sc_cam_eje1,sc_cam_eje2,sc_cam_eje3,sc_cam_eje4])

# Q2 Tren de cargas tren ambas vías

Q2=lcases.LoadCase(preprocessor=prep,name="Q2",loadPType="default",timeSType="constant_ts")
Q2.create()
Q2.addLstLoads([Qptren_v1_e1,Qptren_v1_e2,Qptren_v1_e3,Qptren_v1_e4,
                Qptren_v2_e1,Qptren_v2_e2,Qptren_v2_e3,Qptren_v2_e4])

# Q3 Tren de cargas tren una sola vía

Q3=lcases.LoadCase(preprocessor=prep,name="Q3",loadPType="default",timeSType="constant_ts")
Q3.create()
Q3.addLstLoads([Qptren_v1_e1,Qptren_v1_e2,Qptren_v1_e3,Qptren_v1_e4])

#    ***LIMIT STATE COMBINATIONS***
combContainer= cc.CombContainer()  #Container of load combinations

combContainer.ULS.perm.add("ELU001","1.00*G1 + 1.00*G3")
combContainer.ULS.perm.add("ELU002","1.00*G1 + 1.00*G3+1.00*Q1")
combContainer.ULS.perm.add("ELU003","1.00*G1 + 1.00*G2 + 1.00*G3 + 1.00*Q2")

def polygon(xCent,yCent,Lx,Ly):
    pol=geom.Polygon2d()
    pol.agregaVertice(geom.Pos2d(xCent-Lx/2.0,yCent-Ly/2.0))
    pol.agregaVertice(geom.Pos2d(xCent-Lx/2.0,yCent+Ly/2.0))
    pol.agregaVertice(geom.Pos2d(xCent+Lx/2.0,yCent+Ly/2.0))
    pol.agregaVertice(geom.Pos2d(xCent+Lx/2.0,yCent-Ly/2.0))
    return pol

L=xList[-1]
pol=polygon(xCent=L/2.0,yCent=0,Lx=L+10,Ly=eSize)
dintelBcentral=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=dintel,prismBase=pol,prismAxis='Z',setName='dintelBcentral')


