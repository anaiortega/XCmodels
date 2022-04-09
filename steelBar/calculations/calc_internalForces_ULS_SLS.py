# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
exec(open("../model_gen.py").read()) #FE model generation
lsd.LimitStateData.envConfig= cfg

#Steel beams definition
exec(open("../steel_beams_def.py").read())


#Set of entities for which checking is going to be performed.
setCalc= beamY

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.steelNormalStressesResistance, # Normal stresses resistance.
lsd.steelShearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
] 

#limitStates= [lsd.freqLoadsCrackControl]


for ls in limitStates:
  ls.saveAll(combContainer,setCalc, bucklingMembers= [beam01])
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


