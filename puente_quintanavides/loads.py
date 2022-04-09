# -*- coding: utf-8
# Definición de acciones.

from actions.railway_traffic import IAPF_rail_load_models as iapf
from actions.wind import IAPF_wind

loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= list()
loadCaseNames.append('RETRACC')
loadCaseNames.append('FLU')

loadCaseNames.append('G0') # Peso propio de la sección prefabricada
loadCaseNames.append('G0B') # Peso propio de la losa superior
loadCaseNames.append('G1') # Peso propio de la losa superior y de la carga muerta
loadCaseNames.append('TC1V1') # Tren de cargas 1 en vía 1
loadCaseNames.append('TC1V2') # Tren de cargas 1 en vía 2
loadCaseNames.append('TC2V1') # Tren de cargas 2 en vía 1
loadCaseNames.append('TC2V2') # Tren de cargas 2 en vía 2
loadCaseNames.append('TC3V1') # Tren de cargas 3 en vía 1
loadCaseNames.append('TC3V2') # Tren de cargas 3 en vía 2
loadCaseNames.append('FV1') # Frenado en vía 1
loadCaseNames.append('FV2') # Frenado en vía 2
loadCaseNames.append('ARRV1') # Arranque en vía 1
loadCaseNames.append('ARRV2') # Arranque en vía 2
loadCaseNames.append('LZV1') # Efecto de lazo en vía 1
loadCaseNames.append('LZV2') # Efecto de lazo en vía 2
loadCaseNames.append('VTRSV') # Viento transversal
loadCaseNames.append('VLONG') # Viento longitudinal
loadCaseNames.append('NV') # Nieve
loadCaseNames.append('AD2') # Situación de descarrilo 2
loadCaseManager.defineSimpleLoadCases(loadCaseNames) 

numAcciones= len(loadCaseNames)
nPaso= 0
cargaUnitariaLosaSup= cargaUnitariaTablero/BTablero

# tren de cargas 1 en vía 1
cargaPCarril= 1.21*250e3/2
sepMediaNodos= 0.0
cargaRCarril= 1.21*80e3/2

# Carga viga
pesoUnitarioLosaInf= gammaHA*hormLosaInf.h
pesoUnitarioAlmas30= gammaHA*hormAlmas30.h
pesoUnitarioAlmas27= gammaHA*hormAlmas27.h 
pesoUnitarioAlmas22= gammaHA*hormAlmas22.h 
pesoUnitarioAlmaC40= gammaHA*hormAlmaC40.h 
pesoUnitarioAlmaC50= gammaHA*hormAlmaC50.h 
pesoUnitarioDiafrag= gammaHA*hormDiafrag.h 
pesoUnitarioLosaSup= gammaHA*hormLosaSup.h

f= iapf.CoefReductorCentrifugaIAPF(VelProy,39.2) # Coeficiente reductor según apartado 2.3.2.2 IAPF
Qf= cargaP*f*(VelProy**2)/9.81/radioCurva/1.2 # Dividimos por 1.2 porque v>120 km/h 
qf= cargaR*f*(VelProy**2)/9.81/radioCurva/1.2 # Dividimos por 1.2 porque v>120 km/h 

print("f= ",f,"\n")
print("Qf= ",Qf/1e3," kN\n")
print("qf= ",qf/1e3," kN\n")

## Wind
VRef= 28 # Velocidad de referencia según figura 2.20 IAPF
Ct= 1.0 # Factor de topografía según apartado 2.3.7.2 IAPF
Cr= 1.04 # Factor de riesgo para situaciones persistentes según apartado 2.3.7.2 IAPF
GAE= 2 # Grado de aspereza del entorno según apartado 2.3.7.2 IAPF
kz= IAPF_wind.ParamKIAPF(GAE) # Factor del terreno según cuadro 2.4 IAPF

### Empujes sobre el tablero
z= 10.3-cantoTablero/2 # Altura media de la superficie expuesta del tablero
zmin= IAPF_wind.ZminIAPF(GAE) # Altura mínima según cuadro 2.4 IAPF
z0= IAPF_wind.Z0IAPF(GAE) # Longitud rugosidad según cuadro 2.4 IAPF
Cz= IAPF_wind.CzIAPF(GAE,z) # Factor de altura según apartado 2.3.7.2 IAPF.
Cg= IAPF_wind.CgIAPF(kz,Cz,Ct) # Factor de ráfaga según apartado 2.3.7.2 IAPF.
Vc= Ct*Cr*Cz*Cg*VRef # Velocidad de cálculo según apartado 2.3.7.2 IAPF.
coefReductor= 1-(5/1000*math.degrees(modelSpace.angAlma))
Cd= IAPF_wind.CdTableroAlmaLlenaIAPF(BTablero,cantoTablero,modelSpace.angAlma) # Coeficiente de arrastre para el tablero.
FkHTablero= IAPF_wind.FHkPorMetroIAPF(Cd,cantoTablero,Vc) # Empuje horizontal por metro de tablero.
FkVTablero= IAPF_wind.FVkPorMetroIAPF(BTablero,Vc) # Empuje vertical por metro de tablero.

print("Tablero; kz= ",kz)
print("Tablero; Cz= ",Cz)
print("Tablero; Cg= ",Cg)
print("Tablero; Vc= ",Vc)
print("Tablero; coefReductor= ",coefReductor)
print("Tablero; angAlma= ",math.degrees(modelSpace.angAlma)," grados\n")
print("Tablero; Cd= ",Cd)
print("Tablero; FkH= ",FkHTablero/1e3," kN/m")
print("Tablero; FkV= ",FkVTablero/1e3," kN/m")

### Empujes sobre el vehículo
hVehiculo= 4 # Altura de la sobrecarga ferroviaria según apartado 2.3.7.3 IAPF.
z= 10.3+hVehiculo/2 # Altura media de la superficie expuesta del vehículo
Cz= IAPF_wind.CzIAPF(GAE,z) # Factor de altura según apartado 2.3.7.2 IAPF.
Cg= IAPF_wind.CgIAPF(kz,Cz,Ct) # Factor de ráfaga según apartado 2.3.7.2 IAPF.
Vc= Ct*Cr*Cz*Cg*VRef # Velocidad de cálculo según apartado 2.3.7.2 IAPF.
Cd= 2.2 # Coeficiente de arrastre para la sobrecarga ferroviaria.
FkHTren= IAPF_wind.FHkPorMetroIAPF(Cd,hVehiculo,Vc) # Empuje horizontal por metro de tablero.
FkHCarriles= FkHTren/2 # Acción horizontal del viento sobre los carriles.
FkVCarrilBarlovento= -FkHTren*hVehiculo/2/anchoViaUIC # Acción horizontal del viento sobre el carril a barlovento.
FkVCarrilSotavento= FkHTren*hVehiculo/2/anchoViaUIC # Acción horizontal del viento sobre el carril a sotavento.

print("Sobrecarga ferroviaria; Cz= ",Cz)
print("Sobrecarga ferroviaria; Cg= ",Cg)
print("Sobrecarga ferroviaria; Vc= ",Vc)
print("Sobrecarga ferroviaria; coefReductor= ",coefReductor)
print("Sobrecarga ferroviaria; angAlma= ",math.degrees(modelSpace.angAlma)," grados\n")
print("Sobrecarga ferroviaria; Cd= ",Cd)
print("Sobrecarga ferroviaria; FkH= ",FkHTren/1e3," kN/m")
print("Sobrecarga ferroviaria; FkVCarrilBarlovento= ",FkVCarrilBarlovento/1e3," kN/m")
print("Sobrecarga ferroviaria; FkVCarrilSotavento= ",FkVCarrilSotavento/1e3," kN/m")

### Peso propio de la viga
cLC= loadCaseManager.setCurrentLoadCase('G0')

for e in modelSpace.setLosaInf.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioLosaInf]))

for e in modelSpace.setAlmasC50.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioAlmaC50]))

for e in modelSpace.setAlmasC40.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioAlmaC40]))

for e in modelSpace.setAlmas30.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioAlmas30]))

for e in modelSpace.setAlmas27.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioAlmas27]))

for e in modelSpace.setAlmas22.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioAlmas22]))

for e in modelSpace.setDiafragmas.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioDiafrag]))

## Genera malla losa superior. ¿Otra vez?
modelSpace.mallaLosaSup()

modelSpace.createLoadDefinitionSets()

# Peso propio de la losa superior, se emplea en la
# prueba de carga estática.

cLC= loadCaseManager.setCurrentLoadCase('G0B')
for e in modelSpace.setLosaSup.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioLosaSup]))
cLC= loadCaseManager.setCurrentLoadCase('G1')
for e in modelSpace.setLosaSup.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioLosaSup-cargaUnitariaLosaSup]))

# Arranque en vía 1
cLC= loadCaseManager.setCurrentLoadCase('ARRV1')
arranqueVia= 1.21*33e3*modelSpace.ladoElemento/2*30/LTot
for n in modelSpace.setNodosVia1.nodes:
    n.newLoad(xc.Vector([-arranqueVia,0,0,0,0,0]))

# Arranque en vía 2
cLC= loadCaseManager.setCurrentLoadCase('ARRV2')
arranqueVia= 1.21*33e3*modelSpace.ladoElemento/2*30/38
for n in modelSpace.setNodosVia2.nodes:
    n.newLoad(xc.Vector([-arranqueVia,0,0,0,0,0]))

# Frenado en vía 1
cLC= loadCaseManager.setCurrentLoadCase('FV1')
frenadoVia= 1.21*20e3*modelSpace.ladoElemento/2
for n in modelSpace.setNodosVia1.nodes:
    n.newLoad(xc.Vector([frenadoVia,0,0,0,0,0]))
    
# Frenado en vía 2
cLC= loadCaseManager.setCurrentLoadCase('FV2')
frenadoVia= 1.21*20e3*modelSpace.ladoElemento/2
for n in modelSpace.setNodosVia2.nodes:
    n.newLoad(xc.Vector([frenadoVia,0,0,0,0,0]))

# Carga de lazo en vía 1
cargaLazo= 1.21*100e3
nP1= modelSpace.setNodosVia1.getNearestNode(geom.Pos3d(LTablero/2.0,modelSpace.yVia1CD,modelSpace.zVia1CD))
cLC= loadCaseManager.setCurrentLoadCase('LZV1')
nP1.newLoad(xc.Vector([0,cargaLazo,0,0,0,0]))

# Carga de lazo en vía 2
nP1= modelSpace.setNodosVia2.getNearestNode(geom.Pos3d(LTablero/2.0,modelSpace.yVia2CI,modelSpace.zVia2CI))
cLC= loadCaseManager.setCurrentLoadCase('LZV2')
nP1.newLoad(xc.Vector([0,-cargaLazo,0,0,0,0]))

# Carga de nieve.
cLC= loadCaseManager.setCurrentLoadCase('NV')
cargaNieve= 1e3
for e in modelSpace.setElemsNieve.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-cargaNieve]))

# tren de cargas 1 en vía 1
cLC= loadCaseManager.setCurrentLoadCase('TC1V1')
sepMediaNodos= (LTot-modelSpace.x5TC1)*2/len(modelSpace.setNodosRVia1TC1.nodes)
for n in modelSpace.setNodosRVia1TC1.nodes:
    n.newLoad(xc.Vector([0,0,-cargaRCarril*sepMediaNodos,0,0,0]))
for n in modelSpace.setNodosPVia1TC1.nodes:
    n.newLoad(xc.Vector([0,0,-cargaPCarril,0,0,0]))
    
# tren de cargas 1 en vía 2
cLC= loadCaseManager.setCurrentLoadCase('TC1V2')
sepMediaNodos= (LTot-modelSpace.x5TC1)*2/len(modelSpace.setNodosRVia1TC1.nodes)
for n in modelSpace.setNodosRVia2TC1.nodes:
    n.newLoad(xc.Vector([0,0,-cargaRCarril*sepMediaNodos,0,0,0]))
for n in modelSpace.setNodosPVia2TC1.nodes:
    n.newLoad(xc.Vector([0,0,-cargaPCarril,0,0,0]))

# tren de cargas 2 en vía 1
cLC= loadCaseManager.setCurrentLoadCase('TC2V1')
sepMediaNodos= (LTot-modelSpace.x5TC2+modelSpace.x0TC2)*2/len(modelSpace.setNodosRVia1TC2.nodes)
for n in modelSpace.setNodosRVia1TC2.nodes:
    n.newLoad(xc.Vector([0,0,-cargaRCarril*sepMediaNodos,0,0,0]))
for n in modelSpace.setNodosPVia1TC2.nodes:
    n.newLoad(xc.Vector([0,0,-cargaPCarril,0,0,0]))
    
# tren de cargas 2 en vía 2
cLC= loadCaseManager.setCurrentLoadCase('TC2V2')
sepMediaNodos= (LTot-modelSpace.x5TC2+modelSpace.x0TC2)*2/len(modelSpace.setNodosRVia2TC2.nodes)
for n in modelSpace.setNodosRVia2TC2.nodes:
    n.newLoad(xc.Vector([0,0,-cargaRCarril*sepMediaNodos,0,0,0]))
for n in modelSpace.setNodosPVia2TC2.nodes:
    n.newLoad(xc.Vector([0,0,-cargaPCarril,0,0,0]))

# tren de cargas 3 en vía 1
cLC= loadCaseManager.setCurrentLoadCase('TC3V1')
sepMediaNodos= modelSpace.x0TC3*2/len(modelSpace.setNodosRVia1TC3.nodes)
for n in modelSpace.setNodosRVia1TC3.nodes:
    n.newLoad(xc.Vector([0,0,-cargaRCarril*sepMediaNodos,0,0,0]))
for n in modelSpace.setNodosPVia1TC3.nodes:
    n.newLoad(xc.Vector([0,0,-cargaPCarril,0,0,0]))
    
# tren de cargas 3 en vía 2
cLC= loadCaseManager.setCurrentLoadCase('TC3V2')
sepMediaNodos= modelSpace.x0TC3*2/len(modelSpace.setNodosRVia2TC3.nodes)
for n in modelSpace.setNodosRVia2TC3.nodes:
    n.newLoad(xc.Vector([0,0,-cargaRCarril*sepMediaNodos,0,0,0]))
for n in modelSpace.setNodosPVia2TC3.nodes:
    n.newLoad(xc.Vector([0,0,-cargaPCarril,0,0,0]))
    
# Viento transversal
cLC= loadCaseManager.setCurrentLoadCase('VTRSV')
vientoTrsvH= FkHTablero/cantoTablero*2 # Se aplica en los elementos de la mitad superior para simular el momento.
for e in modelSpace.setElemsVientoTrsvH.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0,vientoTrsvH,0]))
vientoTrsvV= FkVTablero/BTablero*2# Se aplica en los elementos de la mitad derecha para simular el momento.
for e in modelSpace.setElemsVientoTrsvV.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([0,0,vientoTrsvV]))
    
# Viento longitudinal
cLC= loadCaseManager.setCurrentLoadCase('VLONG')
vientoLongH= FkHTablero/cantoTablero*0.25/coefReductor
for e in modelSpace.setElemsVientoLong.elements:
    e.vector3dUniformLoadGlobal(xc.Vector([vientoLongH,0,0]))

# Descarrilo
cLC= loadCaseManager.setCurrentLoadCase('AD2')
sepMediaNodos= (20-modelSpace.x5TC1)/len(modelSpace.setNodosRMureteCI.nodes)
print("sepMediaNodos= ",sepMediaNodos,"n")
for n in modelSpace.setNodosRMureteCI.nodes:
    n.newLoad(xc.Vector([0,0,-2*1.4*cargaRCarril*sepMediaNodos,0,0,0]))
for n in modelSpace.setNodosPMureteCI.nodes:
    n.newLoad(xc.Vector([0,0,-2*1.4*cargaPCarril,0,0,0]))

# modelSpace.createStaticLoadTestSets()

# # Cargas prueba de carga dinámica.
# cLC= loadCaseManager.setCurrentLoadCase('PCD')
# for e in modelSpace.setLosaSup.elements:
#     e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioLosaSup]))
# for n in modelSpace.nodosRuedas:
#     n.newLoad(xc.Vector([0,0,-19500*9.81,0,0,0]))

# # Cargas prueba de carga estática.
# cLC= loadCaseManager.setCurrentLoadCase('PCE')
# for e in modelSpace.setLosaSup.elements:
#     e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioLosaSup]))
# for n in modelSpace.nodosRuedasTraseras:
#     n.newLoad(xc.Vector([0,0,-10*9810,0,0,0]))
# for n in modelSpace.nodosRuedasIntermedias:
#     n.newLoad(xc.Vector([0,0,-13*9810,0,0,0]))
# for n in modelSpace.nodosRuedasDelanteras:
#     n.newLoad(xc.Vector([0,0,-7*9810,0,0,0]))
