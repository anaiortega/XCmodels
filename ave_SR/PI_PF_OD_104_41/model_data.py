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
from postprocess.config import colors
from postprocess.config import sp_captions as cpt


# AVE San Rafael-Cuarto de la Jara
# PI_PF_OD_104_41

#Auxiliary data
 #Geometry
GH=12                         #gálibo horizontal
GV=5.8                        #gálibo vertical
deckTh=1.20                   #espesor dintel
wallTh=1.00                   #espesor hastiales
baseSlabTh=1.20               #espesor losa de cimentación
Hrelli=4.286                  #ver gráfico en memoria de cálculo
Hrelld=4.389                  #ver gráfico en memoria de cálculo
Hbali=0.579                   #ver gráfico en memoria de cálculo
Hbald=0.665                   #ver gráfico en memoria de cálculo
Hcarr1=5.12                   #ver gráfico en memoria de cálculo
Hcarr2=5.21                   #ver gráfico en memoria de cálculo
Hcarr3=5.21                   #ver gráfico en memoria de cálculo
Hcarr4=5.30                   #ver gráfico en memoria de cálculo
pxcarr1=7                     #posición en matriz xk de carril 1
pxcarr2=8                     #posición en matriz xk de carril 2
pxcarr3=10                    #posición en matriz xk de carril 3
pxcarr4=11                    #posición en matriz xk de carril 4
pyhast1=1                     #posición en la matriz yk del hastial izqdo.
pyhast2=4                     #posición en la matriz yk del hastial drcho.
pxcan1=4                      #posición en matriz xk de canal de cables 1
pxcan2=15                     #posición en matriz xk de canal de cables 2
pxmnp1=4                      #posición en matriz xk X mínima de paseo 1
pxmxp1=5                      #posición en matriz xk X máxima de paseo 1
pxmnp2=13                     #posición en matriz xk X mínima de paseo 2
pxmxp2=14                     #posición en matriz xk X máxima de paseo 2
anchvia=1.435                 #ancho de vía (m)
hmuret=0.5                    #altura de muretes en extremos de estructura
emuret=0.5                    #espesor de muretes en extremos de estructura

hTraviesa=0.23               #canto de la traviesa
lTraviesa=2.60               #longitud de la traviesa (m)
distTrav=0.6                 #distancia entre traviesas

hcarril=0.172

pxmn_M2=4                     #posición x mínima módulo 2 (M2:módulo central)
pxmx_M2=14                    #posición x máxima módulo 2 (M2:módulo central)

# Valores auxiliares cargas
pteRepBal=1/4.                # pendiente en balasto del reparto de cargas (H/V)
pteRepRell=1/2.               # pendiente en rellenos del reparto de cargas (H/V)
pteRepConcr=1                 # pendiente en hormigón del reparto de cargas (H/V)

hTotal=(Hrelli+Hrelld)/2.0+(Hbali+Hbald)/2.0+deckTh/2.0
bTotal=(Hrelli+Hrelld)/2.0*pteRepRell+(Hbali+Hbald)/2.0*pteRepBal+deckTh/2.0*pteRepConcr
angrep=math.degrees(math.atan(bTotal/hTotal))

alfa=1.21                     #coeficiente de clasificación
fired=1.00                    #coeficiente de impacto reducido
densrell=2e3                  #densidad del relleno (kg/m3)
densbal=1.8e3                 #densidad del balasto (kg/m3)
Qptren=alfa*fired*125*1e3     #carga puntual tren de cargas (N)
nQptren_carr=4                #nº de cargas puntuales tren de carga en cada carril
distEjesTren=1.6           #distancia entre cargas puntuales en cada carril
qltren=alfa*fired*40*1e3      #carga lineal tren de cargas (N/m)
qnferr=2.5*1e3                #carga uniforme no ferroviaria en paseos (N/m2)
scterr=alfa*30*1e3            #sobrecarga en terraplén (N/m2)
qdesc1=alfa*0.7*(8*125)/((nQptren_carr-1)*distEjesTren)*1e3   #carga lineal en situación de descarrilamiento 1 (N/m)
qdesc2=alfa*1.4*(8*125)/20*1e3            #carga lineal en situación de descarrilamiento 2 (N/m)
Hagua=0.00                            #nivel de agua sobre la cara superior de la losa de cimentación
Kbalasto=5.281e4*1e3                  #coef. balasto (N/m3)
ql_carr_trav=(0.6+2.6)*1e3            #carga lineal peso carril + traviesas (N/m)
ql_can_cabl=3*1e3                     #carga lineal peso canal de cables (N/m)
 # tren de carga carreteras
cunifCarr=4*1e3                       #carga uniforme tren de cargas carreteras (N/m2)
qpCarr=100*1e3                        #carga puntual tren carreteras(N)
lejesCarr=1.5                         #distancia entre ejes tren carreteras
lruedCarr=2                           #distancia entre ruedas tren de carreteras
qlConstruct=23*1e3                    #carga lineal eje en vehículo en fase construcción (N/m)
# Empuje de tierras
fi_terr=30                            #ángulo de rozamiento interno
K0=1-math.sin(math.radians(fi_terr))  #coeficiente de empuje al reposo

# Materials
#*Auxiliary data 
fcmDeck=(30+8)*1e6                       #HA-30 strength  (MPa)
EcDeck=8500*(fcmDeck/1e6)**(1/3.0)*1e6     # elastic modulus (MPa)
fcmWalls=(30+8)*1e6                      #HA-30 strength  (MPa)
EcWalls=8500*(fcmWalls/1e6)**(1/3.0)*1e6   # elastic modulus (MPa)
fcmFound=(30+8)*1e6                      #HA-30 strength  (MPa)
EcFound=8500*(fcmFound/1e6)**(1/3.0)*1e6   #(MPa)
cpoish=0.2                               #Poisson's coefficient of concrete
densh= 2500                              #specific mass of concrete (kg/m3)


eSize=0.40                             #tamaño medio de los elementos
#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
preprocessor=prep

# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)

# coordinates in global X,Y,Z axes for the grid generation
daux1=8.87
daux2=31.5-22.18
xList=[0,daux1/3.,2*daux1/3.,
       8.87,8.90,10.19,11.03,12.152,13.56,14.94,16.82,18.26,19.36,20.55,22.13,
       22.18,22.18+daux2/3., 22.18+2*daux2/3.,
       31.5]
yList=[-GH/2-wallTh-0.5,-GH/2-wallTh/2,-GH/2-wallTh/2+wallTh/2+0.2*GH]
yList.append(-yList[2])
yList.append(-yList[1])
yList.append(-yList[0])
zList=[0,baseSlabTh/2+0.2*GV,baseSlabTh/2+0.8*GV,baseSlabTh/2+GV+deckTh/2]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()

'''
#Displacements of the grid points in a range
for i in range(1,len(xList)):
    r= gm.IJKRange((i,0,lastZpos),(i,lastYpos,lastZpos))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,-trSlope*xList[i]]))

for j in range(1,len(yList)):
    r=gm.IJKRange((0,j,0),(lastXpos,j,0))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,lnSlope*yList[j]]))

#Slope (in X direction, Y direction or both) the grid points in a range
#syntax: slopePointsRange(ijkRange,slopeX,xZeroSlope,slopeY,yZeroSlope)
#     ijkRange: range for the search.
#     slopeX: slope in X direction, expressed as deltaZ/deltaX 
#                       (defaults to 0 = no slope applied)
#     xZeroSlope: coordinate X of the "rotation axis".
#     slopeY: slope in Y direction, expressed as deltaZ/deltaY)
#                       (defaults to 0 = no slope applied)
#     yZeroSlope: coordinate Y of the "rotation axis".

'''

#Ranges for lines and surfaces
losCimExt_M1_rg= [ gm.IJKRange((0,0,0),(pxmn_M2-1,pyhast1+1,0)), gm.IJKRange((0,pyhast2-1,0),(pxmn_M2-1,lastYpos,0)) ]
losCimExt_M2_rg= [ gm.IJKRange((pxmn_M2,0,0),(pxmx_M2,pyhast1+1,0)), gm.IJKRange((pxmn_M2,pyhast2-1,0),(pxmx_M2,lastYpos,0)) ]
losCimExt_M3_rg= [ gm.IJKRange((pxmx_M2+1,0,0),(lastXpos,pyhast1+1,0)), gm.IJKRange((pxmx_M2+1,pyhast2-1,0),(lastXpos,lastYpos,0)) ]

losCimCent_M1_rg= [ gm.IJKRange((0,pyhast1+1,0),(pxmn_M2-1,pyhast2-1,0))]
losCimCent_M2_rg= [ gm.IJKRange((pxmn_M2,pyhast1+1,0),(pxmx_M2,pyhast2-1,0))]
losCimCent_M3_rg= [ gm.IJKRange((pxmx_M2+1,pyhast1+1,0),(lastXpos,pyhast2-1,0))]

hastIzq_M1_rg= [ gm.IJKRange((0,pyhast1,0),(pxmn_M2-1,pyhast1,lastZpos))]
hastIzq_M2_rg= [ gm.IJKRange((pxmn_M2,pyhast1,0),(pxmx_M2,pyhast1,lastZpos))]
hastIzq_M3_rg= [ gm.IJKRange((pxmx_M2+1,pyhast1,0),(lastXpos,pyhast1,lastZpos))]

hastDer_M1_rg= [ gm.IJKRange((0,pyhast2,0),(pxmn_M2-1,pyhast2,lastZpos))]
hastDer_M2_rg= [ gm.IJKRange((pxmn_M2,pyhast2,0),(pxmx_M2,pyhast2,lastZpos))]
hastDer_M3_rg= [ gm.IJKRange((pxmx_M2+1,pyhast2,0),(lastXpos,pyhast2,lastZpos))]

dintExt_M1_rg= [ gm.IJKRange((0,pyhast1,lastZpos),(pxmn_M2-1,pyhast1+1,lastZpos)), gm.IJKRange((0,pyhast2-1,lastZpos),(pxmn_M2-1,pyhast2,lastZpos)) ]
dintExt_M2_rg= [ gm.IJKRange((pxmn_M2,pyhast1,lastZpos),(pxmx_M2,pyhast1+1,lastZpos)), gm.IJKRange((pxmn_M2,pyhast2-1,lastZpos),(pxmx_M2,pyhast2,lastZpos)) ]
dintExt_M3_rg= [ gm.IJKRange((pxmx_M2+1,pyhast1,lastZpos),(lastXpos,pyhast1+1,lastZpos)), gm.IJKRange((pxmx_M2+1,pyhast2-1,lastZpos),(lastXpos,pyhast2,lastZpos)) ]

dintCent_M1_rg= [ gm.IJKRange((0,pyhast1+1,lastZpos),(pxmn_M2-1,pyhast2-1,lastZpos))]
dintCent_M2_rg= [ gm.IJKRange((pxmn_M2,pyhast1+1,lastZpos),(pxmx_M2,pyhast2-1,lastZpos))]
dintCent_M3_rg= [ gm.IJKRange((pxmx_M2+1,pyhast1+1,lastZpos),(lastXpos,pyhast2-1,lastZpos))]

muretes_rg=[gm.IJKRange((0,pyhast1,lastZpos),(0,pyhast2,lastZpos)),gm.IJKRange((lastXpos,pyhast1,lastZpos),(lastXpos,pyhast2,lastZpos))]


#Surfaces generation
losCimExt_M1=gridGeom.genSurfMultiRegion(lstIJKRange=losCimExt_M1_rg,nameSet='losCimExt_M1')
losCimExt_M2=gridGeom.genSurfMultiRegion(lstIJKRange=losCimExt_M2_rg,nameSet='losCimExt_M2')
losCimExt_M3=gridGeom.genSurfMultiRegion(lstIJKRange=losCimExt_M3_rg,nameSet='losCimExt_M3')

losCimCent_M1=gridGeom.genSurfMultiRegion(lstIJKRange=losCimCent_M1_rg,nameSet='losCimCent_M1')
losCimCent_M2=gridGeom.genSurfMultiRegion(lstIJKRange=losCimCent_M2_rg,nameSet='losCimCent_M2')
losCimCent_M3=gridGeom.genSurfMultiRegion(lstIJKRange=losCimCent_M3_rg,nameSet='losCimCent_M3')

hastIzq_M1=gridGeom.genSurfMultiRegion(lstIJKRange=hastIzq_M1_rg,nameSet='hastIzq_M1')
hastIzq_M2=gridGeom.genSurfMultiRegion(lstIJKRange=hastIzq_M2_rg,nameSet='hastIzq_M2')
hastIzq_M3=gridGeom.genSurfMultiRegion(lstIJKRange=hastIzq_M3_rg,nameSet='hastIzq_M3')

hastDer_M1=gridGeom.genSurfMultiRegion(lstIJKRange=hastDer_M1_rg,nameSet='hastDer_M1')
hastDer_M2=gridGeom.genSurfMultiRegion(lstIJKRange=hastDer_M2_rg,nameSet='hastDer_M2')
hastDer_M3=gridGeom.genSurfMultiRegion(lstIJKRange=hastDer_M3_rg,nameSet='hastDer_M3')

dintExt_M1=gridGeom.genSurfMultiRegion(lstIJKRange=dintExt_M1_rg,nameSet='dintExt_M1')
dintExt_M2=gridGeom.genSurfMultiRegion(lstIJKRange=dintExt_M2_rg,nameSet='dintExt_M2')
dintExt_M3=gridGeom.genSurfMultiRegion(lstIJKRange=dintExt_M3_rg,nameSet='dintExt_M3')

dintCent_M1=gridGeom.genSurfMultiRegion(lstIJKRange=dintCent_M1_rg,nameSet='dintCent_M1')
dintCent_M2=gridGeom.genSurfMultiRegion(lstIJKRange=dintCent_M2_rg,nameSet='dintCent_M2')
dintCent_M3=gridGeom.genSurfMultiRegion(lstIJKRange=dintCent_M3_rg,nameSet='dintCent_M3')

#Lines generation
muretes=gridGeom.genLinMultiRegion(lstIJKRange=muretes_rg,nameSet='muretes')
muretes.description='Muretes'


#                         *** MATERIALS *** 

concrDeck=tm.MaterialData(name='concrDeck',E=EcDeck,nu=cpoish,rho=densh)
concrWalls=tm.MaterialData(name='concrWalls',E=EcWalls,nu=cpoish,rho=densh)
concrFound=tm.MaterialData(name='concrFound',E=EcFound,nu=cpoish,rho=densh)

#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectMuretes=sectpr.RectangularSection(name='geomSectMuretes',b=emuret,h=hmuret)

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

losCimExt_M1_mesh=fem.SurfSetToMesh(surfSet=losCimExt_M1,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)
losCimExt_M2_mesh=fem.SurfSetToMesh(surfSet=losCimExt_M2,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)
losCimExt_M3_mesh=fem.SurfSetToMesh(surfSet=losCimExt_M3,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)

losCimCent_M1_mesh=fem.SurfSetToMesh(surfSet=losCimCent_M1,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)
losCimCent_M2_mesh=fem.SurfSetToMesh(surfSet=losCimCent_M2,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)
losCimCent_M3_mesh=fem.SurfSetToMesh(surfSet=losCimCent_M3,matSect=found_mat,elemType='ShellMITC4',elemSize=eSize)

hastIzq_M1_mesh=fem.SurfSetToMesh(surfSet=hastIzq_M1,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)
hastIzq_M2_mesh=fem.SurfSetToMesh(surfSet=hastIzq_M2,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)
hastIzq_M3_mesh=fem.SurfSetToMesh(surfSet=hastIzq_M3,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)

hastDer_M1_mesh=fem.SurfSetToMesh(surfSet=hastDer_M1,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)
hastDer_M2_mesh=fem.SurfSetToMesh(surfSet=hastDer_M2,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)
hastDer_M3_mesh=fem.SurfSetToMesh(surfSet=hastDer_M3,matSect=wall_mat,elemType='ShellMITC4',elemSize=eSize)

dintExt_M1_mesh=fem.SurfSetToMesh(surfSet=dintExt_M1,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)
dintExt_M2_mesh=fem.SurfSetToMesh(surfSet=dintExt_M2,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)
dintExt_M3_mesh=fem.SurfSetToMesh(surfSet=dintExt_M3,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)

dintCent_M1_mesh=fem.SurfSetToMesh(surfSet=dintCent_M1,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)
dintCent_M2_mesh=fem.SurfSetToMesh(surfSet=dintCent_M2,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)
dintCent_M3_mesh=fem.SurfSetToMesh(surfSet=dintCent_M3,matSect=deck_mat,elemType='ShellMITC4',elemSize=eSize)

fem.multi_mesh(preprocessor=prep,lstMeshSets=[losCimExt_M1_mesh,losCimExt_M2_mesh,losCimExt_M3_mesh,
                                              losCimCent_M1_mesh,losCimCent_M2_mesh,losCimCent_M3_mesh,
                                              hastIzq_M1_mesh,hastIzq_M2_mesh,hastIzq_M3_mesh,
                                              hastDer_M1_mesh,hastDer_M2_mesh,hastDer_M3_mesh,
                                              dintExt_M1_mesh,dintExt_M2_mesh,dintExt_M3_mesh,
                                              dintCent_M1_mesh,dintCent_M2_mesh,dintCent_M3_mesh])

muretes_mesh=fem.LinSetToMesh(linSet=muretes,matSect=muretes_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,0,1]),elemType='ElasticBeam3d',coordTransfType='linear')
muretes_mesh.generateMesh(prep)    # mesh this set of lines

overallSet=prep.getSets.getSet('total')
overallSet.description='Marco'
losCim=losCimExt_M1+losCimExt_M2+losCimExt_M3+losCimCent_M1+losCimCent_M2+losCimCent_M3
losCim.name='losCim'
losCim.description='Losa de cimentación'
hastIzq=hastIzq_M1+hastIzq_M2+hastIzq_M3
hastIzq.name='hastIzq'
hastIzq.description='Hastial izquierdo'
hastDer=hastDer_M1+hastDer_M2+hastDer_M3
hastDer.name='hastDer'
hastDer.description='Hastial derecho'
hastiales=hastIzq+hastDer
hastiales.description='Hastiales'
dintel=dintExt_M1+dintExt_M2+dintExt_M3+dintCent_M1+dintCent_M2+dintCent_M3
dintel.name='dintel'
dintel.description='Dintel'
loscPlusHasti=losCim+hastIzq

dintel_M1=dintExt_M1+dintCent_M1
dintel_M1.description='Dintel'
losCim_M1=losCimExt_M1+losCimCent_M1
losCim_M1.description='Losa de cimentación'
hastIzq_M1=hastIzq_M1
hastIzq_M1.description='Hastial izquierdo'
hastDer_M1=hastDer_M1
hastDer_M1.description='Hastial derecho'

dintel_M2=dintExt_M2+dintCent_M2
dintel_M2.description='Dintel'
losCim_M2=losCimExt_M2+losCimCent_M2
losCim_M2.description='Losa de cimentación'
hastIzq_M2=hastIzq_M2
hastIzq_M2.description='Hastial izquierdo'
hastDer_M2=hastDer_M2
hastDer_M2.description='Hastial derecho'

dintel_M1M2=dintExt_M1+dintExt_M2+dintCent_M1+dintCent_M2
dintel_M1M2.description='Dintel'
losCim_M1M2=losCimExt_M1+losCimExt_M2+losCimCent_M1+losCimCent_M2
losCim_M1M2.description='Losa de cimentación'
hastIzq_M1M2=hastIzq_M1+hastIzq_M2
hastIzq_M1M2.name='hastIzq_M1M2'
hastIzq_M1M2.description='Hastial izquierdo'
hastDer_M1M2=hastDer_M1+hastDer_M2
hastDer_M1M2.description='Hastial derecho'
losas_M1M2=dintel_M1M2+losCim_M1M2
losas_M1M2.name='losas_M1M2'
losas_M1M2.description='Losas'

M1_plus_M2=dintExt_M1+dintExt_M2+dintCent_M1+dintCent_M2+losCimExt_M1+losCimExt_M2+losCimCent_M1+losCimCent_M2+hastIzq_M1+hastIzq_M2+hastDer_M1+hastDer_M2
M1_plus_M2.name='M1_plus_M2'
M1_plus_M2.description='Módulos 1 y 2'
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
# Rellenos
rell_tali1_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxmnp1-4,0,lastZpos],[pxmnp1-3,lastYpos,lastZpos]),nameSet='rell_tali1_set')
rell_tali2_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxmnp1-3,0,lastZpos],[pxmnp1-2,lastYpos,lastZpos]),nameSet='rell_tali2_set')
rell_tali3_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxmnp1-2,0,lastZpos],[pxmnp1-1,lastYpos,lastZpos]),nameSet='rell_tali3_set')

rell_i_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxmnp1,0,lastZpos],[pxcarr3-1,lastYpos,lastZpos]),nameSet='rell_i_set')
rell_d_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxcarr3-1,0,lastZpos],[pxmxp2,lastYpos,lastZpos]),nameSet='rell_d_set')

rell_tald1_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxmxp2+3,0,lastZpos],[pxmxp2+4,lastYpos,lastZpos]),nameSet='rell_tald1_set')
rell_tald2_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxmxp2+2,0,lastZpos],[pxmxp2+3,lastYpos,lastZpos]),nameSet='rell_tald2_set')
rell_tald3_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxmxp2+1,0,lastZpos],[pxmxp2+2,lastYpos,lastZpos]),nameSet='rell_tald3_set')
#Balasto

bal_tali_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxmxp1,0,lastZpos],[pxcarr1-1,lastYpos,lastZpos]),nameSet='bal_tali_set')
bal_i_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxcarr1-1,0,lastZpos],[pxcarr3-1,lastYpos,lastZpos]),nameSet='bal_i_set')
bal_d_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxcarr3-1,0,lastZpos],[pxcarr4+1,lastYpos,lastZpos]),nameSet='bal_d_set')
bal_tald_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([pxcarr4+1,0,lastZpos],[pxmnp2,lastYpos,lastZpos]),nameSet='bal_tald_set')
paseos_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange([pxmnp1,pyhast1,lastZpos],[pxmxp1,pyhast2,lastZpos]),gm.IJKRange([pxmnp2,pyhast1,lastZpos],[pxmxp2,pyhast2,lastZpos])],nameSet='paseos_set')
#Losa cimentación interior marco
losc_int_set=gridGeom.getSetSurfOneRegion(ijkRange=gm.IJKRange([0,pyhast1,0],[lastXpos,pyhast2,0]),nameSet='losc_int_set')

#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
selfWeight= loads.InertialLoad(name='selfWeight', lstMeshSets=[losCimExt_M1_mesh,losCimExt_M2_mesh,losCimExt_M3_mesh,losCimCent_M1_mesh,losCimCent_M2_mesh,losCimCent_M3_mesh,hastIzq_M1_mesh,hastIzq_M2_mesh,hastIzq_M3_mesh,hastDer_M1_mesh,hastDer_M2_mesh,hastDer_M3_mesh,dintExt_M1_mesh,dintExt_M2_mesh,dintExt_M3_mesh,dintCent_M1_mesh,dintCent_M2_mesh,dintCent_M3_mesh,muretes_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

# Uniform loads applied on shell elements
#    name:       name identifying the load
#    xcSet:     set that contains the surfaces
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)

#     Dead load.
#relleno
Hrell_tali1=(Hrelli/3.)/2.
Hrell_tali2=Hrell_tali1+Hrelli/3.
Hrell_tali3=Hrell_tali2+Hrelli/3.
cm_rell_tali1=loads.UniformLoadOnSurfaces(name= 'cm_rell_tali1',xcSet=rell_tali1_set,loadVector= xc.Vector([0,0,-grav*densrell*Hrell_tali1,0,0,0]),refSystem='Global')
cm_rell_tali2=loads.UniformLoadOnSurfaces(name= 'cm_rell_tali2',xcSet=rell_tali2_set,loadVector= xc.Vector([0,0,-grav*densrell*Hrell_tali2,0,0,0]),refSystem='Global')
cm_rell_tali3=loads.UniformLoadOnSurfaces(name= 'cm_rell_tali3',xcSet=rell_tali3_set,loadVector= xc.Vector([0,0,-grav*densrell*Hrell_tali3,0,0,0]),refSystem='Global')

cm_rell_i=loads.UniformLoadOnSurfaces(name= 'cm_rell_i',xcSet=rell_i_set,loadVector= xc.Vector([0,0,-grav*densrell*Hrelli,0,0,0]))
cm_rell_d=loads.UniformLoadOnSurfaces(name= 'cm_rell_d',xcSet=rell_d_set,loadVector= xc.Vector([0,0,-grav*densrell*Hrelld,0,0,0]))

Hrell_tald1=(Hrelld/3.)/2.
Hrell_tald2=Hrell_tald1+Hrelld/3.
Hrell_tald3=Hrell_tald2+Hrelld/3.
cm_rell_tald1=loads.UniformLoadOnSurfaces(name= 'cm_rell_tald1',xcSet=rell_tald1_set,loadVector= xc.Vector([0,0,-grav*densrell*Hrell_tald1,0,0,0]),refSystem='Global')
cm_rell_tald2=loads.UniformLoadOnSurfaces(name= 'cm_rell_tald2',xcSet=rell_tald2_set,loadVector= xc.Vector([0,0,-grav*densrell*Hrell_tald2,0,0,0]),refSystem='Global')
cm_rell_tald3=loads.UniformLoadOnSurfaces(name= 'cm_rell_tald3',xcSet=rell_tald3_set,loadVector= xc.Vector([0,0,-grav*densrell*Hrell_tald3,0,0,0]),refSystem='Global')


#balasto        
cm_bal_tali=loads.UniformLoadOnSurfaces(name= 'cm_bal_tali',xcSet=bal_tali_set,loadVector= xc.Vector([0,0,-grav*densbal*Hbali/2]))
cm_bal_i=loads.UniformLoadOnSurfaces(name= 'cm_bal_i',xcSet=bal_i_set,loadVector= xc.Vector([0,0,-grav*densbal*Hbali,0,0,0]))
cm_bal_d=loads.UniformLoadOnSurfaces(name= 'cm_bal_d',xcSet=bal_d_set,loadVector= xc.Vector([0,0,-grav*densbal*Hbald,0,0,0]))
cm_bal_tald=loads.UniformLoadOnSurfaces(name= 'cm_bal_tald',xcSet=bal_tald_set,loadVector= xc.Vector([0,0,-grav*densbal*Hbald/2,0,0,0]))
            
#tren de cargas carreteras sobre losa cimentación
sc_unif_carr=loads.UniformLoadOnSurfaces(name='sc_unif_carr',xcSet=losc_int_set,loadVector= xc.Vector([0,0,-cunifCarr,0,0,0]))

#carga no ferroviaria en paseos
sc_paseos=loads.UniformLoadOnSurfaces(name='sc_paseos',xcSet=paseos_set,loadVector= xc.Vector([0,0,-qnferr,0,0,0]))


# Superficie de reparto sobre el dintel de las cargas puntuales del tren de cargas
# en cada carril
angrep_rad=math.radians(angrep)
Qptren_carr=nQptren_carr*Qptren
L_Qptren_carr=(nQptren_carr-1)*distEjesTren

def polygon(xCent,yCent,Lx,Ly):
    pol=geom.Polygon2d()
    pol.appendVertex(geom.Pos2d(xCent-Lx/2.0,yCent-Ly/2.0))
    pol.appendVertex(geom.Pos2d(xCent-Lx/2.0,yCent+Ly/2.0))
    pol.appendVertex(geom.Pos2d(xCent+Lx/2.0,yCent+Ly/2.0))
    pol.appendVertex(geom.Pos2d(xCent+Lx/2.0,yCent-Ly/2.0))
    return pol

def qLinYsobreMontera(prep,setBusq,hMont,angrepRad,x_coord,y_inic,y_fin,qLin,nameToLoad):
    '''Carga repartida sobre el dintel debida a una carga en línea sobre la montera '''
    Lx=hMont*math.tan(angrepRad)
    Ly=y_fin-y_inic
    pol=polygon(xCent=x_coord,yCent=y_inic+Ly/2.0,Lx=Lx,Ly=Ly)
    aux_set=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=setBusq,prismBase=pol,prismAxis='Z',setName='aux_set'+nameToLoad)
    if aux_set.getNumElements==0:
        print 'OJO!! no encuentro elementos para repartir la carga ', nameToLoad
    areaSet=np.sum([e.getArea(False) for e in aux_set.elements])
    return loads.UniformLoadOnSurfaces(name=nameToLoad,xcSet=aux_set,loadVector=xc.Vector([0,0,-qLin*Ly/areaSet,0,0,0]),refSystem='Global')
    
yCentAll=yList[pyhast1]+(yList[pyhast2]-yList[pyhast1])/2.0
y_inic_all=yCentAll-L_Qptren_carr/2.0
y_fin_all=yCentAll+L_Qptren_carr/2.0

def qPuntEjeReparto(prep,setBusq,hTot,angrepRad,x_punt,y_punt,lTrav,distTrav,Qpunt,nameToLoad):
    '''Carga repartida sobre el dintel debida a la carga puntual de un eje del tren de cargas n vías sobre balasto. La carga vertical puntual actuando sobre el carril se reparte a lo largo de tres traviesas consecutivas, (En el hormigón se reparte a 45º)'''
    Lx=lTrav+2*hTot*math.tan(angrepRad)
    Ly=2*distTrav
    pol=polygon(xCent=x_punt,yCent=y_punt,Lx=Lx,Ly=Ly)
    aux_set=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=setBusq,prismBase=pol,prismAxis='Z',setName='aux_set'+nameToLoad)
    if aux_set.getNumElements==0:
        print 'OJO!! no encuentro elementos para repartir la carga ', nameToLoad
    areaSet=np.sum([e.getArea(False) for e in aux_set.elements])
    return loads.UniformLoadOnSurfaces(name=nameToLoad,xcSet=aux_set,loadVector=xc.Vector([0,0,-Qpunt/areaSet,0,0,0]),refSystem='Global')


yCentAll=yList[pyhast1]+(yList[pyhast2]-yList[pyhast1])/2.0
y_inic_all=yCentAll-L_Qptren_carr/2.0
y_fin_all=yCentAll+L_Qptren_carr/2.0

QpuntEje=2*Qptren
y_cent=(yList[pyhast1]+yList[pyhast2])/2.0
y_e1=y_cent-1.5*distEjesTren
y_e2=y_cent-0.5*distEjesTren
y_e3=y_cent+0.5*distEjesTren
y_e4=y_cent+1.5*distEjesTren
#Cargas puntuales vía 1
x_punt=(xList[pxcarr1]+xList[pxcarr2])/2.0
hTot=Hbali+Hrelli+deckTh/2.0
# eje 1
Qptren_v1_e1=qPuntEjeReparto(prep=prep,setBusq=dintel,hTot=hTot,angrepRad=angrep_rad,x_punt=x_punt,y_punt=y_e1,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v1_e1')
# eje 2
Qptren_v1_e2=qPuntEjeReparto(prep=prep,setBusq=dintel,hTot=hTot,angrepRad=angrep_rad,x_punt=x_punt,y_punt=y_e2,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v1_e2')
# eje 3
Qptren_v1_e3=qPuntEjeReparto(prep=prep,setBusq=dintel,hTot=hTot,angrepRad=angrep_rad,x_punt=x_punt,y_punt=y_e3,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v1_e3')
# eje 4
Qptren_v1_e4=qPuntEjeReparto(prep=prep,setBusq=dintel,hTot=hTot,angrepRad=angrep_rad,x_punt=x_punt,y_punt=y_e4,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v1_e4')

#Cargas puntuales vía 2
x_punt=(xList[pxcarr3]+xList[pxcarr4])/2.0
hTot=Hbald+Hrelld+deckTh/2.0
# eje 1
Qptren_v2_e1=qPuntEjeReparto(prep=prep,setBusq=dintel,hTot=hTot,angrepRad=angrep_rad,x_punt=x_punt,y_punt=y_e1,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v2_e1')
# eje 2
Qptren_v2_e2=qPuntEjeReparto(prep=prep,setBusq=dintel,hTot=hTot,angrepRad=angrep_rad,x_punt=x_punt,y_punt=y_e2,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v2_e2')
# eje 3
Qptren_v2_e3=qPuntEjeReparto(prep=prep,setBusq=dintel,hTot=hTot,angrepRad=angrep_rad,x_punt=x_punt,y_punt=y_e3,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v2_e3')
# eje 4
Qptren_v2_e4=qPuntEjeReparto(prep=prep,setBusq=dintel,hTot=hTot,angrepRad=angrep_rad,x_punt=x_punt,y_punt=y_e4,lTrav=lTraviesa,distTrav=distTrav,Qpunt=QpuntEje,nameToLoad='Qptren_v2_e4')


#carga muerta carril + traviesa
y_inic_all=yList[pyhast1]
y_fin_all=yList[pyhast2]

# carril + traviesa 1
cm_carr_trav_carr1=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr4-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr1],y_inic=y_inic_all,y_fin=y_fin_all,qLin=ql_carr_trav,nameToLoad='cm_carr_trav_carr1')

# carril + traviesa 2
cm_carr_trav_carr2=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr4-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr2],y_inic=y_inic_all,y_fin=y_fin_all,qLin=ql_carr_trav,nameToLoad='cm_carr_trav_carr2')

# carril + traviesa 3
cm_carr_trav_carr3=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr4-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr3],y_inic=y_inic_all,y_fin=y_fin_all,qLin=ql_carr_trav,nameToLoad='cm_carr_trav_carr3')

# carril + traviesa 4
cm_carr_trav_carr4=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr4-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr4],y_inic=y_inic_all,y_fin=y_fin_all,qLin=ql_carr_trav,nameToLoad='cm_carr_trav_carr4')


#carga muerta canal de cables
y_inic_all=yList[pyhast1]
y_fin_all=yList[pyhast2]

  # canal de cables izq.
cm_can_cabl_i=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hrelli+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcan1],y_inic=y_inic_all,y_fin=y_fin_all,qLin=ql_can_cabl,nameToLoad='cm_can_cabl_i')

  # canal de cables der.
cm_can_cabl_d=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hrelld+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcan2],y_inic=y_inic_all,y_fin=y_fin_all,qLin=ql_can_cabl,nameToLoad='cm_can_cabl_d')

# carga lineal ferroviaria sobre el dintel
Ll=(yList[pyhast2]-yList[pyhast1]-L_Qptren_carr-2*0.8)/2.0
ymin_a=yList[pyhast1]
ymax_a=yList[pyhast1]+Ll
ymax_b=yList[pyhast2]
ymin_b=ymax_b-Ll

#  en carril 1
sc_qltren_carr1_a=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr1-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr1],y_inic=ymin_a,y_fin=ymax_a,qLin=qltren,nameToLoad='sc_qltren_carr1_a')
sc_qltren_carr1_b=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr1-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr1],y_inic=ymin_b,y_fin=ymax_b,qLin=qltren,nameToLoad='sc_qltren_carr1_b')

#  en carril 2
sc_qltren_carr2_a=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr2-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr2],y_inic=ymin_a,y_fin=ymax_a,qLin=qltren,nameToLoad='sc_qltren_carr2_a')
sc_qltren_carr2_b=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr2-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr2],y_inic=ymin_b,y_fin=ymax_b,qLin=qltren,nameToLoad='sc_qltren_carr2_b')

#  en carril 3
sc_qltren_carr3_a=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr3-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr3],y_inic=ymin_a,y_fin=ymax_a,qLin=qltren,nameToLoad='sc_qltren_carr3_a')
sc_qltren_carr3_b=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr3-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr3],y_inic=ymin_b,y_fin=ymax_b,qLin=qltren,nameToLoad='sc_qltren_carr3_b')

#  en carril 4
sc_qltren_carr4_a=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr4-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr4],y_inic=ymin_a,y_fin=ymax_a,qLin=qltren,nameToLoad='sc_qltren_carr4_a')
sc_qltren_carr4_b=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr4-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr4],y_inic=ymin_b,y_fin=ymax_b,qLin=qltren,nameToLoad='sc_qltren_carr4_b')

# descarrilamiento en situación de proyecto 1
y_eje=(yList[pyhast1]+yList[pyhast2])/2.0
sc_descarr_1_a=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr3-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr4],y_inic=y_eje-L_Qptren_carr/2.0,y_fin=y_eje+L_Qptren_carr/2.0,qLin=qdesc1,nameToLoad='sc_descarr_1_a')
sc_descarr_1_b=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hcarr4-hcarril+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxcarr4]+anchvia,y_inic=y_eje-L_Qptren_carr/2.0,y_fin=y_eje+L_Qptren_carr/2.0,qLin=qdesc1,nameToLoad='sc_descarr_1_b')
# descarrilamiento en situación de proyecto 2
sc_descarr_2=qLinYsobreMontera(prep=prep,setBusq=dintel,hMont=Hrelld+deckTh/2.0,angrepRad=angrep_rad,x_coord=xList[pxmnp2],y_inic=yList[pyhast1],y_fin=yList[pyhast2],qLin=qdesc2,nameToLoad='sc_descarr_2')

# sobrecargas sobre dintel debidas ala carga lineal del tren de cargas ferroviario
   #en carril 1

# Load acting on one or several nodes
#     name:       name identifying the load
#     lstNod:     list of nodes  on which the load is applied
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).

#  cargas puntuales tren de carreteras
def trafficPointLoads(centerTruck):
    xc=centerTruck.x
    yc=centerTruck.y
    zc=centerTruck.z
    p1=geom.Pos3d(xc-lejesCarr,yc-lruedCarr/2.0,zc)
    p2=geom.Pos3d(xc-lejesCarr,yc+lruedCarr/2.0,zc)
    p3=geom.Pos3d(xc,yc-lruedCarr/2.0,zc)
    p4=geom.Pos3d(xc,yc+lruedCarr/2.0,zc)
    p5=geom.Pos3d(xc+lejesCarr,yc-lruedCarr/2.0,zc)
    p6=geom.Pos3d(xc+lejesCarr,yc+lruedCarr/2.0,zc)
    nodLst=sets.get_lstNod_from_lst3DPos(preprocessor=prep,lst3DPos=[p1,p2,p3,p4,p5,p6])
    return nodLst
centTr=geom.Pos3d(xList[0]+(xList[-1]-xList[0])/2.0,yList[0]+(yList[-1]-yList[0])/2.0,zList[0])
qp_carr=loads.NodalLoad(name='qp_carr',lstNod=trafficPointLoads(centTr),loadVector=xc.Vector([0,0,-qpCarr,0,0,0]))


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
muri_z1_1_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1-4,pyhast1,0),(pxmnp1-3,pyhast1,lastZpos)),gm.IJKRange((pxmxp2+3,pyhast1,0),(pxmxp2+4,pyhast1,lastZpos))],nameSet='muri_z1_1_set')
muri_z1_2_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1-3,pyhast1,0),(pxmnp1-2,pyhast1,lastZpos)),gm.IJKRange((pxmxp2+2,pyhast1,0),(pxmxp2+3,pyhast1,lastZpos))],nameSet='muri_z1_2_set')
muri_z1_3_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1-2,pyhast1,0),(pxmnp1-1,pyhast1,lastZpos)),gm.IJKRange((pxmxp2+1,pyhast1,0),(pxmxp2+2,pyhast1,lastZpos))],nameSet='muri_z1_3_set')

muri_z2_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1,pyhast1,0),(pxmxp1,pyhast1,lastZpos)),gm.IJKRange((pxmnp2,pyhast1,0),(pxmxp2,pyhast1,lastZpos))],nameSet='muri_z2_set')
muri_z3_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmxp1,pyhast1,0),(pxcarr3-1,pyhast1,lastZpos))],nameSet='muri_z3_set')
muri_z4_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxcarr3-1,pyhast1,0),(pxmnp2,pyhast1,lastZpos))],nameSet='muri_z4_set')

#   muro derecho
murd_z1_1_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1-4,pyhast2,0),(pxmnp1-3,pyhast2,lastZpos)),gm.IJKRange((pxmxp2+3,pyhast2,0),(pxmxp2+4,pyhast2,lastZpos))],nameSet='murd_z1_1_set')
murd_z1_2_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1-3,pyhast2,0),(pxmnp1-2,pyhast2,lastZpos)),gm.IJKRange((pxmxp2+2,pyhast2,0),(pxmxp2+3,pyhast2,lastZpos))],nameSet='murd_z1_2_set')
murd_z1_3_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1-2,pyhast2,0),(pxmnp1-1,pyhast2,lastZpos)),gm.IJKRange((pxmxp2+1,pyhast2,0),(pxmxp2+2,pyhast2,lastZpos))],nameSet='murd_z1_3_set')

murd_z2_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1,pyhast2,0),(pxmxp1,pyhast2,lastZpos)),gm.IJKRange((pxmnp2,pyhast2,0),(pxmxp2,pyhast2,lastZpos))],nameSet='murd_z2_set')
murd_z3_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmxp1,pyhast2,0),(pxcarr3-1,pyhast2,lastZpos))],nameSet='murd_z3_set')
murd_z4_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxcarr3-1,pyhast2,0),(pxmnp2,pyhast2,lastZpos))],nameSet='murd_z4_set')

# empuje del terreno
zGroundZ1_1=zList[lastZpos]+deckTh/2.0+(Hrell_tali1+Hrell_tald1)/2.0
zGroundZ1_2=zList[lastZpos]+deckTh/2.0+(Hrell_tali2+Hrell_tald2)/2.0
zGroundZ1_3=zList[lastZpos]+deckTh/2.0+(Hrell_tali3+Hrell_tald3)/2.0

zGroundZ2=zList[lastZpos]+deckTh/2.0+(Hrelli+Hrelld)/2.0
zGroundZ3=zList[lastZpos]+deckTh/2.0+Hrelli+Hbali
zGroundZ4=zList[lastZpos]+deckTh/2.0+Hrelld+Hbald
zGroundZ4_desbalastado=zList[lastZpos]+deckTh/2.0+Hrelld

soilZ1_1=ep.EarthPressureModel( zGround=zGroundZ1_1,zBottomSoils=[-10], KSoils=[K0],gammaSoils=[densrell*grav], zWater=-10.0, gammaWater=grav)
soilZ1_2=ep.EarthPressureModel(zGround=zGroundZ1_2,zBottomSoils=[-10], KSoils=[K0], gammaSoils=[densrell*grav], zWater=-10.0, gammaWater=grav)
soilZ1_3=ep.EarthPressureModel(zGround=zGroundZ1_3, zBottomSoils=[-10], KSoils=[K0],gammaSoils=[densrell*grav], zWater=-10.0, gammaWater=grav)

soilZ2=ep.EarthPressureModel(zGround=zGroundZ2, zBottomSoils=[-10], KSoils=[K0],gammaSoils=[densrell*grav], zWater=0, gammaWater=0)
soilZ3=ep.EarthPressureModel(zGround=zGroundZ3, zBottomSoils=[-10], KSoils=[K0],gammaSoils=[densrell*grav], zWater=-10, gammaWater=grav)
soilZ4=ep.EarthPressureModel(zGround=zGroundZ4, zBottomSoils=[-10], KSoils=[K0],gammaSoils=[densrell*grav], zWater=-10, gammaWater=0)
soilZ4_desbal=ep.EarthPressureModel(zGround=zGroundZ4_desbalastado, zBottomSoils=[-10], KSoils=[K0],gammaSoils=[densrell*grav], zWater=-10, gammaWater=grav)

ep_muri_z1_1= loads.EarthPressLoad(name= 'ep_muri_z1_1', xcSet=muri_z1_1_set,soilData=soilZ1_1, vDir=xc.Vector([0,1,0]))
ep_muri_z1_2= loads.EarthPressLoad(name= 'ep_muri_z1_2', xcSet=muri_z1_2_set,soilData=soilZ1_2, vDir=xc.Vector([0,1,0]))
ep_muri_z1_3= loads.EarthPressLoad(name= 'ep_muri_z1_3', xcSet=muri_z1_3_set,soilData=soilZ1_3, vDir=xc.Vector([0,1,0]))

ep_muri_z2= loads.EarthPressLoad(name= 'ep_muri_z2', xcSet=muri_z2_set,soilData=soilZ2, vDir=xc.Vector([0,1,0]))
ep_muri_z3= loads.EarthPressLoad(name= 'ep_muri_z3', xcSet=muri_z3_set,soilData=soilZ3, vDir=xc.Vector([0,1,0]))
ep_muri_z4= loads.EarthPressLoad(name= 'ep_muri_z4', xcSet=muri_z4_set,soilData=soilZ4, vDir=xc.Vector([0,1,0]))
ep_muri_z4_desbal= loads.EarthPressLoad(name= 'ep_muri_z4', xcSet=muri_z4_set,soilData=soilZ4_desbal, vDir=xc.Vector([0,1,0]))


ep_murd_z1_1= loads.EarthPressLoad(name= 'ep_murd_z1_1', xcSet=murd_z1_1_set,soilData=soilZ1_1, vDir=xc.Vector([0,-1,0]))
ep_murd_z1_2= loads.EarthPressLoad(name= 'ep_murd_z1_2', xcSet=murd_z1_2_set,soilData=soilZ1_2, vDir=xc.Vector([0,-1,0]))
ep_murd_z1_3= loads.EarthPressLoad(name= 'ep_murd_z1_3', xcSet=murd_z1_3_set,soilData=soilZ1_3, vDir=xc.Vector([0,-1,0]))

ep_murd_z2= loads.EarthPressLoad(name= 'ep_murd_z2', xcSet=murd_z2_set,soilData=soilZ2, vDir=xc.Vector([0,-1,0]))
ep_murd_z3= loads.EarthPressLoad(name= 'ep_murd_z3', xcSet=murd_z3_set,soilData=soilZ3, vDir=xc.Vector([0,-1,0]))
ep_murd_z4= loads.EarthPressLoad(name= 'ep_murd_z4', xcSet=murd_z4_set,soilData=soilZ4, vDir=xc.Vector([0,-1,0]))
ep_murd_z4_desbal= loads.EarthPressLoad(name= 'ep_murd_z4', xcSet=murd_z4_set,soilData=soilZ4_desbal, vDir=xc.Vector([0,-1,0]))

# cargas sobre el terreno
qb_Qptren_1_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxcarr1,pyhast1,0),(pxcarr2,pyhast1,lastZpos))],nameSet='qb_Qptren_1_set')
dist_carr=xList[pxcarr2]-xList[pxcarr1]
strip_QPtren=ep.StripLoadOnBackfill(qLoad=2*Qptren_carr/L_Qptren_carr/dist_carr, zLoad=zGroundZ3,distWall=0, stripWidth=L_Qptren_carr)
qb_Qptren_1= loads.EarthPressLoad(name= 'qb_Qptren_1', xcSet=qb_Qptren_1_set,soilData=None, vDir=xc.Vector([0,1,0]))
qb_Qptren_1.stripLoads=[strip_QPtren]

qb_Qptren_2_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxcarr3,pyhast1,0),(pxcarr4,pyhast1,lastZpos))],nameSet='qb_Qptren_2_set')
qb_Qptren_2= loads.EarthPressLoad(name= 'qb_Qptren_2', xcSet=qb_Qptren_2_set,soilData=None, vDir=xc.Vector([0,1,0]))
qb_Qptren_2.stripLoads=[strip_QPtren]

qb_qstren_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxcan1,pyhast1,0),(pxcan2,pyhast1,lastZpos))],nameSet='qb_qstren_set')
strip_qstren=ep.StripLoadOnBackfill(qLoad=scterr, zLoad=zGroundZ3,distWall=0, stripWidth=L_Qptren_carr)
qb_qstren=loads.EarthPressLoad(name= 'qb_qstren', xcSet=qb_qstren_set,soilData=None, vDir=xc.Vector([0,1,0]))
qb_qstren.stripLoads=[strip_qstren]

strip_paseos=ep.StripLoadOnBackfill(qLoad=qnferr, zLoad=zGroundZ2,distWall=0, stripWidth=20)
qb_paseos_i_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1,pyhast1,0),(pxmxp1,pyhast1,lastZpos)),gm.IJKRange((pxmnp2,pyhast1,0),(pxmxp2,pyhast1,lastZpos))],nameSet='qb_paseos_i_set')
qb_paseos_i=loads.EarthPressLoad(name= 'qb_paseos_i', xcSet=qb_paseos_i_set,soilData=None, vDir=xc.Vector([0,1,0]))
qb_paseos_i.stripLoads=[strip_paseos]

qb_paseos_d_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp1,pyhast2,0),(pxmxp1,pyhast2,lastZpos)),gm.IJKRange((pxmnp2,pyhast2,0),(pxmxp2,pyhast2,lastZpos))],nameSet='qb_paseos_d_set')
qb_paseos_d=loads.EarthPressLoad(name= 'qb_paseos_d', xcSet=qb_paseos_d_set,soilData=None, vDir=xc.Vector([0,-1,0]))
qb_paseos_d.stripLoads=[strip_paseos]

qlsup=4*qltren/(xList[pxcarr4]-xList[pxcarr1])
strip_qlsup=ep.StripLoadOnBackfill(qLoad=qlsup, zLoad=zGroundZ3,distWall=0, stripWidth=20)
qb_qltren_i_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxcarr1,pyhast1,0),(pxcarr4,pyhast1,lastZpos))],nameSet='qb_qltren_i_set')
qb_qltren_i=loads.EarthPressLoad(name= 'qb_qltren_i', xcSet=qb_qltren_i_set,soilData=None, vDir=xc.Vector([0,1,0]))
qb_qltren_i.stripLoads=[strip_qlsup]
qb_qltren_d_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxcarr1,pyhast2,0),(pxcarr4,pyhast2,lastZpos))],nameSet='qb_qltren_d_set')
qb_qltren_d=loads.EarthPressLoad(name= 'qb_qltren_d', xcSet=qb_qltren_d_set,soilData=None, vDir=xc.Vector([0,-1,0]))
qb_qltren_d.stripLoads=[strip_qlsup]

#descarrilamiento en situación de proyecto 2
strip_descarr2=ep.StripLoadOnBackfill(qLoad=qdesc2/(xList[pxmxp2]-xList[pxmnp2]), zLoad=zGroundZ2,distWall=0, stripWidth=10-(yList[pyhast2]-yList[pyhast1])/2.0)

qb_descarr_2i_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp2,pyhast1,0),(pxmxp2,pyhast1,lastZpos))],nameSet='qb_descarr_2i_set')
qb_descarr_2i=loads.EarthPressLoad(name= 'qb_descarr_2i', xcSet=qb_descarr_2i_set,soilData=None, vDir=xc.Vector([0,1,0]))
qb_descarr_2i.stripLoads=[strip_descarr2]

qb_descarr_2d_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxmnp2,pyhast2,0),(pxmxp2,pyhast2,lastZpos))],nameSet='qb_descarr_2d_set')
qb_descarr_2d=loads.EarthPressLoad(name= 'qb_descarr_2d', xcSet=qb_descarr_2d_set,soilData=None, vDir=xc.Vector([0,-1,0]))
qb_descarr_2d.stripLoads=[strip_descarr2]

#Empuje del terreno en situación de construcción
soilConstr=ep.EarthPressureModel(zGround=zList[-1], zBottomSoils=[-10], KSoils=[K0],gammaSoils=[densrell*grav], zWater=-10.0, gammaWater=grav)
ep_construct_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((0,pyhast1,0),(lastXpos,pyhast1,lastZpos))],nameSet='ep_construct_set')
ep_construct= loads.EarthPressLoad(name= 'ep_construct', xcSet=ep_construct_set,soilData=soilConstr, vDir=xc.Vector([0,1,0]))
#cargas lineales vehículo en construcción
ql_construct_set=gridGeom.getSetSurfMultiRegion(lstIJKRange=[gm.IJKRange((pxcarr2+1,pyhast1,0),(pxcarr3,pyhast1,lastZpos))],nameSet='ql_construct_set')
ql=qlConstruct*1.3/(xList[pxcarr3]-xList[pxcarr2+1])
lineL1=ep.LineVerticalLoadOnBackfill(qLoad=ql, zLoad=zList[lastZpos],distWall=2.20)
lineL2=ep.LineVerticalLoadOnBackfill(qLoad=ql, zLoad=zList[lastZpos],distWall=0.10)
ql_construct=loads.EarthPressLoad(name= 'ql_construct', xcSet=ql_construct_set,soilData=None, vDir=xc.Vector([0,1,0]))
ql_construct.lineLoads=[lineL1,lineL2]

#    ***LOAD CASES***
# G1: Peso propio
G1=lcases.LoadCase(preprocessor=prep,name="G1",loadPType="default",timeSType="constant_ts")
G1.create()
G1.addLstLoads([selfWeight])

# G2a: Carga muerta en servicio
G2a=lcases.LoadCase(preprocessor=prep,name="G2a",loadPType="default",timeSType="constant_ts")
G2a.create()
G2a.addLstLoads([cm_rell_tali1,cm_rell_tali2,cm_rell_tali3,cm_rell_i,
                 cm_rell_d,cm_rell_tald1,cm_rell_tald2,cm_rell_tald3,
                 cm_carr_trav_carr1,cm_carr_trav_carr2,
                 cm_carr_trav_carr3,cm_carr_trav_carr4,
                 cm_can_cabl_i,cm_can_cabl_d])
eval('1.3*cm_bal_tali')   #add this weighted load to the curret load case
eval('1.3*cm_bal_i')
eval('1.3*cm_bal_d')
eval('1.3*cm_bal_tald')


# G2b: Carga muerta desbalastado 1
G2b=lcases.LoadCase(preprocessor=prep,name="G2b",loadPType="default",timeSType="constant_ts")
G2b.create()
G2b.addLstLoads([cm_rell_tali1,cm_rell_tali2,cm_rell_tali3,cm_rell_i,
                 cm_rell_d,cm_rell_tald1,cm_rell_tald2,cm_rell_tald3,
                 cm_carr_trav_carr1,cm_carr_trav_carr2,
                 cm_can_cabl_i,cm_can_cabl_d])
eval('0.7*cm_bal_tali')   #add this weighted load to the curret load case
eval('0.7*cm_bal_i')
    
# G2c: Carga muerta desbalastado 2
G2c=lcases.LoadCase(preprocessor=prep,name="G2c",loadPType="default",timeSType="constant_ts")
G2c.create()
G2c.addLstLoads([cm_rell_tali1,cm_rell_tali2,cm_rell_tali3,cm_rell_i,
                 cm_rell_d,cm_rell_tald1,cm_rell_tald2,cm_rell_tald3,
                 cm_carr_trav_carr1,cm_carr_trav_carr2,
                 cm_can_cabl_i,cm_can_cabl_d])
eval('0.7*cm_bal_tali')   #add this weighted load to the curret load case
eval('0.7*cm_bal_i')
eval('0.7*cm_bal_d')
eval('0.7*cm_bal_tald')

# G3: Empuje del terreno
G3=lcases.LoadCase(preprocessor=prep,name="G3",loadPType="default",timeSType="constant_ts")
G3.create()
G3.addLstLoads([ep_muri_z1_1,ep_muri_z1_2,ep_muri_z1_3,ep_muri_z2,ep_muri_z3,ep_muri_z4,
                ep_murd_z1_1,ep_murd_z1_2,ep_murd_z1_3,ep_murd_z2,ep_murd_z3,ep_murd_z4])

# Q1a: Tren de cargas posición 1
Q1a=lcases.LoadCase(preprocessor=prep,name="Q1a",loadPType="default",timeSType="constant_ts")
Q1a.create()
Q1a.addLstLoads([Qptren_v1_e1,Qptren_v1_e2,Qptren_v1_e3,Qptren_v1_e4,
                 Qptren_v2_e1,Qptren_v2_e2,Qptren_v2_e3,Qptren_v2_e4,
                 sc_qltren_carr1_a,sc_qltren_carr1_b,
                 sc_qltren_carr2_a,sc_qltren_carr2_b,
                 sc_qltren_carr3_a,sc_qltren_carr3_b,
                 sc_qltren_carr4_a,sc_qltren_carr4_b,
                 sc_paseos,qb_qltren_i,qb_qltren_d])

# Q1a_1via: Tren de cargas posición 1 en situaciones de desbalastado
Q1a_1via=lcases.LoadCase(preprocessor=prep,name="Q1a_1via",loadPType="default",timeSType="constant_ts")
Q1a_1via.create()
Q1a_1via.addLstLoads([Qptren_v1_e1,Qptren_v1_e2,Qptren_v1_e3,Qptren_v1_e4,
                 sc_qltren_carr1_a,sc_qltren_carr1_b,
                 sc_qltren_carr2_a,sc_qltren_carr2_b,
                 sc_paseos,qb_qltren_i,qb_qltren_d])

# Q1b: Tren de cargas posición 2
Q1b=lcases.LoadCase(preprocessor=prep,name="Q1b",loadPType="default",timeSType="constant_ts")
Q1b.create()
Q1b.addLstLoads([qb_Qptren_1,qb_Qptren_2])

# Q1c: Tren de cargas posición 3
Q1c=lcases.LoadCase(preprocessor=prep,name="Q1c",loadPType="default",timeSType="constant_ts")
Q1c.create()
Q1c.addLstLoads([qb_Qptren_1,qb_Qptren_2,qb_qstren])

# Q2b: Tren carretera inferior
Q2b=lcases.LoadCase(preprocessor=prep,name="Q2b",loadPType="default",timeSType="constant_ts")
Q2b.create()
Q2b.addLstLoads([sc_unif_carr,qp_carr])

# A1a: Descarrilamiento situación 1
A1a=lcases.LoadCase(preprocessor=prep,name="A1a",loadPType="default",timeSType="constant_ts")
A1a.create()
A1a.addLstLoads([sc_descarr_1_a,sc_descarr_1_b])

# A1b: Descarrilamiento situación 2
A1b=lcases.LoadCase(preprocessor=prep,name="A1b",loadPType="default",timeSType="constant_ts")
A1b.create()
A1b.addLstLoads([sc_descarr_2,qb_descarr_2i,qb_descarr_2d])

# C1: Empuje del terreno (construcción)
C1=lcases.LoadCase(preprocessor=prep,name="C1",loadPType="default",timeSType="constant_ts")
C1.create()
C1.addLstLoads([ep_construct,ql_construct])

#    ***LIMIT STATE COMBINATIONS***
combContainer= cc.CombContainer()  #Container of load combinations

#sets para chequear cortante en dintel y losa de cimentación (a medio canto del borde
#del apoyo)
L=xList[-1]
pol=polygon(xCent=L/2.0,yCent=0,Lx=L,Ly=GH-deckTh)
dintelCortante=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=dintel_M1M2,prismBase=pol,prismAxis='Z',setName='dintelCortante')
pol=polygon(xCent=L/2.0,yCent=0,Lx=L,Ly=GH-baseSlabTh)
losCimCortante=sets.set_included_in_orthoPrism(preprocessor=prep,setInit=losCim_M1M2,prismBase=pol,prismAxis='Z',setName='losCimCortante')

losasCortante=dintelCortante+losCimCortante
losasCortante.name='losasCortante'
losasCortante.description='Losas, cortante'
cortanteCalc=losasCortante+hastIzq_M1M2
