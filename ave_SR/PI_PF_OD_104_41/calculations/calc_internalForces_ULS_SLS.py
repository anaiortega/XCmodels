# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd


model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read())
lsd.LimitStateData.envConfig= cfg

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read())

#Combinations
exec(open(model_path+"def_hip_elsf.py").read())
exec(open(model_path+"def_hip_elu.py").read())

#RC sections definition.
exec(open("../sectionsDef.py").read())

#Define section names for each element.

preprocessor= FEcase.getPreprocessor
reinfConcreteSectionDistribution.assign(elemSet=dintExt_M1.elements,setRCSects=M1dintExtRCSects)
reinfConcreteSectionDistribution.assign(elemSet=dintCent_M1.elements,setRCSects=M1dintCentRCSects)
reinfConcreteSectionDistribution.assign(elemSet=losCimExt_M1.elements,setRCSects=M1losCimExtRCSects)
reinfConcreteSectionDistribution.assign(elemSet=losCimCent_M1.elements,setRCSects=M1losCimCentRCSects)
reinfConcreteSectionDistribution.assign(elemSet=hastIzq_M1.elements,setRCSects=M1hastIzqRCSects)
reinfConcreteSectionDistribution.assign(elemSet=hastDer_M1.elements,setRCSects=M1hastDerRCSects)

reinfConcreteSectionDistribution.assign(elemSet=dintExt_M2.elements,setRCSects=M2dintExtRCSects)
reinfConcreteSectionDistribution.assign(elemSet=dintCent_M2.elements,setRCSects=M2dintCentRCSects)
reinfConcreteSectionDistribution.assign(elemSet=losCimExt_M2.elements,setRCSects=M2losCimExtRCSects)
reinfConcreteSectionDistribution.assign(elemSet=losCimCent_M2.elements,setRCSects=M2losCimCentRCSects)
reinfConcreteSectionDistribution.assign(elemSet=hastIzq_M2.elements,setRCSects=M2hastIzqRCSects)
reinfConcreteSectionDistribution.assign(elemSet=hastDer_M2.elements,setRCSects=M2hastDerRCSects)

reinfConcreteSectionDistribution.assign(elemSet=dintExt_M3.elements,setRCSects=M1dintExtRCSects)
reinfConcreteSectionDistribution.assign(elemSet=dintCent_M3.elements,setRCSects=M1dintCentRCSects)
reinfConcreteSectionDistribution.assign(elemSet=losCimExt_M3.elements,setRCSects=M1losCimExtRCSects)
reinfConcreteSectionDistribution.assign(elemSet=losCimCent_M3.elements,setRCSects=M1losCimCentRCSects)
reinfConcreteSectionDistribution.assign(elemSet=hastIzq_M3.elements,setRCSects=M1hastIzqRCSects)
reinfConcreteSectionDistribution.assign(elemSet=hastDer_M3.elements,setRCSects=M1hastDerRCSects)

#reinfConcreteSectionDistribution.assign(elemSet=muretes.elements,setRCSects=muretesRCsect)

reinfConcreteSectionDistribution.dump()

#Set of entities for which checking is going to be performed.
#setCalc= M1_plus_M2
#setCalc= M1_plus_M2
setCalc=cortanteCalc 

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [#lsd.normalStressesResistance, # Normal stresses resistance.
lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
#lsd.freqLoadsCrackControl, # RC crack control under frequent loads
#lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
#lsd.fatigueResistance # Fatigue resistance.
] 

#limitStates= [lsd.freqLoadsCrackControl]

for ls in limitStates:
  ls.saveAll(combContainer,setCalc)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


