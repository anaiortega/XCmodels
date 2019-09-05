# -*- coding: utf-8 -*-
from __future__ import division

#Definición armaduras tablero [diámetro,separación] en mm 
#   ***Armadura transversal ***
rnom=35 #recubrimiento nominal 

#Transversal superior (continua en losa, cartabón y voladizo) ((5))
trSup_020L1=[20,200]   #transversal superior en la zona de estribo a 0.20 x luz
                       #vano 1 
trSup_L1cent=[16,200]  #transversal superior en la zona central de vano 1
trSup_020L2=[20,200]   #transversal superior sobre pila (excepto riostra) a
                       #0.20 x luz vano 2
trSup_Rpil=[20,200]    #transversal superior sobre riostra pila.
trSup_L2cent=[16,200]  #transversal superior en la zona central de vano 2

#Transversal inferior losa ((1))
trInf_los_020L1=[16,100] #transversal inferior en losa en la zona de estribo a 
                         #0.20 x luz vano 1
trInf_los=[16,200]       #transversal inferior en losa en todo el resto del
                         #tablero

#Transversal inferior cartabón ((2))
trInf_cart_020L1=[16,100] #transversal inferior en cartabón en la zona de 
                         #estribo a 0.20 x luz vano 1
                         
trInf_cart_L1cent=[10,200]  #transversal inferior en cartabón en la zona
                            #central de vano 1
trInf_cart_Rpil=[10,200]  #transversal inferior en cartabón sobre riostra pila.
trInf_cart_L2cent=[10,200]  #transversal inferior en cartabón en la zona
                            #central de vano 2

#Transversal inferior voladizo ((4))
trInf_vol_020L1=[16,200] #transversal inferior en voladizo en la zona de 
                         #estribo a 0.20 x luz vano 1
trInf_vol_L1cent=[10,200] #transversal inferior en voladizo zona central vano 1
trInf_vol_020L2=[10,200]   #transversal inferior voladizo sobre pila a
                           #0.20 x luz vano 2
trInf_vol_L2=[10,200] #transversal inferior en voladizo vano 2

#   ****Armadura longitudinal***

# Longitudinal superior losa y cartabón ((9a)) y ((9b))
lnSup_base_loscart_L1=[16,200]   #longitudinal superior losa y cart. vano 1 hasta 0.20*L2
lnSup_base_loscart_Rpil=[20,100] #base longitudinal superior losa y cart. riostra pila (se extiende a 0.20xL1 y 0.20*L2)
lnSup_ref_loscart_Rpil=None #refuerzo longitudinal superior losa y cart. riostra pila  
lnSup_ref_loscart_020L2=None #refuerzo longitudinal superior losa y cart.
                             #sobre pila a 0.20 x luz vano 2
lnSup_base_loscart_L2=[16,200] #longitudinal superior losa y cart. vano 2 (a a partir de 0.20*L2)

# Longitudinal inferior losa ((6a)) y ((6b))
lnInf_base_los_L1=[20,100] #base longitudinal inferior losa vano 1
lnInf_ref_los_L1=[16,200]  #refuerzo longitudinal inferior losa vano 1
lnInf_base_los_L2=[20,100] #base longitudinal inferior losa vano 2
lnInf_ref_los_L2=None  #refuerzo longitudinal inferior losa vano 2

# Longitudinal inferior cartabón ((7))
lnInf_cart=[20,100]        # longitudinal inferior cartabón

# Longitudinal superior voladizo ((10))
lnSup_vol_L1=[12,200]    #longitudinal superior voladizo vano 1
lnSup_vol_020L2=[12,200] #longitudinal superior voladizo sobre pila a
                         #0.20 x luz vano 2
lnSup_vol_L2=[12,200]    #longitudinal superior voladizo vano 2

# Longitudinal inferior voladizo ((8))
lnInf_vol_L1=[16,200]    #longitudinal inferior voladizo vano 1
lnInf_vol_L2=[16,200]    #longitudinal inferior voladizo vano 2

#  ***Refuerzo armadura transversal riostra pila***
#((1P)) transversal inferior (losa)
nfis=6
separ=2*LriostrPil/nfis*1000 #[mm]
trInf_ref_Rpil=[16,separ]  #transversal inferior (si None, no se considera)
#((2P)) transversal superior (losa)
nfis=16
separ=2/nfis*1000 #[mm] 
trSup_ref_RPil=[25,separ] #transversal superior (si None, no se considera)
#((3P)) transversal a medio canto (losa)
trMid_ref_RPil=[16,20]  #transversal a medio canto
#((4P)) refurezo cercos (riostra pila)
nramas_m=2 #nº ramas por m en sección transversal
diam_cercos=16
sep_long=125 #separación entre cercos en dirección longitudinal
cercos_Ref=[diam_cercos,nramas_m,sep_long]


#  ***Armadura de cortante ((3))***
# cercos vano 1 (hasta riostra pila)
nram=2*6   #nº de ramas en la sección transversal de la losa
nramas_m=int(round(nram/anchoLosa,0)) #nº ramas por m en sección transversal
diam_cercos=10
sep_long=200 #separación entre cercos en dirección longitudinal
cercos_L1=[diam_cercos,nramas_m,sep_long]
# cercos riostra pila
nram=2*6   #nº de ramas en la sección transversal de la losa
nramas_m=int(round(nram/anchoLosa,0)) #nº ramas por m en sección transversal
diam_cercos=12
sep_long=200 #separación entre cercos en dirección longitudinal
cercos_Rpil=[diam_cercos,nramas_m,sep_long]
# cercos vano 2 (desde riostra pila)
nram=2*6   #nº de ramas en la sección transversal de la losa
nramas_m=int(round(nram/anchoLosa,0)) #nº ramas por m en sección transversal
diam_cercos=10
sep_long=200 #separación entre cercos en dirección longitudinal
cercos_L2=[diam_cercos,nramas_m,sep_long]

#Refuerzo armadura transversal riostra estribo
#((1E)) refuerzo transversal inferior
nfis=11
separ=LriostrEstr/nfis*1000 #[mm] 
trInf_ref_Restr=[20,separ]  #((1E)) transversal inferior
#((2E)) refuerzo transversal superior
nfis=6
separ=LriostrEstr/nfis*1000 #[mm] 
trSup_ref_Restr=[16,separ]  #((1E)) transversal superior
#((3E)) refuerzo transversal medio canto
trMid_ref_Restr=[16,200]  #((1E)) transversal medio canto

#   ***Armadura  pilas***
#Armadura longitudinal en cada cara de la pila
lnPil=[16,50]  #armadura longitudinal en cada cara de la pila
# Cercos
nram=2  #nº de ramas en cada dirección
diam_cercos=12
sep_long=250
cercosPil=[diam_cercos,nram,sep_long]
