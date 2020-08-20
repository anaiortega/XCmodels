# -*- coding: utf-8
# Datos materiales
rhoHA= 2500 # Densidad del hormigón armado.
gammaHA= rhoHA*9.81 # Peso específico del hormigón armado.
densAcero= 7850 # Densidad del acero.
Ec30= 27264041000.0 # Módulo elástico del hormigón HA-30.
Ec50= 31928428000.0 # Módulo elástico del hormigón HP-50.
nu= 0.3
Gc30= Ec30/(2*(1+nu))
Gc50= Ec50/(2*(1+nu))

# Datos básicos del tablero.
cantoTablero= 1.426+1.171+0.15+0.125 # Canto del tablero.
zPlanoMedioLosaInfTablero= 8.1235 # Cota del plano medio de la losa inferior del tablero.
cantoLosaInfTablero= 0.25 # Canto del tablero.
zCDGTablero= 10 # Cota del centro de gravedad del tablero.
yApoyoDerecho= -1.575
yApoyoIzquierdo= -yApoyoDerecho
zVias= zPlanoMedioLosaInfTablero+cantoTablero+cantoLosaInfTablero/2+1.0
brazoPretInferior= zCDGTablero-zPlanoMedioLosaInfTablero # Brazo del pretensado inferior.
brazoPretSuperior= 2.57-0.048-cantoLosaInfTablero/2-brazoPretInferior # Brazo del pretensado superior.
brazoYEjeVia= 2.35 # Distancia del eje de la vía al eje del tablero medida sobre la horizontal.
brazoYEjeVia1= brazoYEjeVia # Distancia del eje de la vía 1 al eje del tablero medida sobre la horizontal.
brazoYEjeVia2= -brazoYEjeVia # Distancia del eje de la vía 2 al eje del tablero medida sobre la horizontal.
brazoZEjeVias= zVias-zCDGTablero # Distancia del eje de la vía al eje del tablero medida sobre la vertical.
BTablero= 14 # Ancho del tablero.
LTablero= 38 # Luz entre apoyos del tablero.
LongTablero= LTablero+2*0.7 # Longitud del tablero.
Aartesa= 2.498 # Área de la sección prefabricada en artesa.
HLosa= 0.35 # Espesor medio de la losa.
Alosa= HLosa*BTablero # Área de la sección de la losa y prelosas.
pesoUnitarioTablero= (Aartesa+Alosa)*gammaHA

# Carga permanente sobre el tablero.
gammaBalasto= 18e3 # Peso específico del balasto.
areaBalasto= 5.539 # Área de la sección de balasto.
gammaHM= 24e3 # Peso específico del hormigón en masa.
bombeo= 2/100 # Bombeo de la superficie de formación de pendientes.
areaFormPend= 1/2*BTablero*(bombeo*BTablero) # Bombeo de la superficie de formación de pendientes.
bMureteGuardaBalasto= 0.2 # Ancho del murete guardabalasto.
hMureteGuardaBalasto= 0.5 # Alto del murete guardabalasto.
areaMureteGuardaBalasto= bMureteGuardaBalasto*hMureteGuardaBalasto # Alto del murete guardabalasto.
numVias= 2 # Número de vías.
pesoTraviesas= numVias*5.2e3 # Peso de las vías por unidad de longitud.
pesoCarriles= numVias*1.2e3 # Peso de los carriles por unidad de longitud.
pesoCableado= numVias*3e3 # Peso del cableado por unidad de longitud.
areaImposta= 0.223 # Área de la imposta.
pesoPantallas= 5e3 # Peso de las pantallas por unidad de longitud.

cargaUnitariaTablero= 1.3*areaBalasto*gammaBalasto+areaFormPend*gammaHM+2*areaMureteGuardaBalasto*gammaHA+pesoTraviesas+pesoCarriles+pesoCableado+2*areaImposta*gammaHA+2*pesoPantallas


# Sobrecargas.
anchoAceras= 1.75 # Ancho de las aceras en metros.
sobrecargaAceras= 5e3 # Sobrecarga sobre las aceras en kN/m2.

anchoViaUIC= 1.435+0.07
VelProy= 270/3.6 # Velocidad de proyecto en m/s.
cargaP= 1.21*250e3
cargaR= 1.21*80e3
radioCurva= 3950 # Radio de la curva expresado en m.
