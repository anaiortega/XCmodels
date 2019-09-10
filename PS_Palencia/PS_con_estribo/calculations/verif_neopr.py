# -*- coding: utf-8 -*-
import numpy as np
execfile('../init_data.py')
#execfile("../env_config_deck.py")
execfile('../data_deck_piers.py')
execfile(fullProjPath+'results_deck/reactions/react.py')

#Cargas permanentes para combinación de presión vertical mínima
CP_sgz_min=['G1']
#Cargas permanentes para combinación de presión vertical máxima
CP_sgz_max=['G1','G2']
#SC uso para combinación de presión vertical máxima
SC_uso_sgz_max=['Q1e']
#Viento  para combinación de presión vertical máxima
W_sgz_max=['Q21']

#Cargas permanentes para combinación de desplazamiento u_y máximo
CP_uy_max=['G1','G2','G4']
#SC uso para combinación de desplazamiento u_y máximo (cargas rápidas)
SC_uso_uy_max_rap=['Q1eFren','Q4']
#Cargas lentas para combinación de desplazamiento u_y máximo
Qlenta_uy_max=['Q32neopr']

def fillMtrx(resDict,lCase,nNeopr):
    l=list()
    for i in range (nNeopr):
        l.append(React[lCase]['neoprStress_e'+str(i+1)])
    return np.array(l)
        
#fin datos
#comprobación presión vertical mínima
mtx=np.zeros((numNeopr,6))
for lc in CP_sgz_min:
    mtx+=fillMtrx(React,lc,numNeopr)
mtx=abs(mtx)
sgz_min=np.amin(mtx,axis=0)[2]
print '$\sigma_{z,min}= ', round(sgz_min*1e-6,2), ' MPa'

#comprobación presión vertical máxima
mtx=np.zeros((numNeopr,6))
for lc in CP_sgz_max:
    mtx+=1.35*fillMtrx(React,lc,numNeopr)
for lc in SC_uso_sgz_max:
    mtx+=1.35*fillMtrx(React,lc,numNeopr)
if len(W_sgz_max)>0:
    for lc in W_sgz_max:
        mtx+=0.90*fillMtrx(React,lc,numNeopr)
mtx=abs(mtx)
sgz_max=np.amax(mtx,axis=0)[2]
print '$\sigma_{z,max}= ', round(abs(sgz_max)*1e-6,2), ' MPa'

#Comprobación distorsión máxima cargas de corta duración
mtx=np.zeros((numNeopr,6))
for lc in CP_uy_max:
    mtx+=fillMtrx(React,lc,numNeopr)
for lc in SC_uso_uy_max_rap:
    mtx+=fillMtrx(React,lc,numNeopr)
mtx=abs(mtx)
uy_max= np.amax(mtx,axis=0)[1]
print '$u_{y,max}= $', round(uy_max*1e-3,2), ' mm'

#Comprobación distorsión máxima cargas lentas
mtx=np.zeros((numNeopr,6))
for lc in CP_uy_max:
    mtx+=fillMtrx(React,lc,numNeopr)
for lc in Qlenta_uy_max:
    mtx+=fillMtrx(React,lc,numNeopr)
mtx=abs(mtx)
uy_max= np.amax(mtx,axis=0)[1]
print '$u_{y,max}= $', round(uy_max*1e-3,2), ' mm'
