# -*- coding: utf-8 -*-


#Definición armaduras tablero [diámetro,separación] en mm 
#   ***Armadura transversal ***

#Transversal superior (continua en losa, cartabón y voladizo) ((5))
trSup_020L1=[20,200]   #transversal superior en la zona de estribo a 0.20 x luz
                       #vano 1 
trSup_L1cent=[16,200]  #transversal superior en la zona central de vano 1
trSup_020L2=[16,100]   #transversal superior sobre pila (excepto riostra) a
                       #0.20 x luz vano 2
trSup_Rpil=[20,100]    #transversal superior sobre riostra pila.
trSup_L2cent=[16,200]  #transversal superior en la zona central de vano 2
#Transversal inferior losa ((1))
trInf_los_020L1=[20,100] #transversal inferior en losa en la zona de estribo a 
                         #0.20 x luz vano 1
trInf_los=[16,200]       #transversal inferior en losa en todo el resto del
                         #tablero

#Transversal inferior cartabón ((2))
trInf_cart_020L1=[12,200] #transversal inferior en cartabón en la zona de 
                         #estribo a 0.20 x luz vano 1
                         
trInf_cart_L1cent=[10,200]  #transversal inferior en cartabón en la zona
                            #central de vano 1
trInf_cart_Rpil=[12,200]  #transversal inferior en cartabón sobre riostra pila.
trInf_cart_L2cent=[10,200]  #transversal inferior en cartabón sen la zona
                            #central de vano 2

#Transversal inferior voladizo ((4))
trInf_vol_L1=[10,200] #transversal inferior en voladizo vano 1
trInf_vol_020L2=[12,200]   #transversal inferior voladizo sobre pila a
                           #0.20 x luz vano 2
trInf_vol_L2=[10,200] #transversal inferior en voladizo vano 2

#   ****Armadura longitudinal***

# Longitudinal superior losa y cartabón ((9a)) y ((9b))
lnSup_base_loscart_L1=[16,200]   #longitudinal superior losa y cart. vano 1 hasta 0.20*L2
lnSup_base_loscart_Rpil=[20,100] #base longitudinal superior losa y cart. riostra pila
lnSup_ref_loscart_Rpil=[20,100] #refuerzo longitudinal superior losa y cart. riostra pila
lnSup_base_loscart_L2=[16,200] #longitudinal superior losa y cart. vano 2 (a a partir de 0.20*L2)

# Longitudinal inferior losa ((6a)) y ((6b))
lnInf_base_los_L1=[20,100] #base longitudinal inferior losa vano 1
lnInf_ref_los_L1=[25,200]  #refuerzo longitudinal inferior losa vano 1
lnInf_base_los_L2=[25,100] #base longitudinal inferior losa vano 2
lnInf_ref_los_L2=[16,100]  #refuerzo longitudinal inferior losa vano 2

# Longitudinal inferior cartabón ((7))
lnInf_cart=[16,200]        # longitudinal inferior cartabón

# Longitudinal superior voladizo ((10))
lnSup_vol_L1=[16,200]    #longitudinal superior voladizo vano 1
lnSup_vol_020L2=[16,100] #longitudinal superior voladizo sobre pila a
                         #0.20 x luz vano 2
lnSup_vol_L2=[16,200]    #longitudinal superior voladizo vano 2

# Longitudinal inferior voladizo ((8))
lnInf_vol_L1=[10,200]    #longitudinal inferior voladizo vano 1
lnInf_vol_L2=[10,200]    #longitudinal inferior voladizo vano 2

