# -*- coding: utf-8 -*-
# Write to a LaTex file verifications of elastomeric bearings
#Takes as parameters:
#      React: dictionary structure than contains strain and stresses
#             previously calculated using calc_reactions.py script
#      numNeopr: number of bearings
#      hNetoNeopr: net thickness of neoprene
#      aNeopr: length (Y-direction, longitudinal) of the bearing
#      bNeopr: width (X-direction, transversal) of the bearing
#      Gneopr: shear modulus of the elastomeric material
#      Eneopr: elactic modulus of neoprene
#      n_capas: number of neoprene layers in each bearing
#      t_capa: thickness of each neoprene layer
#      thetax0: minimum rotation to be added for eccentricity
#      CP___, SC___, ...: list of load cases to be considered for the
#                  different verifications (defined in script verif_neopr.py
#                  for each particular case)
#                         
import numpy as np
def fillMtrx(resDict,lCase,nNeopr):
    l=list()
    for i in range (nNeopr):
        l.append(React[lCase]['neoprStrain_e'+str(i+1)])
    return np.array(l)

def combsStr(lstCombs):
    combStr='Combinación: $'
    for cmb in lstCombs:
        for c in cmb[1]:
            combStr+=str(cmb[0]) + ' \\times ' + c + ' + '
    combStr=combStr[:-2] + '$ \\\\'
    return combStr
        
#comprobación presión vertical mínima
mtx=np.zeros((numNeopr,6))
for lc in CP_sgz_min:
    mtx+=fillMtrx(React,lc,numNeopr)
mtx=abs(mtx)
sgz_min=np.amin(mtx,axis=0)[2]/hNetoNeopr*Eneopr
f.write( "\\noindent \\underline{Tensión vertical mínima:}\\\\")
f.write( combsStr([[1.0,CP_sgz_min]]))
f.write( '$\sigma_{z,min}$ = '+ str(round(sgz_min*1e-6,2)) + ' MPa')
if sgz_min*1e-6 >= 2:
    f.write( '$$\\sigma_{z,min} \\ge 2 MPa \\rightarrow OK $$' )
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
sgz_max=np.amax(mtx,axis=0)[2]/hNetoNeopr*Eneopr
f.write( "\\underline{Tensión vertical máxima:}\\\\")
f.write( combsStr([[1.35,CP_sgz_max],[1.35,SC_uso_sgz_max],[0.90,W_sgz_max]]))
f.write( '$\sigma_{z,max}$ = '+ str(round(abs(sgz_max)*1e-6,2)) + ' MPa')
if sgz_max*1e-6 <= 15:
    f.write( '$$\\sigma_{z,min} \\le 15 MPa \\rightarrow OK $$' )


#Comprobación distorsión máxima cargas de corta duración
mtx=np.zeros((numNeopr,6))
for lc in CP_uy_max:
    mtx+=fillMtrx(React,lc,numNeopr)
for lc in SC_uso_uy_max_rap:
    mtx+=fillMtrx(React,lc,numNeopr)
mtx=abs(mtx)
uy_max= np.amax(mtx,axis=0)[1]
distors=uy_max/hNetoNeopr
f.write( "\\underline{Distorsión máxima por cargas de corta duración:}\\\\")
f.write( combsStr([[1.0,CP_uy_max],[1.0,SC_uso_uy_max_rap]]))
f.write( '$u_{y,max}$ = '+ str(round(uy_max*1e3,2)) + ' mm')
if distors <= 0.7:
    f.write( '$$Distors. = \\cfrac{u_{y,max}}{e_{neto}} = ' + str(round(distors,2)) + ' \\le 0.7 \\rightarrow OK $$' )

#Comprobación distorsión máxima cargas lentas
mtx=np.zeros((numNeopr,6))
for lc in CP_uy_max:
    mtx+=fillMtrx(React,lc,numNeopr)
for lc in Qlenta_uy_max:
    mtx+=fillMtrx(React,lc,numNeopr)
mtx=abs(mtx)
uy_max= np.amax(mtx,axis=0)[1]
distors=uy_max/hNetoNeopr
f.write( "\\underline{Distorsión máxima por cargas lentas:}\\\\")
f.write( combsStr([[1.0,CP_uy_max],[1.0,Qlenta_uy_max]]))
f.write( '$u_{y,max}$ = '+ str(round(uy_max*1e3,2)) + ' mm')
if distors <= 0.5:
    f.write( '$$Distors. = \\cfrac{u_{y,max}}{e_{neto}} = ' + str(round(distors,2)) + ' \\le 0.5 \\rightarrow OK $$' )

#comprobación giro máximo
mtx=np.zeros((numNeopr,6))
for lc in C_tetax_max:
    mtx+=fillMtrx(React,lc,numNeopr)
mtx=abs(mtx)
thetax_max= np.amax(mtx,axis=0)[3]
thetax_comp=thetax_max+thetax0
index_neop=np.where(mtx==thetax_max)[0].item()
sigma_conc=mtx[index_neop,2]/hNetoNeopr*Eneopr
factor_forma=aNeopr*bNeopr/(2*t_capa*(aNeopr+bNeopr))
thetax_adm=n_capas*3/factor_forma*(t_capa/aNeopr)**2*sigma_conc/Gneopr

f.write( "\\underline{Giro máximo:} \\\\")
f.write( combsStr([[1.0,C_tetax_max]]))
f.write( '$\\theta_x$ = '+ str(round(thetax_max,4)) + ' rad \\\\')
f.write( '$\\sigma_{concomitante}$ = '+ str(round(sigma_conc*1e-6,2)) + ' MPa \\\\')
f.write( '$\\theta_{x0}$ = '+ str(thetax0) + ' rad \\\\')
f.write( '$\\theta_{x,max} = \\theta_x + \\theta_{x0}$ = '+  str(round(thetax_comp,4)) + ' rad \\\\')
f.write( 'Factor de forma $S = \\cfrac{a \cdot b}{2 \cdot t (a+b)} = \\cfrac{'+ str(aNeopr)+ '\cdot'+ str(bNeopr)+ '}{2 \cdot '+ str(t_capa) + '('+ str(aNeopr) + '+'+ str(bNeopr) + ')} = ' + str(round(factor_forma,2)) + '$ \\\\')
f.write( '$\\theta_{x,adm} = n \cdot \\cfrac{3}{S} (t/a)^2 \\cfrac{\sigma_{concomitante}}{G}$ = ' + str(round(thetax_adm,4)) + ' rad')
if thetax_comp <= thetax_adm:
    f.write( '$$\\theta_{x,max} \\le \\theta_{x,adm} \\rightarrow OK $$' )

