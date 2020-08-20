# -*- coding: utf-8

# Datos de los cordones de pretensar.
ECordon= 205000e6
areaCordon= 140e-6
cargaRoturaCordon= 260e3
densCordon= densAcero*areaCordon
alphaTesado= 0.75
cargaInicialTesadoCordon= alphaTesado*cargaRoturaCordon
sigmaInicialTesadoCordon= cargaInicialTesadoCordon/areaCordon
prestressingSteel= EHE_materials.EHEPrestressingSteel(steelName= "Y1860S7",fpk= 1171e6, fmax= 1860e6, alpha= alphaTesado)
incSigmaRelajacion= -prestressingSteel.getRelaxationStressLossFinal(sigmaInicialTesadoCordon) #getPerdidaTensionRelajacionFinalEHE("alambre","superestabilizado",alphaTesado,sigmaInicialTesadoCordon)


# Tensión en los cordones descontando las pérdidas por relajación.
sigmaFinalTesadoCordon= sigmaInicialTesadoCordon+incSigmaRelajacion
cargaFinalTesadoCordon= sigmaFinalTesadoCordon*areaCordon

# print("sigmaInicial= ",sigmaInicialTesadoCordon/1e6," MPa\n"
print("incSigmaRelajacion= ",incSigmaRelajacion/1e6," MPa\n")
print("cociente1= ",incSigmaRelajacion/sigmaInicialTesadoCordon,"\n")
print("sigmaFinal= ",sigmaFinalTesadoCordon/1e6," MPa\n")

hp= EHE_materials.HA50
materialHandler= preprocessor.getMaterialHandler

hormAlmas30= hp.defElasticMembranePlateSection(preprocessor, 'hormAlmas30',0.30)
hormAlmas30.rho= rhoHA
hormLosaInf= hp.defElasticMembranePlateSection(preprocessor, 'hormLosaInf',0.25)
hormLosaInf.rho= rhoHA
hormAlmas27= hp.defElasticMembranePlateSection(preprocessor, 'hormAlmas27',0.27)
hormAlmas27.rho= rhoHA
hormAlmas22= hp.defElasticMembranePlateSection(preprocessor, 'hormAlmas22',0.22)
hormAlmas22.rho= rhoHA
hormAlmaC50= hp.defElasticMembranePlateSection(preprocessor, 'hormAlmaC50',0.50)
hormAlmaC50.rho= rhoHA
hormAlmaC40= hp.defElasticMembranePlateSection(preprocessor, 'hormAlmaC40',0.40)
hormAlmaC40.rho= rhoHA
hormDiafrag= hp.defElasticMembranePlateSection(preprocessor, 'hormDiafrag',1.0)
hormDiafrag.rho= rhoHA

ha= EHE_materials.HA30
        
hormLosaSup= ha.defElasticMembranePlateSection(preprocessor, 'hormLosaSup',0.30)
hormLosaSup.rho=rhoHA

# Cables pretensado
cordon= typical_materials.defCableMaterial(preprocessor,name='cordon',E=ECordon, prestress=sigmaFinalTesadoCordon,rho= densAcero)
