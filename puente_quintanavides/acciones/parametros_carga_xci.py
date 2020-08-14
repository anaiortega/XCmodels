cargaUnitariaLosaSup= cargaUnitariaTablero/BTablero
pesoUnitarioLosaSup= 

# tren de cargas 1 en vía 1
cargaPCarril= 1.21*250e3/2
sepMediaNodos= 0.0
cargaRCarril= 1.21*80e3/2

# Carga viga
pesoUnitarioLosaInf= 
pesoUnitarioAlmas30= 
pesoUnitarioAlmas27= 
pesoUnitarioAlmas22= 
pesoUnitarioAlmaC40= 
pesoUnitarioAlmaC50= 
pesoUnitarioDiafrag= 

execfile('acciones/IAPF/centrifugaIAPF_xcm.py')
execfile('../datos_centrifuga_xci.py')
execfile('acciones/IAPF/vientoIAPF_xcm.py')
execfile('../datos_viento_xci.py')
