# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
execfile("../model_gen.py") #FE model generation

#Steel beams definition
execfile("../steel_beams_def.py")


#Set of entities for which checking is going to be performed.
setCalc= beamY

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
] 

#limitStates= [lsd.freqLoadsCrackControl]


for ls in limitStates:
  ls.saveAll(FEcase,combContainer,setCalc,lstSteelBeams=[beam01])
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


