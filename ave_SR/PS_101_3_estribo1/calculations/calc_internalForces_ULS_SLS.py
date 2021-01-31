# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution


#Project directory structure
exec(open('../../PSs/env_config.py').read())
#FE model generation
exec(open("../model_data.py").read())
#Limit states
exec(open("../../PSs_estribos/loadComb.py").read())
lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Set of entities for which checking is going to be performed.
setCalc=shellsToCheck

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
#lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
lsd.freqLoadsCrackControl, # RC crack control under frequent loads
#lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
#lsd.fatigueResistance # Fatigue resistance.
] 

#limitStates= [lsd.freqLoadsCrackControl]

for ls in limitStates:
  ls.saveAll(combContainer,setCalc)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


