# -*- coding: utf-8
# Datos de los cordones de pretensar.
ECordon= 205000e6
areaCordon= 140e-6
cargaRoturaCordon= 260e3
densCordon= densAcero*areaCordon
alphaTesado= 0.75
cargaInicialTesadoCordon= alphaTesado*cargaRoturaCordon
sigmaInicialTesadoCordon= cargaInicialTesadoCordon/areaCordon
incSigmaRelajacion= -getPerdidaTensionRelajacionFinalEHE("alambre","superestabilizado",alphaTesado,sigmaInicialTesadoCordon)


# Tensión en los cordones descontando las pérdidas por relajación.
sigmaFinalTesadoCordon= sigmaInicialTesadoCordon+incSigmaRelajacion
cargaFinalTesadoCordon= sigmaFinalTesadoCordon*areaCordon

# print("sigmaInicial= ",sigmaInicialTesadoCordon/1e6," MPa\n"
print("incSigmaRelajacion= ",incSigmaRelajacion/1e6," MPa\n")
print("cociente1= ",incSigmaRelajacion/sigmaInicialTesadoCordon,"\n")
print("sigmaFinal= ",sigmaFinalTesadoCordon/1e6," MPa\n")}
