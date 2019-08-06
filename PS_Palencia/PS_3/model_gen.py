# -*- coding: utf-8 -*-
from __future__ import division

import os
import xc_base
import geom
import xc
import math
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
from model.geometry import geom_utils as gut
from materials.ehe import EHE_materials
#

fullProjPath='/home/ana/projects/XCmodels/PS_Palencia/PS_3/'
execfile(fullProjPath+'env_config.py')

execfile(fullProjPath+'data.py')

#             *** GEOMETRIC model (points, lines, surfaces) - SETS***0
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)

# grid model definition (tablero y pilas)
gridTabl= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridTabl.generatePoints()

#   Surfaces generation (tablero)
#Riostra estribo 1
x=xRiostrEstr[0]
y=yRiostrEstr[0]
z=zLosa[0]
riostrEstr1=gridTabl.genSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)),nameSet='riostrEstr1')
#Riostra estribo 2
x=xRiostrEstr[1]
y=yRiostrEstr[1]
z=zLosa[0]
riostrEstr2=gridTabl.genSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)),nameSet='riostrEstr2')
#Losa
x=xLosa
y=yLosa
z=zLosa[0]
losa=gridTabl.genSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)),nameSet='losa')
#Cartabones
x=xCartab
y=yLosa
z=zLosa[0]
cartabInt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][1],y[0],z),(x[0][-1],y[-1],z)),((x[1][0],y[0],z),(x[1][1],y[-1],z))], nameSet='cartabInt')
cartabExt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][1],y[-1],z)),((x[1][1],y[0],z),(x[1][-1],y[-1],z))], nameSet='cartabExt')
#Voladizos
x=xVoladz
y=yLosa
z=zLosa[0]
voladzInt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][1],y[0],z),(x[0][-1],y[-1],z)),((x[1][0],y[0],z),(x[1][1],y[-1],z))], nameSet='voladzInt')
voladzExt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][1],y[-1],z)),((x[1][1],y[0],z),(x[1][-1],y[-1],z))], nameSet='voladzExt')

#Lines generation (Pilas)
x=xPil
y=yPil
z=zPil
xyzRang=list()
for j in range(len(y)):
    k=j
    for i in range(len(x)):
        xyzRang.append([(x[i],y[j],z[k][0]),(x[i],y[j],z[k][-1])])
pilas=gridTabl.genLinMultiXYZRegion(lstXYZRange=xyzRang, nameSet='pilas')


#                         *** MATERIALS *** 
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())
# Isotropic elastic section-material appropiate for plate and shell analysis
riostrEstr_mat=tm.DeckMaterialData(name='riostrEstr_mat_mat',thickness= cantoRiostrEstr,material=concrProp)
riostrEstr_mat.setupElasticSection(preprocessor=prep) 
losa_mat=tm.DeckMaterialData(name='losa_mat',thickness= cantoLosa,material=concrProp)
losa_mat.setupElasticSection(preprocessor=prep) 
cartabInt_mat=tm.DeckMaterialData(name='cartabInt_mat',thickness=eCartInt,material=concrProp)
cartabInt_mat.setupElasticSection(preprocessor=prep) 
cartabExt_mat=tm.DeckMaterialData(name='cartabExt_mat',thickness=eCartExt,material=concrProp)
cartabExt_mat.setupElasticSection(preprocessor=prep) 
voladzInt_mat=tm.DeckMaterialData(name='voladzInt_mat',thickness=eVolInt,material=concrProp)
voladzInt_mat.setupElasticSection(preprocessor=prep) 
voladzExt_mat=tm.DeckMaterialData(name='voladzExt_mat',thickness=eVolExt,material=concrProp)
voladzExt_mat.setupElasticSection(preprocessor=prep) 

#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectPilas=sectpr.RectangularSection(name='geomSectPilas',b=lRectEqPila,h=lRectEqPila)
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

pilas_mat= tm.BeamMaterialData(name= 'pilas_mat', section=geomSectPilas, material=concrProp)
pilas_mat.setupElasticShear3DSection(preprocessor=prep)

# Elastomeric bearings.
from materials import bridge_bearings as bb
neopr=bb.ElastomericBearing(G=Gneopr,a=aNeopr,b=bNeopr,e=hNetoNeopr)
neopr.defineMaterials(prep)

#                         ***FE model - MESH***
# IMPORTANT: it's convenient to generate the mesh of surfaces before meshing
# the lines, otherwise, sets of shells can take also beam elements touched by
# them

pilas_mesh=fem.LinSetToMesh(linSet=pilas,matSect=pilas_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')

riostrEstr1_mesh=fem.SurfSetToMesh(surfSet=riostrEstr1,matSect=riostrEstr_mat,elemSize=eSize,elemType='ShellMITC4')
riostrEstr2_mesh=fem.SurfSetToMesh(surfSet=riostrEstr2,matSect=riostrEstr_mat,elemSize=eSize,elemType='ShellMITC4')
losa_mesh=fem.SurfSetToMesh(surfSet=losa,matSect=losa_mat,elemSize=eSize,elemType='ShellMITC4')
cartabInt_mesh=fem.SurfSetToMesh(surfSet=cartabInt,matSect=cartabInt_mat,elemSize=eSize,elemType='ShellMITC4')
cartabExt_mesh=fem.SurfSetToMesh(surfSet=cartabExt,matSect=cartabExt_mat,elemSize=eSize,elemType='ShellMITC4')
voladzExt_mesh=fem.SurfSetToMesh(surfSet=voladzExt,matSect=voladzExt_mat,elemSize=eSize,elemType='ShellMITC4')
voladzInt_mesh=fem.SurfSetToMesh(surfSet=voladzInt,matSect=voladzInt_mat,elemSize=eSize,elemType='ShellMITC4')

allmesh=[riostrEstr1_mesh,riostrEstr2_mesh,losa_mesh,cartabInt_mesh,cartabExt_mesh,voladzInt_mesh,voladzExt_mesh]
fem.multi_mesh(preprocessor=prep,lstMeshSets=allmesh)

pilas_mesh.generateMesh(prep)

#Definition of sets
execfile(fullProjPath+'sets_def.py')

#                       ***BOUNDARY CONDITIONS***
execfile(fullProjPath+'bound_cond.py')
        

#                       ***ACTIONS***
from actions.roadway_trafic import standard_load_models as slm
from actions.imposed_strain import imp_strain as imps
#Peso propio
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=allmesh+[pilas_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

G1=lcases.LoadCase(preprocessor=prep,name="G1",loadPType="default",timeSType="constant_ts")
G1.create()
G1.addLstLoads([selfWeight])
#Dead load case
G2=slm.dead_LC(lcName='G2',drivewaySet=calzada,qAsphalt=pav_sup,sidewalkSet=aceras,qSidewalk=qDeadAcera,barrierSet=barrera,qBarrier=qBarrera,deckEdgeSet=bordTabl,qDeckEdge=qAntivand)
G12=lcases.LoadCase(preprocessor=prep,name="G12",loadPType="default",timeSType="constant_ts")
G12.create()
G12.addLstLoads([selfWeight]+G2.lstOfLoadDef)


#Rheological load cases
G3=slm.thermal_rheological_LC(lcName='G3',lstUnifThStrnData=[imps.unifStrain(elemSet=tablero,DOF=1,strain=eps_retracc)])
#Traffic load cases
Q1a1=slm.IAP_traffic_LC(lcName='Q1a1',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano1,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,sidewalkSet=acerDer)
Q1a2=slm.IAP_traffic_LC(lcName='Q1a2',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano2,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,sidewalkSet=acerDer)
Q1b1=slm.IAP_traffic_LC(lcName='Q1b1',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano1,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=centVFi_vano1,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1b2=slm.IAP_traffic_LC(lcName='Q1b2',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano2,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=centVFi_vano2,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1c=slm.IAP_traffic_LC(lcName='Q1c',deckSet=tablero,virtLane1Set=viaFictDer_cent,xyCentPL1=centVFd_vano2,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq_cent,xyCentPL2=centVFi_vano2,restDrivewaySet=viaFictResto_cent,sidewalkSet=aceras)
Q1d=slm.IAP_traffic_LC(lcName='Q1d',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano2,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano2,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1e=slm.IAP_traffic_LC(lcName='Q1e',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano1,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano1,restDrivewaySet=viaFictResto,sidewalkSet=aceras)

Q1bFren=slm.IAP_traffic_LC(lcName='Q1bFren',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano1,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,vQbraking=vQfren,virtLane2Set=viaFictIzq,xyCentPL2=centVFi_vano1,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1dFren=slm.IAP_traffic_LC(lcName='Q1dFren',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano2,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,vQbraking=vQfren,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano2,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1eFren=slm.IAP_traffic_LC(lcName='Q1eFren',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano1,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,vQbraking=vQfren,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano1,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
#Wind load cases
Q21=slm.wind_LC(lcName='Q21',deckLineSet=bordizqTabl,vectWindDeck=[qWTablero,0],windwardPileSet=pilas,vectWindwardPile=[qWpilas,0])
Q22=slm.wind_LC(lcName='Q22',deckLineSet=bordizqTabl,vectWindDeck=[qWTableroSCuso,0],windwardPileSet=pilas,vectWindwardPile=[qWpilas,0])
#Thermal load cases
#Contraction
Q31=slm.thermal_rheological_LC(lcName='Q31',lstUnifThStrnData=[imps.unifThermalStrain(elemSet=tablero,DOF=1,alpha=coefDilat,temp=Tunif_contr)])
Q31neopr=slm.thermal_rheological_LC(lcName='Q31neopr',lstUnifThStrnData=[imps.unifThermalStrain(elemSet=tablero,DOF=1,alpha=coefDilat,temp=Tunif_contr_neopr)])
#Expansion
Q32=slm.thermal_rheological_LC(lcName='Q32',lstUnifThStrnData=[imps.unifThermalStrain(elemSet=tablero,DOF=1,alpha=coefDilat,temp=Tunif_dilat)])
Q32neopr=slm.thermal_rheological_LC(lcName='Q32neopr',lstUnifThStrnData=[imps.unifThermalStrain(elemSet=tablero,DOF=1,alpha=coefDilat,temp=Tunif_dilat_neopr)])
#Thermal gradient load cases
Q33=slm.gradient_thermal_LC(lcName='Q33',lstGradThStrnData=
    [imps.gradThermalStrain(elemSet=losa,elThick=cantoLosa,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0),
     imps.gradThermalStrain(elemSet=cartabInt,elThick=eCartInt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0),
     imps.gradThermalStrain(elemSet=cartabExt,elThick=eCartExt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0),
     imps.gradThermalStrain(elemSet=voladzInt,elThick=eVolInt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0),
     imps.gradThermalStrain(elemSet=voladzExt,elThick=eVolExt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0)])
Q34=slm.gradient_thermal_LC(lcName='Q34',lstGradThStrnData=
    [imps.gradThermalStrain(elemSet=losa,elThick=cantoLosa,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0),
     imps.gradThermalStrain(elemSet=cartabInt,elThick=eCartInt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0),
     imps.gradThermalStrain(elemSet=cartabExt,elThick=eCartExt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0),
     imps.gradThermalStrain(elemSet=voladzInt,elThick=eVolInt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0),
     imps.gradThermalStrain(elemSet=voladzExt,elThick=eVolExt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0)])
                            


allsets=[riostrEstr1,riostrEstr2,losa,cartabInt,cartabExt,voladzInt,voladzExt,pilas]
for s in allsets:
    s.fillDownwards()
    
overallSet=prep.getSets.getSet("total")
overallSet.fillDownwards()
