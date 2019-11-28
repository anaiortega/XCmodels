# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd


model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')
lsd.LimitStateData.envConfig= cfg

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)

#RC sections definition.
execfile("../sectionsDef.py")

#Define section names for each element.

preprocessor= model.getPreprocessor()
reinfConcreteSectionDistribution.assign(elemSet=preprocessor.getSets.getSet('cantlvSet').elements,setRCSects=cantlvRCSects)

reinfConcreteSectionDistribution.dump()

#Set of entities for which checking is going to be performed.
#setCalc= shellElements.elSet
setCalc= xcTotalSet.elSet

#setCalc=xcTotalSet.elSet

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
lsd.freqLoadsCrackControl, # RC crack control under frequent loads
lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
lsd.fatigueResistance # Fatigue resistance.
] 

#limitStates= [lsd.freqLoadsCrackControl]

for ls in limitStates:
  ls.saveAll(FEcase,combContainer,setCalc)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


