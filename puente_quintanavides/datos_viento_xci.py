# -*- coding: utf-8

VRef= 28 # Velocidad de referencia según figura 2.20 IAPF
Ct= 1.0 # Factor de topografía según apartado 2.3.7.2 IAPF
Cr= 1.04 # Factor de riesgo para situaciones persistentes según apartado 2.3.7.2 IAPF
GAE= 2 # Grado de aspereza del entorno según apartado 2.3.7.2 IAPF
kz= ParamKIAPF(GAE) # Factor del terreno según cuadro 2.4 IAPF

# Empujes sobre el tablero
z= 10.3-cantoTablero/2 # Altura media de la superficie expuesta del tablero
zmin= ZminIAPF(GAE) # Altura mínima según cuadro 2.4 IAPF
z0= Z0IAPF(GAE) # Longitud rugosidad según cuadro 2.4 IAPF
Cz= CzIAPF(GAE,z) # Factor de altura según apartado 2.3.7.2 IAPF.
Cg= CgIAPF(kz,Cz,Ct) # Factor de ráfaga según apartado 2.3.7.2 IAPF.
Vc= Ct*Cr*Cz*Cg*VRef # Velocidad de cálculo según apartado 2.3.7.2 IAPF.
coefReductor= 1-(5/1000*rad2deg(angAlma))
Cd= CdTableroAlmaLlenaIAPF(BTablero,cantoTablero,angAlma) # Coeficiente de arrastre para el tablero.
FkHTablero= FHkPorMetroIAPF(Cd,cantoTablero,Vc) # Empuje horizontal por metro de tablero.
FkVTablero= FVkPorMetroIAPF(BTablero,Vc) # Empuje vertical por metro de tablero.

print("Tablero; kz= ",kz,"\n")
print("Tablero; Cz= ",Cz,"\n")
print("Tablero; Cg= ",Cg,"\n")
print("Tablero; Vc= ",Vc,"\n")
print("Tablero; coefReductor= ",coefReductor,"\n")
print("Tablero; angAlma= ",rad2deg(angAlma)," grados\n")
print("Tablero; Cd= ",Cd,"\n")
print("Tablero; FkH= ",FkHTablero/1e3," kN/m\n")
print("Tablero; FkV= ",FkVTablero/1e3," kN/m\n")


# Empujes sobre el vehículo
hVehiculo= 4 # Altura de la sobrecarga ferroviaria según apartado 2.3.7.3 IAPF.
z= 10.3+hVehiculo/2 # Altura media de la superficie expuesta del vehículo
Cz= CzIAPF(GAE,z) # Factor de altura según apartado 2.3.7.2 IAPF.
Cg= CgIAPF(kz,Cz,Ct) # Factor de ráfaga según apartado 2.3.7.2 IAPF.
Vc= Ct*Cr*Cz*Cg*VRef # Velocidad de cálculo según apartado 2.3.7.2 IAPF.
Cd= 2.2 # Coeficiente de arrastre para la sobrecarga ferroviaria.
FkHTren= FHkPorMetroIAPF(Cd,hVehiculo,Vc) # Empuje horizontal por metro de tablero.
FkHCarriles= FkHTren/2 # Acción horizontal del viento sobre los carriles.
FkVCarrilBarlovento= -FkHTren*hVehiculo/2/anchoViaUIC # Acción horizontal del viento sobre el carril a barlovento.
FkVCarrilSotavento= FkHTren*hVehiculo/2/anchoViaUIC # Acción horizontal del viento sobre el carril a sotavento.

print("Sobrecarga ferroviaria; Cz= ",Cz,"\n")
print("Sobrecarga ferroviaria; Cg= ",Cg,"\n")
print("Sobrecarga ferroviaria; Vc= ",Vc,"\n")
print("Sobrecarga ferroviaria; coefReductor= ",coefReductor,"\n")
print("Sobrecarga ferroviaria; angAlma= ",rad2deg(angAlma)," grados\n")
print("Sobrecarga ferroviaria; Cd= ",Cd,"\n")
print("Sobrecarga ferroviaria; FkH= ",FkHTren/1e3," kN/m\n")
print("Sobrecarga ferroviaria; FkVCarrilBarlovento= ",FkVCarrilBarlovento/1e3," kN/m\n")
print("Sobrecarga ferroviaria; FkVCarrilSotavento= ",FkVCarrilSotavento/1e3," kN/m\n")
