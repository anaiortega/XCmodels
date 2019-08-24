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

fullProjPath='/home/ana/projects/XCmodels/PS_Palencia/PS_1/'
execfile(fullProjPath+'env_config.py')

execfile(fullProjPath+'data.py')
execfile(path_model_slab_bridge+'model_gen.py')

#Definition of sets
execfile(fullProjPath+'sets_def.py')

#                       ***BOUNDARY CONDITIONS***
execfile(fullProjPath+'bound_cond.py')
        
#                       ***ACTIONS***
execfile(path_loads_def+'loads_def.py')                           
'''
#                       ***ACTIONS***
from actions.roadway_trafic import standard_load_models as slm
from actions.imposed_strain import imp_strain as imps
#Peso propio
setsSelfWeight=allmesh+[pilasBarlov_mesh]
if pilasSotav:
    setsSelfWeight.append(pilasSotav_mesh)
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=setsSelfWeight, vAccel=xc.Vector( [0.0,0.0,-grav]))

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
Q1b1=slm.IAP_traffic_LC(lcName='Q1b1',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano1,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=centVFi_vano1,sidewalkSet=aceras)
Q1b2=slm.IAP_traffic_LC(lcName='Q1b2',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano2,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=centVFi_vano2,sidewalkSet=aceras)
Q1c=slm.IAP_traffic_LC(lcName='Q1c',deckSet=tablero,virtLane1Set=viaFictDer_cent,xyCentPL1=centVFd_vano2,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq_cent,xyCentPL2=centVFi_vano2,sidewalkSet=aceras)
Q1d=slm.IAP_traffic_LC(lcName='Q1d',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano2,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano2,sidewalkSet=aceras)
Q1e=slm.IAP_traffic_LC(lcName='Q1e',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano1,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano1,sidewalkSet=aceras)

Q1bFren=slm.IAP_traffic_LC(lcName='Q1bFren',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano1,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,vQbraking=vQfren,virtLane2Set=viaFictIzq,xyCentPL2=centVFi_vano1,sidewalkSet=aceras)
Q1dFren=slm.IAP_traffic_LC(lcName='Q1dFren',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano2,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,vQbraking=vQfren,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano2,sidewalkSet=aceras)
Q1eFren=slm.IAP_traffic_LC(lcName='Q1eFren',deckSet=tablero,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano1,hDistrPL=cantoLosa/2.,slopeDistrPL=1.0,vQbraking=vQfren,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano1,sidewalkSet=aceras)
#Wind load cases
Q21=slm.wind_LC(lcName='Q21',deckLineSet=bordizqTabl,vectWindDeck=[qWTablero,0],windwardPileSet=pilasBarlov,vectWindwardPile=[qWpilasBarlov,0],leewardPileSet=pilasSotav,vectLeewardPile=[qWpilasSotav,0])
Q22=slm.wind_LC(lcName='Q22',deckLineSet=bordizqTabl,vectWindDeck=[qWTableroSCuso,0],windwardPileSet=pilasBarlov,vectWindwardPile=[qWpilasBarlov,0],leewardPileSet=pilasSotav,vectLeewardPile=[qWpilasSotav,0])
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
'''                            


allsets=[riostrEstr1,riostrEstr2,losa,cartabInt,cartabExt,voladzInt,voladzExt,pilasBarlov]
if pilasSotav:
    allsets.append(pilasSotav)
for s in allsets:
    s.fillDownwards()
    
overallSet=prep.getSets.getSet("total")
overallSet.fillDownwards()
