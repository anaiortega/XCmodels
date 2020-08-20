# -*- coding: utf-8
# incluye("datos_base.xci")
# incluye("acciones/IAPF/centrifugaIAPF.xcm")
f= CoefReductorCentrifugaIAPF(VelProy,39.2) # Coeficiente reductor según apartado 2.3.2.2 IAPF
Qf= cargaP*f*sqr(VelProy)/9.81/radioCurva/1.2 # Dividimos por 1.2 porque v>120 km/h 
qf= cargaR*f*sqr(VelProy)/9.81/radioCurva/1.2 # Dividimos por 1.2 porque v>120 km/h 

print("f= ",f,"\n")
print("Qf= ",Qf/1e3," kN\n")
print("qf= ",qf/1e3," kN\n")

