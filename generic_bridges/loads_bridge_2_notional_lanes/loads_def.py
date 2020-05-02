# -*- coding: utf-8 -*-
# Generate load cases for a bridge with two notional lanes.
# The load cases generated are:
# G1: self-weight
# G2: dead load
# G3: shrinkage and creep
# Q1a1 to Q1e: traffic (see figure traffic_loads.pdf)
# Q1bFren to Q1eFren: traffic + bracking
# Q21 to Q22: wind
# Q31, Q31neopr: contraction thermal load
# Q32, Q32neopr: expansion thermal load
# Q33, Q34: thermal gradient
#                       ***ACTIONS***
from actions.roadway_trafic import IAP_load_models as slm
from actions.imposed_strain import imp_strain as imps
#Peso propio
if abutment.lower()[0]=='y':
    allmesh+=[murestrZ1_mesh,murestrZ2_mesh,murestrZ3_mesh]
    allmesh.append(zap_mesh)
    if LaletaIzq>0:
        allmesh+=[aletiZ1_mesh,aletiZ2_mesh,aletiZ3_mesh]
    if LaletaDer>0:
        allmesh+=[aletdZ1_mesh,aletdZ2_mesh,aletdZ3_mesh]

selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=allmesh, vAccel=xc.Vector( [0.0,0.0,-grav]))

G1=lcases.LoadCase(preprocessor=prep,name="G1",loadPType="default",timeSType="constant_ts")
G1.create()
G1.addLstLoads([selfWeight])
#Dead load case
G2=slm.dead_LC(lcName='G2',drivewaySet=calzada,qAsphalt=pav_sup,sidewalkSet=aceras,qSidewalk=qDeadAcera,barrierSet=barrera,qBarrier=qBarrera,deckEdgeSet=bordTabl,qDeckEdge=qAntivand)
G12=lcases.LoadCase(preprocessor=prep,name="G12",loadPType="default",timeSType="constant_ts")
G12.create()
G12.addLstLoads([selfWeight]+G2.lstOfLoadDef)


#Rheological load cases
G3=slm.thermal_rheological_LC(lcName='G3',lstUnifThStrnData=[imps.unifStrain(elemSet=RheoSetDirY,DOF=1,strain=eps_retracc)])
#Traffic load cases
Q1a1=slm.IAP_traffic_LC(lcName='Q1a1',deckSet=calzada,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano1,hDistrPL=hDistrPL,slopeDistrPL=1.0,sidewalkSet=acerDer)
Q1a2=slm.IAP_traffic_LC(lcName='Q1a2',deckSet=calzada,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano2,hDistrPL=hDistrPL,slopeDistrPL=1.0,sidewalkSet=acerDer)
Q1b1=slm.IAP_traffic_LC(lcName='Q1b1',deckSet=calzada,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano1,hDistrPL=hDistrPL,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=centVFi_vano1,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1b2=slm.IAP_traffic_LC(lcName='Q1b2',deckSet=calzada,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano2,hDistrPL=hDistrPL,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=centVFi_vano2,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1c=slm.IAP_traffic_LC(lcName='Q1c',deckSet=calzada,virtLane1Set=viaFictDer_vano2,xyCentPL1=centVFd_vano2,hDistrPL=hDistrPL,slopeDistrPL=1.0,virtLane2Set=viaFictIzq_vano2,xyCentPL2=centVFi_vano2,restDrivewaySet=viaFictResto_vano2,sidewalkSet=aceras)
Q1d=slm.IAP_traffic_LC(lcName='Q1d',deckSet=calzada,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano2,hDistrPL=hDistrPL,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano2,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1e=slm.IAP_traffic_LC(lcName='Q1e',deckSet=calzada,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano1,hDistrPL=hDistrPL,slopeDistrPL=1.0,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano1,restDrivewaySet=viaFictResto,sidewalkSet=aceras)

Q1bFren=slm.IAP_traffic_LC(lcName='Q1bFren',deckSet=calzada,virtLane1Set=viaFictDer,xyCentPL1=centVFd_vano1,hDistrPL=hDistrPL,slopeDistrPL=1.0,vQbraking=vQfren,virtLane2Set=viaFictIzq,xyCentPL2=centVFi_vano1,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1dFren=slm.IAP_traffic_LC(lcName='Q1dFren',deckSet=calzada,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano2,hDistrPL=hDistrPL,slopeDistrPL=1.0,vQbraking=vQfren,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano2,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
Q1eFren=slm.IAP_traffic_LC(lcName='Q1eFren',deckSet=calzada,virtLane1Set=viaFictDer,xyCentPL1=extrVFd_vano1,hDistrPL=hDistrPL,slopeDistrPL=1.0,vQbraking=vQfren,virtLane2Set=viaFictIzq,xyCentPL2=extrVFi_vano1,restDrivewaySet=viaFictResto,sidewalkSet=aceras)
#Wind load cases
Q21=slm.wind_LC(lcName='Q21',deckLineSet=bordizqTabl,vectWindDeck=[qWTablero,0],windwardPileSet=pilasBarlov,vectWindwardPile=[qWpilasBarlov,0],leewardPileSet=pilasSotav,vectLeewardPile=[qWpilasSotav,0])
Q22=slm.wind_LC(lcName='Q22',deckLineSet=bordizqTabl,vectWindDeck=[qWTableroSCuso,0],windwardPileSet=pilasBarlov,vectWindwardPile=[qWpilasBarlov,0],leewardPileSet=pilasSotav,vectLeewardPile=[qWpilasSotav,0])
#Thermal load cases
#Contraction
Q31=slm.thermal_rheological_LC(lcName='Q31',lstUnifThStrnData=[imps.unifThermalStrain(elemSet=ThermalUnifSetDirY,DOF=1,alpha=coefDilat,temp=Tunif_contr)])
Q31neopr=slm.thermal_rheological_LC(lcName='Q31neopr',lstUnifThStrnData=[imps.unifThermalStrain(elemSet=ThermalUnifSetDirY,DOF=1,alpha=coefDilat,temp=Tunif_contr_neopr)])
#Expansion
Q32=slm.thermal_rheological_LC(lcName='Q32',lstUnifThStrnData=[imps.unifThermalStrain(elemSet=ThermalUnifSetDirY,DOF=1,alpha=coefDilat,temp=Tunif_dilat)])
Q32neopr=slm.thermal_rheological_LC(lcName='Q32neopr',lstUnifThStrnData=[imps.unifThermalStrain(elemSet=ThermalUnifSetDirY,DOF=1,alpha=coefDilat,temp=Tunif_dilat_neopr)])
